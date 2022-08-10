from PIL import Image
import sys
import pyocr
import pyocr.builders
import pdf2image

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)

tool = tools[0]


images = pdf2image.convert_from_path("2109.10282.pdf", dpi=200, fmt='jpg')
lang = 'eng'
f = open('output.txt','a',encoding='utf-8')
for image in images:
    txt = tool.image_to_string(
        image,
        lang=lang,
        builder=pyocr.builders.TextBuilder()
    )
    f.write(txt)