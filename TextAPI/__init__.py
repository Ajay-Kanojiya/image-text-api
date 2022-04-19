from flask import Flask, request
from ocr_core.ocr_tesseract import OCR
from flask_restx import Api

app = Flask(__name__)
api = Api(app, version='1.0', title='OCR Image to Text API',
          description="Pytesseract is a wrapper for Tesseract-OCR Engine. It is also useful as a stand-alone "
                      "invocation script to tesseract, as it can read all image types supported by the Pillow and "
                      "Leptonica imaging libraries,\n "
                      " including jpeg, png, gif, bmp, tiff, and others. More info about Python approach read here.\n\n"
                      "\tPage segmentation modes(psm):\n\n"
                      "\t0: Orientation and script detection (OSD) only.\t"
                      "\t1: Automatic page segmentation with OSD.\t"
                      "\t\t\t2: Automatic page segmentation, but no OSD, or OCR.\n"
                      "\t3: Fully automatic page segmentation, but no OSD.\t"
                      "4: Assume a single column of text of variable sizes.\t"
                      "5: Assume a single uniform block of vertically"
                      "aligned text.\n "
                      "\t6: Assume a single uniform block of text.\t"
                      "\t\t7: Treat the image as a single text line.\t"
                      "\t\t\t8: Treat the image as a single word.\n"
                      "\t9: Treat the image as a single word in a circle.\t"
                      "10: Treat the image as a single character.\t"
                      "\n\t11: Sparse text. Find as much text as possible in no "
                      "particular order."
                      "\t\t\t\t\t\t\t\t\t\t12: Sparse text with OSD."
                      "\n\t13: Raw line, Treat the image as a single text line, "
                      "bypassing hacks that are Tesseract-specific.\n\n"


                      "\tOCR Engine modes(oem):\n\n"
                      "\t0: Legacy engine only.\t"
                      "\t1: Neural nets LSTM engine only.\t"
                      "\t2: Legacy + LSTM engines.\t"
                      "\t3: Default, based on what is available.\t")

from TextAPI import view
