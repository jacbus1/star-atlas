# Regenerate the self-contained page after editing catalog.json.
import json,re
from pathlib import Path
p=Path(__file__).parent
data=json.loads((p/'catalog.json').read_text())
text=(p/'index.html').read_text()
encoded=json.dumps(data,ensure_ascii=False).replace('<', '\\u003c')
text=re.sub(r'(<script id="catalog-data" type="application/json">)[\s\S]*?(</script>)',lambda m:m[1]+encoded+m[2],text)
(p/'index.html').write_text(text)
