#!/usr/bin/env python3
"""
capture.py — headless Playwright capture of every prototype screen to PNG.
Output: docs/backlog/screens/<name>.png  (gitignored; attached to Jira via jira.py attach)

Run: python scripts/capture.py            # all screens
     python scripts/capture.py dashboard  # one screen by name
"""
import os
import sys
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "docs", "backlog", "screens")
BASE = "https://danpowell88.github.io/tlapoc/"

# SPA screens in prototype.html: (name, persona, navigation JS)
SPA = [
    ("dashboard", "np", "show('dashboard')"),
    ("schedule", "np", "show('schedule')"),
    ("booking-wizard", "np", "show('booking'); if(typeof wstep=='function')wstep(1)"),
    ("clients", "np", "show('clients')"),
    ("client-360", "np", "show('clients'); if(typeof openClient=='function')openClient(0)"),
    ("followups", "np", "show('followups')"),
    ("checkout", "np", "show('checkout')"),
    ("charting-list", "np", "show('chartlist')"),
    ("charting", "np", "if(typeof openChartFor=='function')openChartFor(0); show('chart')"),
    ("stock", "np", "show('stock')"),
    ("forms-consent", "np", "show('forms')"),
    ("clinical-menu", "np", "goSub('clinical','menu')"),
    ("clinical-skin", "np", "goSub('clinical','skin')"),
    ("clinical-body", "np", "goSub('clinical','body')"),
    ("clinical-safety", "np", "goSub('clinical','safety')"),
    ("clinical-imaging", "np", "goSub('clinical','imaging')"),
    ("ops-openclose", "np", "goSub('operations','openclose')"),
    ("ops-monitors", "np", "goSub('operations','monitors')"),
    ("ops-resources", "np", "goSub('operations','resources')"),
    ("ops-equipment", "np", "goSub('operations','equipment')"),
    ("ops-phone", "np", "goSub('operations','phone')"),
    ("marketing-inbox", "np", "goSub('marketing','inbox')"),
    ("marketing-auto", "np", "goSub('marketing','auto')"),
    ("marketing-camp", "np", "goSub('marketing','camp')"),
    ("growth-leads", "np", "goSub('growth','leads')"),
    ("growth-reviews", "np", "goSub('growth','reviews')"),
    ("memb-overview", "owner", "goSub('memberships','overview')"),
    ("memb-plans", "owner", "goSub('memberships','plans')"),
    ("memb-members", "owner", "goSub('memberships','members')"),
    ("memb-loyalty", "owner", "goSub('memberships','loyalty')"),
    ("memb-referrals", "owner", "goSub('memberships','referrals')"),
    ("memb-gifts", "owner", "goSub('memberships','gifts')"),
    ("memb-pricing", "owner", "goSub('memberships','pricing')"),
    ("reports", "owner", "show('reports')"),
    ("finance", "owner", "show('finance')"),
    ("team-roster", "owner", "goSub('team','roster')"),
    ("team-people", "owner", "goSub('team','people')"),
    ("team-compliance", "owner", "goSub('team','compliance')"),
    ("gov-overview", "owner", "goSub('governance','overview')"),
    ("gov-ae", "owner", "goSub('governance','ae')"),
    ("gov-recalls", "owner", "goSub('governance','recalls')"),
    ("gov-policies", "owner", "goSub('governance','policies')"),
    ("gov-audit", "owner", "goSub('governance','audit')"),
    ("settings-integrations", "owner", "goSub('settings','integrations')"),
    ("settings-booking", "owner", "goSub('settings','booking')"),
]
# standalone device-surface files
DEVICE = [
    ("client-app", "client-app.html"),
    ("checkin", "checkin.html"),
    ("treatment-room", "treatment-room.html"),
    ("backroom", "backroom.html"),
    ("public-booking", "booking.html"),
    ("booking-widget", "booking-widget.html"),
]


def main():
    os.makedirs(OUT, exist_ok=True)
    only = sys.argv[1] if len(sys.argv) > 1 else None
    with sync_playwright() as p:
        b = p.chromium.launch()
        ctx = b.new_context(viewport={"width": 1440, "height": 1000}, device_scale_factor=2)
        pg = ctx.new_page()
        pg.set_default_timeout(45000)
        n = 0
        for name, persona, js in SPA:
            if only and name != only:
                continue
            try:
                pg.goto(BASE + "prototype.html", wait_until="domcontentloaded")
                pg.wait_for_timeout(700)
                pg.evaluate(f"login('{persona}')")
                pg.wait_for_timeout(300)
                pg.evaluate(js)
                pg.wait_for_timeout(900)
                pg.evaluate("window.scrollTo(0,0)")
                pg.screenshot(path=os.path.join(OUT, name + ".png"), full_page=True)
                n += 1
                print("captured", name)
            except Exception as e:
                print("FAIL", name, str(e)[:120])
        for name, f in DEVICE:
            if only and name != only:
                continue
            try:
                pg.goto(BASE + f, wait_until="domcontentloaded")
                pg.wait_for_timeout(1200)
                pg.screenshot(path=os.path.join(OUT, name + ".png"), full_page=True)
                n += 1
                print("captured", name)
            except Exception as e:
                print("FAIL", name, str(e)[:120])
        b.close()
        print(f"done: {n} screens -> {OUT}")


if __name__ == "__main__":
    main()
