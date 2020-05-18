import pytesseract
import json
from PIL import Image

with open('settings.json') as config_file:
    data = json.load(config_file)
    pytesseract.pytesseract.tesseract_cmd = data["tesseract_cmd"]
    
def ocr(imagepath):
    try:
        img = Image.open(imagepath)
        text = pytesseract.image_to_string(img, config='-l eng+equ -c textord_equation_detect=1 txt hocr')
        print(text)
        return text
    except:
        print("ERROR")