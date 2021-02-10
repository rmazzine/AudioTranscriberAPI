# Audio Transcriber API

This is a simple flask API that accepts a ogg base64 data (although it may be compatible to other types of audio formats), converts to WAV (using librosa and soundfile) and then transcribe using vosk, returning the text transcribed.

The current code is with the Portuguese-BR model, however, it can be easily changed to other vosk model (https://alphacephei.com/vosk/models).

## How to run (development env)

Install packages
```commandline
pip install -r requirements
```

Go to flask API folder
```commandline
cd ./flaskapp
```

Start flask server (http://localhost:5000)
```commandline
flask run
```

## How to run (production env)

Instead running a flask server, use gunicorn WSGI HTTP server
```commandline
gunicorn -w 1 --bind 0.0.0.0:3800 wsgi
```

## Create docker image
To create a docker image, build it with:

```commandline
docker build -t audiotranscriberapi .
```

Then run it port-forwarding the required port
```commandline
docker run -p 3800:3800 audiotranscriberapi
```

## How to use

It's recommended to use an API tool like [Postman](https://www.postman.com/downloads/).

On Headers:
Include the key `Content-Type` with value `application/json` as we will send the base64 audio data using a JSON format.

In Body:
Create a JSON where the `data` key has the base64 audio data, for example:
```json
{
  "data": "BASE64DATA"
}
```

Finally on URL field, select the POST method and send the JSON to the following address: `http://localhost:5000/transcribe`.

If successful, it will return a JSON with code 200 and the transcribed text in `data`.