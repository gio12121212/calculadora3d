"""Regenera los hashes CSP después de editar el script o los estilos."""
from pathlib import Path
import re, hashlib, base64
p=Path(__file__).resolve().parents[1]/'dist/index.html'
s=p.read_text(encoding='utf-8')
def digest(tag):
    content=re.search(r'<'+tag+r'>(.*?)</'+tag+r'>',s,re.S).group(1)
    return base64.b64encode(hashlib.sha256(content.encode()).digest()).decode()
for directive,tag in [('script-src','script'),('style-src','style')]:
    s=re.sub(directive+r" 'sha256-[^']+'",directive+" 'sha256-"+digest(tag)+"'",s)
p.write_text(s,encoding='utf-8',newline='\n')
