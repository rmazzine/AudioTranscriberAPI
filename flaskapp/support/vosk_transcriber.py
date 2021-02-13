import os
import audioop

from vosk import Model, KaldiRecognizer
import wave

model = Model("model")


def transcribe_wav(filepath):

    wf = wave.open(filepath, 'rb')

    n_channels = wf.getnchannels()

    # If not mono, convert it to mono
    if n_channels != 1:
        mono_filename = f'{filepath}.monofile.wav'
        mono = wave.open(mono_filename, 'wb')
        mono.setparams(wf.getparams())
        mono.setnchannels(1)
        mono.writeframes(audioop.tomono(wf.readframes(float('inf')), wf.getsampwidth(), 1, 1))
        mono.close()

        wf = wave.open(mono_filename, 'rb')

        os.remove(mono_filename)

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
