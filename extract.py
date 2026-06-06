import zipfile
import xml.etree.ElementTree as ET
import os

pptx_path = r'c:\Users\DELL\OneDrive\Desktop\PORTFOLIO\Premium Portfolio Vision Young Founder’s World-Class Profile.pptx'

def extract_text_from_pptx(path):
    text_runs = []
    try:
        with zipfile.ZipFile(path, 'r') as z:
            slide_list = [f for f in z.namelist() if f.startswith('ppt/slides/slide') and f.endswith('.xml')]
            slide_list.sort(key=lambda x: int(x.replace('ppt/slides/slide', '').replace('.xml', '')))
            for slide in slide_list:
                xml_content = z.read(slide)
                tree = ET.fromstring(xml_content)
                slide_text = []
                for node in tree.iter('{http://schemas.openxmlformats.org/drawingml/2006/main}t'):
                    if node.text:
                        slide_text.append(node.text)
                if slide_text:
                    text_runs.append(f'--- {slide} ---\n' + ' '.join(slide_text))
        return '\n\n'.join(text_runs)
    except Exception as e:
        return str(e)

print(extract_text_from_pptx(pptx_path))
