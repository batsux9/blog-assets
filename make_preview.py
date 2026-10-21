"""Create a local visual-only preview from Tumblr source files."""
from pathlib import Path
import re

R=Path(__file__).resolve().parent
s=(R/"src/template.html").read_text(encoding="utf-8")
s=s.replace("__INLINE_CSS__",(R/"src/theme.css").read_text(encoding="utf-8"))
s=s.replace("__INLINE_JS__",(R/"src/theme.js").read_text(encoding="utf-8"))
assets={}  # Current wallpaper and blog avatar use Tumblr theme variables
assets.update({x.upper():"../assets/icons/"+x+".svg" for x in ("plumbob","home","ask","downloads","resources","archive")})
for name,path in assets.items(): s=s.replace("__ASSET_"+name+"__",path)
s=s.replace("{image:Wallpaper}","../assets/images/neighborhood-night.webp").replace("{image:Featured Screenshot}","../assets/images/neighborhood-night.webp").replace("{PortraitURL-128}","../assets/legacy/avatar.jpg")
s=s.replace("{Title}","little world of batsu").replace("{MetaDescription}","Visual preview").replace("{Favicon}","../assets/icons/plumbob.svg")
s=re.sub(r"\\{/?block:[^{}]+\\}","",s,flags=re.I)
s=re.sub(r"\\{[A-Za-z][A-Za-z0-9: ]*\\}","",s)
(R/"dist/local-preview.html").write_text(s,encoding="utf-8")
print("Visual-only preview written; Tumblr blocks are not evaluated.")
