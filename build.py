"""Builds the static site: legal/*.txt (the texts the game ships) plus the pages below become plain HTML in
the repo root. Run `python build.py` after editing, commit the result. No build step on Cloudflare."""
import html
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))
EMAIL = "noobstudios.in@gmail.com"
NAME = "5 Cards"
STUDIO = "Noob Studios"
SITE = "https://5cards.noobstudios.in"

CSS = """
:root{
--navy:#081538;--navy2:#0f2a73;--blue:#1d4ed8;--sky:#4aa3ff;--gold:#ffc83d;--gold2:#ffe08a;--pink:#ff5d8f;--mint:#2ee6a6;--violet:#7c5cff;
--ink:#101b3a;--muted:#5a6788;--bg:#f4f6fd;--card:#fff;--line:#e2e8f6;--radius:20px;
--shadow:0 20px 60px rgba(8,21,56,.16);
}
*{box-sizing:border-box}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{margin:0;font:17px/1.65 "Inter",system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;color:var(--ink);background:var(--bg);overflow-x:hidden}
img{max-width:100%;display:block}
a{color:var(--blue)}
h1,h2,h3{font-family:"Poppins","Inter",system-ui,sans-serif;line-height:1.12;letter-spacing:-.015em;margin:0}
.container{max-width:1160px;margin:0 auto;padding:0 24px}

/* header */
.site-header{position:sticky;top:0;z-index:30;background:rgba(8,21,56,.88);backdrop-filter:saturate(1.5) blur(14px);border-bottom:1px solid rgba(255,255,255,.08)}
.site-header .container{display:flex;align-items:center;gap:22px;height:72px}
.brand{display:flex;align-items:center;gap:12px;color:#fff;text-decoration:none;font:800 20px "Poppins",sans-serif}
.brand img{height:46px;width:auto}
.nav{margin-left:auto;display:flex;align-items:center;gap:4px}
.nav a{color:#c9d6f5;text-decoration:none;font-size:15px;font-weight:500;padding:9px 13px;border-radius:10px}
.nav a:hover{color:#fff;background:rgba(255,255,255,.08)}
.nav a[aria-current]{color:var(--gold2)}
.nav .cta{background:linear-gradient(180deg,#ffd75e,#ffb81f);color:#3a2a00;font-weight:700;margin-left:8px;box-shadow:0 6px 18px rgba(255,184,31,.35)}
.nav .cta:hover{color:#3a2a00;filter:brightness(1.05)}
@media(max-width:860px){.nav a:not(.cta){display:none}}

/* phone frame: the screen keeps the exact 450:1000 shape of the screenshot, so nothing is cropped or stretched */
.phone{position:relative;container-type:inline-size;border-radius:13% / 5.85%;background:linear-gradient(150deg,#3b4d82 0%,#111a38 45%,#070c1c 100%);box-shadow:0 34px 70px rgba(3,8,30,.5),inset 0 0 0 1.5px rgba(255,255,255,.16)}
.phone:before,.phone:after{content:"";position:absolute;width:max(2px,1.1cqw);border-radius:2px;background:#222c4d}
.phone:before{left:max(-2px,-1.1cqw);top:18%;height:7%}
.phone:after{right:max(-2px,-1.1cqw);top:24%;height:12%}
.phone .screen{margin:3.4cqw;border-radius:10cqw;overflow:hidden;aspect-ratio:450/1000;background:#000}
.phone .screen img{width:100%;height:100%;object-fit:cover}

/* hero */
.hero{position:relative;overflow:hidden;color:#fff;background:
radial-gradient(900px 520px at 80% 28%,rgba(74,163,255,.42),transparent 62%),
radial-gradient(700px 460px at 8% 95%,rgba(255,93,143,.2),transparent 60%),
radial-gradient(600px 400px at 50% 0%,rgba(124,92,255,.28),transparent 65%),
linear-gradient(165deg,var(--navy) 0%,var(--navy2) 100%)}
.suits{position:absolute;inset:0;pointer-events:none;font:700 42px/1 "Poppins",sans-serif;color:rgba(255,255,255,.07)}
.suits span{position:absolute}
.hero .container{position:relative;display:grid;grid-template-columns:1.02fr .98fr;gap:30px;align-items:center;padding-top:64px;padding-bottom:72px}
.hero-copy{padding:0}
.hero-logo{width:min(190px,50%);margin:0 0 14px -6px;filter:drop-shadow(0 14px 28px rgba(0,0,0,.35))}
.eyebrow{display:inline-block;font:700 12.5px "Poppins",sans-serif;letter-spacing:.14em;text-transform:uppercase;color:var(--gold2);background:rgba(255,200,61,.12);border:1px solid rgba(255,200,61,.32);padding:7px 15px;border-radius:999px}
.hero h1{font-size:clamp(38px,4.8vw,58px);margin:20px 0 18px;font-weight:800}
.hero h1 em{font-style:normal;background:linear-gradient(90deg,var(--gold),var(--pink));-webkit-background-clip:text;background-clip:text;color:transparent}
.lead{font-size:20px;color:#cfdcff;max-width:540px;margin:0}
.actions{display:flex;gap:14px;flex-wrap:wrap;margin-top:34px}
.btn{display:inline-flex;align-items:center;gap:12px;padding:14px 26px;border-radius:15px;font:700 16px "Poppins",sans-serif;text-decoration:none;border:2px solid transparent;transition:transform .15s}
.btn:hover{transform:translateY(-2px)}
.btn.gold{background:linear-gradient(180deg,#ffd75e,#ffb81f);color:#3a2a00;box-shadow:0 10px 28px rgba(255,184,31,.4)}
.btn.ghost{color:#fff;border-color:rgba(255,255,255,.35)}
.btn.ghost:hover{background:rgba(255,255,255,.09)}
.btn small{display:block;font:500 11px "Inter",sans-serif;opacity:.75;margin-bottom:-2px}
.btn svg{width:26px;height:26px;fill:currentColor}
.chips{display:flex;gap:10px;flex-wrap:wrap;margin-top:30px}
.chip{font-size:14px;color:#d6e2ff;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.14);padding:7px 14px;border-radius:999px}
.hero-art{position:relative;width:100%;max-width:560px;margin:0 auto;aspect-ratio:1/1.16}
.hero-art .phone{position:absolute}
.hero-art .c{width:48%;left:26%;top:0;z-index:3}
.hero-art .l{width:38%;left:0;top:15%;transform:rotate(-8deg);z-index:2}
.hero-art .r{width:38%;right:0;top:15%;transform:rotate(8deg);z-index:2}
@media(max-width:940px){
.hero .container{grid-template-columns:1fr;padding-top:40px}
.hero-copy{text-align:center}
.hero-logo{margin:0 auto 14px}.lead{margin:0 auto}.actions,.chips{justify-content:center}
.hero-art{max-width:460px}
}

/* sections */
section{padding:92px 0}
.section-head{max-width:680px;margin:0 auto 56px;text-align:center}
.section-head h2{font-size:clamp(30px,4vw,46px);margin:12px 0;font-weight:800}
.section-head p{color:var(--muted);font-size:18px;margin:0}
.kicker{font:700 12.5px "Poppins",sans-serif;letter-spacing:.15em;text-transform:uppercase;color:var(--blue)}
.band{background:#fff;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.ticker{background:linear-gradient(90deg,var(--violet),var(--blue),var(--sky));color:#fff;padding:16px 0;font:700 15px "Poppins",sans-serif;letter-spacing:.06em;text-transform:uppercase}
.ticker .container{display:flex;justify-content:space-between;gap:18px;flex-wrap:wrap}
.ticker span{white-space:nowrap}
.ticker i{font-style:normal;color:var(--gold2)}
@media(max-width:700px){.ticker .container{justify-content:center}}

.row{display:grid;grid-template-columns:1fr 1fr;gap:72px;align-items:center;margin:0 0 100px}
.row:last-child{margin-bottom:0}
.row.flip .row-art{order:-1}
.row h3{font-size:clamp(28px,3.4vw,40px);margin:12px 0 16px;font-weight:800}
.row p{color:var(--muted);margin:0 0 14px}
.ticks{list-style:none;padding:0;margin:20px 0 0}
.ticks li{position:relative;padding-left:34px;margin:11px 0}
.ticks li:before{content:"";position:absolute;left:0;top:4px;width:22px;height:22px;border-radius:50%;background:var(--gold) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20'%3E%3Cpath d='M5.5 10.5l3 3 6-7' fill='none' stroke='%233a2a00' stroke-width='2.4' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/22px no-repeat}
.row-art{position:relative;display:flex;justify-content:center;align-items:center;min-height:520px}
.row-art:before{content:"";position:absolute;width:78%;aspect-ratio:1;border-radius:50%;background:radial-gradient(circle,rgba(74,163,255,.32),rgba(124,92,255,.16) 55%,transparent 70%);filter:blur(6px)}
.row.flip .row-art:before{background:radial-gradient(circle,rgba(255,93,143,.26),rgba(255,200,61,.14) 55%,transparent 70%)}
.row-art .phone{position:relative;width:min(290px,72%)}
.row-art.duo{gap:26px}
.row-art.duo .phone{width:min(230px,44%)}
@media(max-width:900px){.row,.row.flip{grid-template-columns:1fr;gap:34px;margin-bottom:72px}.row.flip .row-art{order:0}.row-art{min-height:0}}

.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}
@media(max-width:940px){.grid3{grid-template-columns:repeat(2,1fr)}}
@media(max-width:600px){.grid3{grid-template-columns:1fr}}
.tile{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:30px;transition:transform .2s,box-shadow .2s}
.tile:hover{transform:translateY(-4px);box-shadow:var(--shadow)}
.tile .ico{width:52px;height:52px;border-radius:16px;display:grid;place-items:center;margin-bottom:18px;background:linear-gradient(145deg,var(--blue),var(--sky))}
.tile:nth-child(2) .ico{background:linear-gradient(145deg,var(--violet),#b49bff)}
.tile:nth-child(3) .ico{background:linear-gradient(145deg,#ff9a3d,var(--gold))}
.tile:nth-child(4) .ico{background:linear-gradient(145deg,var(--mint),#7df2cb)}
.tile:nth-child(5) .ico{background:linear-gradient(145deg,var(--pink),#ff9ab9)}
.tile .ico svg{width:27px;height:27px;stroke:#fff;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.tile h3{font-size:20px;margin:0 0 8px}
.tile p{margin:0;color:var(--muted);font-size:16px}

.steps{counter-reset:s;display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:26px}
.step{position:relative;padding:34px 28px 28px;background:var(--card);border:1px solid var(--line);border-radius:var(--radius)}
.step:before{counter-increment:s;content:counter(s);position:absolute;top:-20px;left:26px;width:42px;height:42px;border-radius:50%;background:linear-gradient(180deg,#ffd75e,#ffb81f);color:#3a2a00;font:800 19px/42px "Poppins",sans-serif;text-align:center;box-shadow:0 8px 18px rgba(255,184,31,.4)}
.step h3{font-size:20px;margin:0 0 8px}
.step p{margin:0;color:var(--muted);font-size:16px}

.party{position:relative;overflow:hidden;color:#fff;text-align:center;background:
radial-gradient(500px 300px at 15% 20%,rgba(255,93,143,.35),transparent 70%),
radial-gradient(520px 320px at 85% 80%,rgba(46,230,166,.28),transparent 70%),
linear-gradient(160deg,#2a1b7a,#0f2a73)}
.party h2{font-size:clamp(32px,4.4vw,52px);font-weight:800;margin:12px 0 14px}
.party p{color:#d7e0ff;max-width:600px;margin:0 auto;font-size:19px}
.party .chips{justify-content:center;margin-top:26px}

.faq{max-width:780px;margin:0 auto}
.faq details{background:var(--card);border:1px solid var(--line);border-radius:16px;margin:0 0 12px;padding:0 24px}
.faq summary{cursor:pointer;list-style:none;padding:20px 28px 20px 0;font:600 18px "Poppins",sans-serif;position:relative}
.faq summary::-webkit-details-marker{display:none}
.faq summary:after{content:"+";position:absolute;right:0;top:50%;transform:translateY(-50%);font-size:26px;color:var(--blue);font-weight:500}
.faq details[open] summary:after{content:"\\2212"}
.faq details p{margin:0 0 20px;color:var(--muted)}

.studio{background:#fff;border-top:1px solid var(--line)}
.studio .container{display:grid;grid-template-columns:260px 1fr;gap:56px;align-items:center;max-width:920px}
.studio img{width:100%;filter:drop-shadow(0 16px 28px rgba(8,21,56,.18))}
.studio h2{font-size:clamp(28px,3.4vw,38px);font-weight:800;margin:10px 0 14px}
.studio p{color:var(--muted);margin:0 0 12px}
@media(max-width:720px){.studio .container{grid-template-columns:1fr;text-align:center;gap:26px}.studio img{max-width:220px;margin:0 auto}}

.cta-band{background:linear-gradient(165deg,var(--navy),var(--navy2));color:#fff;text-align:center;position:relative;overflow:hidden}
.cta-band:before{content:"";position:absolute;inset:0;background:radial-gradient(700px 320px at 50% 0,rgba(74,163,255,.34),transparent 70%)}
.cta-band .container{position:relative}
.cta-band img{width:190px;margin:0 auto 10px;filter:drop-shadow(0 14px 26px rgba(0,0,0,.4))}
.cta-band h2{font-size:clamp(32px,4.4vw,48px);margin:8px 0 14px;font-weight:800}
.cta-band p{color:#cfdcff;max-width:540px;margin:0 auto 30px;font-size:19px}

/* document pages */
.page-hero{position:relative;overflow:hidden;background:radial-gradient(700px 300px at 85% 0,rgba(74,163,255,.38),transparent 65%),linear-gradient(165deg,var(--navy),var(--navy2));color:#fff;padding:60px 0 56px}
.page-hero h1{font-size:clamp(34px,4.6vw,50px);margin:14px 0 10px;font-weight:800}
.page-hero p{margin:0;color:#b9c9f3}
.doc{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);box-shadow:var(--shadow);padding:46px clamp(22px,5vw,60px);margin:-28px auto 80px;max-width:880px;position:relative}
.doc h2{font-size:23px;margin:42px 0 10px;padding-top:28px;border-top:1px solid var(--line);font-weight:700}
.doc h2:first-of-type{margin-top:8px}
.doc p,.doc li{color:#2a3858}
.doc ul,.doc ol{padding-left:22px}
.doc li{margin:7px 0}
.doc .meta{color:var(--muted);font-size:15px;margin-top:0}
.toc{background:var(--bg);border:1px solid var(--line);border-radius:14px;padding:16px 22px;margin:0 0 8px}
.toc b{font:600 13px "Poppins",sans-serif;letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
.toc ol{columns:2;column-gap:30px;margin:8px 0 0;padding-left:20px;font-size:15px}
.toc a{text-decoration:none}
@media(max-width:640px){.toc ol{columns:1}}
.note{background:#fff8e1;border:1px solid #ffe29a;border-left:4px solid var(--gold);border-radius:12px;padding:14px 18px;margin:22px 0}
code{background:#eef2fb;padding:2px 7px;border-radius:6px;font-size:.92em}
.cards2{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:18px;margin:22px 0}
.cards2 .tile{padding:24px}
.cards2 .tile:hover{transform:none;box-shadow:none}

/* footer */
.site-footer{background:#060f2b;color:#9fb2e4;padding:60px 0 30px;font-size:15px}
.fgrid{display:grid;grid-template-columns:1.5fr 1fr 1fr;gap:40px}
.site-footer h4{margin:0 0 14px;color:#fff;font:600 13px "Poppins",sans-serif;letter-spacing:.12em;text-transform:uppercase}
.site-footer a{display:block;color:#b9c9f3;text-decoration:none;padding:4px 0}
.site-footer a:hover{color:var(--gold2)}
.site-footer .logos{display:flex;align-items:center;gap:20px;margin-bottom:16px}
.site-footer .logos img{height:64px;width:auto}
.fine{border-top:1px solid rgba(255,255,255,.1);margin-top:36px;padding-top:22px;font-size:13.5px;color:#7f93c8;line-height:1.6}
@media(max-width:760px){.fgrid{grid-template-columns:1fr}}

/* ---- motion + card styling ---- */
.hero-art .c{--r:0deg}.hero-art .l{--r:-8deg}.hero-art .r{--r:8deg}
.hero-art .l,.hero-art .r{transform:rotate(var(--r))}
.hero-art .phone{animation:deal 1s cubic-bezier(.2,.9,.25,1) both,bob 7s ease-in-out 1.2s infinite}
.hero-art .c{animation-delay:.1s,1.2s}.hero-art .l{animation-delay:.35s,2s}.hero-art .r{animation-delay:.55s,2.8s}
@keyframes deal{from{opacity:0;transform:translateY(90px) scale(.86) rotate(0deg)}to{opacity:1;transform:translateY(0) scale(1) rotate(var(--r))}}
@keyframes bob{0%,100%{transform:translateY(0) rotate(var(--r))}50%{transform:translateY(-12px) rotate(var(--r))}}
.hero-copy>*{animation:rise .8s cubic-bezier(.2,.8,.2,1) both}
.hero-copy>:nth-child(2){animation-delay:.08s}.hero-copy>:nth-child(3){animation-delay:.16s}.hero-copy>:nth-child(4){animation-delay:.24s}.hero-copy>:nth-child(5){animation-delay:.32s}.hero-copy>:nth-child(6){animation-delay:.4s}
@keyframes rise{from{opacity:0;transform:translateY(26px)}to{opacity:1;transform:none}}
.suits span{animation:drift 9s ease-in-out infinite}
.suits span:nth-child(2n){animation-duration:12s;animation-direction:reverse}
@keyframes drift{0%,100%{translate:0 0}50%{translate:0 -16px}}
.js .rv{opacity:0}
.js .rv.in{opacity:1;animation:rise .8s cubic-bezier(.2,.8,.2,1) var(--d,0s) backwards}
.js .pcard.rv.in{animation:dealcard .85s cubic-bezier(.2,.85,.25,1) var(--d,0s) backwards}
@keyframes dealcard{from{opacity:0;transform:translateY(70px) rotate(var(--r0,-7deg)) scale(.9)}to{opacity:1;transform:none}}

.ticker{overflow:hidden;padding:15px 0}
.ticker .track{display:flex;gap:30px;width:max-content;animation:marquee 32s linear infinite}
.ticker .track span,.ticker .track i{white-space:nowrap}
.ticker:hover .track{animation-play-state:paused}
@keyframes marquee{to{transform:translateX(-50%)}}

/* store badge */
.gp{display:inline-flex;align-items:center;gap:13px;background:#000;color:#fff;text-decoration:none;border:1.5px solid #a6a6a6;border-radius:13px;padding:9px 22px 9px 16px;transition:transform .2s,box-shadow .2s,border-color .2s;box-shadow:0 10px 26px rgba(0,0,0,.35)}
.gp:hover{transform:translateY(-3px) scale(1.02);border-color:#fff;box-shadow:0 16px 34px rgba(0,0,0,.45)}
.gp svg{width:34px;height:34px;flex:none}
.gp span{display:block;text-align:left;font:600 11px/1.1 "Inter",sans-serif;letter-spacing:.08em;text-transform:uppercase;color:#e8e8e8}
.gp b{display:block;font:600 24px/1.1 "Poppins",sans-serif;letter-spacing:-.01em;margin-top:2px}
.actions{align-items:center}

/* playing-card features */
.fan{display:grid;grid-template-columns:repeat(3,1fr);gap:30px 26px}
@media(max-width:940px){.fan{grid-template-columns:repeat(2,1fr)}}
@media(max-width:600px){.fan{grid-template-columns:1fr;max-width:360px;margin:0 auto}}
.pcard{--c:#101b3a;position:relative;min-height:330px;padding:62px 28px 56px;text-align:center;background:linear-gradient(165deg,#fff 0%,#f4f7ff 100%);border-radius:22px;border:1px solid #d9e1f5;box-shadow:0 2px 0 #fff inset,0 14px 34px rgba(8,21,56,.1);transition:transform .35s cubic-bezier(.2,.8,.2,1),box-shadow .35s;overflow:hidden}
.pcard:before{content:"";position:absolute;inset:9px;border:1.5px solid rgba(16,27,58,.09);border-radius:15px;pointer-events:none}
.pcard:after{content:"";position:absolute;top:0;left:-70%;width:45%;height:100%;background:linear-gradient(105deg,transparent,rgba(255,255,255,.75),transparent);transform:skewX(-18deg);transition:left .7s ease;pointer-events:none}
.pcard:hover{transform:translateY(-12px) rotate(var(--tilt,-1.5deg));box-shadow:0 30px 56px rgba(8,21,56,.2)}
.pcard:hover:after{left:130%}
.pcard:nth-child(2n){--tilt:1.5deg}
.pcard.red{--c:#e0245e}.pcard.blk{--c:#101b3a}
.pcard .idx{position:absolute;display:flex;flex-direction:column;align-items:center;line-height:1;font:800 22px "Poppins",sans-serif;color:var(--c);z-index:1}
.pcard .idx i{font-style:normal;font-size:20px;margin-top:3px}
.pcard .idx.tl{top:20px;left:22px}
.pcard .idx.br{bottom:20px;right:22px;transform:rotate(180deg)}
.pcard .ico{width:68px;height:68px;border-radius:50%;display:grid;place-items:center;margin:0 auto 20px;background:linear-gradient(145deg,var(--blue),var(--sky));box-shadow:0 12px 24px rgba(29,78,216,.28);transition:transform .4s cubic-bezier(.2,.8,.2,1)}
.pcard:hover .ico{transform:scale(1.12) rotate(-6deg)}
.pcard:nth-child(2) .ico{background:linear-gradient(145deg,var(--violet),#b49bff);box-shadow:0 12px 24px rgba(124,92,255,.3)}
.pcard:nth-child(3) .ico{background:linear-gradient(145deg,#ff9a3d,var(--gold));box-shadow:0 12px 24px rgba(255,154,61,.3)}
.pcard:nth-child(4) .ico{background:linear-gradient(145deg,var(--mint),#7df2cb);box-shadow:0 12px 24px rgba(46,230,166,.3)}
.pcard:nth-child(5) .ico{background:linear-gradient(145deg,var(--pink),#ff9ab9);box-shadow:0 12px 24px rgba(255,93,143,.3)}
.pcard:nth-child(6) .ico{background:linear-gradient(145deg,#ef4444,#ff8a8a);box-shadow:0 12px 24px rgba(239,68,68,.3)}
.pcard .ico svg{width:32px;height:32px;stroke:#fff;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.pcard h3{font-size:21px;margin:0 0 10px}
.pcard p{margin:0;color:var(--muted);font-size:16px}

.step{transition:transform .3s,box-shadow .3s;overflow:visible}
.step:hover{transform:translateY(-6px);box-shadow:var(--shadow)}
.step:after{content:"\\2660";position:absolute;right:20px;bottom:10px;font-size:34px;color:rgba(16,27,58,.07)}
.step:nth-child(2):after{content:"\\2665";color:rgba(224,36,94,.1)}
.step:nth-child(3):after{content:"\\2666";color:rgba(224,36,94,.1)}
.row-art .phone{transition:transform .5s cubic-bezier(.2,.8,.2,1)}
.row-art:hover .phone{transform:translateY(-8px) rotate(-1.5deg)}
.faq details{transition:box-shadow .25s,border-color .25s}
.faq details:hover{border-color:#c5d3f5}
.faq details[open]{box-shadow:0 12px 30px rgba(8,21,56,.08)}
.faq details[open] p{animation:rise .35s ease both}
@media(prefers-reduced-motion:reduce){*,*:before,*:after{animation:none!important;transition:none!important;scroll-behavior:auto!important}.js .rv{opacity:1}}
"""

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Poppins:wght@600;700;800&display=swap" rel="stylesheet">'

NAV = [("/privacy/", "Privacy"), ("/terms/", "Terms"), ("/delete-account/", "Delete account"), ("/contact/", "Contact")]


def shell(path, title, description, body):
    links = "".join('<a href="%s"%s>%s</a>' % (h, ' aria-current="page"' if h == path else "", t) for h, t in NAV)
    out = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<meta name="theme-color" content="#081538">
<script>document.documentElement.classList.add("js")</script>
<link rel="canonical" href="%(url)s">
<link rel="icon" href="/assets/favicon.png">
<meta property="og:type" content="website">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:image" content="%(site)s/assets/icon.png">
<meta name="twitter:card" content="summary">
%(fonts)s
<style>%(css)s</style>
</head>
<body>
<header class="site-header"><div class="container">
<a class="brand" href="/" aria-label="%(name)s home"><img src="/assets/logo-5cards-sm.png" alt="" width="50" height="46">%(name)s</a>
<nav class="nav" aria-label="Main">%(links)s<a class="cta" href="/#play">Play</a></nav>
</div></header>
%(body)s
<footer class="site-footer"><div class="container">
<div class="fgrid">
<div><div class="logos"><img src="/assets/logo-5cards.webp" alt="%(name)s" width="70" height="64"><img src="/assets/logo-studio.webp" alt="%(studio)s" width="81" height="64"></div>
<p style="margin:0;max-width:360px">%(name)s is a fast, friendly multiplayer card game for Android, made with love by %(studio)s.</p></div>
<div><h4>Game</h4><a href="/#features">Features</a><a href="/#screens">Screenshots</a><a href="/#faq">FAQ</a><a href="/#play">Get the game</a></div>
<div><h4>Legal and support</h4><a href="/privacy/">Privacy Policy</a><a href="/terms/">Terms of Service</a><a href="/delete-account/">Delete your account</a><a href="mailto:%(email)s">%(email)s</a></div>
</div>
<div class="fine">&copy; 2026 %(studio)s. All rights reserved. %(name)s is a game of skill and luck played for fun: there is no gambling and no cash prizes, and coins cannot be turned into money. Coins can be earned in the game or bought with optional in-app purchases. Google Play is a trademark of Google LLC. Facebook is a trademark of Meta Platforms, Inc.</div>
</div></footer>
<script>
(function(){var els=document.querySelectorAll(".rv");if(!els.length)return;
if(!("IntersectionObserver" in window)){els.forEach(function(e){e.classList.add("in")});return}
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add("in");io.unobserve(e.target)}})},{threshold:.12,rootMargin:"0px 0px -5%% 0px"});
els.forEach(function(e){io.observe(e)});
setTimeout(function(){els.forEach(function(e){e.classList.add("in")})},4000);})();
</script>
</body>
</html>
""" % {"title": html.escape(title), "desc": html.escape(description), "url": SITE + path, "site": SITE, "fonts": FONTS, "css": CSS,
       "name": NAME, "links": links, "body": body, "studio": STUDIO, "email": EMAIL}
    d = os.path.join(ROOT, path.strip("/"))
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8", newline="\n") as f:
        f.write(out)


def inline(s):
    s = html.escape(s, quote=False)
    return re.sub(r"([A-Za-z0-9._+-]+@[A-Za-z0-9.-]+\.[a-z]{2,})", r'<a href="mailto:\1">\1</a>', s)


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def legal(src):
    """The in-game legal text: '# title', 'Effective date: ...', '## n. Heading', '- bullet', paragraphs.
    Returns (effective date line, body html with a table of contents)."""
    lines = open(os.path.join(ROOT, "legal", src), encoding="utf-8").read().replace("\r\n", "\n").split("\n")
    out, in_list, para, toc, effective = [], False, [], [], ""

    def flush():
        nonlocal para
        if para:
            out.append("<p>%s</p>" % "<br>".join(inline(p) for p in para))
            para = []

    def close_list():
        nonlocal in_list
        if in_list:
            out.append("</ul>")
            in_list = False

    for ln in lines:
        if ln.startswith("# "):
            continue
        if ln.startswith("Effective date:"):
            effective = ln
            continue
        if ln.startswith("## "):
            flush()
            close_list()
            h = ln[3:]
            toc.append((slug(h), h))
            out.append('<h2 id="%s">%s</h2>' % (slug(h), inline(h)))
        elif ln.startswith("- "):
            flush()
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append("<li>%s</li>" % inline(ln[2:]))
        elif not ln.strip():
            flush()
            close_list()
        else:
            if in_list and not ln.startswith(" "):
                close_list()
            para.append(ln)
    flush()
    close_list()
    nav = ""
    if toc:
        nav = '<nav class="toc" aria-label="Contents"><b>Contents</b><ol>%s</ol></nav>' % "".join(
            '<li><a href="#%s">%s</a></li>' % (i, html.escape(re.sub(r"^\d+\.\s*", "", t))) for i, t in toc)
    return effective, nav + "\n".join(out)


def doc_page(path, title, description, kicker, h1, sub, inner):
    body = """<div class="page-hero"><div class="container"><span class="eyebrow">%s</span><h1>%s</h1><p>%s</p></div></div>
<div class="container"><article class="doc">%s</article></div>""" % (kicker, h1, sub, inner)
    shell(path, title, description, body)


def phone(name, alt, cls="", eager=False):
    return '<div class="phone %s"><div class="screen"><img src="/assets/shot-%s.webp" alt="%s" width="450" height="1000"%s></div></div>' % (
        cls, name, html.escape(alt), "" if eager else ' loading="lazy"')


ICON = {
    "bolt": '<svg viewBox="0 0 24 24"><path d="M13 2L4 14h7l-1 8 9-12h-7z"/></svg>',
    "users": '<svg viewBox="0 0 24 24"><path d="M17 21v-2a4 4 0 0 0-4-4H7a4 4 0 0 0-4 4v2"/><circle cx="10" cy="7" r="4"/><path d="M21 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/></svg>',
    "trophy": '<svg viewBox="0 0 24 24"><path d="M8 21h8M12 17v4M7 4h10v5a5 5 0 0 1-10 0zM17 5h3v2a3 3 0 0 1-3 3M7 5H4v2a3 3 0 0 0 3 3"/></svg>',
    "coin": '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 7v10M9.5 9.5h4a1.5 1.5 0 0 1 0 3h-3a1.5 1.5 0 0 0 0 3h4"/></svg>',
    "heart": '<svg viewBox="0 0 24 24"><path d="M20.8 5.6a5 5 0 0 0-7.1 0L12 7.3l-1.7-1.7a5 5 0 0 0-7.1 7.1l8.8 8.8 8.8-8.8a5 5 0 0 0 0-7.1z"/></svg>',
    "cards": '<svg viewBox="0 0 24 24"><rect x="3" y="6" width="11" height="15" rx="2"/><path d="M8 6l2-3 9 2-3 14-2 .5"/></svg>',
}


CARDS = [("A", "&#9824;", "blk"), ("K", "&#9829;", "red"), ("Q", "&#9827;", "blk"), ("J", "&#9830;", "red"), ("10", "&#9824;", "blk"), ("9", "&#9829;", "red")]
_n = [0]


def tile(icon, h, p):
    r, g, c = CARDS[_n[0] % 6]
    d = (_n[0] % 3) * 0.12
    tilt = -8 + 8 * (_n[0] % 3)
    _n[0] += 1
    return ('<div class="pcard %s rv" style="--d:%.2fs;--r0:%ddeg"><div class="idx tl">%s<i>%s</i></div><div class="idx br">%s<i>%s</i></div>'
            '<div class="ico">%s</div><h3>%s</h3><p>%s</p></div>') % (c, d, tilt, r, g, r, g, ICON[icon], h, p)


PLAY_ICON = ('<svg viewBox="0 0 512 512" aria-hidden="true">'
    '<path fill="#00d7fe" stroke="#00d7fe" stroke-width="22" stroke-linejoin="round" d="M60 40L290 256 60 472z"/>'
    '<path fill="#00f076" stroke="#00f076" stroke-width="22" stroke-linejoin="round" d="M60 40L380 208 290 256z"/>'
    '<path fill="#ff3a44" stroke="#ff3a44" stroke-width="22" stroke-linejoin="round" d="M60 472L380 304 290 256z"/>'
    '<path fill="#ffc400" stroke="#ffc400" stroke-width="22" stroke-linejoin="round" d="M380 208L462 256 380 304 290 256z"/></svg>')

SUITS = "".join('<span style="left:%d%%;top:%d%%;font-size:%dpx;transform:rotate(%ddeg)">%s</span>' % (x, y, s, r, g)
                for x, y, s, r, g in [(4, 12, 56, -14, "&spades;"), (46, 6, 40, 12, "&hearts;"), (92, 18, 60, 18, "&clubs;"),
                                      (30, 70, 48, -8, "&diams;"), (62, 82, 44, 10, "&spades;"), (8, 86, 36, 20, "&hearts;")])

FAQS = [
    ("Is 5 Cards free?", "Yes. 5 Cards is free to download and play. You earn coins by playing and from daily rewards, and you can also top up with optional in-app purchases if you like. You never need to buy anything to play."),
    ("Is it gambling?", "No. 5 Cards is a party card game played for fun. There are no cash prizes and coins can never be turned into money, goods or services. Just bragging rights and good vibes."),
    ("Can I play with my friends?", "Absolutely. Open a private room, share the room code and your friends can jump straight in. You can also add friends and invite them to a game."),
    ("Which devices does it run on?", "5 Cards is built for Android phones. It is coming soon to Google Play."),
    ("How do I sign in?", "Continue with Google or Facebook, or jump in as a guest. We never see your passwords."),
    ("How do I delete my account?", "In the game go to Settings, Support, Delete Account. No game installed? Email us and we will take care of it. See the <a href=\"/delete-account/\">account deletion page</a>."),
]

HOME = """
<section class="hero"><div class="suits" aria-hidden="true">%(suits)s</div><div class="container">
<div class="hero-copy">
<img class="hero-logo" src="/assets/logo-5cards.webp" alt="5 Cards" width="250" height="226">
<span class="eyebrow">The multiplayer card game</span>
<h1>Game night, <em>right in your pocket.</em></h1>
<p class="lead">%(name)s is the fast, friendly card game made for friends, rivals and good vibes. Jump into a quick match, spin up a private room or climb the Trophy Road. Every round is a party.</p>
<div class="actions" id="play">
<a class="gp" href="/contact/" aria-label="Coming soon on Google Play">%(play)s<div><span>Coming soon on</span><b>Google Play</b></div></a>
<a class="btn ghost" href="#screens">See the game</a>
</div>
<div class="chips"><span class="chip">Free to play</span><span class="chip">Android</span><span class="chip">No gambling, all vibes</span></div>
</div>
<div class="hero-art">%(menu)s%(table)s%(trophy)s</div>
</div></section>

<div class="ticker" aria-hidden="true"><div class="track"><span>Quick matches</span><i>&#9824;</i><span>Private rooms</span><i>&#9829;</i><span>Trophy Road</span><i>&#9827;</i><span>Card skins</span><i>&#9830;</i><span>Daily rewards</span><i>&#9824;</i><span>Quick matches</span><i>&#9824;</i><span>Private rooms</span><i>&#9829;</i><span>Trophy Road</span><i>&#9827;</i><span>Card skins</span><i>&#9830;</i><span>Daily rewards</span><i>&#9824;</i></div></div>

<section id="features"><div class="container">
<div class="section-head rv"><span class="kicker">Why you will love it</span><h2>Easy to learn. Impossible to put down.</h2><p>Short rounds, big laughs and always one more match to play.</p></div>
<div class="fan">%(t1)s%(t2)s%(t3)s%(t4)s%(t5)s%(t6)s</div>
</div></section>

<section class="band" id="screens"><div class="container">
<div class="section-head rv"><span class="kicker">Inside the game</span><h2>A table that feels alive</h2><p>Colourful, smooth and made for one-handed play on your phone.</p></div>

<div class="row">
<div class="rv"><span class="kicker">Play your way</span><h3>Jump in, or throw a party</h3>
<p>Tap <b>Play Now</b> to find an opponent in seconds, open a <b>Private Room</b> and share the code with your crew, or warm up offline in <b>Practice</b>.</p>
<ul class="ticks"><li>Quick online matches</li><li>Private rooms with room codes</li><li>Offline practice against computer players</li></ul></div>
<div class="row-art rv">%(menu2)s</div>
</div>

<div class="row flip">
<div class="rv"><span class="kicker">The table</span><h3>Draw, pair up, call your show</h3>
<p>On your turn discard a card or a pair, then draw. Keep your hand value low and when you think you hold the lowest hand, call <b>Show</b>. Emotes and quick chat keep the table friendly, with no open text chat.</p>
<ul class="ticks"><li>Clear turn timer and round tracker</li><li>Playful emotes and quick chat</li><li>Built-in tutorial for new players</li></ul></div>
<div class="row-art rv">%(table2)s</div>
</div>

<div class="row">
<div class="rv"><span class="kicker">Climb the ranks</span><h3>Trophies, tiers and bragging rights</h3>
<p>Every win earns trophies. Rise from Rookie to Challenger to Ace on the Trophy Road, grab a reward at every step and see how you stack up on the global and friends leaderboards.</p>
<ul class="ticks"><li>Seasonal Trophy Road with rewards</li><li>Global and friends leaderboards</li><li>Daily challenges and bonuses</li></ul></div>
<div class="row-art duo rv">%(trophy2)s%(lb)s</div>
</div>

<div class="row flip">
<div class="rv"><span class="kicker">Make it yours</span><h3>Show off your style</h3>
<p>Unlock striking card skins, emotes and quick chat lines in the shop. Earn coins by playing and from free daily rewards like Lucky Pick and Scratch Your Luck, or top up with optional in-app coin packs.</p>
<ul class="ticks"><li>Dozens of card skins to collect</li><li>Free daily coins</li><li>Optional in-app coin packs</li></ul></div>
<div class="row-art rv">%(shop)s</div>
</div>
</div></section>

<section><div class="container">
<div class="section-head rv"><span class="kicker">How a round works</span><h2>Learn it in a minute</h2><p>The in-game tutorial walks you through it with a real table and real cards.</p></div>
<div class="steps">
<div class="step rv"><h3>Get your five cards</h3><p>Everyone is dealt a hand of five. Your goal is to end the round with the lowest hand value.</p></div>
<div class="step rv"><h3>Discard and draw</h3><p>On your turn, discard one card or a matching pair, then draw a new card to improve your hand.</p></div>
<div class="step rv"><h3>Call your show</h3><p>Think yours is the lowest hand? Call <b>Show</b>: if you are right you score zero, but a wrong call costs you a penalty. The highest score each round is knocked out, and the last player standing wins.</p></div>
</div></div></section>

<section class="party"><div class="container">
<span class="eyebrow">Private rooms</span>
<h2>Who is coming to game night?</h2>
<p>Create a room, share the code and get everyone around the same table, wherever they are. Bring the snacks, we will bring the cards.</p>
<div class="chips"><span class="chip">Room codes</span><span class="chip">Friends list</span><span class="chip">Emotes and quick chat</span></div>
</div></section>

<section id="faq"><div class="container">
<div class="section-head rv"><span class="kicker">Good to know</span><h2>Questions, answered</h2></div>
<div class="faq rv">%(faq)s</div>
</div></section>

<section class="studio"><div class="container">
<img src="/assets/logo-studio.webp" alt="%(studio)s logo" width="260" height="205" loading="lazy">
<div><span class="kicker">The studio</span><h2>Made by %(studio)s</h2>
<p>We are an indie studio that loves games you can pick up in seconds and share with friends. %(name)s is built with care for the casual card table: quick, colourful and full of good vibes.</p>
<p>Say hello at <a href="mailto:%(email)s">%(email)s</a>.</p></div>
</div></section>

<section class="cta-band"><div class="container">
<img src="/assets/logo-5cards.webp" alt="%(name)s logo" width="190" height="172" loading="lazy">
<h2>Ready for your first match?</h2>
<p>%(name)s is coming to Google Play. Questions in the meantime? We would love to hear from you.</p>
<div class="actions" style="justify-content:center"><a class="gp" href="/contact/" aria-label="Coming soon on Google Play">%(play)s<div><span>Coming soon on</span><b>Google Play</b></div></a><a class="btn ghost" href="/contact/">Get in touch</a><a class="btn ghost" href="/privacy/">Read our privacy policy</a></div>
</div></section>
""" % {
    "name": NAME, "studio": STUDIO, "email": EMAIL, "suits": SUITS, "play": PLAY_ICON,
    "menu": phone("menu", "5 Cards main menu with Play Now, Private Room and Practice", "l", eager=True),
    "table": phone("table", "A 5 Cards table with four players", "c", eager=True),
    "trophy": phone("trophy", "The Trophy Road with tiers from Rookie to Ace", "r", eager=True),
    "menu2": phone("menu", "5 Cards main menu with Play Now, Private Room and Practice"),
    "table2": phone("table", "A 5 Cards table with four players"),
    "trophy2": phone("trophy", "The Trophy Road with tiers from Rookie to Ace"),
    "lb": phone("leaderboard", "The global leaderboard with the top three players"),
    "shop": phone("shop", "The shop with card skins"),
    "t1": tile("bolt", "Quick matches", "Find an opponent in seconds and play a round of %s on the go." % NAME),
    "t2": tile("users", "Private rooms", "Share a room code and play with friends, wherever they are."),
    "t3": tile("trophy", "Trophy Road", "Win to earn trophies, rise through the tiers and claim rewards."),
    "t4": tile("coin", "Coins, your way", "Earn coins by playing and from daily rewards, or top up with optional in-app purchases."),
    "t5": tile("cards", "Card skins", "Collect colourful decks, emotes and quick chat lines to show off your style."),
    "t6": tile("heart", "Good vibes only", "No open chat, no gambling and friendly emotes. You can delete your account in the game."),
    "faq": "".join("<details><summary>%s</summary><p>%s</p></details>" % (q, a) for q, a in FAQS),
}

DELETE = """<p class="meta">How to delete your %(n)s account and the data we hold about you.</p>
<div class="cards2">
<div class="tile"><h3>In the game</h3><p>The fastest way. Takes under a minute and needs no email.</p></div>
<div class="tile"><h3>By email</h3><p>No game installed? Email us and we will start the same process.</p></div>
</div>
<h2>Delete it in the game</h2>
<ol>
<li>Open %(n)s and go to <b>Settings</b>, then <b>Support</b>.</li>
<li>Tap <b>Delete Account</b>.</li>
<li>Confirm by typing your User ID (shown on the screen) and the word <code>DELETE</code>.</li>
</ol>
<p>You are signed out at once and your account disappears from leaderboards and friend search. Your account and personal data are permanently deleted 30 days after your request. If you sign in again before that date, the deletion is cancelled and your account is restored as it was.</p>
<h2>Delete it without the game</h2>
<p>If you cannot open the game (for example you uninstalled it), email <a href="mailto:%(e)s?subject=Delete%%20my%%20%(n)s%%20account">%(e)s</a> from the address linked to your Google or Facebook account, with your Player ID if you have it. We will start the same process and confirm by email.</p>
<h2>What is deleted, and what we keep</h2>
<ul>
<li><b>Deleted after 30 days:</b> your profile, display name and avatar, Coins, XP and progress, friends and requests, leaderboard entries and sign-in links.</li>
<li><b>Kept:</b> a deletion record with the dates only (no name, e-mail or Player ID) to show the request was carried out, and any problem report you sent, without your identity. Server logs are removed within 12 months.</li>
</ul>
<h2>Facebook users: data deletion</h2>
<p>If you signed in with Facebook, you can also remove %(n)s from your Facebook account: open <b>Settings and privacy, Settings, Apps and websites</b> on Facebook, find <b>5 Cards Multiplayer Card Game</b> and choose <b>Remove</b>. That stops Facebook sharing data with the game. To have the data the game already holds deleted, use one of the two methods above; we treat a removal request that reaches us by email as a deletion request.</p>
<div class="note">Questions? Write to <a href="mailto:%(e)s">%(e)s</a>. We reply within 30 days, usually much sooner.</div>
""" % {"e": EMAIL, "n": NAME}

CONTACT = """<p class="meta">Support, feedback and privacy requests.</p>
<div class="cards2">
<div class="tile"><h3>Support and feedback</h3><p>Email <a href="mailto:%(e)s">%(e)s</a>. Please include your Player ID (on your profile in the game) and, for a problem, your Android version and phone model. You can also use <b>Settings, Support, Report a Problem</b> in the game.</p></div>
<div class="tile"><h3>Privacy and data requests</h3><p>To see, correct or delete your data, or to make a privacy complaint, write to the same address from the email linked to your Google or Facebook account. See the <a href="/privacy/">Privacy Policy</a> and the <a href="/delete-account/">account deletion page</a>.</p></div>
</div>
<h2>Publisher</h2>
<p>%(s)s<br>Email: <a href="mailto:%(e)s">%(e)s</a><br>We reply to every message, normally within a few days and always within 30 days.</p>
""" % {"e": EMAIL, "s": STUDIO}

shell("/", "5 Cards - the multiplayer card game | Noob Studios",
      "5 Cards is a fast, friendly multiplayer card game for Android by Noob Studios. Quick matches, private rooms for game night, the Trophy Road and card skins.",
      HOME)

eff, body = legal("privacy.txt")
doc_page("/privacy/", "Privacy Policy | 5 Cards", "How 5 Cards by Noob Studios collects, uses and protects your personal data.",
         "Legal", "Privacy Policy", eff, body)
eff, body = legal("terms.txt")
doc_page("/terms/", "Terms of Service | 5 Cards", "The terms that apply when you play 5 Cards by Noob Studios.",
         "Legal", "Terms of Service", eff, body)
doc_page("/delete-account/", "Delete your account | 5 Cards",
         "How to delete your 5 Cards account and data, including for Facebook sign-in.",
         "Your data", "Delete your account", "Your account, your choice.", DELETE)
doc_page("/contact/", "Contact and support | 5 Cards", "Contact Noob Studios about 5 Cards.",
         "Help", "Contact and support", "We are here to help.", CONTACT)

with open(os.path.join(ROOT, "robots.txt"), "w", newline="\n") as f:
    f.write("User-agent: *\nAllow: /\n")
print("built")
