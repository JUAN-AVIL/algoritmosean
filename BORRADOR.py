from PIL import image

from pytesseract import *

pytesseract.tesseract_cmd = r'C:\Users\SALA\AppData\Local\Programs\Tesseract-OCR'

img = image.open ("image.png")

resultado = pytesseract.image_to_string (img,lang="spa")

print (resultado)