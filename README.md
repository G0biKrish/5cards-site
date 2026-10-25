# 5cards-site

Static website for 5 Cards (home, privacy policy, terms, account deletion, contact), served by Cloudflare Pages.
These URLs are what Google Play (privacy policy, account deletion) and Meta (privacy policy, data deletion) ask for.

- `legal/*.txt` are copies of the texts the game ships (`resources/legal/` in U10-Mobile). Keep them in step.
- `python build.py` regenerates the HTML; commit the result. No build step on Cloudflare (output directory `/`).
