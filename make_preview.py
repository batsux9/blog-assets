"""Refresh CSS/JS inside the checked-in static preview snapshot.

The preview HTML is a visual fixture, not a Tumblr render. Markup changes
must be checked against the actual Tumblr theme or updated in the snapshot.
"""
from pathlib import Path
import re

R = Path(__file__).resolve().parent
snapshot = R / "dist/local-preview.html"
html = snapshot.read_text(encoding="utf-8")
css = (R / "src/theme.css").read_text(encoding="utf-8")
css = css.replace('url("{image:Wallpaper}")', 'url("../assets/images/neighborhood-night.webp")')
js = (R / "src/theme.js").read_text(encoding="utf-8")
html, css_matches = re.subn(r"<style>[\s\S]*?</style>", lambda _: "<style>\n" + css + "\n</style>", html, count=1)
html, js_matches = re.subn(r"<script>[\s\S]*?</script>", lambda _: "<script>\n" + js + "\n</script>", html, count=1)
if css_matches != 1 or js_matches != 1:
    raise RuntimeError("Expected exactly one inline style and script in preview")
snapshot.write_text(html, encoding="utf-8")
print("Updated static visual preview styles/scripts:", snapshot)
