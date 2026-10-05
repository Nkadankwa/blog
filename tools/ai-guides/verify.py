from pathlib import Path
import re
import subprocess
from PIL import Image, ImageOps, ImageDraw
from pypdf import PdfReader
from content import adult, teen

ROOT=Path(__file__).resolve().parents[2]
POPPLER=Path('C:/Users/kwadw/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/Library/bin/pdftoppm.exe')
def norm(text):
    return re.sub(r'[^a-z0-9]','',text.lower())
for kind,book in [('adult',adult),('teen',teen)]:
    pdf=ROOT/f'nkadankwablog/static/ebooks/v1.1/ai-dos-and-donts-{kind}-v1.1.pdf'
    reader=PdfReader(pdf)
    offset=3 if kind=='adult' else 2
    for idx,chapter in enumerate(book['pages']):
        actual=norm(reader.pages[idx+offset].extract_text())
        for label,text in chapter['blocks']:
            if 'Click a reference' in text or 'Linked sources are at the end.' in text: continue
            assert norm(text) in actual,(kind,chapter['key'],label)
    target=ROOT/f'tmp/pdfs/{kind}'
    target.mkdir(parents=True,exist_ok=True)
    subprocess.run([str(POPPLER),'-r','72','-png',str(pdf),str(target/'page')],check=True,capture_output=True)
    files=sorted(target.glob('page-*.png'))
    for start in range(0,len(files),6):
        sheet=Image.new('RGB',(918,900),'#ccc')
        for j,file in enumerate(files[start:start+6]):
            im=Image.open(file).convert('RGB');im.thumbnail((300,424))
            x=(j%3)*306;y=(j//3)*450
            sheet.paste(im,(x,y));ImageDraw.Draw(sheet).text((x+8,y+428),file.stem,fill='black')
        sheet.save(target/f'sheet-{start//6+1}.png')
    print(kind,'all manuscript blocks preserved;',len(files),'pages rendered')
