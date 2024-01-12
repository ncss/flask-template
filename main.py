import re, requests
from pprint import pprint
from random import randint

import cohere_module

from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

index_page = " ".join([(lambda font: f'<h{font}>{"James Curran"}</h{font}>')(str(randint(1, 4))) for x in range(100)])
@app.route("/")
def index():
    return index_page

@app.post('/chat')
def chat():
    message = request.json
    print(f"\nIncoming message to {request.path}:")
    pprint(message, indent=2)

    message_text = message['text']
    message_room = message['room']

    if re.search("clearchat", message_text, re.IGNORECASE):
        pass

    return {
        'author': 'James Curran [BOT]',
        'text': f"Hello! Your message was: {message_text}"
    }

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
