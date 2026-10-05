"""Build the two PDF editions from the preserved ebook manuscript."""
from pathlib import Path
import html
import json
from hashlib import sha256
import re
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.platypus import Paragraph
from pypdf import PdfReader
from content import adult, teen, SOURCES

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'nkadankwablog/static/ebooks/v1.1'
OUT.mkdir(parents=True, exist_ok=True)
W, H, M = 612, 864, 48
INK, PAPER, MUTED = '#203C3B', '#FAF8F2', '#4D625D'
for name, file in [('Body','arial.ttf'), ('Bold','arialbd.ttf'), ('Display','georgia.ttf')]:
    pdfmetrics.registerFont(TTFont(name, str(Path('C:/Windows/Fonts') / file)))
TEEN_SOURCES = {'t1':['G4','G6'],'t2':['G4'],'t3':['N2'],'t4':['G4'],'t5':['G5','G6'],'t6':['G5'],'t7':['G1'],'t8':['G3'],'t9':['G4'],'t10':[],'t11':[],'t12':['G4']}

def clean(text):
    return text.replace('\u2011','-').replace('\u2013','-').replace('\u2014','-')

def paragraph(text, width, size=11.3, font='Body', color=INK, leading=None):
    markup = html.escape(clean(text))
    markup = re.sub(r'\[([NG]\d+)\]', lambda m: f'<link href="{SOURCES[m[1]][2]}" color="#176B60">[{m[1]}]</link>', markup)
    p = Paragraph(markup, ParagraphStyle('text',fontName=font,fontSize=size,leading=leading or size*1.38,textColor=HexColor(color)))
    _, height = p.wrap(width, 2000)
    return p, height

def draw(c, text, x, top, width, **kwargs):
    p, height = paragraph(text, width, **kwargs)
    p.drawOn(c, x, top-height)
    return top-height

def line(c,x,y,x2,color):
    c.setStrokeColor(HexColor(color));c.setLineWidth(.6);c.line(x,y,x2,y)

def sources_for(book,p):
    if not re.fullmatch('[at][0-9]+',p['key']): return []
    return TEEN_SOURCES[p['key']] if book is teen else list(dict.fromkeys(re.findall(r'\[([NG]\d+)\]',' '.join(t for _,t in p['blocks']))))

def build(book):
    young = book is teen
    accent = '#A4472D' if young else '#176B60'
    title = 'Using AI\nsafely' if young else 'Rules for\nusing AI'
    cover_title = title.replace('\n',' ')
    pages = [{'key':'cover','title':cover_title}, {'key':'toc0','title':'Contents'}]
    if not young: pages.append({'key':'toc1','title':'Contents'})
    pages += book['pages']
    nums = {p['key']:i+1 for i,p in enumerate(pages)}
    path = OUT / f'ai-dos-and-donts-{"teen" if young else "adult"}-v1.1.pdf'
    c = canvas.Canvas(str(path), pagesize=(W,H))
    c.setTitle(cover_title+' - '+book['edition'].title())
    c.setAuthor('Created by @Nkadankwa on github')
    qa=[]
    for index,p in enumerate(pages):
        c.setFillColor(HexColor(PAPER));c.rect(0,0,W,H,fill=1,stroke=0)
        c.bookmarkPage(p['key']);c.addOutlineEntry(clean(p['title']),p['key'])
        if p['key']=='cover':
            c.setFillColor(HexColor('#F2DFCE' if young else '#DCE6DE'))
            c.rect(W-152,0,152,H,fill=1,stroke=0)
            y=H-118
            for row in title.split('\n'):
                y=draw(c,row,M,y,W-2*M,size=62,font='Display',leading=70)-4
            y=draw(c,book['subtitle'],M,y-26,360,size=19,leading=26)
            line(c,M,y-34,W-M,accent)
            draw(c,book['tagline'],M,y-62,330,size=15,leading=22)
            c.setFillColor(HexColor(accent));c.setFont('Display',112)
            c.drawString(M,186,'12' if young else '14')
            draw(c,'rules for everyday use',M,164,350,size=15)
            draw(c,book['edition'].title(),M,92,300,size=11,font='Bold',color=accent)
            draw(c,'October 2026  /  Layout edition 1.1',M,69,400,size=10,color=MUTED)
            c.showPage();continue

        # Quiet running furniture leaves the main title in charge.
        draw(c,cover_title,M,H-25,340,size=9,color=MUTED)
        c.setFont('Body',9);c.setFillColor(HexColor(MUTED));c.drawRightString(W-M,H-35,book['edition'].title())
        line(c,M,H-49,W-M,'#BBCAC1')
        c.setFont('Bold',9);c.setFillColor(HexColor(accent));c.drawString(M,28,'Contents')
        c.linkRect('', 'toc0',(M,22,M+65,40),thickness=0)
        c.setFont('Body',9);c.setFillColor(HexColor(MUTED));c.drawRightString(W-M,28,f'{index+1:02d}')

        if p['key'].startswith('toc'):
            y=draw(c,'Find your rule',M,H-85,W-2*M,size=34,font='Display')-14
            y=draw(c,'Select any title to go straight to the page.',M,y,W-2*M,size=11,color=MUTED)-26
            entries=book['pages']
            if not young:
                split=next(i for i,e in enumerate(entries) if e.get('category')=='Work')
                entries=entries[:split] if p['key']=='toc0' else entries[split:]
            category=None
            for entry in entries:
                cat=entry.get('category')
                if cat and cat!=category:
                    y-=10;y=draw(c,cat,M,y,400,size=10,font='Bold',color=accent)-13;category=cat
                label=re.sub(r'^Rule (\d+) ',r'\1. ',entry['title'])
                bottom=draw(c,label,M,y,W-2*M-35,size=11.5,leading=16)
                c.setFont('Body',10);c.setFillColor(HexColor(accent));c.drawRightString(W-M,y-12,str(nums[entry['key']]))
                if entry.get('subcategory'):
                    bottom=draw(c,entry['subcategory'],M,bottom-5,W-2*M-35,size=9,color=MUTED)
                c.linkRect('',entry['key'],(M,bottom-5,W-M,y+3),thickness=0)
                y=bottom-9;line(c,M,y+3,W-M,'#D7DED7');y-=5
            assert y>60,(p['key'],y)
            c.showPage();continue

        rule=re.match(r'Rule (\d+) (.*)',p['title'])
        if rule:
            c.setFont('Display',54);c.setFillColor(HexColor(accent));c.drawString(M,H-119,rule[1].zfill(2))
            y=draw(c,rule[2],M+88,H-77,W-2*M-88,size=27,font='Display',leading=32)-12
            y=min(y,H-143)
            if p.get('category'):
                y=draw(c,p['category']+' / '+p['subcategory'],M+88,y,W-2*M-88,size=9.5,color=accent)-17
            else:y-=10
        else:
            y=draw(c,p['title'],M,H-83,W-2*M,size=32,font='Display',leading=38)-26

        # A continuous reading column, with margin labels instead of panels.
        text_x=M+88
        text_w=W-M-text_x
        for label,txt in p['blocks']:
            txt=txt.replace('Click a reference to read its source entry and article link.','Sources and further reading appear beneath each rule. Click a reference or article title to open the original.').replace('Linked sources are at the end.','Sources and further reading are listed with each rule.')
            if not label:
                y=draw(c,txt,text_x,y,text_w,size=13 if young else 12.5,leading=18 if young else 17.5)-22
                continue
            label="Don't" if label=='Dont' else label
            if label == "Don't":
                line(c,M,y+5,W-M,accent)
                y-=7
            lp,lh=paragraph(label,72,size=10,font='Bold',color=accent,leading=13)
            closing=label in ('Conclusion','Remember')
            bp,bh=paragraph(txt,text_w,size=14 if closing else (13 if young else 12),font='Display' if closing else 'Body',leading=19 if closing else (18.2 if young else 16.5))
            lp.drawOn(c,M,y-lh);bp.drawOn(c,text_x,y-bh)
            y-=max(lh,bh)+15

        if rule:
            refs=sources_for(book,p)
            line(c,text_x,y-1,W-M,'#BBCAC1');y-=12
            y=draw(c,'Sources and further reading',text_x,y,text_w,size=8.5,font='Bold',color=accent)-6
            if not refs:
                y=draw(c,'This rule offers original practical guidance; no specific news incident is cited.',text_x,y,text_w,size=8.5,leading=11,color=MUTED)-5
            for sid in refs:
                meta,st,url=SOURCES[sid]
                markup=html.escape(clean(f'[{sid}] {meta} '))+f'<link href="{html.escape(url,quote=True)}" color="{accent}">{html.escape(clean(st))}</link>'
                sp=Paragraph(markup,ParagraphStyle('source',fontName='Body',fontSize=8.5,leading=11,textColor=HexColor(MUTED)))
                _,sh=sp.wrap(text_w,1000);sp.drawOn(c,text_x,y-sh);y-=sh+5
        assert y>54,(book['slug'],p['key'],y)
        qa.append({'page':index+1,'key':p['key'],'bottom':round(y,1)})
        c.showPage()
    c.save()
    reader=PdfReader(path)
    assert len(reader.pages)==len(pages)
    ids={pg.indirect_reference.idnum for pg in reader.pages}
    for pg in reader.pages:
        for item in pg.get('/Annots',[]):
            a=item.get_object()
            if '/Dest' in a: assert a['/Dest'][0].idnum in ids
    print(path.name,len(reader.pages),'pages; lowest content:',min(q['bottom'] for q in qa))
    return qa

if __name__=='__main__':
    qa={key:build(book) for key,book in [('adult',adult),('teen',teen)]}
    (OUT/'SHA256SUMS.txt').write_text(''.join(
        f'{sha256(pdf.read_bytes()).hexdigest()}  {pdf.name}\n'
        for pdf in sorted(OUT.glob('*.pdf'))
    ),encoding='utf-8')
    (ROOT/'tmp/pdfs').mkdir(parents=True,exist_ok=True)
    (ROOT/'tmp/pdfs/layout-check.json').write_text(json.dumps(qa,indent=2))
