from flask_restful import Resource, request

from flaskapp.support.ogg_to_wav import convert
from flaskapp.support.vosk_transcriber import transcribe_wav


class Transcribe(Resource):

    def post(self):
        try:
            args = request.get_json()

            # Get media encoded as base64
            mediabase64 = args['data']

            filepath_wav = convert(mediabase64)

            return {'code': 200, 'data': transcribe_wav(filepath_wav)}

        except Exception as e:
            print(e)

            return {'code': 500, 'data': ''}
