# -*- coding: utf-8 -*-
# templates.py — MALZ CODEX UI Templates (Indonesian)
# Author: malz codex

_FONTS = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Orbitron:wght@500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
"""

_CSS = """
*{margin:0;padding:0;box-sizing:border-box}
html,body{height:100%}
body{font-family:'Inter',system-ui,sans-serif;background:#000;color:#fff;min-height:100vh;-webkit-font-smoothing:antialiased}
:root{--bg:#000;--card:#08080c;--card2:#101015;--line:#1a1a22;--line2:#25252e;--txt:#fff;--mut:#8a8a95;--dim:#55555f;--green:#22c55e;--red:#ef4444;--blue:#3b82f6;--purple:#8b5cf6;--gold:#f59e0b;--cyan:#00ffd5}
.mono{font-family:'JetBrains Mono',monospace}
.orb{font-family:'Orbitron',sans-serif}
::-webkit-scrollbar{width:8px;height:8px}
::-webkit-scrollbar-track{background:#0a0a0a}
::-webkit-scrollbar-thumb{background:#262626;border-radius:4px}
::-webkit-scrollbar-thumb:hover{background:#3a3a3a}
"""

_ICONS = {
    "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>',
    "fast": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 19 22 12 13 5 13 19"></polygon><polygon points="2 19 11 12 2 5 2 19"></polygon></svg>',
    "users": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>',
    "refresh": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="23 4 23 10 17 10"></polyline><polyline points="1 20 1 14 7 14"></polyline><path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"></path></svg>',
    "cloud": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 10h-1.26A8 8 0 1 0 9 20h9a5 5 0 0 0 0-10z"></path></svg>',
    "wa": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>',
    "list": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="6" height="4" rx="1"></rect><rect x="3" y="15" width="6" height="4" rx="1"></rect><line x1="14" y1="7" x2="21" y2="7"></line><line x1="14" y1="17" x2="21" y2="17"></line></svg>',
    "bolt": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>',
    "star": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>',
    "crown": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 18h20l-1.5-9-4 3-4.5-7-4.5 7-4-3z"></path></svg>',
    "gear": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"></circle><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 2.83-2.83l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"></path></svg>',
    "pause": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><rect x="6" y="4" width="4" height="16" rx="1"></rect><rect x="14" y="4" width="4" height="16" rx="1"></rect></svg>',
    "play": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polygon points="6 4 20 12 6 20 6 4"></polygon></svg>',
    "trash": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6l-1 14a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2L5 6"></path><path d="M10 11v6M14 11v6"></path><path d="M9 6V4a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2"></path></svg>',
    "monitor": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg>',
    "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>',
    "gamepad": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><line x1="6" y1="12" x2="10" y2="12"></line><line x1="8" y1="10" x2="8" y2="14"></line><line x1="15" y1="13" x2="15.01" y2="13"></line><line x1="18" y1="11" x2="18.01" y2="11"></line><rect x="2" y="6" width="20" height="12" rx="6"></rect></svg>',
    "user": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>',
    "globe": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>',
    "id": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"></rect><circle cx="9" cy="11" r="2"></circle><path d="M15 10h3M15 14h3"></path></svg>',
    "trophy": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 21h8M12 17v4M7 4h10v6a5 5 0 0 1-10 0V4z"></path><path d="M17 5h3a2 2 0 0 1 0 4h-1M7 5H4a2 2 0 0 0 0 4h1"></path></svg>',
    "chat": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>',
    "warn": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M10.29 3.86 1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path><line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>',
    "x": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>',
    "plus": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>',
    "arrow_right": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>',
    "star_fill": '<svg viewBox="0 0 24 24" fill="currentColor" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>',
    "bolt_fill": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>',
    "crown_fill": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M2 18h20l-1.5-9-4 3-4.5-7-4.5 7-4-3z"></path></svg>',
}

def _icon(name, color="currentColor", size=16, stroke_extra=""):
    svg = _ICONS.get(name, "")
    if not svg:
        return ""
    svg = svg.replace('stroke="currentColor"', f'stroke="{color}"')
    svg = svg.replace('<svg ', f'<svg width="{size}" height="{size}" ', 1)
    return svg

def _icon_inline(name, color="currentColor", size=16):
    svg = _ICONS.get(name, "")
    if not svg:
        return ""
    svg = svg.replace('stroke="currentColor"', f'stroke="{color}"')
    svg = svg.replace('<svg ', f'<svg width="{size}" height="{size}" style="display:inline-block;vertical-align:middle" ', 1)
    return svg


# ==================== HOME (Landing) ====================
HOME_HTML = """<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=no">
<title>MALZ CODEX — Free Fire Automation</title>
""" + _FONTS + """
<style>
""" + _CSS + """
html{scroll-behavior:smooth}
html,body{height:100%}
body{background:#050505;min-height:100vh;position:relative;overflow-x:hidden}
body::before{content:'';position:fixed;inset:0;background:
  linear-gradient(rgba(255,255,255,0.015) 1px,transparent 1px),
  linear-gradient(90deg,rgba(255,255,255,0.015) 1px,transparent 1px);
  background-size:60px 60px;pointer-events:none;z-index:0;
  mask-image:radial-gradient(ellipse at 50% 40%,#000 20%,transparent 75%);
  -webkit-mask-image:radial-gradient(ellipse at 50% 40%,#000 20%,transparent 75%)}

.ann{position:relative;z-index:5;background:linear-gradient(90deg,#00ffd5,#8b5cf6);color:#000;padding:10px 40px 10px 14px;text-align:center;font-size:12px;font-weight:700;font-family:'Inter',sans-serif;letter-spacing:0.2px}
.ann a{color:#000;text-decoration:underline;font-weight:900}
.ann .cls{position:absolute;right:12px;top:50%;transform:translateY(-50%);background:transparent;border:none;cursor:pointer;color:#000;font-size:16px;line-height:1;padding:4px}

.hdr{position:relative;z-index:5;display:flex;align-items:center;justify-content:space-between;padding:14px 18px;border-bottom:1px solid #151515}
.hlogo{display:flex;align-items:center;gap:10px}
.hshield{width:34px;height:34px;display:inline-flex;align-items:center;justify-content:center}
.hshield svg{width:34px;height:34px;stroke:#fff;fill:none;stroke-width:1.8}
.hname{font-family:'Inter',sans-serif;font-size:14px;font-weight:800;letter-spacing:2.5px;color:#fff}
.hbell{background:transparent;border:none;cursor:pointer;padding:6px;color:#fff}
.hbell svg{width:20px;height:20px;stroke:#fff;fill:none;stroke-width:1.8}

.status{position:relative;z-index:5;display:flex;justify-content:center;padding:16px 18px 0}
.spill{display:inline-flex;align-items:center;gap:8px;background:#0d0d0d;border:1px solid #1c1c1c;border-radius:24px;padding:7px 14px 7px 11px;font-family:'Inter',sans-serif;font-size:11px;font-weight:600;color:#b8b8b8}
.spill .dot{width:7px;height:7px;border-radius:50%;background:#00ffd5;box-shadow:0 0 8px #00ffd5;animation:pl 1.4s infinite}
.spill .mut{color:#5a5a5a;font-weight:400;margin-left:2px}
@keyframes pl{0%,100%{opacity:1}50%{opacity:0.4}}

.hero{position:relative;z-index:5;padding:50px 22px 20px;max-width:680px;margin:0 auto;text-align:center}
.hero h1{font-family:'Orbitron',sans-serif;font-size:30px;font-weight:900;letter-spacing:3px;margin-bottom:34px;
  background:linear-gradient(90deg,#00ffd5,#a78bfa,#00ffd5);
  -webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;
  filter:drop-shadow(0 0 24px rgba(0,255,213,0.35));}
.hero p{font-family:'Inter',sans-serif;font-size:16px;font-weight:500;line-height:1.7;color:#b8b8b8;letter-spacing:0.2px}
.hero p + p{margin-top:14px}

.ctas{position:relative;z-index:5;display:flex;gap:12px;justify-content:center;padding:24px 18px 50px;flex-wrap:wrap;max-width:460px;margin:0 auto}
.cbtn{flex:1;min-width:150px;padding:14px 20px;border-radius:10px;font-family:'Inter',sans-serif;font-size:14px;font-weight:800;letter-spacing:0.5px;cursor:pointer;text-decoration:none;display:inline-flex;align-items:center;justify-content:center;gap:8px;border:1px solid transparent;transition:all 0.2s}
.cb-white{background:#fff;color:#000}
.cb-white:hover{background:#e5e5e5}
.cb-out{background:transparent;border-color:#2a2a2a;color:#fff}
.cb-out:hover{border-color:#555;background:#0d0d0d}
.cbtn svg{width:16px;height:16px;stroke:currentColor;fill:none;stroke-width:2.2}

.psec{position:relative;z-index:5;max-width:1200px;margin:0 auto;padding:0 18px 80px;scroll-margin-top:20px}
.ptitle{text-align:center;font-family:'Orbitron',sans-serif;font-size:26px;font-weight:800;letter-spacing:2px;color:#fff;margin-bottom:8px;text-transform:uppercase}
.psub{text-align:center;font-size:11px;color:#7a7a7a;letter-spacing:3px;text-transform:uppercase;margin-bottom:14px;font-weight:700}
.pnote{text-align:center;font-size:12px;color:#7a8ba0;max-width:580px;margin:0 auto 30px;line-height:1.6;padding:12px 18px;background:rgba(0,255,213,0.04);border:1px solid rgba(0,255,213,0.15);border-radius:10px}
.pgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:18px}
@media(max-width:700px){.pgrid{grid-template-columns:1fr}}

.pc{background:#0b0b0e;border:1.5px solid #1f1f24;border-radius:18px;padding:32px 22px 22px;position:relative;display:flex;flex-direction:column;transition:all 0.3s}
.pc.blue{border-color:rgba(0,255,213,0.45)}
.pc.blue:hover{border-color:#00ffd5;box-shadow:0 0 40px rgba(0,255,213,0.25);transform:translateY(-4px)}
.pc.purple{border-color:rgba(139,92,246,0.5)}
.pc.purple:hover{border-color:#8b5cf6;box-shadow:0 0 40px rgba(139,92,246,0.3);transform:translateY(-4px)}
.pc.gold{border-color:rgba(245,158,11,0.5)}
.pc.gold:hover{border-color:#f59e0b;box-shadow:0 0 40px rgba(245,158,11,0.25);transform:translateY(-4px)}
.ribbon{position:absolute;top:-11px;right:20px;background:linear-gradient(135deg,#8b5cf6,#6d28d9);color:#fff;font-family:'Orbitron',sans-serif;font-size:9px;font-weight:800;letter-spacing:1.5px;padding:5px 12px;border-radius:20px;text-transform:uppercase;box-shadow:0 4px 20px rgba(139,92,246,0.5)}
.pi{width:64px;height:64px;margin:0 auto 20px;border-radius:50%;display:flex;align-items:center;justify-content:center}
.pc.blue .pi{background:rgba(0,255,213,0.08);border:1.5px solid rgba(0,255,213,0.35);color:#00ffd5}
.pc.purple .pi{background:rgba(139,92,246,0.08);border:1.5px solid rgba(139,92,246,0.4);color:#a78bfa}
.pc.gold .pi{background:rgba(245,158,11,0.08);border:1.5px solid rgba(245,158,11,0.4);color:#fbbf24}
.pi svg{width:28px;height:28px}
.pn{text-align:center;font-family:'Orbitron',sans-serif;font-size:20px;font-weight:800;letter-spacing:5px;margin-bottom:14px;color:#fff;text-transform:uppercase}
.pl{display:flex;justify-content:center;align-items:center;gap:10px;margin-bottom:8px}
.op{font-family:'Inter',sans-serif;font-size:15px;font-weight:700;color:#4a4a4a;text-decoration:line-through}
.deal{background:#dc2626;color:#fff;font-family:'Orbitron',sans-serif;font-size:9px;font-weight:800;letter-spacing:1.2px;padding:3px 8px;border-radius:5px}
.pm{text-align:center;font-family:'Orbitron',sans-serif;font-size:48px;font-weight:900;letter-spacing:-1px;margin-bottom:26px;line-height:1;color:#fff}
.pm .cur{font-size:26px;font-weight:700;vertical-align:top;line-height:1;display:inline-block;margin-right:2px}
.feats{list-style:none;margin-bottom:22px;flex:1}
.feats li{display:flex;align-items:flex-start;gap:10px;padding:7px 0;font-size:13px;color:#d8d8dd;line-height:1.45;font-weight:500}
.feats li .ic{flex-shrink:0;width:18px;height:18px;display:flex;align-items:center;justify-content:center;margin-top:2px;color:#00ffd5}
.feats li .ic svg{width:14px;height:14px}
.bb{width:100%;padding:13px;border-radius:10px;font-family:'Orbitron',sans-serif;font-size:12px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;border:none;cursor:pointer;transition:all 0.25s;color:#fff}
.pc.blue .bb{background:linear-gradient(135deg,#00ffd5,#00b894);color:#000;box-shadow:0 6px 24px rgba(0,255,213,0.3)}
.pc.purple .bb{background:linear-gradient(135deg,#8b5cf6,#7c3aed);box-shadow:0 6px 24px rgba(139,92,246,0.35)}
.pc.gold .bb{background:linear-gradient(135deg,#f59e0b,#d97706);box-shadow:0 6px 24px rgba(245,158,11,0.3);color:#000}
.an{text-align:center;font-size:10px;color:#4a4a4a;margin-top:10px;letter-spacing:0.5px;font-weight:500}

.tg{position:fixed;right:18px;bottom:18px;width:52px;height:52px;border-radius:50%;background:#22a7e8;display:flex;align-items:center;justify-content:center;box-shadow:0 8px 28px rgba(34,167,232,0.5);cursor:pointer;z-index:20;border:none;text-decoration:none}
.tg svg{width:26px;height:26px;fill:#fff}

.devsec{position:relative;z-index:5;max-width:700px;margin:0 auto;padding:0 22px 70px;text-align:center}
.devsec h3{font-family:'Orbitron',sans-serif;font-size:14px;font-weight:700;letter-spacing:5px;color:#555;text-transform:uppercase;margin-bottom:22px}
.devgrid{display:grid;grid-template-columns:repeat(2,1fr);gap:12px;max-width:520px;margin:0 auto}
@media(max-width:520px){.devgrid{grid-template-columns:1fr}}
.devcard{display:flex;align-items:center;gap:12px;padding:14px 16px;background:#0b0b0e;border:1px solid #1c1c22;border-radius:12px;text-decoration:none;color:#fff;transition:all 0.25s}
.devcard:hover{border-color:#00ffd5;background:#0d0d12;transform:translateY(-2px)}
.devcard .ic{width:38px;height:38px;border-radius:10px;background:linear-gradient(135deg,#0f1218,#151a22);border:1px solid #252a32;display:flex;align-items:center;justify-content:center;color:#00ffd5;flex-shrink:0}
.devcard .ic svg{width:18px;height:18px}
.devcard .info{text-align:left;min-width:0;flex:1}
.devcard .info .lb{font-family:'Orbitron',sans-serif;font-size:9px;color:#666;letter-spacing:1.5px;text-transform:uppercase;font-weight:700;margin-bottom:2px}
.devcard .info .hd{font-family:'JetBrains Mono',monospace;font-size:12px;color:#fff;font-weight:700;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}

.mtop{position:fixed;inset:0;background:rgba(0,0,0,0.85);backdrop-filter:blur(8px);z-index:100;display:none;align-items:center;justify-content:center;padding:18px}
.mtop.on{display:flex}
.mbox{background:#141414;border:1px solid #262626;border-radius:18px;padding:22px;max-width:440px;width:100%;position:relative;font-family:'Inter',sans-serif}
.mh-row{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:24px}
.mh-row h3{font-size:17px;font-weight:700;color:#fff;letter-spacing:0.2px}
.mclose{width:34px;height:34px;border-radius:50%;border:1px solid #2a2a2a;background:transparent;color:#fff;cursor:pointer;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.mclose:hover{background:#1e1e1e}
.mclose svg{width:16px;height:16px;stroke:#fff;fill:none;stroke-width:2}
.micon{width:56px;height:56px;margin:0 auto 18px;display:flex;align-items:center;justify-content:center}
.micon svg{width:56px;height:56px;stroke:#00ffd5;fill:none;stroke-width:1.5}
.mtitle{text-align:center;font-size:19px;font-weight:800;color:#fff;margin-bottom:14px;letter-spacing:0.3px}
.mtext{text-align:center;font-size:13px;line-height:1.65;color:#a8a8a8;margin-bottom:22px}
.mbtn{width:100%;padding:14px;border-radius:10px;background:#fff;color:#000;border:none;font-family:'Inter',sans-serif;font-size:14px;font-weight:700;cursor:pointer;display:flex;align-items:center;justify-content:center;gap:8px;text-decoration:none}
.mbtn:hover{background:#e5e5e5}
</style>
</head>
<body>

<div class="ann" id="ann">
⚡ Server IND sedang dalam pemeliharaan — mohon tunggu update selanjutnya! <a href="#pricing">Pelajari Lebih</a>
<button class="cls" onclick="document.getElementById('ann').style.display='none'">✕</button>
</div>

<div class="hdr">
<div class="hlogo">
<span class="hshield"><svg viewBox="0 0 24 24"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg></span>
<span class="hname">MALZ CODEX</span>
</div>
<button class="hbell"><svg viewBox="0 0 24 24"><path d="M18 8a6 6 0 0 0-12 0c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.73 21a2 2 0 0 1-3.46 0"/></svg></button>
</div>

<div class="status">
<span class="spill"><span class="dot"></span> Sistem Beroperasi Normal <span class="mut">0ms</span></span>
</div>

<div class="hero">
<h1>MALZ CODEX</h1>
<p>Bot level-up Free Fire cepat, stabil, dan reliable. Dibuat buat lo yang mau naik level tanpa grinding manual. Setup gampang, hasil nyata.</p>
<p>Naikkan level akun lo lebih cepat — tetap di depan, tinggal duduk manis.</p>
</div>

<div class="ctas">
<a href="/dashboard" class="cbtn cb-white">Mulai Sekarang <svg viewBox="0 0 24 24"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg></a>
<a href="#pricing" class="cbtn cb-out">Lihat Harga <svg viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"/></svg></a>
</div>

<div class="psec" id="pricing">
<div class="ptitle">Pilih Paket Lo</div>
<div class="psub">Bisa Dipakai di Semua Server</div>
<div class="pnote">Semua paket bisa dipakai di seluruh server Free Fire — IND, BD, EUROPE, SG, TH, PH, VN, MY, ID, HK, TW, dan lain-lain. Harga dalam USD.</div>
<div class="pgrid" id="pgrid"></div>
</div>

<div class="devsec">
<h3>D E V E L O P E R</h3>
<div class="devgrid">
<a class="devcard" href="https://tiktok.com/@malzwithyou" target="_blank" rel="noopener">
<div class="ic"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-5.2 1.74 2.89 2.89 0 0 1 2.31-4.64 2.93 2.93 0 0 1 .88.13V9.4a6.84 6.84 0 0 0-1-.05A6.33 6.33 0 0 0 5 20.1a6.34 6.34 0 0 0 10.86-4.43v-7a8.16 8.16 0 0 0 4.77 1.52v-3.4a4.85 4.85 0 0 1-1-.1z"/></svg></div>
<div class="info"><div class="lb">TikTok</div><div class="hd">@malzwithyou</div></div>
</a>
<a class="devcard" href="https://youtube.com/@Nikmal_hsb" target="_blank" rel="noopener">
<div class="ic"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg></div>
<div class="info"><div class="lb">YouTube</div><div class="hd">@Nikmal_hsb</div></div>
</a>
<a class="devcard" href="https://github.com/ini_nikmal" target="_blank" rel="noopener">
<div class="ic"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg></div>
<div class="info"><div class="lb">GitHub</div><div class="hd">@ini_nikmal</div></div>
</a>
<a class="devcard" href="https://t.me/malzwithyou" target="_blank" rel="noopener">
<div class="ic"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M9.78 18.65l.28-4.23 7.68-6.92c.34-.31-.07-.46-.52-.19L7.74 13.3 3.64 12c-.88-.25-.89-.86.2-1.3l15.97-6.16c.73-.33 1.43.18 1.15 1.3l-2.72 12.81c-.19.91-.74 1.13-1.5.71L12.6 16.3l-1.99 1.93c-.23.23-.42.42-.83.42z"/></svg></div>
<div class="info"><div class="lb">Telegram</div><div class="hd">@malzwithyou</div></div>
</a>
</div>
</div>

<a class="tg" href="https://t.me/malzwithyou" target="_blank"><svg viewBox="0 0 24 24"><path d="M9.78 18.65l.28-4.23 7.68-6.92c.34-.31-.07-.46-.52-.19L7.74 13.3 3.64 12c-.88-.25-.89-.86.2-1.3l15.97-6.16c.73-.33 1.43.18 1.15 1.3l-2.72 12.81c-.19.91-.74 1.13-1.5.71L12.6 16.3l-1.99 1.93c-.23.23-.42.42-.83.42z"/></svg></a>

<script>
const PLANS=[
{id:'starting',name:'STARTING',style:'blue',icon:'bolt',hours:24,slots:3,price:'1',old:'2',pop:false},
{id:'basic',name:'BASIC',style:'purple',icon:'star',hours:48,slots:3,price:'2',old:'4',pop:true},
{id:'premium',name:'PREMIUM',style:'gold',icon:'crown',hours:72,slots:4,price:'2.5',old:'6',pop:false}
];
const TG='malzwithyou';
const ICONS={
bolt:'__SVG_BOLT__',
star:'__SVG_STAR__',
crown:'__SVG_CROWN__',
check:'__SVG_CHECK__'
};

function feat(p){
const d=p.hours>=24?Math.round(p.hours/24)+' Hari':p.hours+' Jam';
const sp=p.id==='premium'?'Level Up Paling Cepat':'Performa Level Up Cepat';
const off=p.id==='premium'?'Jalan 24/7 — Gak Perlu Online':'Jalan Walau Lo Offline';
return[
'Akses Panel Selama '+d,
sp,
'Bisa Banyak Akun Sekaligus',
'Restart & Manage Akun Kapan Saja',
off,
'Support Pembayaran & Bantuan Cepat via Telegram',
p.slots+' Slot Akun Aktif'
];
}

function render(){
const g=document.getElementById('pgrid');
let h='';
PLANS.forEach(p=>{
let fh='';
feat(p).forEach(t=>{fh+='<li><span class="ic">'+ICONS.check+'</span><span>'+t+'</span></li>';});
h+='<div class="pc '+p.style+'">';
if(p.pop)h+='<div class="ribbon">Paling Laris</div>';
h+='<div class="pi">'+ICONS[p.icon]+'</div>';
h+='<div class="pn">'+p.name+'</div>';
h+='<div class="pl"><span class="op">$'+p.old+'</span><span class="deal">DEAL</span></div>';
h+='<div class="pm"><span class="cur">$</span>'+p.price+'</div>';
h+='<ul class="feats">'+fh+'</ul>';
h+='<button class="bb" onclick="buy(\\''+p.id+'\\')">Beli '+p.name+'</button>';
h+='<div class="an">Aktivasi Instan Setelah Pembayaran</div>';
h+='</div>';
});
g.innerHTML=h;
}

function buy(id){
const p=PLANS.find(x=>x.id===id);
let m='Halo, saya mau beli paket '+p.name+'.\\n\\nPaket: $'+p.price+'\\nDurasi: '+p.hours+' Jam\\nSlot: '+p.slots+'\\n\\nMohon info cara bayarnya.';
window.open('https://t.me/'+TG+'?text='+encodeURIComponent(m),'_blank');
}
render();

document.querySelectorAll('a[href^="#"]').forEach(a=>{
  a.addEventListener('click',e=>{
    const id=a.getAttribute('href');
    if(id.length>1){
      const el=document.querySelector(id);
      if(el){
        e.preventDefault();
        el.scrollIntoView({behavior:'smooth',block:'start'});
      }
    }
  });
});
</script>
</body>
</html>
"""

HOME_HTML = HOME_HTML.replace("__SVG_BOLT__", _icon("bolt_fill", "currentColor", 28).replace('"', '\\"'))
HOME_HTML = HOME_HTML.replace("__SVG_STAR__", _icon("star_fill", "currentColor", 28).replace('"', '\\"'))
HOME_HTML = HOME_HTML.replace("__SVG_CROWN__", _icon("crown_fill", "currentColor", 28).replace('"', '\\"'))
HOME_HTML = HOME_HTML.replace("__SVG_CHECK__", _icon("check", "#00ffd5", 14).replace('"', '\\"'))


# ==================== LOGIN ====================
LOGIN_HTML = """<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=no">
<title>Login — MALZ CODEX</title>
""" + _FONTS + """
<style>
""" + _CSS + """
body{background:#0a0a0a;display:flex;align-items:center;justify-content:center;padding:20px;min-height:100vh;position:relative}
body::before{content:'';position:absolute;inset:0;background:
  radial-gradient(circle at 20% 10%,rgba(0,255,213,0.08),transparent 45%),
  radial-gradient(circle at 85% 90%,rgba(139,92,246,0.08),transparent 45%),
  linear-gradient(rgba(255,255,255,0.012) 1px,transparent 1px),
  linear-gradient(90deg,rgba(255,255,255,0.012) 1px,transparent 1px);
  background-size:auto,auto,60px 60px,60px 60px;pointer-events:none}

.wrap{width:100%;max-width:440px;position:relative;z-index:1}
.brand{display:flex;align-items:center;justify-content:center;gap:12px;margin-bottom:60px}
.shield{width:36px;height:36px;display:inline-flex;align-items:center;justify-content:center}
.shield svg{width:36px;height:36px;stroke:#00ffd5;fill:none;stroke-width:1.8}
.brand-txt{font-family:'Orbitron',sans-serif;font-size:16px;font-weight:800;letter-spacing:3px;color:#fff}
.brand-txt .dot{color:#555;font-weight:700}

.welcome{text-align:center;margin-bottom:36px}
.welcome h1{font-family:'Orbitron',sans-serif;font-size:24px;font-weight:800;letter-spacing:1px;color:#fff;margin-bottom:10px;text-transform:uppercase}
.welcome p{font-size:13px;color:#7a7a7a;font-weight:400;line-height:1.6}

.err{background:rgba(239,68,68,0.08);border:1px solid rgba(239,68,68,0.3);color:#ef4444;padding:11px;border-radius:10px;font-size:12px;margin-bottom:16px;display:none;text-align:center}
.err.on{display:block}

.f{margin-bottom:20px}
.f label{display:block;font-size:13px;font-weight:700;color:#fff;margin-bottom:9px;text-align:center;font-family:'Orbitron',sans-serif;letter-spacing:1.5px;text-transform:uppercase;font-size:10px}
.iw{position:relative}
.iw svg.lft{position:absolute;left:16px;top:50%;transform:translateY(-50%);width:18px;height:18px;stroke:#6a6a6a;fill:none;stroke-width:1.8;pointer-events:none}
.iw svg.rgt{position:absolute;right:16px;top:50%;transform:translateY(-50%);width:18px;height:18px;stroke:#6a6a6a;fill:none;stroke-width:1.8;cursor:pointer;transition:stroke 0.2s}
.iw svg.rgt:hover{stroke:#00ffd5}
.f input{
  width:100%;background:transparent;
  border:1px solid #2a2a2a;border-radius:10px;
  padding:15px 46px;
  color:#fff;font-size:14px;
  font-family:'Inter',sans-serif;font-weight:500;
  outline:none;transition:all 0.2s;
}
.f input::placeholder{color:#4a4a4a;font-weight:400}
.f input:focus{border-color:#00ffd5;background:rgba(0,255,213,0.02);box-shadow:0 0 0 3px rgba(0,255,213,0.08)}

.remember{display:flex;align-items:center;justify-content:center;gap:10px;margin:24px 0 22px}
.remember input[type=checkbox]{
  appearance:none;-webkit-appearance:none;
  width:20px;height:20px;border-radius:5px;
  border:1.5px solid #444;background:transparent;
  cursor:pointer;position:relative;transition:all 0.2s;flex-shrink:0;
}
.remember input[type=checkbox]:checked{background:#00ffd5;border-color:#00ffd5}
.remember input[type=checkbox]:checked::after{
  content:'';position:absolute;left:6px;top:2px;
  width:6px;height:11px;
  border:solid #000;border-width:0 2px 2px 0;
  transform:rotate(45deg);
}
.remember label{font-size:14px;color:#b8b8b8;cursor:pointer;font-weight:500}

.btn{
  width:100%;padding:17px;border-radius:10px;
  background:linear-gradient(135deg,#00ffd5,#00b894);color:#000;
  border:none;cursor:pointer;
  font-family:'Orbitron',sans-serif;
  font-size:13px;font-weight:800;
  letter-spacing:2px;text-transform:uppercase;
  display:flex;align-items:center;justify-content:center;gap:10px;
  transition:all 0.2s;
  box-shadow:0 6px 24px rgba(0,255,213,0.25);
}
.btn:hover{box-shadow:0 8px 32px rgba(0,255,213,0.4);transform:translateY(-1px)}
.btn svg{width:18px;height:18px;stroke:#000;fill:none;stroke-width:2.2}
.btn:disabled{opacity:0.6;cursor:not-allowed;transform:none}

.foot{text-align:center;margin-top:28px;font-size:13px;color:#6a6a6a}
.foot a{color:#00ffd5;text-decoration:none;font-weight:600;border-bottom:1px solid rgba(0,255,213,0.3);padding-bottom:1px}
.foot a:hover{border-color:#00ffd5}
</style>
</head>
<body>
<div class="wrap">

<div class="brand">
<span class="shield">
<svg viewBox="0 0 24 24"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2" fill="none"/></svg>
</span>
<span class="brand-txt">MALZ CODEX</span>
</div>

<div class="welcome">
<h1>Selamat Datang Kembali</h1>
<p>Login aman &mdash; token lo terlindungi.</p>
</div>

<div class="err" id="err"></div>

<form id="f">
<div class="f">
<label>Username</label>
<div class="iw">
<svg class="lft" viewBox="0 0 24 24"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
<input type="text" id="u" placeholder="username lo" autocomplete="username" required>
</div>
</div>

<div class="f">
<label>Password</label>
<div class="iw">
<svg class="lft" viewBox="0 0 24 24"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
<svg class="rgt" id="eye" viewBox="0 0 24 24"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>
<input type="password" id="p" placeholder="••••••••••" autocomplete="current-password" required>
</div>
</div>

<div class="remember">
<input type="checkbox" id="rm" checked>
<label for="rm">Ingat saya</label>
</div>

<button type="submit" class="btn" id="sb">
<span id="btn-text">Login</span>
<svg viewBox="0 0 24 24"><path d="M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4"/><polyline points="10 17 15 12 10 7"/><line x1="15" y1="12" x2="3" y2="12"/></svg>
</button>
</form>

<div class="foot">Belum punya akun? <a href="/plans">Daftar di sini</a></div>
</div>

<script>
const eye=document.getElementById('eye');
const pw=document.getElementById('p');
eye.addEventListener('click',()=>{
const t=pw.type==='password'?'text':'password';
pw.type=t;
eye.style.stroke=t==='text'?'#00ffd5':'#6a6a6a';
});

document.getElementById('f').addEventListener('submit',async(e)=>{
e.preventDefault();
const err=document.getElementById('err');
const btn=document.getElementById('sb');
const bt=document.getElementById('btn-text');
err.classList.remove('on');
btn.disabled=true;bt.textContent='Memproses...';
const u=document.getElementById('u').value.trim();
const p=document.getElementById('p').value;
try{
const r=await fetch('/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({username:u,password:p})});
const d=await r.json();
if(d.status==='ok')window.location.href=d.redirect||'/dashboard';
else{err.textContent=d.error||'Login Gagal';err.classList.add('on')}
}catch(ex){err.textContent='Error Jaringan';err.classList.add('on')}
btn.disabled=false;bt.textContent='Login';
});
</script>
</body>
</html>
"""


# ==================== PLANS ====================
PLANS_HTML = """<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Harga — MALZ CODEX</title>
""" + _FONTS + """
<style>
""" + _CSS + """
body{background:radial-gradient(ellipse at top,#0a1a1a 0%,#000 55%);padding-bottom:60px}
.head{display:flex;align-items:center;justify-content:space-between;padding:18px 22px;border-bottom:1px solid var(--line);max-width:1400px;margin:0 auto}
.logo{display:flex;align-items:center;gap:10px;font-family:'Orbitron',sans-serif;font-size:14px;font-weight:700;letter-spacing:2px}
.logo .lm{width:36px;height:36px;background:linear-gradient(135deg,#00ffd5,#00b894);border-radius:10px;display:inline-flex;align-items:center;justify-content:center;font-weight:900;font-size:16px;color:#000;box-shadow:0 0 20px rgba(0,255,213,0.35)}
.wrap{max-width:1200px;margin:0 auto;padding:44px 22px 0}
.t{text-align:center;font-family:'Orbitron',sans-serif;font-size:30px;font-weight:800;letter-spacing:2px;text-transform:uppercase;margin-bottom:10px}
.sub{text-align:center;font-size:11px;color:var(--mut);letter-spacing:4px;text-transform:uppercase;margin-bottom:14px;font-weight:600}
.note{text-align:center;font-size:12px;color:#7a8ba0;max-width:640px;margin:0 auto 40px;line-height:1.6;padding:12px 18px;background:rgba(0,255,213,0.04);border:1px solid rgba(0,255,213,0.15);border-radius:10px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:20px}
@media(max-width:700px){.grid{grid-template-columns:1fr}}

.pc{background:var(--card);border:1.5px solid var(--line2);border-radius:20px;padding:36px 24px 24px;position:relative;transition:all 0.3s;display:flex;flex-direction:column}
.pc.blue{border-color:rgba(0,255,213,0.45)}
.pc.blue:hover{border-color:#00ffd5;box-shadow:0 0 40px rgba(0,255,213,0.25);transform:translateY(-4px)}
.pc.purple{border-color:rgba(139,92,246,0.5)}
.pc.purple:hover{border-color:#8b5cf6;box-shadow:0 0 40px rgba(139,92,246,0.3);transform:translateY(-4px)}
.pc.gold{border-color:rgba(245,158,11,0.5)}
.pc.gold:hover{border-color:#f59e0b;box-shadow:0 0 40px rgba(245,158,11,0.25);transform:translateY(-4px)}
.ribbon{position:absolute;top:-12px;right:22px;background:linear-gradient(135deg,#8b5cf6,#6d28d9);color:#fff;font-family:'Orbitron',sans-serif;font-size:9px;font-weight:700;letter-spacing:1.5px;padding:6px 14px;border-radius:20px;text-transform:uppercase;box-shadow:0 4px 20px rgba(139,92,246,0.5)}
.pi{width:70px;height:70px;margin:0 auto 22px;border-radius:50%;display:flex;align-items:center;justify-content:center}
.pc.blue .pi{background:rgba(0,255,213,0.08);border:1.5px solid rgba(0,255,213,0.35);color:#00ffd5}
.pc.purple .pi{background:rgba(139,92,246,0.08);border:1.5px solid rgba(139,92,246,0.4);color:#a78bfa}
.pc.gold .pi{background:rgba(245,158,11,0.08);border:1.5px solid rgba(245,158,11,0.4);color:#fbbf24}
.pi svg{width:30px;height:30px}
.pn{text-align:center;font-family:'Orbitron',sans-serif;font-size:24px;font-weight:700;letter-spacing:6px;margin-bottom:16px;color:#fff}
.pl{display:flex;justify-content:center;align-items:center;gap:12px;margin-bottom:8px}
.op{font-family:'Inter',sans-serif;font-size:16px;font-weight:700;color:var(--dim);text-decoration:line-through}
.deal{background:#dc2626;color:#fff;font-family:'Orbitron',sans-serif;font-size:9px;font-weight:700;letter-spacing:1.5px;padding:3px 9px;border-radius:5px}
.pm{text-align:center;font-family:'Orbitron',sans-serif;font-size:52px;font-weight:900;letter-spacing:-1px;margin-bottom:30px;line-height:1;color:#fff}
.pm .cur{font-size:30px;font-weight:700;vertical-align:top;line-height:1;display:inline-block;margin-right:2px}
.feats{list-style:none;margin-bottom:26px;flex:1}
.feats li{display:flex;align-items:flex-start;gap:12px;padding:8px 0;font-size:14px;color:#d8d8dd;line-height:1.45;font-weight:500}
.feats li .ic{flex-shrink:0;width:18px;height:18px;display:flex;align-items:center;justify-content:center;margin-top:2px;color:#00ffd5}
.feats li .ic svg{width:15px;height:15px}
.bb{width:100%;padding:15px;border-radius:12px;font-family:'Orbitron',sans-serif;font-size:12px;font-weight:700;letter-spacing:2px;text-transform:uppercase;border:none;cursor:pointer;transition:all 0.25s;color:#fff}
.pc.blue .bb{background:linear-gradient(135deg,#00ffd5,#00b894);color:#000;box-shadow:0 6px 24px rgba(0,255,213,0.3)}
.pc.purple .bb{background:linear-gradient(135deg,#8b5cf6,#7c3aed);box-shadow:0 6px 24px rgba(139,92,246,0.35)}
.pc.gold .bb{background:linear-gradient(135deg,#f59e0b,#d97706);box-shadow:0 6px 24px rgba(245,158,11,0.3);color:#000}
.an{text-align:center;font-size:11px;color:var(--dim);margin-top:12px;letter-spacing:0.5px;font-weight:500}
.flink{text-align:center;margin-top:36px;font-size:13px;color:var(--mut)}
.flink a{color:#00ffd5;text-decoration:none;font-weight:700}
</style>
</head>
<body>
<div class="head">
<div class="logo"><span class="lm">M</span><span>MALZ CODEX</span></div>
<a href="/login" style="color:#fff;text-decoration:none;font-size:13px;font-weight:700">Login →</a>
</div>
<div class="wrap">
<div class="t">Pilih Paket Lo</div>
<div class="sub">Bisa Dipakai di Semua Server</div>
<div class="note">Semua paket bisa dipakai di seluruh server Free Fire — IND, BD, EUROPE, SG, TH, PH, VN, MY, ID, HK, TW, dan lain-lain. Harga dalam USD.</div>
<div class="grid" id="grid"></div>
<div class="flink">Sudah Punya Akun? <a href="/login">Login</a></div>
</div>
<script>
const SVG={
check:'__SVG_CHECK__',
bolt:'__SVG_BOLT__',
star:'__SVG_STAR__',
crown:'__SVG_CROWN__'
};
const PLANS=[
{id:'starting',name:'STARTING',style:'blue',icon:'bolt',hours:24,slots:3,price:'1',old:'2',pop:false},
{id:'basic',name:'BASIC',style:'purple',icon:'star',hours:48,slots:3,price:'2',old:'4',pop:true},
{id:'premium',name:'PREMIUM',style:'gold',icon:'crown',hours:72,slots:4,price:'2.5',old:'6',pop:false}
];
const TG='malzwithyou';

function feat(p){
const d=p.hours>=24?Math.round(p.hours/24)+' Hari':p.hours+' Jam';
const sp=p.id==='premium'?'Level Up Paling Cepat':'Performa Level Up Cepat';
const off=p.id==='premium'?'Jalan 24/7 — Gak Perlu Online':'Jalan Walau Lo Offline';
return[
{ic:'check',txt:'Akses Panel Selama '+d},
{ic:'check',txt:sp},
{ic:'check',txt:'Bisa Banyak Akun Sekaligus'},
{ic:'check',txt:'Restart & Manage Akun Kapan Saja'},
{ic:'check',txt:off},
{ic:'check',txt:'Support Pembayaran & Bantuan Cepat via Telegram'},
{ic:'check',txt:p.slots+' Slot Akun Aktif'}
];
}

function render(){
const g=document.getElementById('grid');
let h='';
PLANS.forEach(p=>{
let fh='';
feat(p).forEach(f=>{
fh+='<li><span class="ic">'+SVG.check+'</span><span>'+f.txt+'</span></li>';
});
h+='<div class="pc '+p.style+'">';
if(p.pop)h+='<div class="ribbon">Paling Laris</div>';
h+='<div class="pi">'+SVG[p.icon]+'</div>';
h+='<div class="pn">'+p.name+'</div>';
h+='<div class="pl"><span class="op">$'+p.old+'</span><span class="deal">DEAL</span></div>';
h+='<div class="pm"><span class="cur">$</span>'+p.price+'</div>';
h+='<ul class="feats">'+fh+'</ul>';
h+='<button class="bb" onclick="buy(\\''+p.id+'\\')">Beli '+p.name+'</button>';
h+='<div class="an">Aktivasi Instan Setelah Pembayaran</div>';
h+='</div>';
});
g.innerHTML=h;
}

function buy(id){
const p=PLANS.find(x=>x.id===id);
let m='Halo, saya mau beli paket '+p.name+'.\\n\\nPaket: $'+p.price+'\\nDurasi: '+p.hours+' Jam\\nSlot: '+p.slots+'\\n\\nMohon info cara bayarnya.';
window.open('https://t.me/'+TG+'?text='+encodeURIComponent(m),'_blank');
}
render();
</script>
</body>
</html>
"""

PLANS_HTML = PLANS_HTML.replace("__SVG_CHECK__", _icon("check", "#00ffd5", 15).replace('"', '\\"'))
PLANS_HTML = PLANS_HTML.replace("__SVG_BOLT__", _icon("bolt_fill", "currentColor", 30).replace('"', '\\"'))
PLANS_HTML = PLANS_HTML.replace("__SVG_STAR__", _icon("star_fill", "currentColor", 30).replace('"', '\\"'))
PLANS_HTML = PLANS_HTML.replace("__SVG_CROWN__", _icon("crown_fill", "currentColor", 30).replace('"', '\\"'))


# ==================== EXPIRED ====================
EXPIRED_HTML = """<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Paket Kadaluarsa — MALZ CODEX</title>
""" + _FONTS + """
<style>
""" + _CSS + """
body{display:flex;align-items:center;justify-content:center;padding:24px;background:radial-gradient(ellipse at top,#200a0a 0%,#000 60%)}
.wrap{width:100%;max-width:460px;text-align:center}
.ic{width:84px;height:84px;border-radius:50%;background:rgba(239,68,68,0.08);border:1.5px solid var(--red);display:inline-flex;align-items:center;justify-content:center;margin-bottom:24px;color:var(--red)}
h1{font-family:'Orbitron',sans-serif;font-size:24px;font-weight:800;letter-spacing:2px;text-transform:uppercase;margin-bottom:14px}
p{font-size:14px;color:var(--mut);line-height:1.7;margin-bottom:30px}
.br{display:flex;flex-direction:column;gap:10px;max-width:300px;margin:0 auto}
.b{display:block;padding:14px;border-radius:10px;font-family:'Orbitron',sans-serif;font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;text-decoration:none;text-align:center;transition:all 0.2s;border:none;cursor:pointer}
.b1{background:linear-gradient(135deg,#00ffd5,#00b894);color:#000}
.b1:hover{box-shadow:0 8px 28px rgba(0,255,213,0.5)}
.b2{background:transparent;border:1px solid var(--line2);color:var(--mut)}
.b2:hover{border-color:var(--red);color:var(--red)}
</style>
</head>
<body>
<div class="wrap">
<div class="ic">""" + _icon("warn", "currentColor", 40) + """</div>
<h1>Paket Kadaluarsa</h1>
<p>Masa aktif paket lo sudah habis dan semua bot telah dihentikan.<br>Buat perpanjang, hubungi <b style="color:#00ffd5">@malzwithyou</b> di Telegram.</p>
<div class="br">
<a class="b b1" href="/plans">Perpanjang Paket</a>
<a class="b b2" href="/logout">Logout</a>
</div>
</div>
</body>
</html>
"""


# ==================== DASHBOARD ====================
DASHBOARD_HTML = """<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=no">
<title>Dashboard — MALZ CODEX</title>
""" + _FONTS + """
<style>
""" + _CSS + """
body{background:radial-gradient(ellipse at top,#0a1a1a 0%,#000 55%);padding-bottom:80px;overflow-x:hidden}
*{-webkit-tap-highlight-color:transparent}

.top{position:sticky;top:0;z-index:50;background:rgba(0,0,0,0.9);backdrop-filter:blur(14px);border-bottom:1px solid var(--line)}
.top-in{max-width:1200px;margin:0 auto;padding:12px 16px;display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap}
.logo{display:flex;align-items:center;gap:8px;font-family:'Orbitron',sans-serif;font-size:11px;font-weight:700;letter-spacing:1.5px}
.lm{width:28px;height:28px;background:linear-gradient(135deg,#00ffd5,#00b894);color:#000;border-radius:8px;display:inline-flex;align-items:center;justify-content:center;font-weight:900;font-size:13px;box-shadow:0 0 12px rgba(0,255,213,0.4)}
.meta{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.mi{display:flex;flex-direction:column;gap:1px;padding:3px 9px;border-left:2px solid #00ffd5}
.mi .l{font-size:8px;color:var(--mut);letter-spacing:1.2px;text-transform:uppercase;font-weight:800;font-family:'Orbitron',sans-serif}
.mi .v{font-family:'JetBrains Mono',monospace;font-size:11px;font-weight:700;white-space:nowrap}
.act{display:flex;gap:5px}
.bs{padding:8px 12px;font-family:'Orbitron',sans-serif;font-size:9px;font-weight:700;letter-spacing:1.2px;text-transform:uppercase;border-radius:8px;cursor:pointer;text-decoration:none;border:1px solid transparent;display:inline-flex;align-items:center;justify-content:center;gap:4px;transition:all 0.2s;white-space:nowrap}
.bw{background:#00ffd5;color:#000}
.bw:hover{opacity:0.88}
.bg{background:transparent;border-color:var(--line2);color:var(--mut)}
.bg:hover{border-color:var(--red);color:var(--red)}
.bf{background:transparent;border-color:var(--line2);color:#fff;width:32px;height:32px;padding:0}
.bf:hover{background:var(--card2);border-color:#00ffd5}
.bf.sp svg{animation:sp 0.7s linear infinite}
@keyframes sp{to{transform:rotate(360deg)}}
@keyframes pl{0%,100%{opacity:1}50%{opacity:0.4}}

.main{max-width:1200px;margin:0 auto;padding:18px 14px 80px}
.grid{display:grid;grid-template-columns:1fr;gap:14px}

.cc{
  position:relative;
  background:linear-gradient(145deg,#0b1418 0%,#080c0c 100%);
  border:1px solid #1a3038;
  border-radius:16px;
  overflow:hidden;
  transition:border-color 0.25s, box-shadow 0.25s;
}
.cc:hover{border-color:#1e4a52;box-shadow:0 0 0 1px rgba(0,255,213,0.08), 0 8px 32px rgba(0,0,0,0.5)}

.tagline{padding:14px 16px 10px;display:flex;align-items:center;gap:7px;flex-wrap:wrap}
.pill{
  display:inline-flex;align-items:center;gap:6px;
  background:rgba(255,255,255,0.03);
  border:1px solid rgba(255,255,255,0.08);
  border-radius:20px;
  padding:5px 12px;
  font-family:'Orbitron',sans-serif;
  font-size:9px;font-weight:700;
  letter-spacing:1.2px;
  text-transform:uppercase;
  color:#d0d5dd;
}
.pill.uid{font-family:'JetBrains Mono',monospace;letter-spacing:0.4px;font-size:10px}
.pill svg{width:11px;height:11px;opacity:0.75}

.status-top{
  display:inline-flex;align-items:center;gap:5px;
  background:rgba(0,255,213,0.12);
  border:1px solid rgba(0,255,213,0.5);
  border-radius:20px;
  padding:5px 12px;
  font-family:'Orbitron',sans-serif;
  font-size:9px;font-weight:800;
  letter-spacing:1.2px;
  text-transform:uppercase;
  color:#00ffd5;
  white-space:nowrap;
  margin-left:auto;
}
.status-top .dot{width:6px;height:6px;border-radius:50%;background:#00ffd5;box-shadow:0 0 6px #00ffd5;animation:pl 1.4s infinite}
.status-top.paused{background:rgba(138,138,149,0.12);border-color:rgba(138,138,149,0.4);color:#8a8a95}
.status-top.paused .dot{background:#8a8a95;box-shadow:none;animation:none}
.status-top.match{background:rgba(245,158,11,0.12);border-color:rgba(245,158,11,0.5);color:#f59e0b}
.status-top.match .dot{background:#f59e0b;box-shadow:0 0 6px #f59e0b}
.status-top.online{background:rgba(59,130,246,0.12);border-color:rgba(59,130,246,0.5);color:#60a5fa}
.status-top.online .dot{background:#3b82f6;box-shadow:0 0 6px #3b82f6}

.refresh-btn{
  display:inline-flex;align-items:center;gap:6px;
  background:rgba(0,255,213,0.08);
  border:1px solid rgba(0,255,213,0.35);
  border-radius:9px;
  padding:7px 14px;
  color:#00ffd5;
  font-size:12px;font-weight:700;
  cursor:pointer;
  transition:all 0.2s;
  margin:0 16px 14px;
  font-family:'Inter',sans-serif;
}
.refresh-btn:hover{background:rgba(0,255,213,0.15);border-color:#00ffd5}
.refresh-btn svg{width:12px;height:12px}
.refresh-btn.spin svg{animation:sp 0.7s linear infinite}

.acc-head{
  display:flex;align-items:center;gap:12px;
  padding:14px 16px;
  background:linear-gradient(135deg,rgba(0,255,213,0.06),rgba(0,255,213,0.01));
  border-top:1px solid rgba(0,255,213,0.1);
  border-bottom:1px solid rgba(0,255,213,0.1);
}
.avatar{
  width:48px;height:48px;border-radius:11px;
  background:linear-gradient(135deg,#0f2a26,#0a1a18);
  border:1px solid rgba(0,255,213,0.3);
  display:flex;align-items:center;justify-content:center;
  font-family:'Orbitron',sans-serif;
  font-weight:900;font-size:19px;color:#00ffd5;
  flex-shrink:0;
  box-shadow:inset 0 0 16px rgba(0,255,213,0.1);
}
.hinfo{flex:1;min-width:0}
.hinfo h3{
  font-family:'Orbitron',sans-serif;
  font-size:14px;font-weight:800;
  letter-spacing:0.3px;
  color:#fff;
  margin-bottom:3px;
  overflow:hidden;text-overflow:ellipsis;white-space:nowrap;
}
.hinfo p{
  font-family:'JetBrains Mono',monospace;
  font-size:10px;color:#7c869a;
  letter-spacing:0.3px;
}
.lvl-badge{
  background:rgba(0,255,213,0.12);
  border:1px solid rgba(0,255,213,0.45);
  border-radius:8px;
  padding:6px 11px;
  font-family:'Orbitron',sans-serif;
  font-size:11px;font-weight:800;
  letter-spacing:0.8px;
  color:#00ffd5;
  white-space:nowrap;
  flex-shrink:0;
}

.cd{padding:12px 16px;border-bottom:1px solid rgba(255,255,255,0.05);display:grid;grid-template-columns:1fr 1fr;gap:8px 22px}
@media(max-width:560px){.cd{grid-template-columns:1fr}}
.row{display:flex;align-items:center;gap:7px;font-size:12px;min-width:0}
.row .k{color:var(--mut);font-size:9px;font-weight:800;letter-spacing:1.3px;text-transform:uppercase;min-width:76px;font-family:'Orbitron',sans-serif}
.row .v{color:#fff;font-weight:700;font-family:'JetBrains Mono',monospace;font-size:11px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}

.timerow{padding:9px 16px;border-bottom:1px solid rgba(255,255,255,0.05);display:flex;align-items:center;gap:7px;font-size:10px;color:var(--mut);font-family:'JetBrains Mono',monospace}
.td{width:4px;height:4px;border-radius:50%;background:#fff;opacity:0.5}

.lvlrow{padding:11px 16px;border-bottom:1px solid rgba(255,255,255,0.05);display:flex;justify-content:space-between;align-items:center;font-size:10px;color:var(--mut);font-weight:800;letter-spacing:1.5px;text-transform:uppercase;font-family:'Orbitron',sans-serif}
.lvlrow .v{font-family:'Orbitron',sans-serif;color:#fff;font-weight:800;font-size:14px;letter-spacing:1px}

.statrow{display:grid;grid-template-columns:1fr 1fr 1fr;border-bottom:1px solid rgba(255,255,255,0.05);background:rgba(0,0,0,0.25)}
.sc{padding:12px 6px;text-align:center;border-right:1px solid rgba(255,255,255,0.05)}
.sc:last-child{border-right:none}
.sc .l{font-size:8px;color:var(--mut);letter-spacing:1.3px;text-transform:uppercase;font-weight:800;margin-bottom:5px;font-family:'Orbitron',sans-serif}
.sc .v{font-family:'JetBrains Mono',monospace;font-size:14px;font-weight:800;color:#fff;word-break:break-all}
.sc .v.g{color:#00ffd5}
@media(max-width:400px){.sc .v{font-size:12px}}

.matchrow{padding:11px 16px;border-bottom:1px solid rgba(255,255,255,0.05);display:flex;justify-content:space-between;align-items:center;font-size:10px;color:var(--mut);font-family:'Orbitron',sans-serif;font-weight:800;letter-spacing:1.5px;text-transform:uppercase}
.matchrow .v{color:#fff;font-family:'JetBrains Mono',monospace;font-weight:700;font-size:13px;letter-spacing:0.5px}

.acc-actions{
  display:flex;
  gap:8px;
  padding:12px 14px 14px;
  background:transparent;
}
.acc-actions button{
  flex:1;
  padding:11px 6px;
  background:#121a1c;
  border:1px solid #1e2a2e;
  border-radius:10px;
  color:#fff;
  font-family:'Inter',sans-serif;
  font-size:11px;
  font-weight:800;
  letter-spacing:0.8px;
  text-transform:uppercase;
  cursor:pointer;
  transition:all 0.18s;
  display:flex;
  align-items:center;
  justify-content:center;
  gap:5px;
  min-width:0;
}
.acc-actions button:hover{background:#182428;border-color:#00ffd5;color:#00ffd5}
.acc-actions button svg{width:13px;height:13px;flex-shrink:0}
.acc-actions button.danger{
  background:#1a0f10;
  border:1px solid #7a1f1f;
  color:#ff3b3b;
}
.acc-actions button.danger:hover{background:#241012;border-color:#ff3b3b;color:#ff3b3b}
.acc-actions button.danger svg{stroke:#ff3b3b}

@media(max-width:360px){
  .acc-actions{gap:6px;padding:10px 12px}
  .acc-actions button{padding:10px 3px;font-size:10px;letter-spacing:0.5px;gap:4px}
  .acc-actions button svg{width:11px;height:11px}
}

.add{
  background:transparent;
  border:1.5px dashed var(--line2);
  border-radius:14px;
  padding:40px 20px;
  text-align:center;cursor:pointer;
  color:var(--mut);font-family:inherit;
  width:100%;transition:all 0.2s;
}
.add:hover{border-color:#00ffd5;color:#00ffd5}
.add .plus{display:flex;justify-content:center;margin-bottom:10px;color:#00ffd5}
.add .plus svg{width:32px;height:32px}
.add .txt{font-family:'Orbitron',sans-serif;font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase}
.add .sub{font-size:9px;color:var(--dim);margin-top:6px;letter-spacing:1px}

.empty{text-align:center;padding:60px 20px;color:var(--mut)}
.empty .big{display:flex;justify-content:center;margin-bottom:12px;opacity:0.25}
.empty .big svg{width:44px;height:44px}

.modal{position:fixed;inset:0;background:rgba(0,0,0,0.9);backdrop-filter:blur(6px);display:none;align-items:center;justify-content:center;z-index:100;padding:16px}
.modal.on{display:flex}
.mc{background:var(--card);border:1px solid var(--line2);border-radius:16px;padding:22px;max-width:420px;width:100%;max-height:90vh;overflow-y:auto}
.mh{display:flex;justify-content:space-between;align-items:center;margin-bottom:18px}
.mh h3{font-family:'Orbitron',sans-serif;font-size:13px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase}
.mx{background:transparent;border:none;color:var(--mut);cursor:pointer;padding:0;width:28px;height:28px;display:flex;align-items:center;justify-content:center;border-radius:6px;transition:all 0.2s}
.mx:hover{background:var(--card2);color:#00ffd5}
.mx svg{width:18px;height:18px}
.tabs{display:flex;gap:4px;background:var(--card2);padding:4px;border-radius:10px;margin-bottom:16px}
.tb{flex:1;padding:10px;text-align:center;font-family:'Orbitron',sans-serif;font-size:10px;font-weight:700;letter-spacing:1px;text-transform:uppercase;border-radius:7px;cursor:pointer;color:var(--mut);border:none;background:transparent;transition:all 0.2s}
.tb.on{background:#00ffd5;color:#000}
.f{margin-bottom:14px}
.f label{display:block;font-size:10px;font-weight:800;color:var(--mut);text-transform:uppercase;letter-spacing:1.5px;margin-bottom:6px}
.f input,.f textarea{width:100%;background:var(--card2);border:1px solid var(--line2);border-radius:10px;padding:12px 14px;color:#fff;font-size:14px;font-family:'Inter',sans-serif;outline:none;transition:border 0.2s;resize:none}
.f input:focus,.f textarea:focus{border-color:#00ffd5;box-shadow:0 0 0 3px rgba(0,255,213,0.15)}
.sb{width:100%;padding:14px;border-radius:10px;font-family:'Orbitron',sans-serif;font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;cursor:pointer;border:none;background:linear-gradient(135deg,#00ffd5,#00b894);color:#000;transition:all 0.2s}
.sb:hover{box-shadow:0 8px 24px rgba(0,255,213,0.4)}
.sb:disabled{opacity:0.5;cursor:not-allowed}
.err{background:rgba(239,68,68,0.1);border:1px solid rgba(239,68,68,0.3);color:var(--red);padding:10px;border-radius:10px;font-size:12px;margin-bottom:14px;display:none}
.err.on{display:block}
.hide{display:none!important}

.conf{position:fixed;inset:0;background:rgba(0,0,0,0.88);backdrop-filter:blur(8px);display:none;align-items:center;justify-content:center;z-index:200;padding:18px}
.conf.on{display:flex}
.conf-box{background:#141414;border:1px solid #262626;border-radius:16px;padding:22px;max-width:400px;width:100%;font-family:'Inter',sans-serif}
.conf-head{font-size:16px;font-weight:700;color:#fff;margin-bottom:14px;text-align:center}
.conf-msg{font-size:13px;line-height:1.65;color:#a8a8a8;text-align:center;margin-bottom:22px}
.conf-btns{display:flex;gap:10px}
.conf-btns button{flex:1;padding:13px 10px;border-radius:10px;font-family:'Inter',sans-serif;font-size:13px;font-weight:700;cursor:pointer;border:none;transition:all 0.2s}
.conf-yes{background:#00ffd5;color:#000}
.conf-yes:hover{background:#00d4b3}
.conf-no{background:#1c1c1e;color:#fff;border:1px solid #2a2a2e!important}
.conf-no:hover{background:#242428}

.mtop{position:fixed;inset:0;background:rgba(0,0,0,0.88);backdrop-filter:blur(8px);display:none;align-items:center;justify-content:center;z-index:300;padding:18px}
.mtop.on{display:flex}
.mbox{background:#141414;border:1px solid #262626;border-radius:18px;padding:22px;max-width:440px;width:100%;position:relative;font-family:'Inter',sans-serif}
.mh-row{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:22px}
.mh-row h3{font-size:17px;font-weight:700;color:#fff;letter-spacing:0.2px}
.mclose{width:34px;height:34px;border-radius:50%;border:1px solid #2a2a2a;background:transparent;color:#fff;cursor:pointer;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.mclose:hover{background:#1e1e1e}
.mclose svg{width:16px;height:16px;stroke:#fff;fill:none;stroke-width:2}
.micon{width:56px;height:56px;margin:0 auto 16px;display:flex;align-items:center;justify-content:center}
.micon svg{width:56px;height:56px;stroke:#00ffd5;fill:none;stroke-width:1.5}
.mtitle{text-align:center;font-size:19px;font-weight:800;color:#fff;margin-bottom:12px;letter-spacing:0.3px}
.mtext{text-align:center;font-size:13px;line-height:1.65;color:#a8a8a8;margin-bottom:20px}
.mbtn{width:100%;padding:14px;border-radius:10px;background:#fff;color:#000;border:none;font-family:'Inter',sans-serif;font-size:14px;font-weight:700;cursor:pointer;display:flex;align-items:center;justify-content:center;gap:8px;text-decoration:none}
.mbtn:hover{background:#e5e5e5}
</style>
</head>
<body>
<div class="top">
<div class="top-in">
<div class="logo"><span class="lm">M</span><span>MALZ CODEX</span></div>
<div class="meta">
<div class="mi"><span class="l">User</span><span class="v" id="ui-u">{{USERNAME}}</span></div>
<div class="mi"><span class="l">Sisa</span><span class="v" id="ui-t">--</span></div>
<div class="mi"><span class="l">Slot</span><span class="v" id="ui-s">0/0</span></div>
</div>
<div class="act">
<button class="bs bf" id="rf">__ICON_REFRESH__</button>
<a class="bs bw" href="/plans">Beli</a>
<a class="bs bg" href="/logout">Logout</a>
</div>
</div>
</div>
<div class="main"><div class="grid" id="grid"></div></div>

<div class="modal" id="am">
<div class="mc">
<div class="mh"><h3>Tambah Akun Free Fire</h3><button class="mx" onclick="closeAdd()">__ICON_X__</button></div>
<div class="err" id="aer"></div>
<div class="tabs">
<button class="tb on" data-t="guest" onclick="sw('guest')">UID + Password</button>
<button class="tb" data-t="token" onclick="sw('token')">Access Token</button>
</div>
<form id="af">
<div id="fg">
<div class="f"><label>Free Fire UID</label><input type="text" id="fu" autocomplete="off" placeholder="contoh: 7872038363"></div>
<div class="f"><label>Password</label><input type="text" id="fp" autocomplete="off" placeholder="password guest lo"></div>
</div>
<div id="ft" class="hide">
<div class="f"><label>Access Token</label><textarea id="fk" rows="4" placeholder="paste access token di sini..."></textarea></div>
</div>
<div id="mode-hint" style="margin:10px 0 12px;padding:10px 12px;border:1px solid rgba(0,255,213,.25);border-radius:9px;background:rgba(0,255,213,.06);color:#8fd9c4;font:700 10px Inter,sans-serif;letter-spacing:.7px;text-align:center">MODE: OTOMATIS • Lv 1–2 BR / Lv 3–39 LONE WOLF / Lv 40+ BR</div>
<button type="submit" class="sb" id="ab">Mulai Bot</button>
</form>
</div>
</div>

<div class="conf" id="cm">
<div class="conf-box">
<div class="conf-head" id="cm-t">Konfirmasi</div>
<div class="conf-msg" id="cm-m">Yakin?</div>
<div class="conf-btns">
<button class="conf-yes" id="cm-y">Ya</button>
<button class="conf-no" id="cm-n">Batal</button>
</div>
</div>
</div>

<div class="mtop" id="maint">
<div class="mbox">
<div class="mh-row">
<h3>Pemberitahuan Penting</h3>
<button class="mclose" onclick="document.getElementById('maint').classList.remove('on')"><svg viewBox="0 0 24 24"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg></button>
</div>
<div class="micon"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><polyline points="8 12 11 15 16 9"/></svg></div>
<div class="mtitle">Pemeliharaan Server IND</div>
<div class="mtext">Karena restriksi game di server IND, sistem level up kita cuma bisa farming 5K EXP per hari. Untuk itu server IND kita tutup sementara sampai tim dev selesai memperbaiki. Kita bakal online lagi segera.</div>
<a class="mbtn" href="https://t.me/malzwithyou" target="_blank">Chat Sekarang</a>
</div>
</div>

<script>
const SVG={
pause:'__SVG_PAUSE__',
play:'__SVG_PLAY__',
trash:'__SVG_TRASH__',
refresh:'__SVG_REFRESH__',
globe:'__SVG_GLOBE__',
id:'__SVG_ID__',
plus:'__SVG_PLUS__',
warn:'__SVG_WARN__'
};
let CT='guest';
function sw(t){CT=t;document.querySelectorAll('.tb').forEach(el=>el.classList.toggle('on',el.dataset.t===t));document.getElementById('fg').classList.toggle('hide',t!=='guest');document.getElementById('ft').classList.toggle('hide',t!=='token')}
function openAdd(){document.getElementById('am').classList.add('on');document.getElementById('aer').classList.remove('on')}
function closeAdd(){document.getElementById('am').classList.remove('on');document.getElementById('af').reset();document.getElementById('aer').classList.remove('on')}

function showConfirm(title,msg,yesText,noText){
return new Promise(resolve=>{
document.getElementById('cm-t').textContent=title;
document.getElementById('cm-m').textContent=msg;
document.getElementById('cm-y').textContent=yesText||'Ya';
document.getElementById('cm-n').textContent=noText||'Batal';
document.getElementById('cm-n').style.display='';
document.getElementById('cm').classList.add('on');
const clean=()=>{
document.getElementById('cm').classList.remove('on');
document.getElementById('cm-y').onclick=null;
document.getElementById('cm-n').onclick=null;
};
document.getElementById('cm-y').onclick=()=>{clean();resolve(true)};
document.getElementById('cm-n').onclick=()=>{clean();resolve(false)};
});
}

document.getElementById('af').addEventListener('submit',async(e)=>{
e.preventDefault();
const err=document.getElementById('aer');
err.classList.remove('on');
const btn=document.getElementById('ab');
btn.disabled=true;btn.textContent='Cek Akun...';
let pl={};
if(CT==='guest'){
pl.uid=document.getElementById('fu').value.trim();
pl.password=document.getElementById('fp').value.trim();
if(!pl.uid||!pl.password){err.textContent='UID Dan Password Wajib Diisi';err.classList.add('on');btn.disabled=false;btn.textContent='Mulai Bot';return}
}else{
pl.token=document.getElementById('fk').value.trim();
if(!pl.token){err.textContent='Token Wajib Diisi';err.classList.add('on');btn.disabled=false;btn.textContent='Mulai Bot';return}
}

let check;
try{
const r=await fetch('/api/account/check',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(pl)});
check=await r.json();
}catch(ex){
err.textContent='Error Jaringan';err.classList.add('on');btn.disabled=false;btn.textContent='Mulai Bot';return;
}

if(check.status!=='ok'){
err.textContent=check.error||'Login Gagal';err.classList.add('on');btn.disabled=false;btn.textContent='Mulai Bot';return;
}

const lvl=check.level||1;
const reg=(check.region||'').toUpperCase();
const isIND=(reg==='IND'||reg==='IN');
const mode=(lvl<=2||lvl>=40)?'BR':'LONE WOLF';
const modeHint=document.getElementById('mode-hint');
if(modeHint) modeHint.textContent='MODE: '+mode+' • otomatis sesuai level';

if(isIND){
const ok=await showConfirm(
'IND EXP Rendah',
'Lo harus setuju dulu sebelum nambah akun IND karena akun IND cuma dapat EXP rendah. Maksimal 5K EXP per 5 menit.',
'Ya, Setuju',
'Batal'
);
if(!ok){btn.disabled=false;btn.textContent='Mulai Bot';return}
}

btn.textContent='Menambahkan...';
try{
const r=await fetch('/api/account/add',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(pl)});
const d=await r.json();
if(d.status==='ok'){closeAdd();fetchS()}
else{err.textContent=d.error||'Gagal';err.classList.add('on')}
}catch(ex){err.textContent='Error Jaringan';err.classList.add('on')}
btn.disabled=false;btn.textContent='Mulai Bot';
});

async function delAcc(uid){
const ok=await showConfirm('Hapus Akun','Konfirmasi bahwa lo mau hapus akun ini permanen.','Ya, Hapus','Batal');
if(!ok)return;
try{await fetch('/api/account/delete',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({uid})});fetchS()}catch(e){}
}
async function toggleAcc(uid,action){
try{await fetch('/api/account/'+action,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({uid})});fetchS()}catch(e){}
}
async function refreshAcc(uid,btn){
if(btn)btn.classList.add('spin');
try{
await fetch('/api/account/refresh',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({uid})});
await fetchS();
}catch(e){}
setTimeout(()=>{if(btn)btn.classList.remove('spin')},700);
}

function esc(s){if(s==null)return'';return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#39;')}
function ago(ts){
if(!ts)return'--';
const s=Math.floor(Date.now()/1000-ts);
if(s<5)return'Baru Saja';
if(s<60)return s+' dtk lalu';
if(s<3600)return Math.floor(s/60)+' mnt lalu';
if(s<86400)return Math.floor(s/3600)+' jam lalu';
return Math.floor(s/86400)+' hr lalu'
}
function fmtLeft(s){
if(s<=0)return'Kadaluarsa';
const h=Math.floor(s/3600);
const m=Math.floor((s%3600)/60);
if(h>0)return h+'j '+m+'m';
return m+'m'
}

function render(data){
const g=document.getElementById('grid');
const a=data.accounts||[];
const slots=data.slots||0;
if(data.expired){window.location.href='/expired';return}
let h='';

a.forEach(acc=>{
const gained=acc.gained_exp||0;
const isPaused=acc.status==='PAUSED';
const isMatch=acc.status==='IN_MATCH';
const nickname=esc(acc.nickname||'Player');
const initial=nickname.charAt(0).toUpperCase()||'P';
const uid=esc(acc.uid);
const region=esc(acc.region||'IND');

let statusLabel, statusCls;
if(isPaused){statusLabel='DIJEDA';statusCls='status-top paused'}
else if(isMatch){statusLabel='DALAM MATCH';statusCls='status-top match'}
else if(acc.status==='ONLINE'){statusLabel='ONLINE';statusCls='status-top online'}
else {statusLabel='LIVE';statusCls='status-top'}

const cardMode=((acc.level||1)<=2||(acc.level||1)>=40)?'BR':'LONE WOLF';

h+='<div class="cc">';
h+='<div class="tagline">';
h+='<span class="pill">'+SVG.globe+' '+region+'</span>';
h+='<span class="pill uid">'+SVG.id+' '+uid+'</span>';
h+='<span class="'+statusCls+'"><span class="dot"></span>'+statusLabel+'</span>';
h+='<span class="pill" style="border-color:rgba(168,85,247,.35);color:#c084fc">MODE: '+cardMode+'</span>';
h+='</div>';
h+='<button class="refresh-btn" onclick="refreshAcc(\\''+uid+'\\',this)">'+SVG.refresh+' Refresh</button>';
h+='<div class="acc-head">';
h+='<div class="avatar">'+initial+'</div>';
h+='<div class="hinfo"><h3>'+nickname+'</h3><p>UID: '+uid+'</p></div>';
h+='<div class="lvl-badge">Lv.'+(acc.level||1)+'</div>';
h+='</div>';
h+='<div class="cd">';
h+='<div class="row"><span class="k">Dibuat</span><span class="v">'+ago(acc.created_at)+'</span></div>';
h+='<div class="row"><span class="k">Main</span><span class="v">'+(acc.matches_played||0)+' match</span></div>';
h+='<div class="row"><span class="k">Nickname</span><span class="v">'+nickname+'</span></div>';
h+='<div class="row"><span class="k">Region</span><span class="v">'+region+'</span></div>';
h+='</div>';
h+='<div class="timerow"><span class="td"></span> Update '+ago(acc.last_update)+'</div>';
h+='<div class="lvlrow"><span>Level</span><span class="v">'+(acc.level||1)+'</span></div>';
h+='<div class="matchrow"><span>Mode Aktif</span><span class="v">'+cardMode+'</span></div>';
h+='<div class="statrow">';
h+='<div class="sc"><div class="l">EXP</div><div class="v">'+(acc.current_exp||0).toLocaleString()+'</div></div>';
h+='<div class="sc"><div class="l">Awal</div><div class="v">'+(acc.initial_exp||0).toLocaleString()+'</div></div>';
h+='<div class="sc"><div class="l">Nambah</div><div class="v g">+'+gained.toLocaleString()+'</div></div>';
h+='</div>';
h+='<div class="matchrow"><span>Total Match</span><span class="v">'+(acc.matches_played||0)+'</span></div>';
h+='<div class="acc-actions">';
h+='<button onclick="toggleAcc(\\''+uid+'\\',\\'pause\\')">'+SVG.pause+' JEDA</button>';
h+='<button onclick="refreshAcc(\\''+uid+'\\',this)">'+SVG.refresh+' REFRESH</button>';
h+='<button class="danger" onclick="delAcc(\\''+uid+'\\')">'+SVG.trash+' HAPUS</button>';
h+='</div>';
h+='</div>';
});

if(a.length<slots){
h+='<button class="add" onclick="openAdd()">';
h+='<div class="plus">'+SVG.plus+'</div>';
h+='<div class="txt">Tambah Akun</div>';
h+='<div class="sub">SLOT '+(a.length+1)+' DARI '+slots+'</div>';
h+='</button>'
}
if(a.length===0&&slots===0){
h='<div class="empty"><div class="big">'+SVG.warn+'</div><p>Belum ada paket. Hubungi @malzwithyou</p></div>'
}

g.innerHTML=h;
document.getElementById('ui-u').textContent=data.username||'{{USERNAME}}';
document.getElementById('ui-t').textContent=fmtLeft(data.seconds_left||0);
document.getElementById('ui-s').textContent=a.length+'/'+slots
}

async function fetchS(){
try{
const r=await fetch('/api/stats');
if(r.status===401){window.location.href='/login';return}
const d=await r.json();
render(d)
}catch(e){}
}
document.getElementById('rf').addEventListener('click',async()=>{
const b=document.getElementById('rf');
b.classList.add('sp');
await fetchS();
setTimeout(()=>b.classList.remove('sp'),700)
});

document.getElementById('maint').classList.add('on');
document.getElementById('maint').addEventListener('click',e=>{
if(e.target.id==='maint')document.getElementById('maint').classList.remove('on');
});

fetchS();
setInterval(fetchS,3000);
</script>
</body>
</html>
"""

DASHBOARD_HTML = DASHBOARD_HTML.replace("__SVG_PAUSE__", _icon("pause", "currentColor", 13).replace('"', '\\"'))
DASHBOARD_HTML = DASHBOARD_HTML.replace("__SVG_PLAY__", _icon("play", "currentColor", 13).replace('"', '\\"'))
DASHBOARD_HTML = DASHBOARD_HTML.replace("__SVG_TRASH__", _icon("trash", "currentColor", 13).replace('"', '\\"'))
DASHBOARD_HTML = DASHBOARD_HTML.replace("__SVG_REFRESH__", _icon("refresh", "currentColor", 13).replace('"', '\\"'))
DASHBOARD_HTML = DASHBOARD_HTML.replace("__SVG_GLOBE__", _icon("globe", "currentColor", 11).replace('"', '\\"'))
DASHBOARD_HTML = DASHBOARD_HTML.replace("__SVG_ID__", _icon("id", "currentColor", 11).replace('"', '\\"'))
DASHBOARD_HTML = DASHBOARD_HTML.replace("__SVG_PLUS__", _icon("plus", "#00ffd5", 32).replace('"', '\\"'))
DASHBOARD_HTML = DASHBOARD_HTML.replace("__SVG_WARN__", _icon("warn", "currentColor", 44).replace('"', '\\"'))
DASHBOARD_HTML = DASHBOARD_HTML.replace("__ICON_REFRESH__", _icon("refresh", "currentColor", 14))
DASHBOARD_HTML = DASHBOARD_HTML.replace("__ICON_X__", _icon("x", "currentColor", 18))


# ==================== ADMIN LOGIN ====================
ADMIN_LOGIN_HTML = """<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Akses Admin — MALZ CODEX</title>
""" + _FONTS + """
<style>
""" + _CSS + """
body{display:flex;align-items:center;justify-content:center;padding:24px;background:radial-gradient(ellipse at top,#1a0a1a 0%,#000 60%)}
.wrap{width:100%;max-width:380px}
.badge{text-align:center;margin-bottom:30px}
.badge .ic{display:inline-flex;width:60px;height:60px;background:rgba(239,68,68,0.08);border:1px solid rgba(239,68,68,0.4);border-radius:14px;align-items:center;justify-content:center;margin-bottom:16px;color:var(--red)}
.badge .ic svg{width:26px;height:26px}
.badge h2{font-family:'Orbitron',sans-serif;font-size:17px;font-weight:800;letter-spacing:2px;text-transform:uppercase}
.badge p{font-size:10px;color:var(--red);margin-top:8px;letter-spacing:3px;text-transform:uppercase;opacity:0.8;font-weight:700}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:28px}
.f{margin-bottom:16px}
.f label{display:block;font-size:10px;font-weight:800;color:var(--mut);text-transform:uppercase;letter-spacing:1.5px;margin-bottom:7px}
.f input{width:100%;background:var(--card2);border:1px solid var(--line2);border-radius:10px;padding:12px 14px;color:#fff;font-size:15px;font-family:'Inter',sans-serif;outline:none;transition:border 0.2s}
.f input:focus{border-color:var(--red);box-shadow:0 0 0 3px rgba(239,68,68,0.15)}
.btn{width:100%;background:linear-gradient(135deg,#ef4444,#dc2626);color:#fff;border:none;border-radius:10px;padding:14px;font-family:'Orbitron',sans-serif;font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;cursor:pointer;transition:all 0.2s}
.btn:hover{box-shadow:0 8px 28px rgba(239,68,68,0.45)}
.err{background:rgba(239,68,68,0.1);border:1px solid rgba(239,68,68,0.3);color:var(--red);padding:12px;border-radius:10px;font-size:13px;margin-bottom:16px;display:none}
.err.on{display:block}
</style>
</head>
<body>
<div class="wrap">
<div class="badge">
<div class="ic">""" + _icon("warn", "currentColor", 26) + """</div>
<h2>Akses Admin</h2>
<p>Area Terbatas</p>
</div>
<div class="card">
<div id="err" class="err"></div>
<form id="f">
<div class="f"><label>Username Admin</label><input type="text" id="u" autocomplete="off" required></div>
<div class="f"><label>Password Admin</label><input type="password" id="p" autocomplete="off" required></div>
<button type="submit" class="btn">Masuk Panel</button>
</form>
</div>
</div>
<script>
document.getElementById('f').addEventListener('submit',async(e)=>{
e.preventDefault();
const err=document.getElementById('err');
err.classList.remove('on');
const u=document.getElementById('u').value.trim();
const p=document.getElementById('p').value;
try{
const r=await fetch(window.location.pathname,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({username:u,password:p})});
const d=await r.json();
if(d.status==='ok')window.location.href=d.redirect;
else{err.textContent=d.error||'Akses Ditolak';err.classList.add('on')}
}catch(ex){err.textContent='Error Jaringan';err.classList.add('on')}
});
</script>
</body>
</html>
"""


# ==================== ADMIN PANEL ====================
ADMIN_PANEL_HTML = """<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Panel Admin — MALZ CODEX</title>
""" + _FONTS + """
<style>
""" + _CSS + """
body{background:#000}
.top{background:rgba(0,0,0,0.95);border-bottom:1px solid var(--line);position:sticky;top:0;z-index:50}
.top-in{max-width:1400px;margin:0 auto;padding:14px 24px;display:flex;align-items:center;justify-content:space-between}
.logo{display:flex;align-items:center;gap:10px;font-family:'Orbitron',sans-serif;font-size:12px;font-weight:700;letter-spacing:2px}
.lm{width:30px;height:30px;background:linear-gradient(135deg,#ef4444,#b91c1c);color:#fff;border-radius:8px;display:inline-flex;align-items:center;justify-content:center;font-weight:900;font-size:14px}
.out{background:transparent;border:1px solid var(--line2);color:var(--mut);padding:8px 14px;border-radius:8px;font-family:'Orbitron',sans-serif;font-size:10px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;text-decoration:none;transition:all 0.2s}
.out:hover{border-color:var(--red);color:var(--red)}
.main{max-width:1400px;margin:0 auto;padding:28px 24px 80px}
.st{font-family:'Orbitron',sans-serif;font-size:14px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;margin-bottom:14px;display:flex;align-items:center;gap:10px}
.st::before{content:'';width:3px;height:16px;background:#00ffd5;border-radius:2px}
.panel{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:22px;margin-bottom:28px}
.grid4{display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:14px;margin-bottom:18px}
@media(max-width:900px){.grid4{grid-template-columns:1fr 1fr}}
@media(max-width:600px){.grid4{grid-template-columns:1fr}}
.f label{display:block;font-size:10px;font-weight:800;color:var(--mut);text-transform:uppercase;letter-spacing:1.5px;margin-bottom:6px}
.f input{width:100%;background:var(--card2);border:1px solid var(--line2);border-radius:10px;padding:11px 14px;color:#fff;font-size:14px;font-family:'Inter',sans-serif;outline:none;transition:border 0.2s}
.f input:focus{border-color:#00ffd5}
.btn{background:linear-gradient(135deg,#00ffd5,#00b894);color:#000;border:none;padding:12px 26px;border-radius:10px;font-family:'Orbitron',sans-serif;font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;cursor:pointer;transition:all 0.2s}
.btn:hover{box-shadow:0 8px 24px rgba(0,255,213,0.4)}
.hint{font-size:11px;color:var(--mut);margin-top:10px}
.tw{background:var(--card);border:1px solid var(--line);border-radius:14px;overflow:hidden}
table{width:100%;border-collapse:collapse;font-size:13px}
th{text-align:left;padding:14px 16px;font-family:'Orbitron',sans-serif;font-size:9px;font-weight:700;color:var(--mut);letter-spacing:1.5px;text-transform:uppercase;border-bottom:1px solid var(--line2);background:var(--card2)}
td{padding:14px 16px;border-bottom:1px solid var(--line);vertical-align:middle;color:#fff}
tbody tr:last-child td{border-bottom:none}
tbody tr:hover{background:rgba(255,255,255,0.02)}
.mono{font-family:'JetBrains Mono',monospace;font-size:12px}
.muted{color:var(--mut)}
.badge{display:inline-block;padding:4px 10px;border-radius:6px;font-family:'Orbitron',sans-serif;font-size:9px;font-weight:700;letter-spacing:1px}
.ba{background:rgba(0,255,213,0.15);color:var(--cyan);border:1px solid rgba(0,255,213,0.3)}
.be{background:rgba(239,68,68,0.15);color:var(--red);border:1px solid rgba(239,68,68,0.3)}
.acts{display:flex;gap:6px;flex-wrap:wrap}
.mini{background:var(--card2);border:1px solid var(--line2);color:var(--mut);padding:7px 11px;font-family:'Orbitron',sans-serif;font-size:9px;font-weight:700;letter-spacing:1px;border-radius:6px;cursor:pointer;transition:all 0.15s}
.mini:hover{border-color:#00ffd5;color:#00ffd5}
.mini.danger:hover{border-color:var(--red);color:var(--red)}
.empty{text-align:center;padding:60px 20px;color:var(--mut);font-size:14px}
.toast{position:fixed;bottom:24px;right:24px;background:var(--card2);border:1px solid #00ffd5;color:#fff;padding:14px 20px;border-radius:10px;font-size:13px;font-weight:700;box-shadow:0 8px 32px rgba(0,0,0,0.6);opacity:0;transform:translateY(20px);transition:all 0.3s;pointer-events:none;z-index:200;max-width:360px}
.toast.on{opacity:1;transform:translateY(0)}
.toast.err{border-color:var(--red)}
</style>
</head>
<body>
<div class="top">
<div class="top-in">
<div class="logo"><span class="lm">A</span><span>MALZ CODEX — ADMIN</span></div>
<a class="out" href="/admin/mehedi/levelup/adm-dash/logout">Logout</a>
</div>
</div>
<div class="main">
<div class="st">Buat User Baru</div>
<div class="panel">
<div class="grid4">
<div class="f"><label>Username</label><input type="text" id="nu" autocomplete="off"></div>
<div class="f"><label>Password</label><input type="text" id="np" autocomplete="off"></div>
<div class="f"><label>Slot</label><input type="number" id="ns" value="3" min="1" max="20"></div>
<div class="f"><label>Durasi (Jam)</label><input type="number" id="nh" value="24" min="1" max="8760"></div>
</div>
<button class="btn" onclick="createU()">Buat User</button>
<div class="hint">Timer langsung mulai saat user dibuat.</div>
</div>
<div class="st">Semua User</div>
<div class="tw" id="tbl"><div class="empty">Memuat...</div></div>
</div>
<div class="toast" id="toast"></div>
<script>
function esc(s){if(s==null)return'';return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#39;')}
function toast(msg,err){const t=document.getElementById('toast');t.textContent=msg;t.classList.toggle('err',!!err);t.classList.add('on');setTimeout(()=>t.classList.remove('on'),2600)}
function fmtLeft(exp){const now=Math.floor(Date.now()/1000);const s=exp-now;if(s<=0)return{t:'Kadaluarsa',e:true};const h=Math.floor(s/3600);const m=Math.floor((s%3600)/60);return{t:h+'j '+m+'m',e:false}}
function fmtDate(ts){return new Date(ts*1000).toLocaleString('id-ID')}
async function createU(){
const u=document.getElementById('nu').value.trim();
const p=document.getElementById('np').value.trim();
const s=parseInt(document.getElementById('ns').value);
const h=parseInt(document.getElementById('nh').value);
if(!u||!p){toast('Username Dan Password Wajib',true);return}
if(s<1||s>20){toast('Slot Harus 1-20',true);return}
if(h<1||h>8760){toast('Jam Harus 1-8760',true);return}
try{
const r=await fetch('/api/admin/create-user',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({username:u,password:p,slots:s,hours:h})});
const d=await r.json();
if(d.status==='ok'){toast('User Dibuat: '+u);document.getElementById('nu').value='';document.getElementById('np').value='';loadU()}
else{toast(d.error||'Gagal',true)}
}catch(e){toast('Error Jaringan',true)}
}
async function loadU(){
try{
const r=await fetch('/api/admin/list-users');
const d=await r.json();
if(d.status!=='ok')return;
const users=d.users||[];
const w=document.getElementById('tbl');
if(users.length===0){w.innerHTML='<div class="empty">Belum Ada User</div>';return}
let h='<table><thead><tr>';
h+='<th>Username</th><th>Slot</th><th>Terpakai</th><th>Kadaluarsa</th><th>Dibuat</th><th>Aksi</th>';
h+='</tr></thead><tbody>';
users.forEach(u=>{
const e=fmtLeft(u.expires_at);
const b=e.e?'<span class="badge be">Kadaluarsa</span>':'<span class="badge ba">'+e.t+'</span>';
h+='<tr>';
h+='<td class="mono">'+esc(u.username)+'</td>';
h+='<td class="mono">'+u.slots+'</td>';
h+='<td class="mono muted">'+(u.used_slots||0)+'</td>';
h+='<td>'+b+'</td>';
h+='<td class="muted">'+fmtDate(u.created_at)+'</td>';
h+='<td><div class="acts">';
h+='<button class="mini" onclick="ext(\\''+esc(u.username)+'\\',24)">+24J</button>';
h+='<button class="mini" onclick="slot(\\''+esc(u.username)+'\\',1)">+1 Slot</button>';
h+='<button class="mini danger" onclick="delU(\\''+esc(u.username)+'\\')">Hapus</button>';
h+='</div></td>';
h+='</tr>'
});
h+='</tbody></table>';
w.innerHTML=h
}catch(e){}
}
async function ext(u,h){
try{
const r=await fetch('/api/admin/extend-time',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({username:u,hours:h})});
const d=await r.json();
if(d.status==='ok'){toast('Ditambah '+h+'j untuk '+u);loadU()}
else{toast(d.error||'Gagal',true)}
}catch(e){toast('Error Jaringan',true)}
}
async function slot(u,c){
try{
const r=await fetch('/api/admin/add-slot',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({username:u,count:c})});
const d=await r.json();
if(d.status==='ok'){toast('Tambah '+c+' slot untuk '+u);loadU()}
else{toast(d.error||'Gagal',true)}
}catch(e){toast('Error Jaringan',true)}
}
async function delU(u){
if(!confirm('Hapus user '+u+'? Semua data akan hilang.'))return;
try{
const r=await fetch('/api/admin/delete-user',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({username:u})});
const d=await r.json();
if(d.status==='ok'){toast('Dihapus: '+u);loadU()}
else{toast(d.error||'Gagal',true)}
}catch(e){toast('Error Jaringan',true)}
}
loadU();
setInterval(loadU,5000);
</script>
</body>
</html>
"""


ALL_TEMPLATES = {
    "home": HOME_HTML,
    "login": LOGIN_HTML,
    "plans": PLANS_HTML,
    "dashboard": DASHBOARD_HTML,
    "expired": EXPIRED_HTML,
    "admin_login": ADMIN_LOGIN_HTML,
    "admin_panel": ADMIN_PANEL_HTML,
}