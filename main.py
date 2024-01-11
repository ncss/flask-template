import pprint

from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.post('/bogan')
def bogan():
    message = request.json
    print(f"\nIncoming message to {request.path}:")
    pprint.pprint(message, indent=2)

    message_text = message['text']
    return {
        'author': 'BoganBot',
        'text': f"Hello! Your message was: {message_text}"
    }


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
