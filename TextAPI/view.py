from TextAPI import api
from TextAPI.control import get_image_c
from flask_restx import Resource, reqparse, fields
from werkzeug.datastructures import FileStorage


parser = reqparse.RequestParser()
upload_parser = api.parser()
parser.add_argument('image_file', type=FileStorage, location='files', required=True)
parser.add_argument("psm", type=int, help="Page segmentation modes", location='args', default=6)
parser.add_argument("oem", type=int, help="OCR Engine modes", location='args', default=3)
ns = api.namespace("uploadImage", description="Image to text coversion")


@ns.route("")
@api.expect(upload_parser)
class ImageToText(Resource):
    @api.doc(parser=parser)
    def post(self):
        try:
            args = parser.parse_args()
            uploaded_img = args["image_file"]
            psm = int(args.get("psm"))
            oem = int(args.get("oem"))
            return get_image_c(uploaded_img, psm, oem)
        except Exception:
            pass          
