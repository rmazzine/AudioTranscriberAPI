import base64
import random
import os

import librosa
import soundfile as sf


def convert(mediabase64):
    """
    Converts a base64 ogg stream to a WAV file in the local path.

    :param mediabase64: stream base64 encoded of the audio file
    :return: (str) Filepath of the saved WAV file
    """
    random_name = random.randint(1, 100000)

    tempfilepath = f'./temp{random_name}.ogg'
    filebytes = base64.b64decode(mediabase64)

    open(tempfilepath, 'wb').write(filebytes)

    wavdata, sr = librosa.load(tempfilepath)

    os.remove(tempfilepath)

    output_name = f'./temp{random_name}.wav'

    sf.write(output_name, wavdata, sr)

    return output_name

