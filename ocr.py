from PIL import Image
import pytesseract
import numpy as np
import re
tesseract_cmd = 'C:/Users/Lavanya V-2571/PycharmProjects/OCR/tessdata'
filename = 'C:/Users/Lavanya V-2571/PycharmProjects/OCR/tl.jpg'
img1 = np.array(Image.open(filename))
txt = pytesseract.image_to_string(img1)
def extract_id_from_text(txt, name):
   pattern = fr'{name}\s*-\s*(\d+)'
   match = re.search(pattern, txt)
   if match:
       return match.group(0)
   else:
       return None

name = "PS!"
marketing_manager_id = extract_id_from_text(txt, name)
print(marketing_manager_id)
