import random
import base64

from flask_restful import Resource, request

from flaskapp.support.vosk_transcriber import transcribe_wav


class TranscribeWav(Resource):

    def post(self):
        try:
            args = request.get_json()

            random_name = random.randint(1, 100000)
            tempfilepath = f'./temp{random_name}.wav'

            # Get media encoded as base64
            mediawavbase64 = base64.b64decode(args['data'])

            open(tempfilepath, 'wb').write(mediawavbase64)

            return {'code': 200, 'data': transcribe_wav(tempfilepath)}

        except Exception as e:
            print(e)

            return {'code': 500, 'data': 'error'}
