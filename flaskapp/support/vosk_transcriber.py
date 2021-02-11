import os

from vosk import Model, KaldiRecognizer
import wave

model = Model("model")


def transcribe_wav(filepath):

    wf = wave.open(filepath, 'rb')

    rec = KaldiRecognizer(model, wf.getframerate())

    transcription = ''
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            transcription += str(eval(rec.Result())['text'])+' '

    transcription += str(eval(rec.FinalResult())['text'])

    os.remove(filepath)

    return transcription
