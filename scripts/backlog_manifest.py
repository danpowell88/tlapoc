#!/usr/bin/env python3
"""Index the hand-authored Backlog.md task/doc files into backlog/manifest.json.

This does NOT generate any backlog content — it only reads the frontmatter of the
existing markdown task files so the static viewer (backlog.html) can render an
epic/story tree and a board without a directory-listing API. Re-run after adding,
editing or removing tasks:  python scripts/backlog_manifest.py
"""
import json
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TASKS = ROOT / "backlog" / "tasks"
DOCS = ROOT / "backlog" / "docs"
OUT = ROOT / "backlog" / "manifest.json"


def parse_frontmatter(text):
    """Minimal YAML-frontmatter parser for the small, fixed shape Backlog.md emits."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    fm_raw = text[3:end].strip("\n")
    body = text[end + 4:].lstrip("\n")
    data = {}
    key = None
    for line in fm_raw.split("\n"):
        if re.match(r"^\s*-\s+", line) and key:           # list item
            val = line.strip()[1:].strip().strip("'\"")
            data.setdefault(key, [])
            if isinstance(data[key], list):
                data[key].append(val)
            continue
        m = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
        if not m:
            continue
        key, val = m.group(1), m.group(2).strip()
        if val == "":
            data[key] = []                                 # likely a list to follow
        else:
            data[key] = val.strip("'\"")
    return data, body


def first_line(body):
    for ln in body.split("\n"):
        s = ln.strip()
        if s:
            return re.sub(r"\*\*|`", "", s)[:160]
    return ""


def labels_of(fm):
    v = fm.get("labels", [])
    return v if isinstance(v, list) else ([v] if v else [])


def main():
    tasks = []
    for f in sorted(TASKS.glob("*.md")):
        fm, body = parse_frontmatter(f.read_text(encoding="utf-8"))
        tid = fm.get("id", "")
        labels = labels_of(fm)
        stage = next((l.split(":", 1)[1] for l in labels if l.startswith("milestone:")), "")
        tasks.append({
            "id": tid,
            "title": fm.get("title", f.stem),
            "status": fm.get("status", ""),
            "priority": fm.get("priority", ""),
            "parent": fm.get("parent_task_id", ""),
            "labels": labels,
            "stage": stage,
            "isEpic": "type:epic" in labels,
            "tier": "mvp" if "mvp" in labels else ("later" if "later" in labels else ""),
            "file": "backlog/tasks/" + f.name,
            "summary": first_line(body),
        })

    docs = []
    if DOCS.exists():
        for f in sorted(DOCS.glob("*.md")):
            fm, _ = parse_frontmatter(f.read_text(encoding="utf-8"))
            docs.append({
                "id": fm.get("id", f.stem),
                "title": fm.get("title", f.stem),
                "file": "backlog/docs/" + f.name,
            })

    manifest = {
        "project": "The Lounge Aesthetics Platform",
        "generated": "by scripts/backlog_manifest.py",
        "epics": [t for t in tasks if t["isEpic"]],
        "stories": [t for t in tasks if not t["isEpic"]],
        "docs": docs,
        "counts": {
            "epics": sum(1 for t in tasks if t["isEpic"]),
            "stories": sum(1 for t in tasks if not t["isEpic"]),
            "mvp": sum(1 for t in tasks if not t["isEpic"] and t["tier"] == "mvp"),
            "later": sum(1 for t in tasks if not t["isEpic"] and t["tier"] == "later"),
        },
    }
    OUT.write_text(json.dumps(manifest, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {OUT.relative_to(ROOT)}: {manifest['counts']}")


if __name__ == "__main__":
    main()
