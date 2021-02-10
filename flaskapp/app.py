import sys
sys.path.append('../')  # Must have a best solution

from flask import Flask
from flask_restful import Api

from flaskapp.routes.transcribe import Transcribe

app = Flask(__name__)

api = Api(app)

api.add_resource(Transcribe, '/transcribe')
