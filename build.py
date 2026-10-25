"""Builds the static site: legal/*.txt (the texts the game ships) plus the pages below become plain HTML in
the repo root. Run `python build.py` after editing, commit the result. No build step on Cloudflare."""
import html
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))
EMAIL = "noobstudios.in@gmail.com"
NAME = "5 Cards"
STUDIO = "Noob Studios"
SITE = "https://5cards-site.pages.dev"  # replaced by the real domain once one is attached

CSS = """
:root{
--navy:#0a1a44;--navy2:#10286a;--blue:#1c4fc4;--sky:#4aa3ff;--gold:#ffc83d;--gold2:#ffe08a;--red:#e8433f;
--ink:#14213d;--muted:#5a6785;--bg:#f5f7fc;--card:#ffffff;--line:#e3e8f4;--radius:18px;
--shadow:0 18px 50px rgba(10,26,68,.16);
}
*{box-sizing:border-box}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{margin:0;font:17px/1.65 "Inter",system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;color:var(--ink);background:var(--bg)}
img{max-width:100%;display:block}
a{color:var(--blue)}
h1,h2,h3{font-family:"Poppins","Inter",system-ui,sans-serif;line-height:1.15;letter-spacing:-.01em}
.container{max-width:1120px;margin:0 auto;padding:0 22px}

/* header */
.site-header{position:sticky;top:0;z-index:20;background:rgba(10,26,68,.92);backdrop-filter:saturate(1.4) blur(12px);border-bottom:1px solid rgba(255,255,255,.08)}
.site-header .container{display:flex;align-items:center;gap:22px;height:66px}
.brand{display:flex;align-items:center;gap:11px;color:#fff;text-decoration:none;font:700 20px "Poppins",sans-serif}
.brand img{width:36px;height:36px;border-radius:9px}
.nav{margin-left:auto;display:flex;align-items:center;gap:6px}
.nav a{color:#c9d6f5;text-decoration:none;font-size:15px;font-weight:500;padding:8px 12px;border-radius:9px}
.nav a:hover{color:#fff;background:rgba(255,255,255,.08)}
.nav a[aria-current]{color:var(--gold2)}
.nav .cta{background:var(--gold);color:#3a2a00;font-weight:700;margin-left:6px}
.nav .cta:hover{background:var(--gold2);color:#3a2a00}
@media(max-width:820px){.nav a:not(.cta){display:none}.nav{margin-left:auto}}

/* hero */
.hero{position:relative;overflow:hidden;color:#fff;background:
radial-gradient(900px 480px at 78% 30%,rgba(74,163,255,.38),transparent 62%),
radial-gradient(700px 420px at 12% 90%,rgba(255,200,61,.14),transparent 60%),
linear-gradient(160deg,var(--navy) 0%,var(--navy2) 100%)}
.hero .container{display:grid;grid-template-columns:1.05fr .95fr;gap:36px;align-items:center;padding-top:64px;padding-bottom:0}
.hero-copy{padding-bottom:72px}
.eyebrow{display:inline-block;font:600 13px "Poppins",sans-serif;letter-spacing:.14em;text-transform:uppercase;color:var(--gold2);background:rgba(255,200,61,.12);border:1px solid rgba(255,200,61,.3);padding:6px 14px;border-radius:999px}
.hero h1{font-size:clamp(38px,5.4vw,62px);margin:20px 0 16px;font-weight:800}
.hero h1 span{color:var(--gold)}
.hero p.lead{font-size:20px;color:#cfdcff;max-width:520px;margin:0}
.actions{display:flex;gap:14px;flex-wrap:wrap;margin-top:32px}
.btn{display:inline-flex;align-items:center;gap:10px;padding:14px 26px;border-radius:14px;font:700 16px "Poppins",sans-serif;text-decoration:none;border:2px solid transparent}
.btn.gold{background:linear-gradient(180deg,#ffd75e,#ffb81f);color:#3a2a00;box-shadow:0 8px 24px rgba(255,184,31,.35)}
.btn.ghost{color:#fff;border-color:rgba(255,255,255,.35)}
.btn.ghost:hover{background:rgba(255,255,255,.08)}
.btn small{display:block;font:500 11px "Inter",sans-serif;opacity:.8;margin-bottom:-2px}
.trust{display:flex;gap:26px;flex-wrap:wrap;margin-top:34px;color:#a9bbec;font-size:14.5px}
.trust b{color:#fff}
.hero-art{position:relative;height:640px}
.hero-art .phone{position:absolute}
.hero-art .p1{left:50%;top:34px;width:300px;transform:translateX(-40%) rotate(5deg);z-index:2}
.hero-art .p2{left:0;top:96px;width:250px;transform:rotate(-8deg);z-index:1;opacity:.96}
@media(max-width:900px){
.hero .container{grid-template-columns:1fr;padding-top:44px}
.hero-copy{padding-bottom:20px;text-align:center}
.hero p.lead{margin:0 auto}.actions,.trust{justify-content:center}
.hero-art{height:500px}.hero-art .p1{width:230px;left:auto;right:6%;transform:rotate(5deg)}.hero-art .p2{width:190px;left:4%;top:90px}
}

/* phone frame */
.phone{aspect-ratio:450/1000;border-radius:38px;padding:9px;background:linear-gradient(145deg,#2b3a63,#0b1020);box-shadow:0 30px 70px rgba(2,8,30,.55),inset 0 0 0 1.5px rgba(255,255,255,.14)}
.phone img{width:100%;height:100%;object-fit:cover;border-radius:30px;background:#000}
.phone.light{box-shadow:var(--shadow),inset 0 0 0 1.5px rgba(255,255,255,.14)}

/* sections */
section{padding:84px 0}
.section-head{max-width:640px;margin:0 auto 52px;text-align:center}
.section-head h2{font-size:clamp(30px,4vw,44px);margin:12px 0 12px;font-weight:800}
.section-head p{color:var(--muted);font-size:18px;margin:0}
.kicker{font:700 13px "Poppins",sans-serif;letter-spacing:.14em;text-transform:uppercase;color:var(--blue)}
.band{background:#fff;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.row{display:grid;grid-template-columns:1fr 1fr;gap:64px;align-items:center;margin:0 0 84px}
.row:last-child{margin-bottom:0}
.row.flip .row-art{order:-1}
.row h3{font-size:clamp(26px,3.2vw,36px);margin:10px 0 14px;font-weight:800}
.row p{color:var(--muted);margin:0 0 14px}
.ticks{list-style:none;padding:0;margin:18px 0 0}
.ticks li{position:relative;padding-left:32px;margin:10px 0;color:var(--ink)}
.ticks li:before{content:"";position:absolute;left:0;top:5px;width:20px;height:20px;border-radius:50%;background:var(--gold) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20'%3E%3Cpath d='M5.5 10.5l3 3 6-7' fill='none' stroke='%233a2a00' stroke-width='2.4' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/20px no-repeat}
.row-art{display:flex;justify-content:center}
.row-art .phone{width:min(300px,100%)}
.row-art.duo{gap:22px}
.row-art.duo .phone{width:min(230px,46%)}
.row-art.duo .phone:nth-child(2){margin-top:46px}
@media(max-width:860px){.row,.row.flip{grid-template-columns:1fr;gap:34px}.row.flip .row-art{order:0}.row{margin-bottom:64px}}

.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}
@media(max-width:900px){.grid3{grid-template-columns:repeat(2,1fr)}}
@media(max-width:560px){.grid3{grid-template-columns:1fr}}
.tile{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:28px;box-shadow:0 2px 0 rgba(10,26,68,.03)}
.tile .ico{width:48px;height:48px;border-radius:14px;background:linear-gradient(145deg,var(--blue),var(--sky));display:grid;place-items:center;margin-bottom:16px}
.tile .ico svg{width:26px;height:26px;stroke:#fff;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.tile h3{font-size:19px;margin:0 0 8px}
.tile p{margin:0;color:var(--muted);font-size:16px}

.steps{counter-reset:s;display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:22px}
.step{position:relative;padding:28px 26px 26px;background:var(--card);border:1px solid var(--line);border-radius:var(--radius)}
.step:before{counter-increment:s;content:counter(s);position:absolute;top:-18px;left:24px;width:38px;height:38px;border-radius:50%;background:var(--gold);color:#3a2a00;font:800 18px/38px "Poppins",sans-serif;text-align:center;box-shadow:0 6px 16px rgba(255,184,31,.4)}
.step h3{margin:6px 0 8px;font-size:19px}
.step p{margin:0;color:var(--muted);font-size:16px}

.cta-band{background:linear-gradient(160deg,var(--navy),var(--navy2));color:#fff;text-align:center;position:relative;overflow:hidden}
.cta-band:before{content:"";position:absolute;inset:0;background:radial-gradient(600px 300px at 50% 0,rgba(74,163,255,.3),transparent 70%)}
.cta-band .container{position:relative}
.cta-band img{width:140px;margin:0 auto 6px}
.cta-band h2{font-size:clamp(30px,4vw,42px);margin:8px 0 12px;font-weight:800}
.cta-band p{color:#cfdcff;max-width:520px;margin:0 auto 28px}

/* document pages */
.page-hero{background:linear-gradient(160deg,var(--navy),var(--navy2));color:#fff;padding:54px 0 46px}
.page-hero h1{font-size:clamp(32px,4.4vw,46px);margin:10px 0 8px;font-weight:800}
.page-hero p{margin:0;color:#b9c9f3}
.doc{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);box-shadow:var(--shadow);padding:44px clamp(22px,5vw,56px);margin:-26px auto 72px;max-width:860px;position:relative}
.doc h2{font-size:23px;margin:40px 0 10px;padding-top:26px;border-top:1px solid var(--line);font-weight:700}
.doc h2:first-of-type{margin-top:8px}
.doc p,.doc li{color:#2c3957}
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
.cards2 .tile{padding:22px}

/* footer */
.site-footer{background:#07122f;color:#9fb2e4;padding:56px 0 30px;font-size:15px}
.fgrid{display:grid;grid-template-columns:1.4fr 1fr 1fr;gap:36px}
.site-footer h4{margin:0 0 12px;color:#fff;font:600 14px "Poppins",sans-serif;letter-spacing:.1em;text-transform:uppercase}
.site-footer a{display:block;color:#b9c9f3;text-decoration:none;padding:4px 0}
.site-footer a:hover{color:var(--gold2)}
.site-footer .brand{margin-bottom:12px}
.fine{border-top:1px solid rgba(255,255,255,.1);margin-top:34px;padding-top:20px;font-size:13.5px;color:#7f93c8}
@media(max-width:760px){.fgrid{grid-template-columns:1fr}}
"""

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Poppins:wght@600;700;800&display=swap" rel="stylesheet">'

NAV = [("/privacy/", "Privacy"), ("/terms/", "Terms"), ("/delete-account/", "Delete account"), ("/contact/", "Contact")]


def shell(path, title, description, body, extra_head=""):
    links = "".join('<a href="%s"%s>%s</a>' % (h, ' aria-current="page"' if h == path else "", t) for h, t in NAV)
    url = SITE + path
    out = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<meta name="theme-color" content="#0a1a44">
<link rel="canonical" href="%(url)s">
<link rel="icon" href="/assets/favicon.png">
<meta property="og:type" content="website">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:image" content="%(site)s/assets/icon.png">
<meta name="twitter:card" content="summary">
%(fonts)s
<style>%(css)s</style>%(extra)s
</head>
<body>
<header class="site-header"><div class="container">
<a class="brand" href="/"><img src="/assets/favicon.png" alt="" width="36" height="36">%(name)s</a>
<nav class="nav" aria-label="Main">%(links)s<a class="cta" href="/#play">Play</a></nav>
</div></header>
%(body)s
<footer class="site-footer"><div class="container">
<div class="fgrid">
<div><a class="brand" href="/"><img src="/assets/favicon.png" alt="" width="36" height="36">%(name)s</a>
<p style="margin:0;max-width:340px">A fast multiplayer card game for Android, made by %(studio)s.</p></div>
<div><h4>Game</h4><a href="/#features">Features</a><a href="/#screens">Screenshots</a><a href="/#play">Get the game</a></div>
<div><h4>Legal and support</h4><a href="/privacy/">Privacy Policy</a><a href="/terms/">Terms of Service</a><a href="/delete-account/">Delete your account</a><a href="mailto:%(email)s">%(email)s</a></div>
</div>
<div class="fine">&copy; 2026 %(studio)s. All rights reserved. %(name)s is a game of skill and luck played for fun with virtual items only. No real-money gambling. Google Play is a trademark of Google LLC. Facebook is a trademark of Meta Platforms, Inc.</div>
</div></footer>
</body>
</html>
""" % {"title": html.escape(title), "desc": html.escape(description), "url": url, "site": SITE, "fonts": FONTS, "css": CSS,
       "extra": extra_head, "name": NAME, "links": links, "body": body, "studio": STUDIO, "email": EMAIL}
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


def shot(name, alt, cls="", eager=False):
    return '<div class="phone %s"><img src="/assets/shot-%s.webp" alt="%s" width="450" height="1000"%s></div>' % (
        cls, name, html.escape(alt), "" if eager else ' loading="lazy"')


ICON = {
    "bolt": '<svg viewBox="0 0 24 24"><path d="M13 2L4 14h7l-1 8 9-12h-7z"/></svg>',
    "users": '<svg viewBox="0 0 24 24"><path d="M17 21v-2a4 4 0 0 0-4-4H7a4 4 0 0 0-4 4v2"/><circle cx="10" cy="7" r="4"/><path d="M21 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/></svg>',
    "trophy": '<svg viewBox="0 0 24 24"><path d="M8 21h8M12 17v4M7 4h10v5a5 5 0 0 1-10 0zM17 5h3v2a3 3 0 0 1-3 3M7 5H4v2a3 3 0 0 0 3 3"/></svg>',
    "coin": '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 7v10M9.5 9.5h4a1.5 1.5 0 0 1 0 3h-3a1.5 1.5 0 0 0 0 3h4"/></svg>',
    "shield": '<svg viewBox="0 0 24 24"><path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/></svg>',
    "cards": '<svg viewBox="0 0 24 24"><rect x="3" y="6" width="11" height="15" rx="2"/><path d="M8 6l2-3 9 2-3 14-2 .5"/></svg>',
}


def tile(icon, h, p):
    return '<div class="tile"><div class="ico">%s</div><h3>%s</h3><p>%s</p></div>' % (ICON[icon], h, p)


HOME = """
<section class="hero"><div class="container">
<div class="hero-copy">
<span class="eyebrow">Multiplayer card game</span>
<h1>Five cards. Real rivals. <span>Pure bragging rights.</span></h1>
<p class="lead">%(name)s is the quick, clever card game you play with friends or against players from around the world. Match, discard, show your hand and climb the trophy road.</p>
<div class="actions" id="play">
<a class="btn gold" href="/contact/"><span><small>Coming soon to</small>Google Play</span></a>
<a class="btn ghost" href="#screens">See the game</a>
</div>
<div class="trust"><span><b>Free</b> to play</span><span><b>Android</b></span><span><b>No real-money</b> gambling</span></div>
</div>
<div class="hero-art">
<div class="phone p2">%(menu)s</div>
<div class="phone p1">%(table)s</div>
</div>
</div></section>

<section class="band" id="features"><div class="container">
<div class="section-head"><span class="kicker">Why you will love it</span><h2>Easy to learn. Hard to put down.</h2><p>Every round is short, every decision matters, and there is always one more match to play.</p></div>
<div class="grid3">
%(t1)s%(t2)s%(t3)s%(t4)s%(t5)s%(t6)s
</div></div></section>

<section id="screens"><div class="container">
<div class="section-head"><span class="kicker">Inside the game</span><h2>A table that feels alive</h2><p>Colourful, smooth and built for one-handed play on your phone.</p></div>

<div class="row">
<div><span class="kicker">Play your way</span><h3>Jump in, or invite your friends</h3>
<p>Tap <b>Play Now</b> to find an opponent in seconds, open a <b>Private Room</b> and share the code with friends, or sharpen your skills offline in <b>Practice</b>.</p>
<ul class="ticks"><li>Quick online matches</li><li>Private rooms with room codes</li><li>Offline practice against computer players</li></ul></div>
<div class="row-art">%(menu2)s</div>
</div>

<div class="row flip">
<div><span class="kicker">The table</span><h3>Draw, pair up and call your show</h3>
<p>On your turn discard a card or a pair, then draw. Keep your hand value low, and when you think you hold the lowest hand, call <b>Show</b>. Emotes and quick chat keep the table friendly without open text chat.</p>
<ul class="ticks"><li>Clear turn timer and round tracker</li><li>Playful emotes and quick chat</li><li>Built-in tutorial for new players</li></ul></div>
<div class="row-art">%(table2)s</div>
</div>

<div class="row">
<div><span class="kicker">Climb the ranks</span><h3>Trophies, tiers and leaderboards</h3>
<p>Every win earns trophies. Move from Rookie to Challenger to Ace on the Trophy Road, claim a reward at every step and see how you stack up against the world on the global and friends leaderboards.</p>
<ul class="ticks"><li>Seasonal Trophy Road with rewards</li><li>Global and friends leaderboards</li><li>Daily challenges and bonuses</li></ul></div>
<div class="row-art duo">%(trophy)s%(lb)s</div>
</div>

<div class="row flip">
<div><span class="kicker">Make it yours</span><h3>Collect card skins and more</h3>
<p>Unlock striking card decks, emotes and quick chat lines in the shop. Earn coins by playing, and claim free coins every day with Lucky Pick and Scratch Your Luck.</p>
<ul class="ticks"><li>Dozens of card skins to collect</li><li>Free daily coins</li><li>Everything is earned with in-game coins</li></ul></div>
<div class="row-art">%(shop)s</div>
</div>
</div></section>

<section class="band"><div class="container">
<div class="section-head"><span class="kicker">How a round works</span><h2>Learn it in a minute</h2><p>The in-game tutorial walks you through it with a real table and real cards.</p></div>
<div class="steps">
<div class="step"><h3>Get your five cards</h3><p>Everyone is dealt a hand of five. Your goal is to end the round with the lowest hand value.</p></div>
<div class="step"><h3>Discard and draw</h3><p>On your turn, discard one card or a matching pair, then draw a new card to improve your hand.</p></div>
<div class="step"><h3>Call your show</h3><p>Think yours is the lowest hand? Call <b>Show</b>: if you are right you score zero, but a wrong call costs you a penalty. The highest score each round is knocked out, and the last player standing wins.</p></div>
</div></div></section>

<section class="cta-band"><div class="container">
<img src="/assets/logo.png" alt="%(name)s logo" width="140" height="128" loading="lazy">
<h2>Ready for your first match?</h2>
<p>%(name)s is coming to Google Play. Questions in the meantime? We would love to hear from you.</p>
<div class="actions" style="justify-content:center"><a class="btn gold" href="/contact/">Get in touch</a><a class="btn ghost" href="/privacy/">Read our privacy policy</a></div>
</div></section>
""" % {
    "name": NAME,
    "menu": shot("menu", "5 Cards main menu with Play Now, Private Room and Practice", eager=True),
    "table": shot("table", "A 5 Cards table with four players", eager=True),
    "menu2": shot("menu", "5 Cards main menu with Play Now, Private Room and Practice", "light"),
    "table2": shot("table", "A 5 Cards table with four players", "light"),
    "trophy": shot("trophy", "The Trophy Road with tiers from Rookie to Ace", "light"),
    "lb": shot("leaderboard", "The global leaderboard with the top three players", "light"),
    "shop": shot("shop", "The shop with card skins", "light"),
    "t1": tile("bolt", "Quick matches", "Find an opponent in seconds and play a round of %s on the go." % NAME),
    "t2": tile("users", "Private rooms", "Share a room code and play with friends, wherever they are."),
    "t3": tile("trophy", "Trophy Road", "Win to earn trophies, rise through the tiers and claim rewards."),
    "t4": tile("coin", "Free daily coins", "Come back every day for rewards, Lucky Pick and Scratch Your Luck."),
    "t5": tile("cards", "Card skins", "Collect colourful decks, emotes and quick chat lines."),
    "t6": tile("shield", "Safe and fair", "No open chat, no real-money gambling, and you can delete your account in the game."),
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
      "5 Cards is a fast multiplayer card game for Android by Noob Studios. Play quick matches or private rooms, climb the Trophy Road and collect card skins.",
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
