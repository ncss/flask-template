import re
import requests
from cohere_module import ChatBot

import markdown
from markdown.extensions.codehilite import CodeHiliteExtension

from json import loads, load

from flask import Flask
from flask_cors import CORS

JSON_PATH = "./static/jamesywamesy.json"

def load_json():
    return load(open(JSON_PATH, "r"))

def ascii_james_curran():
    return "\n".join(load_json()["ascii"])

class WebServer(Flask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        CORS(self)

    def run(self):
        print(ascii_james_curran())
        super().run(host='0.0.0.0', debug=False)

# class my_markdown(markdown.Markdown):
#     def __init__(self, extensions, extension_configs=None):
#         extension_configs = extension_configs or {}
#         extension_configs['codehilite'] = {
#             'use_pygments': True,
#             'css_class': 'highlight',
#         }
#         super().__init__(extensions, extension_configs)

class Agent:
    def __init__(self, name: str, room: str):
        self.room = room
        self.name = name
        self.timer = 0

        self.chatbot = ChatBot(model="command", temperature=0.3)

    def print_name(self):
        print(self.room)

    def send_message(self, message: str):
        data = {
            "room": self.room,
            "author": self.name,
            "text": message
        }
        r = requests.post("https://chat.ncss.cloud/api/actions/message", json=data)

    def call(self, message: str):
        
        base_msg = self.chatbot.chat_invoke(message).json()
        base_msg = loads(base_msg)

        response = base_msg["content"]

        # Formatting from Markdown to HTML
        # response = re.sub(r"\*\*(.+?)\*\*", r'<strong>\1</strong>', response)
        # response = re.sub(r"\*(.+?)\*", r'<em>\1</em>', response)
        # response = re.sub(r"\n", '<br>', response)
        # response = re.sub('python', '', response)

        response = markdown.markdown(response, extensions=["fenced_code", CodeHiliteExtension()])
        # response = re.sub(r'<p>(<|</)code>', r'<p>\1pre>', response)
        # response = re.sub(r'(<|</)code></p>', r'\1pre></p>', response)

        return response