# 5cards-site

Static website for 5 Cards (home, privacy policy, terms, account deletion, contact), served by Cloudflare Pages.
These URLs are what Google Play (privacy policy, account deletion) and Meta (privacy policy, data deletion) ask for.

- `legal/*.txt` are copies of the texts the game ships (`resources/legal/` in U10-Mobile). Keep them in step.
- `python build.py` regenerates the HTML; commit the result. No build step on Cloudflare (output directory `/`).
- `build.py` also writes `_headers` (Cloudflare Pages reads it): CSP with the SHA-256 of every inline script the pages have, HSTS, no framing. Edit a page's script in `build.py`/`home.py` and rebuild, or the browser blocks it.
- Everything in this folder is published (output directory `/`): never commit a private file here.
