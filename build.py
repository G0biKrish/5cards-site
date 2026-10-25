"""Builds the static site: legal/*.txt (the same texts the game ships) plus the hand-written pages
below become plain HTML in the repo root. Run `python build.py` after editing a text, commit the result."""
import html
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))
EMAIL = "noobstudios.in@gmail.com"
NAME = "5 Cards"

CSS = """
:root{--bg:#0d2a1f;--bg2:#143a2b;--card:#fbf7ec;--ink:#1d2b24;--muted:#5d6b63;--gold:#e0b341;--gold2:#f3d27a;--line:#e5dfcc}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;font:17px/1.65 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;color:var(--ink);background:var(--bg)}
a{color:#0b6b4a}
header.top{background:var(--bg);border-bottom:1px solid rgba(255,255,255,.08)}
.bar{max-width:980px;margin:0 auto;padding:14px 20px;display:flex;align-items:center;gap:20px;flex-wrap:wrap}
.brand{display:flex;align-items:center;gap:10px;color:#fff;text-decoration:none;font-weight:700;font-size:20px;letter-spacing:.2px}
.brand img{width:34px;height:34px;border-radius:8px}
nav{margin-left:auto;display:flex;gap:18px;flex-wrap:wrap}
nav a{color:#cfe3d8;text-decoration:none;font-size:15px}
nav a:hover,nav a[aria-current]{color:var(--gold2)}
.hero{background:radial-gradient(1200px 500px at 50% -10%,#1d5a41 0,var(--bg) 70%);color:#fff;text-align:center;padding:72px 20px 84px}
.hero img{width:112px;height:112px;border-radius:26px;box-shadow:0 12px 40px rgba(0,0,0,.45)}
.hero h1{font-size:clamp(34px,6vw,54px);line-height:1.1;margin:24px 0 12px}
.hero p{max-width:620px;margin:0 auto;color:#cfe3d8;font-size:19px}
.badge{display:inline-block;margin-top:28px;padding:12px 22px;border-radius:999px;background:var(--gold);color:#2a1f00;font-weight:700;text-decoration:none}
.badge.soon{background:transparent;border:1px solid var(--gold);color:var(--gold2)}
main.page{background:var(--card);padding:48px 20px 72px}
.wrap{max-width:760px;margin:0 auto}
.wrap h1{font-size:34px;line-height:1.2;margin:0 0 6px}
.wrap h2{font-size:22px;margin:38px 0 8px;padding-top:6px;border-top:1px solid var(--line)}
.wrap p.meta{color:var(--muted);margin:0 0 22px}
.wrap ul{padding-left:22px}
.wrap li{margin:6px 0}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:18px;max-width:980px;margin:0 auto}
.tile{background:var(--bg2);border:1px solid rgba(255,255,255,.08);border-radius:16px;padding:22px;color:#e8f2ec}
.tile h3{margin:0 0 8px;color:var(--gold2);font-size:18px}
.tile p{margin:0;color:#c3d8cc;font-size:15.5px}
section.features{padding:56px 20px;background:var(--bg)}
.note{background:#fff;border:1px solid var(--line);border-left:4px solid var(--gold);border-radius:10px;padding:14px 18px;margin:18px 0}
footer{background:#08180f;color:#9bb5a6;padding:30px 20px;font-size:14.5px}
footer .bar{padding:0}
footer a{color:#cfe3d8}
code{background:#efe9d6;padding:1px 6px;border-radius:5px;font-size:.92em}
"""

NAV = [("/", "Home"), ("/privacy/", "Privacy"), ("/terms/", "Terms"), ("/delete-account/", "Delete account"), ("/contact/", "Contact")]


def page(path, title, description, body, hero=None):
    links = "".join(
        '<a href="%s"%s>%s</a>' % (h, ' aria-current="page"' if h == path else "", t) for h, t in NAV)
    out = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%s</title>
<meta name="description" content="%s">
<meta name="theme-color" content="#0d2a1f">
<link rel="icon" href="/assets/favicon.png">
<style>%s</style>
</head>
<body>
<header class="top"><div class="bar">
<a class="brand" href="/"><img src="/assets/favicon.png" alt="" width="34" height="34">%s</a>
<nav>%s</nav>
</div></header>
%s
%s
<footer><div class="bar">
<span>&copy; 2026 GOB Interactive. %s is a multiplayer card game for Android.</span>
<nav><a href="/privacy/">Privacy Policy</a><a href="/terms/">Terms of Service</a><a href="/delete-account/">Delete account</a><a href="mailto:%s">%s</a></nav>
</div></footer>
</body>
</html>
""" % (html.escape(title), html.escape(description), CSS, NAME, links, hero or "", body, NAME, EMAIL, EMAIL)
    d = os.path.join(ROOT, path.strip("/"))
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8", newline="\n") as f:
        f.write(out)


def inline(s):
    s = html.escape(s)
    s = re.sub(r"([A-Za-z0-9._+-]+@[A-Za-z0-9.-]+\.[a-z]{2,})", r'<a href="mailto:\1">\1</a>', s)
    return s


def legal(src):
    """The in-game legal text: '# title', 'Effective date: ...', '## n. Heading', '- bullet', paragraphs."""
    lines = open(os.path.join(ROOT, "legal", src), encoding="utf-8").read().replace("\r\n", "\n").split("\n")
    out, in_list, para = [], False, []

    def flush():
        nonlocal para
        if para:
            out.append("<p>%s</p>" % "<br>".join(inline(p) for p in para))
            para = []

    for ln in lines:
        if ln.startswith("# "):
            continue
        if ln.startswith("Effective date:"):
            flush()
            out.append('<p class="meta">%s</p>' % inline(ln))
            continue
        if ln.startswith("## "):
            flush()
            if in_list:
                out.append("</ul>")
                in_list = False
            out.append("<h2>%s</h2>" % inline(ln[3:]))
        elif ln.startswith("- "):
            flush()
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append("<li>%s</li>" % inline(ln[2:]))
        elif not ln.strip():
            flush()
            if in_list:
                out.append("</ul>")
                in_list = False
        else:
            if in_list and not ln.startswith(" "):
                out.append("</ul>")
                in_list = False
            para.append(ln)
    flush()
    if in_list:
        out.append("</ul>")
    return "\n".join(out)


def doc(title, inner):
    return '<main class="page"><div class="wrap"><h1>%s</h1>\n%s</div></main>' % (html.escape(title), inner)


HERO = """<section class="hero">
<img src="/assets/icon.png" alt="5 Cards app icon" width="112" height="112">
<h1>5 Cards</h1>
<p>The fast multiplayer card game. Play with friends in private rooms or jump into a quick match, climb the leaderboards and collect trophies.</p>
<a class="badge soon" href="/contact/">Coming soon to Google Play</a>
</section>"""

FEATURES = """<section class="features"><div class="grid">
<div class="tile"><h3>Quick matches</h3><p>Find an opponent in seconds and play a round of 5 Cards on your phone.</p></div>
<div class="tile"><h3>Private rooms</h3><p>Share a room code and play with your friends, wherever they are.</p></div>
<div class="tile"><h3>Trophies and leaderboards</h3><p>Win to earn trophies, move up the tiers and see where you rank.</p></div>
<div class="tile"><h3>Free coins</h3><p>Claim daily rewards and try your luck with Lucky Pick and Scratch Your Luck.</p></div>
<div class="tile"><h3>Sign in your way</h3><p>Continue with Google or Facebook, or play as a guest.</p></div>
<div class="tile"><h3>Your data, your call</h3><p>You can delete your account from the game at any time. <a style="color:#f3d27a" href="/delete-account/">Learn how</a>.</p></div>
</div></section>"""

DELETE = """<p class="meta">How to delete your 5 Cards account and the data we hold about you.</p>
<h2>Delete it in the game (fastest)</h2>
<ol>
<li>Open 5 Cards and go to <b>Settings</b>, then <b>Support</b>.</li>
<li>Tap <b>Delete Account</b>.</li>
<li>Confirm by typing your User ID (shown on the screen) and the word <code>DELETE</code>.</li>
</ol>
<p>You are signed out at once and your account disappears from leaderboards and friend search. Your account and personal data are permanently deleted 30 days after your request. If you sign in again before that date, the deletion is cancelled and your account is restored as it was.</p>
<h2>Delete it without the game</h2>
<p>If you cannot open the game (for example you uninstalled it), email <a href="mailto:%(e)s?subject=Delete%%20my%%205%%20Cards%%20account">%(e)s</a> from the address linked to your Google or Facebook account, with your Player ID if you have it. We will start the same process and confirm by email.</p>
<h2>What is deleted, and what we keep</h2>
<ul>
<li><b>Deleted after 30 days:</b> your profile, display name and avatar, Coins, XP and progress, friends and requests, leaderboard entries and sign-in links.</li>
<li><b>Kept:</b> a deletion record with the dates only (no name, e-mail or Player ID) to show the request was carried out, and any problem report you sent, without your identity. Server logs are removed within 12 months.</li>
</ul>
<h2>Facebook users: data deletion</h2>
<p>If you signed in with Facebook, you can also remove 5 Cards from your Facebook account: open <b>Settings and privacy, Settings, Apps and websites</b> on Facebook, find <b>5 Cards Multiplayer Card Game</b> and choose <b>Remove</b>. That stops Facebook sharing data with the game. To have the data the game already holds deleted, use one of the two methods above; we will treat a removal request that reaches us by email as a deletion request.</p>
<div class="note">Questions? Write to <a href="mailto:%(e)s">%(e)s</a>. We reply within 30 days, usually much sooner.</div>
""" % {"e": EMAIL}

CONTACT = """<p class="meta">Support, feedback and privacy requests.</p>
<p>Email <a href="mailto:%(e)s">%(e)s</a>. Please include your Player ID (on your profile in the game) and the Android version and phone model if you are reporting a problem. You can also use <b>Settings, Support, Report a Problem</b> inside the game.</p>
<h2>Privacy and data requests</h2>
<p>To see, correct or delete your data, or to make a privacy complaint, write to the same address from the email linked to your Google or Facebook account. See the <a href="/privacy/">Privacy Policy</a> and the <a href="/delete-account/">account deletion page</a>.</p>
<h2>Publisher</h2>
<p>GOB Interactive<br>Email: <a href="mailto:%(e)s">%(e)s</a></p>
""" % {"e": EMAIL}

page("/", "5 Cards - multiplayer card game", "5 Cards is a fast multiplayer card game for Android. Play quick matches or private rooms with friends.",
     FEATURES, HERO)
page("/privacy/", "Privacy Policy - 5 Cards", "How 5 Cards collects, uses and protects your personal data.", doc("Privacy Policy", legal("privacy.txt")))
page("/terms/", "Terms of Service - 5 Cards", "The terms that apply when you play 5 Cards.", doc("Terms of Service", legal("terms.txt")))
page("/delete-account/", "Delete your account - 5 Cards", "How to delete your 5 Cards account and data, including for Facebook sign-in.", doc("Delete your account", DELETE))
page("/contact/", "Contact and support - 5 Cards", "Contact GOB Interactive about 5 Cards.", doc("Contact and support", CONTACT))

with open(os.path.join(ROOT, "robots.txt"), "w", newline="\n") as f:
    f.write("User-agent: *\nAllow: /\n")
print("built")
