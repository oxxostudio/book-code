# Copyright © https://steam.oxxostudio.tw

from flask import Flask

app = Flask(__name__)

@app.route("/<name>")
def home(name):
    return f"<h1>hello {name}</h1>"

app.run()

