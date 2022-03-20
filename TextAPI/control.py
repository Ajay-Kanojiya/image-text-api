from ocr_core.ocr_tesseract import OCR


def get_image_c(uploaded_img, psm, oem):
    try:
        img = OCR()
        text, psm, oem = img.image_to_text(uploaded_img, psm, oem)
        dimension = img.get_dimension(uploaded_img)
        image_type = uploaded_img.content_type.split("/")[1]
        image_name = uploaded_img.filename
        ocr_resp = dict(text=text.replace("\n", " "), image_name=image_name, image_type=image_type, dimesnion=dimension,
                        psm=psm, oem=oem)
        return ocr_resp, 201
    except Exception:
        return {"response": "Something went wrong!"}
