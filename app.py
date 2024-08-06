#!env/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask_cors import CORS
from livereload import Server


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
CORS(app)

@app.after_request
def add_header(response):
    response.cache_control.no_store = True
    return response

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    server = Server(app)
    server.watch("static/*")
    server.watch("templates/*")
    server.serve(port=5000)
