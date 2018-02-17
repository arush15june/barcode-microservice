"""

Barcode Reader API
    - github.com/arush15june
"""

import sys
from io import BytesIO

from reader import BarcodeReader
from flask import Flask, request
from flask_restful import Resource, Api, reqparse, abort
from werkzeug.datastructures import FileStorage

"""
    Flask Config
"""

ALLOWED_EXTENSIONS = ['jpg', 'jpeg', 'png']

app = Flask(__name__)
app.config.from_object(__name__)

api = Api(app)


"""
    Helper Methods
"""

class FileStorageArgument(reqparse.Argument):
    """This argument class for flask-restful will be used in
    all cases where file uploads need to be handled."""
    
    def convert(self, value, op):
        if self.type is FileStorage:  # only in the case of files
            # this is done as self.type(value) makes the name attribute of the
            # FileStorage object same as argument name and value is a FileStorage
            # object itself anyways
            return value

        # called so that this argument class will also be useful in
        # cases when argument type is not a file.
        super(FileStorageArgument, self).convert(*args, **kwargs)


class Reader(Resource):
    put_parser = reqparse.RequestParser(argument_class=FileStorageArgument)
    put_parser.add_argument('image', required=True, type=FileStorage, location='files')

    reader = BarcodeReader()

    @staticmethod
    def verify_extension(image):
        extension = image.filename.rsplit('.', 1)[1].lower()
        if '.' in image.filename and not extension in app.config['ALLOWED_EXTENSIONS']:
            return False
        else:
            return True


    def get(self):
        args = self.put_parser.parse_args()
        image = args['image']

        if not self.verify_extension(image):
            abort(400, message='Unsupported File Extension')

        image_file = BytesIO()
        try:
            image.save(image_file)
        except:
            abort(400, message="Invalid Input")

        barcode_result = self.reader.scanImage(image_file.getvalue())

        response = { 'results' : [] }

        for result in barcode_result:
            response['results'].append({
                                'type' : result.type,
                                'data' : result.data.decode()
                            })
            
        return response

        



api.add_resource(Reader, "/scan")

if __name__ == '__main__':
    app.run(debug=True)