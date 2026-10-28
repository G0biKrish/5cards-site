"""The home page: markup, styles and scripts. Imported by build.py, which owns the shell, header and footer."""
import html

NAME = "5 Cards"
STUDIO = "Noob Studios"
EMAIL = "noobstudios.in@gmail.com"

# --------------------------------------------------------------------------------------------------------------------
# Icons: one hand-drawn set (24px grid, rounded strokes, a soft fill for depth). Used through <use href="#i-name">.
# --------------------------------------------------------------------------------------------------------------------
SPRITE = """<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false"><defs>
<symbol id="i-bolt" viewBox="0 0 24 24"><path d="M13.5 2.5 5 13.5h6l-1 8 8.5-11h-6z" fill="currentColor" fill-opacity=".28" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></symbol>
<symbol id="i-room" viewBox="0 0 24 24"><circle cx="9" cy="8" r="3.4" fill="currentColor" fill-opacity=".28" stroke="currentColor" stroke-width="1.8"/><path d="M2.8 20c.4-3.4 3-5.4 6.2-5.4s5.8 2 6.2 5.4" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/><circle cx="17" cy="9" r="2.6" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M17.4 14.2c2.2.3 3.6 2 3.9 4.6" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></symbol>
<symbol id="i-trophy" viewBox="0 0 24 24"><path d="M7 3.5h10v5.2a5 5 0 0 1-10 0z" fill="currentColor" fill-opacity=".28" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><path d="M7 5.5H3.8v1.4A3.4 3.4 0 0 0 7 10.3M17 5.5h3.2v1.4a3.4 3.4 0 0 1-3.2 3.4M12 13.7v3.6M8.2 20.5h7.6M9.5 17.3h5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></symbol>
<symbol id="i-coin" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9" fill="currentColor" fill-opacity=".28" stroke="currentColor" stroke-width="1.8"/><circle cx="12" cy="12" r="5.6" fill="none" stroke="currentColor" stroke-width="1.4" stroke-opacity=".7"/><path d="M12 8.8v6.4M10 10.4c.4-.9 1.2-1.2 2-1.2 1.1 0 2 .6 2 1.5s-.9 1.3-2 1.5-2 .6-2 1.5.9 1.5 2 1.5c.8 0 1.6-.3 2-1.2" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/></symbol>
<symbol id="i-cards" viewBox="0 0 24 24"><rect x="3.2" y="5.6" width="11.6" height="15.4" rx="2.4" fill="currentColor" fill-opacity=".28" stroke="currentColor" stroke-width="1.8"/><path d="M8.2 5.2 9.4 3.4a1.6 1.6 0 0 1 2.1-.5l8 3.9c.8.4 1.2 1.4.9 2.3l-3.4 9.3" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><path d="M9 11.2c1.2-1.4 3-.4 2.4 1.2-.4 1-1.6 1.8-2.4 2.6-.8-.8-2-1.6-2.4-2.6-.6-1.6 1.2-2.6 2.4-1.2z" fill="currentColor" stroke="none"/></symbol>
<symbol id="i-vibes" viewBox="0 0 24 24"><path d="M12 3 4.6 6v5.6c0 4.4 3 7.6 7.4 9.4 4.4-1.8 7.4-5 7.4-9.4V6z" fill="currentColor" fill-opacity=".28" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><path d="M8.6 12.2c.7 2 2 3 3.4 3s2.7-1 3.4-3" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/><circle cx="9.4" cy="9.4" r="1" fill="currentColor"/><circle cx="14.6" cy="9.4" r="1" fill="currentColor"/></symbol>
<symbol id="i-play" viewBox="0 0 24 24"><path d="M7 4.6v14.8L19.4 12z" fill="currentColor"/></symbol>
<symbol id="i-android" viewBox="0 0 24 24"><path d="M7.2 9.4h9.6v7.2a1.4 1.4 0 0 1-1.4 1.4H8.6a1.4 1.4 0 0 1-1.4-1.4zM7.2 8.6a4.8 4.8 0 0 1 9.6 0zM9.2 4.4 8.2 2.8M14.8 4.4l1-1.6M4.2 10.4v5M19.8 10.4v5M10 18v3M14 18v3" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><circle cx="9.9" cy="6.5" r=".8" fill="currentColor"/><circle cx="14.1" cy="6.5" r=".8" fill="currentColor"/></symbol>
<symbol id="i-check" viewBox="0 0 24 24"><path d="m5.5 12.5 4.2 4.2 8.8-9.4" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></symbol>
<symbol id="i-arrow" viewBox="0 0 24 24"><path d="M5 12h14m-5.5-5.5L19 12l-5.5 5.5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></symbol>
<symbol id="i-mail" viewBox="0 0 24 24"><rect x="3" y="5.4" width="18" height="13.2" rx="2.6" fill="currentColor" fill-opacity=".2" stroke="currentColor" stroke-width="1.8"/><path d="m4 7.4 8 6 8-6" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></symbol>
<symbol id="i-spade" viewBox="0 0 24 24"><path d="M12 2.6c3.2 3.8 7.4 6.2 7.4 10a4.2 4.2 0 0 1-7.4 2.7c.1 2.1.6 3.7 1.8 5.1H10.2c1.2-1.4 1.7-3 1.8-5.1a4.2 4.2 0 0 1-7.4-2.7c0-3.8 4.2-6.2 7.4-10z" fill="currentColor"/></symbol>
<symbol id="i-heart" viewBox="0 0 24 24"><path d="M12 20.6C5.4 15.6 3 12.6 3 9.2A4.7 4.7 0 0 1 7.8 4.4c1.7 0 3.2.9 4.2 2.3 1-1.4 2.5-2.3 4.2-2.3A4.7 4.7 0 0 1 21 9.2c0 3.4-2.4 6.4-9 11.4z" fill="currentColor"/></symbol>
<symbol id="i-club" viewBox="0 0 24 24"><path d="M12 3a4 4 0 0 0-3.4 6.1A4.2 4.2 0 1 0 11 15.2c0 2-.5 3.6-1.8 5.4h5.6c-1.3-1.8-1.8-3.4-1.8-5.4a4.2 4.2 0 1 0 2.4-6.1A4 4 0 0 0 12 3z" fill="currentColor"/></symbol>
<symbol id="i-diamond" viewBox="0 0 24 24"><path d="M12 2.4 19.4 12 12 21.6 4.6 12z" fill="currentColor"/></symbol>
</defs></svg>"""


def ico(name, cls=""):
    return '<svg class="ic %s" aria-hidden="true"><use href="#i-%s"/></svg>' % (cls, name)


PLAY_ICON = ('<svg viewBox="0 0 512 512" aria-hidden="true">'
    '<path fill="#00d7fe" stroke="#00d7fe" stroke-width="22" stroke-linejoin="round" d="M60 40L290 256 60 472z"/>'
    '<path fill="#00f076" stroke="#00f076" stroke-width="22" stroke-linejoin="round" d="M60 40L380 208 290 256z"/>'
    '<path fill="#ff3a44" stroke="#ff3a44" stroke-width="22" stroke-linejoin="round" d="M60 472L380 304 290 256z"/>'
    '<path fill="#ffc400" stroke="#ffc400" stroke-width="22" stroke-linejoin="round" d="M380 208L462 256 380 304 290 256z"/></svg>')

CSS = r"""
/* ============ home: dark stage ============ */
body.home{background:#060f2b;color:#dbe6ff}
.home section{padding:110px 0;position:relative}
.home .container{position:relative}
.home h2,.home h3{color:#fff}
.home .kicker{color:var(--sky)}
.home .section-head p{color:#9fb2e4}
:where(.home) img{height:auto}
.ic{width:1em;height:1em;display:inline-block;vertical-align:-.12em;flex:none}
.progress{position:fixed;left:0;top:0;height:3px;width:100%;transform-origin:0 50%;transform:scaleX(0);background:linear-gradient(90deg,var(--pink),var(--gold),var(--mint),var(--sky));z-index:60}
.site-header{transition:background .3s,box-shadow .3s}
.site-header.scrolled{background:rgba(6,15,43,.92);box-shadow:0 10px 30px rgba(0,0,0,.35)}
.brand{transition:transform .25s}.brand:hover{transform:scale(1.03)}
.menu-btn{display:none;margin-left:auto;width:46px;height:46px;border-radius:14px;border:1px solid rgba(255,255,255,.18);background:rgba(255,255,255,.06);color:#fff;cursor:pointer;align-items:center;justify-content:center}
.menu-btn i,.menu-btn i:before,.menu-btn i:after{display:block;width:20px;height:2px;border-radius:2px;background:currentColor;transition:transform .3s,background .3s;content:"";position:relative}
.menu-btn i:before{position:absolute;top:-6px}.menu-btn i:after{position:absolute;top:6px}
.site-header.open .menu-btn i{background:transparent}
.site-header.open .menu-btn i:before{transform:translateY(6px) rotate(45deg)}
.site-header.open .menu-btn i:after{transform:translateY(-6px) rotate(-45deg)}
@media(max-width:860px){
.menu-btn{display:inline-flex}
.site-header .nav{position:absolute;left:0;right:0;top:72px;flex-direction:column;align-items:stretch;gap:2px;padding:12px 20px 20px;margin:0;background:rgba(6,15,43,.97);border-bottom:1px solid rgba(255,255,255,.1);transform:translateY(-12px);opacity:0;pointer-events:none;transition:opacity .25s,transform .25s}
.site-header.open .nav{opacity:1;transform:none;pointer-events:auto}
.site-header .nav a:not(.cta){display:block;padding:14px 16px;font-size:17px}
.nav .cta{margin:8px 0 0;text-align:center;padding:14px}
}

/* ============ hero ============ */
.home .hero{padding:0;background:#071238}
.hero-bg{position:absolute;inset:0;overflow:hidden;pointer-events:none}
.orb{position:absolute;border-radius:50%;filter:blur(70px);opacity:.55;animation:orb 16s ease-in-out infinite}
.orb.a{width:560px;height:560px;left:62%;top:-10%;background:#2d7bff}
.orb.b{width:460px;height:460px;left:-8%;top:55%;background:#ff4d8d;opacity:.32;animation-duration:20s;animation-direction:reverse}
.orb.c{width:380px;height:380px;left:38%;top:62%;background:#7c5cff;opacity:.32;animation-duration:23s}
@keyframes orb{0%,100%{transform:translate(0,0) scale(1)}50%{transform:translate(40px,-34px) scale(1.12)}}
.hero-grid{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.045) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.045) 1px,transparent 1px);background-size:56px 56px;mask-image:radial-gradient(ellipse at 70% 40%,#000 0,transparent 70%);-webkit-mask-image:radial-gradient(ellipse at 70% 40%,#000 0,transparent 70%)}
.home .hero .container{padding-top:44px;padding-bottom:84px;min-height:min(calc(100svh - 72px),860px)}
.hero h1{font-size:clamp(38px,4.4vw,62px);letter-spacing:-.03em;line-height:1.05;margin:18px 0 16px}
.hero .lead{font-size:clamp(17px,1.5vw,20px)}
.hero-logo{width:min(112px,30%)}
.store-row{display:flex;align-items:center;gap:16px;flex-wrap:wrap;margin-top:34px}
.btn.glass{color:#fff;background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.22);backdrop-filter:blur(8px)}
.btn.glass:hover{background:rgba(255,255,255,.14)}
.btn .ic{width:20px;height:20px}
.hero-meta{display:flex;gap:22px;flex-wrap:wrap;margin-top:34px;color:#b9c9f3;font-size:15px}
.hero-meta span{display:inline-flex;align-items:center;gap:8px}
.hero-meta .ic{width:20px;height:20px;color:var(--mint)}
.hero-art{--mx:0;--my:0;perspective:1200px}
.hero-art .phone{will-change:transform}
.hero-art .c{translate:calc(var(--mx)*-14px) calc(var(--my)*-10px)}
.hero-art .l{translate:calc(var(--mx)*-30px) calc(var(--my)*-18px)}
.hero-art .r{translate:calc(var(--mx)*-22px) calc(var(--my)*-26px)}
.float-chip{position:absolute;z-index:5;display:flex;align-items:center;gap:10px;padding:10px 16px 10px 10px;border-radius:16px;background:rgba(10,24,70,.72);border:1px solid rgba(255,255,255,.2);backdrop-filter:blur(12px);color:#fff;font:600 14px "Poppins",sans-serif;box-shadow:0 18px 40px rgba(0,0,0,.4);animation:chipfloat 6s ease-in-out infinite}
.float-chip img{width:34px;height:34px;border-radius:50%}
.float-chip .ic{width:34px;height:34px;padding:7px;border-radius:50%;background:linear-gradient(145deg,#ff9a3d,var(--gold));color:#3a2a00}
.float-chip small{display:block;font:500 11.5px "Inter",sans-serif;color:#a9bbea}
.float-chip.f1{left:-3%;top:6%}.float-chip.f2{right:-4%;top:56%;animation-delay:-2s}.float-chip.f3{left:2%;bottom:5%;animation-delay:-4s}
@keyframes chipfloat{0%,100%{transform:translateY(0)}50%{transform:translateY(-12px)}}
.scroll-cue{position:absolute;left:50%;bottom:22px;translate:-50% 0;width:26px;height:42px;border-radius:14px;border:2px solid rgba(255,255,255,.35)}
.scroll-cue:after{content:"";position:absolute;left:50%;top:8px;width:4px;height:8px;margin-left:-2px;border-radius:2px;background:#fff;animation:wheel 1.8s ease-in-out infinite}
@keyframes wheel{0%{opacity:0;transform:translateY(0)}30%{opacity:1}100%{opacity:0;transform:translateY(14px)}}
@media(max-width:940px){.home .hero .container{min-height:0;padding-top:46px}.float-chip{display:none}.scroll-cue{display:none}.hero-meta,.store-row{justify-content:center}}

/* ticker */
.home .ticker{background:#0a1c57;border-top:1px solid rgba(255,255,255,.08);border-bottom:1px solid rgba(255,255,255,.08)}
.home .ticker .track{gap:34px}
.home .ticker i{color:var(--gold)}

/* ============ bento features ============ */
.bento{display:grid;grid-template-columns:repeat(6,1fr);gap:20px}
.bcard{--x:50%;--y:0%;position:relative;overflow:hidden;border-radius:26px;padding:32px;min-height:300px;background:linear-gradient(160deg,rgba(255,255,255,.075),rgba(255,255,255,.025));border:1px solid rgba(255,255,255,.1);isolation:isolate;transition:transform .45s cubic-bezier(.2,.8,.2,1),border-color .3s}
.bcard:before{content:"";position:absolute;inset:0;z-index:-1;background:radial-gradient(420px circle at var(--x) var(--y),rgba(74,163,255,.2),transparent 60%);opacity:0;transition:opacity .3s}
.bcard:hover{transform:translateY(-6px);border-color:rgba(255,255,255,.26)}
.bcard:hover:before{opacity:1}
.bcard .badge{width:54px;height:54px;border-radius:17px;display:grid;place-items:center;margin-bottom:20px;color:#fff;box-shadow:0 12px 26px rgba(0,0,0,.3),inset 0 1px 0 rgba(255,255,255,.35)}
.bcard .badge .ic{width:28px;height:28px}
.b-blue .badge{background:linear-gradient(145deg,#2d7bff,var(--sky))}
.b-violet .badge{background:linear-gradient(145deg,var(--violet),#b49bff)}
.b-gold .badge{background:linear-gradient(145deg,#ff9a3d,var(--gold));color:#3a2a00}
.b-mint .badge{background:linear-gradient(145deg,#12c98f,#7df2cb);color:#053a2a}
.b-pink .badge{background:linear-gradient(145deg,var(--pink),#ff9ab9)}
.b-red .badge{background:linear-gradient(145deg,#ef4444,#ff8a8a)}
.bcard h3{font-size:24px;margin:0 0 10px}
.bcard p{margin:0;color:#a9bbea;font-size:16px;max-width:420px}
.s2{grid-column:span 2}.s3{grid-column:span 3}.s4{grid-column:span 4}
@media(max-width:980px){.bento{grid-template-columns:repeat(2,1fr)}.s2,.s3,.s4{grid-column:span 1}.s4{grid-column:span 2}}
@media(max-width:620px){.bento{grid-template-columns:1fr}.s2,.s3,.s4{grid-column:span 1}.bcard{min-height:0;padding:26px}}
.viz{position:relative;margin-top:26px}
/* quick match viz */
.match{display:flex;align-items:center;gap:18px}
.match .av{width:68px;height:68px;border-radius:50%;border:3px solid rgba(255,255,255,.85);box-shadow:0 10px 24px rgba(0,0,0,.35);background:#fff}
.match .av.l{animation:slideL 4.8s ease-in-out infinite}.match .av.r{animation:slideR 4.8s ease-in-out infinite}
.match .vs{font:800 22px "Poppins",sans-serif;color:var(--gold);animation:vs 4.8s ease-in-out infinite}
.match .pill{margin-left:6px;padding:8px 16px;border-radius:999px;font:600 14px "Poppins",sans-serif;background:rgba(46,230,166,.16);color:var(--mint);border:1px solid rgba(46,230,166,.4);animation:pillpop 4.8s ease-in-out infinite}
@keyframes slideL{0%,12%{transform:translateX(-46px);opacity:0}30%,88%{transform:none;opacity:1}100%{transform:translateX(-46px);opacity:0}}
@keyframes slideR{0%,12%{transform:translateX(46px);opacity:0}30%,88%{transform:none;opacity:1}100%{transform:translateX(46px);opacity:0}}
@keyframes vs{0%,22%{transform:scale(0);opacity:0}34%{transform:scale(1.4);opacity:1}44%,88%{transform:scale(1);opacity:1}100%{opacity:0}}
@keyframes pillpop{0%,40%{opacity:0;transform:translateY(8px)}52%,88%{opacity:1;transform:none}100%{opacity:0}}
/* room code viz */
.code{display:flex;gap:10px}
.code b{width:50px;height:62px;display:grid;place-items:center;border-radius:14px;font:800 28px "Poppins",sans-serif;color:#fff;background:linear-gradient(160deg,#16307f,#0d1f5c);border:1px solid rgba(255,255,255,.2);animation:codein 5.2s ease-in-out infinite}
.code b:nth-child(2){animation-delay:.12s}.code b:nth-child(3){animation-delay:.24s}.code b:nth-child(4){animation-delay:.36s}
@keyframes codein{0%,6%{transform:translateY(24px) rotateX(70deg);opacity:0}18%,86%{transform:none;opacity:1}100%{transform:translateY(-10px);opacity:0}}
.avstack{display:flex;margin-top:18px}
.avstack img{width:44px;height:44px;border-radius:50%;border:3px solid #0d1f5c;margin-left:-12px;background:#fff}
.avstack img:first-child{margin-left:0}
/* trophy viz */
.ranks{display:flex;align-items:flex-end;gap:12px;justify-content:space-between}
.ranks figure{margin:0;text-align:center;flex:1;opacity:.35;transform:translateY(8px) scale(.9);transition:opacity .6s,transform .6s}
.ranks img{width:100%;max-width:62px;margin:0 auto;filter:drop-shadow(0 8px 14px rgba(0,0,0,.4))}
.ranks figcaption{font:600 11.5px "Poppins",sans-serif;color:#9fb2e4;margin-top:6px}
.bcard.in .ranks figure{opacity:1;transform:none}
.bcard.in .ranks figure:nth-child(2){transition-delay:.15s}.bcard.in .ranks figure:nth-child(3){transition-delay:.3s}.bcard.in .ranks figure:nth-child(4){transition-delay:.45s}.bcard.in .ranks figure:nth-child(5){transition-delay:.6s}.bcard.in .ranks figure:nth-child(6){transition-delay:.75s}
.bar{height:10px;border-radius:10px;background:rgba(255,255,255,.1);margin-top:18px;overflow:hidden}
.bar i{display:block;height:100%;width:0;border-radius:10px;background:linear-gradient(90deg,var(--gold),var(--pink));transition:width 1.8s cubic-bezier(.2,.8,.2,1) .4s}
.bcard.in .bar i{width:62%}
/* coin viz */
.coinwrap{display:flex;align-items:center;gap:22px}
.bigcoin{width:92px;height:92px;border-radius:50%;flex:none;display:grid;place-items:center;font:800 40px "Poppins",sans-serif;color:#7a4b00;background:radial-gradient(circle at 32% 28%,#fff3b0,#ffc83d 55%,#e08a00);box-shadow:inset 0 0 0 6px rgba(255,255,255,.35),0 16px 34px rgba(255,184,31,.4);animation:spin 5s linear infinite}
@keyframes spin{from{transform:rotateY(0)}to{transform:rotateY(360deg)}}
.coinwrap ul{list-style:none;margin:0;padding:0;color:#d6e2ff;font-size:15px}
.coinwrap li{display:flex;gap:8px;align-items:center;margin:6px 0}
.coinwrap li .ic{color:var(--mint);width:18px;height:18px}
/* skins viz */
.fanrow{display:flex;justify-content:center;align-items:flex-end;height:230px;margin-top:6px}
.fanrow img{width:136px;border-radius:14px;margin:0 -22px;box-shadow:0 18px 36px rgba(0,0,0,.5);transform-origin:50% 120%;transition:transform .5s cubic-bezier(.2,.8,.2,1)}
.fanrow img:nth-child(1){transform:rotate(-14deg) translateY(14px)}.fanrow img:nth-child(2){transform:rotate(-5deg)}.fanrow img:nth-child(3){transform:rotate(5deg)}.fanrow img:nth-child(4){transform:rotate(14deg) translateY(14px)}
.bcard:hover .fanrow img:nth-child(1){transform:rotate(-22deg) translate(-26px,8px)}.bcard:hover .fanrow img:nth-child(2){transform:rotate(-8deg) translateY(-14px)}.bcard:hover .fanrow img:nth-child(3){transform:rotate(8deg) translateY(-14px)}.bcard:hover .fanrow img:nth-child(4){transform:rotate(22deg) translate(26px,8px)}
/* vibes viz */
.emotes{display:flex;gap:12px;flex-wrap:wrap}
.emotes span{width:54px;height:54px;border-radius:18px;display:grid;place-items:center;font-size:28px;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.14);animation:emo 3.6s ease-in-out infinite}
.emotes span:nth-child(2){animation-delay:.4s}.emotes span:nth-child(3){animation-delay:.8s}.emotes span:nth-child(4){animation-delay:1.2s}
@keyframes emo{0%,100%{transform:translateY(0) rotate(0)}50%{transform:translateY(-10px) rotate(-6deg)}}

/* ============ sticky showcase ============ */
.show{background:linear-gradient(180deg,#060f2b,#0a1a52 50%,#060f2b)}
.show-grid{display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:start}
.show-steps .show-step{min-height:82vh;display:flex;flex-direction:column;justify-content:center;opacity:.35;transition:opacity .5s,transform .5s;transform:translateX(-12px)}
.show-steps .show-step.active{opacity:1;transform:none}
.show-step h3{font-size:clamp(30px,3.6vw,46px);margin:12px 0 16px;font-weight:800;letter-spacing:-.02em}
.show-step p{color:#a9bbea;font-size:18px;margin:0 0 6px;max-width:500px}
.show-step .kicker{display:flex;align-items:center;gap:10px}
.show-step .kicker .ic{width:22px;height:22px}
.show-step .ticks{margin-top:22px}
.show-step .ticks li{color:#dbe6ff}
.show-step .step-phone{display:none}
.show-stage{position:sticky;top:calc(50vh - 360px);top:max(88px,calc(50vh - 360px));height:720px;display:grid;place-items:center}
.stage-ring{position:absolute;width:560px;height:560px;border-radius:50%;background:conic-gradient(from 0deg,rgba(74,163,255,.5),rgba(124,92,255,.4),rgba(255,93,143,.4),rgba(255,200,61,.35),rgba(74,163,255,.5));filter:blur(46px);opacity:.55;animation:ring 14s linear infinite}
@keyframes ring{to{transform:rotate(360deg)}}
.stage-phone{position:relative;width:340px;z-index:2;transition:transform .8s cubic-bezier(.2,.8,.2,1)}
.stage-phone .screen{position:relative}
.stage-phone .screen img{position:absolute;inset:0;opacity:0;transform:scale(1.06);transition:opacity .7s,transform .9s cubic-bezier(.2,.8,.2,1)}
.stage-phone .screen img.on{opacity:1;transform:none}
.stage-dots{position:absolute;right:calc(50% - 280px);top:50%;translate:0 -50%;display:flex;flex-direction:column;gap:10px;z-index:3}
.stage-dots i{width:9px;height:9px;border-radius:50%;background:rgba(255,255,255,.28);transition:all .3s}
.stage-dots i.on{background:var(--gold);height:30px;border-radius:6px}
@media(max-width:980px){
.show-grid{grid-template-columns:1fr;gap:0}
.show-stage{display:none}
.show-steps .show-step{min-height:0;opacity:1;transform:none;padding:0 0 76px;align-items:center;text-align:center}
.show-step .ticks{text-align:left}
.show-step .step-phone{display:block;width:min(270px,70%);margin:36px auto 0}
}

/* ============ how a round works: dealt cards ============ */
.rounds{display:grid;grid-template-columns:repeat(3,1fr);gap:28px;perspective:1400px}
@media(max-width:900px){.rounds{grid-template-columns:1fr;max-width:380px;margin:0 auto}}
.rcard{position:relative;height:420px;transform-style:preserve-3d;transition:transform 1s cubic-bezier(.2,.8,.2,1);transition-delay:var(--d,0s)}
.rcard.in{transform:rotateY(180deg)}
.rcard>div{position:absolute;inset:0;border-radius:26px;backface-visibility:hidden;-webkit-backface-visibility:hidden;overflow:hidden}
.rcard .back{background:#0d1f5c center/cover no-repeat;box-shadow:0 24px 50px rgba(0,0,0,.45);border:6px solid #fff}
.rcard .face{transform:rotateY(180deg);background:linear-gradient(165deg,#fff,#eef3ff);color:#101b3a;padding:34px 28px;box-shadow:0 30px 60px rgba(0,0,0,.45);display:flex;flex-direction:column}
.rcard .face:before{content:"";position:absolute;inset:9px;border:1.5px solid rgba(16,27,58,.1);border-radius:19px;pointer-events:none}
.rcard .num{position:absolute;top:18px;left:22px;font:800 30px/1 "Poppins",sans-serif;color:var(--c,#101b3a);display:flex;flex-direction:column;align-items:center;gap:2px}
.rcard .num .ic{width:22px;height:22px}
.rcard .face .pip{width:92px;height:92px;margin:34px auto 18px;color:var(--c,#101b3a);opacity:.95}
.rcard .face h3{color:#101b3a;font-size:24px;margin:0 0 10px;text-align:center}
.rcard .face p{margin:0;color:#4a5878;font-size:16px;text-align:center}
.rcard.red{--c:#e0245e}
.rcard:hover{transform:rotateY(180deg) translateY(-10px)}

/* ============ collect: marquees and fans ============ */
.collect{background:radial-gradient(900px 500px at 50% 0,rgba(124,92,255,.22),transparent 70%),#060f2b;overflow:hidden}
.mq{overflow:hidden;mask-image:linear-gradient(90deg,transparent,#000 8%,#000 92%,transparent);-webkit-mask-image:linear-gradient(90deg,transparent,#000 8%,#000 92%,transparent);padding:18px 0}
.mq .lane{display:flex;gap:22px;width:max-content;animation:marquee 46s linear infinite}
.mq.rev .lane{animation-direction:reverse;animation-duration:52s}
.mq:hover .lane{animation-play-state:paused}
.skin{flex:none;width:190px;border-radius:20px;overflow:hidden;box-shadow:0 20px 44px rgba(0,0,0,.5);transition:transform .35s cubic-bezier(.2,.8,.2,1);transform-style:preserve-3d}
.skin:hover{transform:translateY(-12px) scale(1.05) rotate(-1.5deg)}
.skin img{width:100%;display:block}
.avs .lane{gap:16px;animation-duration:60s}
.avs.rev .lane{animation-duration:68s}
.avs img{flex:none;width:96px;height:96px;border-radius:50%;border:3px solid rgba(255,255,255,.9);background:#fff;box-shadow:0 12px 26px rgba(0,0,0,.4);transition:transform .3s}
.avs img:hover{transform:scale(1.14) rotate(6deg)}
.sub-head{text-align:center;margin:60px 0 6px;font:700 13px "Poppins",sans-serif;letter-spacing:.16em;text-transform:uppercase;color:#9fb2e4}
.backs{display:flex;justify-content:center;margin:34px 0 10px;height:300px;align-items:center}
.backs img{width:170px;border-radius:14px;margin:0 -30px;box-shadow:0 22px 44px rgba(0,0,0,.55);transition:transform .6s cubic-bezier(.2,.8,.2,1);border:4px solid #fff}
.backs img:nth-child(1){transform:rotate(-12deg) translateY(10px)}.backs img:nth-child(2){transform:rotate(-4deg)}.backs img:nth-child(3){transform:rotate(4deg)}.backs img:nth-child(4){transform:rotate(12deg) translateY(10px)}
.backs:hover img:nth-child(1){transform:rotate(-18deg) translate(-70px,10px)}.backs:hover img:nth-child(2){transform:rotate(-6deg) translate(-24px,-12px)}.backs:hover img:nth-child(3){transform:rotate(6deg) translate(24px,-12px)}.backs:hover img:nth-child(4){transform:rotate(18deg) translate(70px,10px)}
@media(max-width:700px){.skin{width:150px}.avs img{width:76px;height:76px}.backs img{width:110px;margin:0 -22px}.backs{height:220px}}

/* ============ ranks band ============ */
.rankband{background:linear-gradient(135deg,#1b1470,#0f2a73 60%,#0a1a52)}
.rankband .container{display:grid;grid-template-columns:.9fr 1.1fr;gap:60px;align-items:center}
.rankband h2{font-size:clamp(30px,4vw,48px);font-weight:800;margin:12px 0 16px}
.rankband p{color:#c3d1f7;font-size:18px;margin:0}
.shields{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.shield{text-align:center;padding:22px 10px 16px;border-radius:22px;background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.14);transition:transform .35s,background .35s}
.shield:hover{transform:translateY(-8px) scale(1.04);background:rgba(255,255,255,.13)}
.shield img{width:76px;margin:0 auto 10px;filter:drop-shadow(0 10px 16px rgba(0,0,0,.45));animation:bob2 5s ease-in-out infinite}
.shield:nth-child(2n) img{animation-delay:-1.4s}.shield:nth-child(3n) img{animation-delay:-2.6s}
@keyframes bob2{0%,100%{transform:translateY(0)}50%{transform:translateY(-8px)}}
.shield b{display:block;font:700 15px "Poppins",sans-serif;color:#fff}
.shield small{color:#9fb2e4;font-size:12.5px}
@media(max-width:900px){.rankband .container{grid-template-columns:1fr;text-align:center}}

/* ============ party ============ */
.party{padding:120px 0!important}
.party .floaters{position:absolute;inset:0;pointer-events:none}
.party .floaters img{position:absolute;width:84px;height:84px;border-radius:50%;border:3px solid rgba(255,255,255,.85);background:#fff;box-shadow:0 16px 34px rgba(0,0,0,.4);animation:chipfloat 7s ease-in-out infinite}
@media(max-width:900px){.party .floaters img{width:56px;height:56px}.party .floaters img:nth-child(n+5){display:none}}
.party .container{position:relative;z-index:2}

/* ============ faq / cta / studio ============ */
.home .faq details{background:rgba(255,255,255,.05);border-color:rgba(255,255,255,.12)}
.home .faq details:hover{border-color:rgba(255,255,255,.3)}
.home .faq summary{color:#fff}
.home .faq summary:after{color:var(--gold)}
.home .faq details p{color:#a9bbea}
.home .faq a{color:var(--sky)}
.home .studio{background:#081538;border-top:1px solid rgba(255,255,255,.08)}
.home .studio h2{color:#fff}
.home .studio p{color:#a9bbea}
.home .studio img{filter:drop-shadow(0 20px 36px rgba(0,0,0,.5));transition:transform .5s}
.home .studio img:hover{transform:rotate(-4deg) scale(1.05)}
.home .cta-band{padding:120px 0}
.home .cta-band img{width:170px}
.home .cta-band h2{font-size:clamp(34px,5vw,60px)}
.socials{display:flex;gap:12px;justify-content:center;margin-top:26px}
.socials a{display:inline-flex;align-items:center;gap:10px;color:#fff;text-decoration:none;font:600 15px "Poppins",sans-serif;padding:12px 20px;border-radius:14px;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.18);transition:background .25s,transform .25s}
.socials a:hover{background:rgba(255,255,255,.16);transform:translateY(-2px)}
.socials .ic{width:20px;height:20px}
.app-icon{width:84px;height:84px;border-radius:22px;box-shadow:0 14px 30px rgba(0,0,0,.4),0 0 0 1px rgba(255,255,255,.15)}
.site-footer .appline{display:flex;align-items:center;gap:14px;margin-bottom:16px}
.site-footer .appline img{height:56px;width:56px;border-radius:15px}

/* ============ reveal system ============ */
.js .rv{opacity:0;transform:translateY(34px);transition:opacity .9s cubic-bezier(.2,.8,.2,1) var(--d,0s),transform .9s cubic-bezier(.2,.8,.2,1) var(--d,0s)}
.js .rv.in{opacity:1;transform:none;animation:none}
.js .pcard.rv.in{animation:none}
.js .rcard.rv{opacity:1;transform:none;transition:transform 1s cubic-bezier(.2,.8,.2,1) var(--d,0s)}
.js .rcard.rv.in{transform:rotateY(180deg)}
.js .rcard.rv.in:hover{transform:rotateY(180deg) translateY(-10px)}
.js .bcard.rv{transition:opacity .9s cubic-bezier(.2,.8,.2,1) var(--d,0s),transform .9s cubic-bezier(.2,.8,.2,1) var(--d,0s),border-color .3s}
.js .bcard.rv.in:hover{transform:translateY(-6px)}
.tilt{transition:transform .2s ease-out;will-change:transform}
@media(prefers-reduced-motion:reduce){
.orb,.stage-ring,.float-chip,.mq .lane,.bigcoin,.match *,.code b,.emotes span,.shield img,.party .floaters img{animation:none!important}
.js .rv,.rcard{opacity:1!important;transform:none!important}
.rcard .back{display:none}.rcard .face{transform:none!important;position:relative;height:100%}
.show-steps .show-step{opacity:1}
}
"""

JS = r"""
(function(){
var d=document,h=d.querySelector(".site-header"),bar=d.querySelector(".progress");
var rm=window.matchMedia&&window.matchMedia("(prefers-reduced-motion: reduce)").matches;
function onScroll(){var y=window.scrollY||0,m=d.documentElement.scrollHeight-window.innerHeight;
 if(h)h.classList.toggle("scrolled",y>20);
 if(bar)bar.style.transform="scaleX("+(m>0?Math.min(1,y/m):0)+")";}
window.addEventListener("scroll",onScroll,{passive:true});onScroll();
var mb=d.querySelector(".menu-btn");
if(mb&&h){mb.addEventListener("click",function(){var o=h.classList.toggle("open");mb.setAttribute("aria-expanded",o)});
 d.querySelectorAll(".nav a").forEach(function(a){a.addEventListener("click",function(){h.classList.remove("open");mb.setAttribute("aria-expanded","false")})});}
/* hero parallax */
var art=d.querySelector(".hero-art"),hero=d.querySelector(".hero");
if(art&&hero&&!rm&&window.matchMedia("(pointer:fine)").matches){
 hero.addEventListener("pointermove",function(e){var r=hero.getBoundingClientRect();
  art.style.setProperty("--mx",((e.clientX-r.left)/r.width-.5).toFixed(3));
  art.style.setProperty("--my",((e.clientY-r.top)/r.height-.5).toFixed(3));});
 hero.addEventListener("pointerleave",function(){art.style.setProperty("--mx",0);art.style.setProperty("--my",0)});}
/* spotlight on bento cards */
d.querySelectorAll(".bcard").forEach(function(c){c.addEventListener("pointermove",function(e){var r=c.getBoundingClientRect();
 c.style.setProperty("--x",(e.clientX-r.left)+"px");c.style.setProperty("--y",(e.clientY-r.top)+"px");});});
/* gentle 3D tilt */
if(!rm&&window.matchMedia("(pointer:fine)").matches){d.querySelectorAll(".tilt").forEach(function(t){
 t.addEventListener("pointermove",function(e){var r=t.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;
  t.style.transform="perspective(900px) rotateY("+(x*10).toFixed(1)+"deg) rotateX("+(-y*10).toFixed(1)+"deg) translateY(-6px)"});
 t.addEventListener("pointerleave",function(){t.style.transform=""});});}
/* sticky showcase: which step is in the middle of the screen */
var steps=d.querySelectorAll(".show-step"),imgs=d.querySelectorAll(".stage-phone .screen img"),dots=d.querySelectorAll(".stage-dots i");
function setStep(i){steps.forEach(function(s,k){s.classList.toggle("active",k===i)});
 imgs.forEach(function(s,k){s.classList.toggle("on",k===i)});dots.forEach(function(s,k){s.classList.toggle("on",k===i)});}
if(steps.length&&"IntersectionObserver" in window){
 var so=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting)setStep(+e.target.getAttribute("data-i"))})},{rootMargin:"-45% 0px -45% 0px"});
 steps.forEach(function(s){so.observe(s)});}
setStep(0);
})();
"""


def phone(name, alt, cls="", eager=False):
    return '<div class="phone %s"><div class="screen"><img src="/assets/shot-%s.webp" alt="%s" width="450" height="1000"%s></div></div>' % (
        cls, name, html.escape(alt), "" if eager else ' loading="lazy"')


def img(path, alt="", w=None, h=None, cls="", lazy=True):
    return '<img src="/assets/%s" alt="%s"%s%s%s%s>' % (
        path, html.escape(alt), ' width="%d"' % w if w else "", ' height="%d"' % h if h else "",
        ' class="%s"' % cls if cls else "", ' loading="lazy" decoding="async"' if lazy else "")


FAQS = [
    ("Is 5 Cards free?", "Yes. 5 Cards is free to download and play. You earn coins by playing and from daily rewards, and you can also top up with optional in-app purchases if you like. You never need to buy anything to play."),
    ("Is it gambling?", "No. 5 Cards is a party card game played for fun. There are no cash prizes and coins can never be turned into money, goods or services. Just bragging rights and good vibes."),
    ("Can I play with my friends?", "Absolutely. Open a private room, share the room code and your friends can jump straight in. You can also add friends and invite them to a game."),
    ("Which devices does it run on?", "5 Cards is built for Android phones. It is coming soon to Google Play."),
    ("How do I sign in?", "Continue with Google or Facebook, or jump in as a guest. We never see your passwords."),
    ("How do I delete my account?", "In the game go to Settings, Support, Delete Account. No game installed? Email us and we will take care of it. See the <a href=\"/delete-account/\">account deletion page</a>."),
]

SUIT_BITS = "".join('<span style="left:%d%%;top:%d%%;font-size:%dpx;transform:rotate(%ddeg)">%s</span>' % (x, y, s, r, g)
                    for x, y, s, r, g in [(4, 12, 56, -14, "&spades;"), (46, 6, 40, 12, "&hearts;"), (92, 18, 60, 18, "&clubs;"),
                                          (30, 70, 48, -8, "&diams;"), (62, 82, 44, 10, "&spades;"), (8, 86, 36, 20, "&hearts;")])

RANKS = [("Rookie", 1), ("Challenger", 2), ("Ace", 3), ("Expert", 4), ("Master", 5), ("Legend", 6)]


def home_body():
    ticker_items = ["Quick matches", "Private rooms", "Trophy Road", "Card skins", "Daily rewards"]
    suits = ["spade", "heart", "club", "diamond", "spade"]
    track = "".join("<span>%s</span><i>%s</i>" % (t, ico(suits[i % 5])) for i, t in enumerate(ticker_items * 2))

    skins = ["galaxy", "diwali", "inferno", "neon", "ocean", "sakura"]
    skin_lane = "".join('<a class="skin tilt" href="#collect" tabindex="-1">%s</a>' % img("skin-%s.webp" % s, "%s card skin" % s.title(), 360, 540) for s in skins * 2)
    av_names = ["male", "female", "animal"]
    avs = [("%s" % k, i) for i in range(1, 9) for k in av_names]
    av_a = "".join(img("av-%s-%d.webp" % (k, i), "", 160, 160) for k, i in avs[:12]) * 2
    av_b = "".join(img("av-%s-%d.webp" % (k, i), "", 160, 160) for k, i in avs[12:]) * 2

    shields = "".join('<div class="shield rv" style="--d:%.2fs">%s<b>%s</b><small>Rank %d</small></div>' % (
        i * .08, img("rank-%d.webp" % n, "%s rank badge" % name, 120, 140), name, n) for i, (name, n) in enumerate(RANKS))
    mini_ranks = "".join("<figure>%s<figcaption>%s</figcaption></figure>" % (img("rank-%d.webp" % n, "%s rank" % name, 120, 140), name) for name, n in RANKS)

    steps = [
        ("play", "Play your way", "Jump in, or throw a party",
         "Tap <b>Play Now</b> to find an opponent in seconds, open a <b>Private Room</b> and share the code with your crew, or warm up offline in <b>Practice</b>.",
         ["Quick online matches", "Private rooms with room codes", "Offline practice against computer players"], "menu", "5 Cards main menu with Play Now, Private Room and Practice"),
        ("cards", "The table", "Draw, pair up, call your show",
         "On your turn discard a card or a pair, then draw. Keep your hand value low and when you think you hold the lowest hand, call <b>Show</b>. Emotes and quick chat keep the table friendly, with no open text chat.",
         ["Clear turn timer and round tracker", "Playful emotes and quick chat", "Built-in tutorial for new players"], "table", "A 5 Cards table with four players"),
        ("trophy", "Climb the ranks", "Trophies, tiers and bragging rights",
         "Every win earns trophies. Rise from Rookie to Challenger to Ace on the Trophy Road, grab a reward at every step and see how you stack up on the global and friends leaderboards.",
         ["Seasonal Trophy Road with rewards", "Global and friends leaderboards", "Daily challenges and bonuses"], "trophy", "The Trophy Road with tiers from Rookie to Ace"),
        ("coin", "Make it yours", "Show off your style",
         "Unlock striking card skins, emotes and quick chat lines in the shop. Earn coins by playing and from free daily rewards like Pick Your Luck and Scratch Your Luck, or top up with optional in-app coin packs.",
         ["Dozens of card skins to collect", "Free daily coins", "Optional in-app coin packs"], "shop", "The shop with card skins"),
    ]
    step_html = ""
    for i, (ic, kick, h3, p, ticks, shot, alt) in enumerate(steps):
        step_html += ('<div class="show-step" data-i="%d"><span class="kicker">%s%s</span><h3>%s</h3><p>%s</p><ul class="ticks">%s</ul>'
                      '<div class="step-phone">%s</div></div>') % (
            i, ico(ic), kick, h3, p, "".join("<li>%s</li>" % t for t in ticks), phone(shot, alt))
    stage_imgs = "".join('<img src="/assets/shot-%s.webp" alt="%s" width="450" height="1000"%s>' % (
        s[5], html.escape(s[6]), ' class="on"' if i == 0 else ' loading="lazy"') for i, s in enumerate(steps))
    stage_dots = "".join("<i></i>" for _ in steps)

    rounds = [
        ("1", "spade", "", "Get your five cards", "Everyone is dealt a hand of five. Your goal is to end the round with the lowest hand value.", "ocean"),
        ("2", "heart", "red", "Discard and draw", "On your turn, discard one card or a matching pair, then draw a new card to improve your hand.", "midnight"),
        ("3", "diamond", "red", "Call your show", "Think yours is the lowest hand? Call <b>Show</b>: if you are right you score zero, but a wrong call costs you a penalty. The highest score each round is knocked out, and the last player standing wins.", "sunset"),
    ]
    round_html = "".join(
        ('<div class="rcard %s rv" style="--d:%.2fs"><div class="back" style="background-image:url(/assets/back-%s.webp)"></div>'
         '<div class="face"><div class="num">%s%s</div>%s<h3>%s</h3><p>%s</p></div></div>') % (
            c, i * .18, back, n, ico(s), ico(s, "pip"), h, p) for i, (n, s, c, h, p, back) in enumerate(rounds))

    floaters = "".join('<img style="left:%d%%;top:%d%%;animation-delay:%.1fs" src="/assets/av-%s-%d.webp" alt="" width="84" height="84" loading="lazy">' % (x, y, dl, k, i)
                       for x, y, dl, k, i in [(7, 18, 0, "female", 2), (86, 14, -2, "male", 5), (14, 70, -4, "animal", 3), (82, 68, -1, "female", 6),
                                              (30, 8, -3, "male", 2), (68, 80, -5, "animal", 7)])

    faq = "".join("<details><summary>%s</summary><p>%s</p></details>" % (q, a) for q, a in FAQS)

    return """
<div class="progress" aria-hidden="true"></div>
<section class="hero">
<div class="hero-bg" aria-hidden="true"><div class="hero-grid"></div><span class="orb a"></span><span class="orb b"></span><span class="orb c"></span><div class="suits">SUITS</div></div>
<div class="container">
<div class="hero-copy">
<img class="hero-logo" src="/assets/logo-5cards.webp" alt="5 Cards" width="250" height="226">
<span class="eyebrow">The multiplayer card game</span>
<h1>Game night, <em>right in your pocket.</em></h1>
<p class="lead">5 Cards is the fast, friendly card game made for friends, rivals and good vibes. Jump into a quick match, spin up a private room or climb the Trophy Road. Every round is a party.</p>
<div class="store-row" id="play">
<a class="gp" href="/contact/" aria-label="Coming soon on Google Play">PLAYICON<div><span>Coming soon on</span><b>Google Play</b></div></a>
<a class="btn glass" href="#gameplay">See the game ARROW</a>
</div>
<div class="hero-meta"><span>CHECK Free to play</span><span>ANDROID Android</span><span>CHECK No gambling, all vibes</span></div>
</div>
<div class="hero-art">MENU TABLE TROPHY
<div class="float-chip f1">AV1<div>Quick match<small>Opponent found</small></div></div>
<div class="float-chip f2"><span class="ic">TROPHYICON</span><div>Trophy Road<small>New rank unlocked</small></div></div>
<div class="float-chip f3">AV2<div>Private room<small>Friends joined</small></div></div>
</div>
</div>
<span class="scroll-cue" aria-hidden="true"></span>
</section>

<div class="ticker" aria-hidden="true"><div class="track">TRACK</div></div>

<section id="features"><div class="container">
<div class="section-head rv"><span class="kicker">Why you will love it</span><h2>Easy to learn. Impossible to put down.</h2><p>Short rounds, big laughs and always one more match to play.</p></div>
<div class="bento">
<div class="bcard b-blue s4 rv"><div class="badge">BOLT</div><h3>Quick matches</h3><p>Find an opponent in seconds and play a round of 5 Cards on the go.</p>
<div class="viz match"><img class="av l" src="/assets/av-male-1.webp" alt="" width="68" height="68"><span class="vs">VS</span><img class="av r" src="/assets/av-female-3.webp" alt="" width="68" height="68"><span class="pill">Match found</span></div></div>
<div class="bcard b-violet s2 rv" style="--d:.1s"><div class="badge">ROOM</div><h3>Private rooms</h3><p>Share a room code and play with friends, wherever they are.</p>
<div class="viz"><div class="code"><b>K</b><b>7</b><b>Q</b><b>2</b></div><div class="avstack"><img src="/assets/av-animal-1.webp" alt="" width="44" height="44"><img src="/assets/av-female-5.webp" alt="" width="44" height="44"><img src="/assets/av-male-4.webp" alt="" width="44" height="44"><img src="/assets/av-animal-6.webp" alt="" width="44" height="44"></div></div></div>
<div class="bcard b-gold s3 rv"><div class="badge">TROPHY</div><h3>Trophy Road</h3><p>Win to earn trophies, rise through the tiers and claim rewards.</p>
<div class="viz"><div class="ranks">MINIRANKS</div><div class="bar"><i></i></div></div></div>
<div class="bcard b-mint s3 rv" style="--d:.1s"><div class="badge">COIN</div><h3>Coins, your way</h3><p>Earn coins by playing and from daily rewards, or top up with optional in-app purchases.</p>
<div class="viz coinwrap"><div class="bigcoin">5</div><ul><li>CHECK Earn by playing</li><li>CHECK Free daily rewards</li><li>CHECK Optional coin packs</li></ul></div></div>
<div class="bcard b-pink s4 rv"><div class="badge">CARDS</div><h3>Card skins</h3><p>Collect colourful decks, emotes and quick chat lines to show off your style.</p>
<div class="fanrow">FANSKINS</div></div>
<div class="bcard b-red s2 rv" style="--d:.1s"><div class="badge">VIBES</div><h3>Good vibes only</h3><p>No open chat, no gambling and friendly emotes. You can delete your account in the game.</p>
<div class="viz"><div class="emotes"><span>&#128514;</span><span>&#128079;</span><span>&#128293;</span><span>&#127881;</span></div></div></div>
</div>
</div></section>

<section class="show" id="gameplay"><div class="container">
<div class="section-head rv"><span class="kicker">Inside the game</span><h2>A table that feels alive</h2><p>Colourful, smooth and made for one-handed play on your phone.</p></div>
<div class="show-grid">
<div class="show-steps">STEPS</div>
<div class="show-stage" aria-hidden="true"><div class="stage-ring"></div>
<div class="phone stage-phone"><div class="screen">STAGEIMGS</div></div><div class="stage-dots">STAGEDOTS</div></div>
</div>
</div></section>

<section id="how"><div class="container">
<div class="section-head rv"><span class="kicker">How a round works</span><h2>Learn it in a minute</h2><p>The in-game tutorial walks you through it with a real table and real cards.</p></div>
<div class="rounds">ROUNDS</div>
</div></section>

<section class="collect" id="collect"><div class="container">
<div class="section-head rv"><span class="kicker">Make it yours</span><h2>Collect the whole deck</h2><p>Card skins, card backs and a whole crowd of avatars. Pick the look that is you.</p></div>
</div>
<div class="mq" aria-label="Card skins"><div class="lane">SKINLANE</div></div>
<p class="sub-head">Card backs</p>
<div class="backs">BACKS</div>
<p class="sub-head">Avatars for everyone</p>
<div class="mq avs" aria-hidden="true"><div class="lane">AVA</div></div>
<div class="mq avs rev" aria-hidden="true"><div class="lane">AVB</div></div>
</section>

<section class="rankband" id="ranks"><div class="container">
<div class="rv"><span class="kicker">Trophy Road</span><h2>From Rookie to Legend</h2><p>Six ranks, a reward at every step and a season to chase. Every win moves you up the road.</p></div>
<div class="shields">SHIELDS</div>
</div></section>

<section class="party"><div class="floaters" aria-hidden="true">FLOATERS</div><div class="container">
<span class="eyebrow">Private rooms</span>
<h2>Who is coming to game night?</h2>
<p>Create a room, share the code and get everyone around the same table, wherever they are. Bring the snacks, we will bring the cards.</p>
<div class="chips"><span class="chip">Room codes</span><span class="chip">Friends list</span><span class="chip">Emotes and quick chat</span></div>
</div></section>

<section id="faq"><div class="container">
<div class="section-head rv"><span class="kicker">Good to know</span><h2>Questions, answered</h2></div>
<div class="faq rv">FAQ</div>
</div></section>

<section class="studio"><div class="container">
<img src="/assets/logo-studio.webp" alt="Noob Studios logo" width="260" height="205" loading="lazy">
<div><span class="kicker">The studio</span><h2>Made by Noob Studios</h2>
<p>We are an indie studio that loves games you can pick up in seconds and share with friends. 5 Cards is built with care for the casual card table: quick, colourful and full of good vibes.</p>
<p>Say hello at <a href="mailto:EMAIL">EMAIL</a>.</p></div>
</div></section>

<section class="cta-band"><div class="container">
<img class="app-icon" style="width:96px;height:96px;margin:0 auto 20px" src="/assets/icon.png" alt="5 Cards app icon" width="96" height="96" loading="lazy">
<h2>Ready for your first match?</h2>
<p>5 Cards is coming to Google Play. Questions in the meantime? We would love to hear from you.</p>
<div class="actions" style="justify-content:center"><a class="gp" href="/contact/" aria-label="Coming soon on Google Play">PLAYICON<div><span>Coming soon on</span><b>Google Play</b></div></a></div>
<div class="socials"><a href="/contact/">MAIL Get in touch</a><a href="/privacy/">VIBES Privacy policy</a></div>
</div></section>
""".replace("SUITS", SUIT_BITS).replace("PLAYICON", PLAY_ICON).replace("ARROW", ico("arrow")) \
   .replace("CHECK", ico("check")).replace("ANDROID", ico("android")).replace("TROPHYICON", ico("trophy")) \
   .replace("MENU", phone("menu", "5 Cards main menu with Play Now, Private Room and Practice", "l", eager=True)) \
   .replace("TABLE", phone("table", "A 5 Cards table with four players", "c", eager=True)) \
   .replace("TROPHY</div><h3>", ico("trophy") + "</div><h3>") \
   .replace("TROPHY", phone("trophy", "The Trophy Road with tiers from Rookie to Ace", "r", eager=True)) \
   .replace("AV1", img("av-male-2.webp", "", 34, 34, lazy=False)).replace("AV2", img("av-female-6.webp", "", 34, 34, lazy=False)) \
   .replace("TRACK", track).replace("BOLT", ico("bolt")).replace("ROOM</div>", ico("room") + "</div>").replace("COIN</div>", ico("coin") + "</div>") \
   .replace("CARDS</div>", ico("cards") + "</div>").replace("VIBES</div>", ico("vibes") + "</div>") \
   .replace("MINIRANKS", mini_ranks) \
   .replace("FANSKINS", "".join(img("skin-%s.webp" % s, "", 360, 540) for s in ["galaxy", "neon", "sakura", "inferno"])) \
   .replace("STEPS", step_html).replace("STAGEIMGS", stage_imgs).replace("STAGEDOTS", stage_dots).replace("ROUNDS", round_html) \
   .replace("SKINLANE", skin_lane).replace("AVA", av_a).replace("AVB", av_b) \
   .replace("BACKS", "".join(img("back-%s.webp" % b, "%s card back" % b.title(), 340, 481) for b in ["ocean", "midnight", "zellige", "sunset"])) \
   .replace("SHIELDS", shields).replace("FLOATERS", floaters).replace("FAQ", faq) \
   .replace("EMAIL", EMAIL).replace("MAIL ", ico("mail") + " ").replace("VIBES Privacy", ico("vibes") + " Privacy")
