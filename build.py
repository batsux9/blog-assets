"""Build the Tumblr theme, rejecting template block tags inside CSS/JS."""
from pathlib import Path
import json
import re

R = Path(__file__).resolve().parent
template = (R / "src/template.html").read_text(encoding="utf-8")
css = (R / "src/theme.css").read_text(encoding="utf-8")
js = (R / "src/theme.js").read_text(encoding="utf-8")

# Tumblr expands its template blocks even when they appear in comments.
# Block tags belong in the HTML template, not in inlined styles or scripts.
for label, content in (("CSS", css), ("JavaScript", js)):
    if re.search(r"\{/?block:[^}]+\}", content, flags=re.IGNORECASE):
        raise ValueError(f"Unexpected Tumblr block tag in {label}; check CSS/JS comments")

result = template.replace("__INLINE_CSS__", css).replace("__INLINE_JS__", js)
assets = json.loads((R / "asset-map.json").read_text(encoding="utf-8"))
for key, url in assets.items():
    result = result.replace("__ASSET_" + key.upper() + "__", url)
if "__ASSET_" in result:
    raise ValueError("Unresolved asset reference")
path = R / "dist/theme.html"
path.parent.mkdir(exist_ok=True)
path.write_text(result, encoding="utf-8")
print("Built", path)
