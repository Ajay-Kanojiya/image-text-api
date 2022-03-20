from flask import Flask, request
from ocr_core.ocr_tesseract import OCR
from flask_restx import Api

app = Flask(__name__)
api = Api(app, version='1.0', title='OCR Image to Text API',
          description="Pytesseract is a wrapper for Tesseract-OCR Engine. It is also useful as a stand-alone "
                      "invocation script to tesseract, as it can read all image types supported by the Pillow and Leptonica imaging libraries,\n"
                      " including jpeg, png, gif, bmp, tiff, and others. More info about Python approach read here.\n\n"
                      "       Page segmentation modes(psm)     \n"
                      "0: Orientation and script detection (OSD) only.\n"
                      "1: Automatic page segmentation with OSD.\n"
                      "2: Automatic page segmentation, but no OSD, or OCR.\n"
                      "3: Fully automatic page segmentation, but no OSD.\n"
                      "4: Assume a single column of text of variable sizes.\n"
                      "5: Assume a single uniform block of vertically"
                      "aligned text.\n "
                      "6: Assume a single uniform block of text.\n"
                      "7: Treat the image as a single text line.\n"
                      "8: Treat the image as a single word.\n"
                      "9: Treat the image as a single word in a circle.\n"
                      "10: Treat the image as a single character.\n"
                      "11: Sparse text. Find as much text as possible in no "
                      "particular order.\n "
                      "12: Sparse text with OSD.\n"
                      "13: Raw line, Treat the image as a single text line, "
                      "bypassing hacks that are Tesseract-specific.\n\n"
                      "        OCR Engine modes(oem)      \n"
                      "0: Legacy engine only.\n"
                      "1: Neural nets LSTM engine only.\n"
                      "2: Legacy + LSTM engines.\n"
                      "3: Default, based on what is available.\n")

from TextAPI import view
