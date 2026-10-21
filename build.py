from pathlib import Path
import json
R=Path(__file__).resolve().parent
s=(R/"src/template.html").read_text(encoding="utf-8")
s=s.replace("__INLINE_CSS__",(R/"src/theme.css").read_text(encoding="utf-8")).replace("__INLINE_JS__",(R/"src/theme.js").read_text(encoding="utf-8"))
for key,url in json.loads((R/"asset-map.json").read_text(encoding="utf-8")).items():
    s=s.replace("__ASSET_"+key.upper()+"__",url)
if "__ASSET_" in s: raise ValueError("Unresolved asset reference")
p=R/"dist/theme.html"; p.parent.mkdir(exist_ok=True); p.write_text(s,encoding="utf-8"); print("Built",p)
