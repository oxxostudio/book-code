# Copyright © https://steam.oxxostudio.tw

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    name = request.args.get('name')
    return render_template('test.html', name=name)

app.run()

