
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract'


def picture_read(alpha):
    for x in alpha:
        print(pytesseract.image_to_string(Image.open(x)))

picture_read(['test.png','legitymacja.jpg'])


