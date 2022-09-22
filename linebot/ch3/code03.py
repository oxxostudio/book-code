# Copyright © https://steam.oxxostudio.tw

from flask import Flask
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)

@app.route("/<name>")
def home(name):
    return f"<h1>hello {name}</h1>"

app.run()
