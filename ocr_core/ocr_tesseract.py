import pytesseract
import platform
from PIL import Image


class OCR:

    def __init__(self, engine_path=r"C:\Program Files\Tesseract-OCR\tesseract.exe"):
        if platform.system() == "Windows":
            pytesseract.pytesseract.tesseract_cmd = engine_path

    @staticmethod
    def image_to_text(image_path, psm=6, oem=3):
        try:
            custom_config = r"-l eng --psm {} --oem {} ".format(psm, oem)
            img = Image.open(image_path)
            return pytesseract.image_to_string(img, config=custom_config), psm, oem
        except Exception:
            pass

    @staticmethod
    def get_dimension(image):
        return Image.open(image).size
