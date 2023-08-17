# Copyright © https://steam.oxxostudio.tw

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>hello world</h1>"

app.run(host="0.0.0.0", port=5555)

