/*!
 * The Lounge Aesthetics — public booking embed loader (POC).
 *
 * Renders the price-free, white-label booking widget inside a clinic's own site.
 * Two ways to use it:
 *
 *  1) INLINE — drop a container where the widget should appear:
 *       <div data-tla-booking
 *            data-clinic="Bayside Skin & Laser"
 *            data-primary="#7c3aed" data-radius="18" data-theme="light"
 *            data-config='{"services":[{"id":"a","name":"Glow consult","schedule":"non-S4","dur":30,"roles":["NP","RN","DT"],"desc":"..."}]}'></div>
 *       <script src="https://danpowell88.github.io/tlapoc/embed.js" async></script>
 *
 *  2) POPUP — any element opens the widget in a centered modal:
 *       <button data-tla-booking-popup data-clinic="Bayside Skin & Laser" data-primary="#7c3aed">Book now</button>
 *       <script src="https://danpowell88.github.io/tlapoc/embed.js" async></script>
 *
 * Styling never leaks in or out: the widget always renders in a sandboxed <iframe>,
 * so the clinic's CSS can't break it and it can't break theirs. The iframe auto-resizes
 * to its content. A `tla:booking` window event (and optional callback) fires on completion.
 *
 * Programmatic API:  TLABooking.inline(targetEl, opts)  ·  TLABooking.popup(opts)
 */
(function(){
  "use strict";

  // Resolve where booking-widget.html lives, relative to this script.
  var SELF = document.currentScript || (function(){ var s=document.getElementsByTagName('script'); return s[s.length-1]; })();
  var BASE = SELF && SELF.src ? SELF.src.replace(/[^/]+$/, '') : './';
  var WIDGET = BASE + 'booking-widget.html';

  // Keys that travel as URL params (simple theming knobs the iframe understands directly).
  var URL_KEYS = ['clinic','primary','radius','theme','header','cta','mode','font'];

  function buildSrc(opts, src){
    var u = new URL(src || WIDGET, location.href);
    URL_KEYS.forEach(function(k){
      if(opts[k]==null || opts[k]==='') return;
      var v = opts[k];
      if(k==='primary') v = String(v).replace(/^#/,'');
      if(k==='header')  v = (v===false||v==='false'||v==='0') ? '0' : '1';
      u.searchParams.set(k, v);
    });
    return u.toString();
  }

  // Read data-* off an element into an opts object; parse data-config JSON if present.
  function readAttrs(el){
    var o = {};
    URL_KEYS.forEach(function(k){
      var v = el.getAttribute('data-'+k);
      if(v!=null) o[k] = v;
    });
    if(el.hasAttribute('data-src')) o.src = el.getAttribute('data-src');
    var cfg = el.getAttribute('data-config');
    if(cfg){ try{ o.config = JSON.parse(cfg); }catch(e){ console.warn('[TLABooking] bad data-config JSON', e); } }
    return o;
  }

  // Wire postMessage handling for one iframe: auto-resize + ready/booking events.
  function bind(iframe, opts){
    function onMsg(e){
      if(e.source !== iframe.contentWindow) return;       // only our frame
      var d = e.data || {};
      if(d.type === 'tla:ready'){
        // Push rich config (services/practitioners/etc.) that doesn't fit in URL params.
        if(opts.config) iframe.contentWindow.postMessage({type:'tla:config', config:opts.config}, '*');
      } else if(d.type === 'tla:resize' && d.height){
        iframe.style.height = d.height + 'px';
      } else if(d.type === 'tla:booking'){
        if(typeof opts.onBooking === 'function') opts.onBooking(d.payload);
        window.dispatchEvent(new CustomEvent('tla:booking', {detail:d.payload}));
      }
    }
    window.addEventListener('message', onMsg);
    return function off(){ window.removeEventListener('message', onMsg); };
  }

  function makeIframe(opts){
    var f = document.createElement('iframe');
    f.src = buildSrc(opts, opts.src);
    f.title = 'Book an appointment';
    f.loading = 'lazy';
    f.setAttribute('allowtransparency','true');
    f.style.cssText = 'width:100%;border:0;display:block;background:transparent;height:560px;transition:height .15s ease;';
    bind(f, opts);
    return f;
  }

  /* ---- inline -------------------------------------------------------- */
  function inline(target, opts){
    target = typeof target==='string' ? document.querySelector(target) : target;
    if(!target){ console.warn('[TLABooking] inline target not found'); return; }
    opts = opts || {};
    target.innerHTML = '';
    target.appendChild(makeIframe(opts));
  }

  /* ---- popup --------------------------------------------------------- */
  function popup(opts){
    opts = opts || {};
    var ov = document.createElement('div');
    ov.style.cssText = 'position:fixed;inset:0;z-index:2147483646;background:rgba(15,23,42,.55);'+
      'display:flex;align-items:flex-start;justify-content:center;padding:24px;overflow:auto;'+
      'opacity:0;transition:opacity .15s ease;';
    var box = document.createElement('div');
    box.style.cssText = 'width:100%;max-width:560px;margin:auto;position:relative;';
    var close = document.createElement('button');
    close.setAttribute('aria-label','Close');
    close.innerHTML = '&times;';
    close.style.cssText = 'position:absolute;top:-14px;right:-14px;width:34px;height:34px;border-radius:99px;'+
      'border:0;background:#fff;color:#0f172a;font-size:22px;line-height:1;cursor:pointer;'+
      'box-shadow:0 4px 14px rgba(0,0,0,.25);z-index:1;';
    var f = makeIframe(opts);
    f.style.height = '560px';
    function dismiss(){ ov.style.opacity='0'; setTimeout(function(){ ov.remove(); }, 160); document.removeEventListener('keydown', onKey); }
    function onKey(e){ if(e.key==='Escape') dismiss(); }
    close.onclick = dismiss;
    ov.addEventListener('click', function(e){ if(e.target===ov) dismiss(); });
    document.addEventListener('keydown', onKey);
    box.appendChild(close); box.appendChild(f); ov.appendChild(box);
    document.body.appendChild(ov);
    requestAnimationFrame(function(){ ov.style.opacity='1'; });
    return dismiss;
  }

  /* ---- auto-init from markup ----------------------------------------- */
  function auto(){
    document.querySelectorAll('[data-tla-booking]').forEach(function(el){
      if(el.__tla) return; el.__tla = 1;
      inline(el, readAttrs(el));
    });
    document.querySelectorAll('[data-tla-booking-popup]').forEach(function(el){
      if(el.__tla) return; el.__tla = 1;
      el.addEventListener('click', function(e){ e.preventDefault(); popup(readAttrs(el)); });
    });
  }

  window.TLABooking = { inline:inline, popup:popup, refresh:auto, widgetUrl:WIDGET };

  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded', auto);
  else auto();
})();
