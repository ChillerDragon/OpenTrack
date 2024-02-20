#!/usr/bin/env python3

from flask import Flask
from flask import render_template
from flask import request

import src.log_config

app = Flask(__name__)

def req_ipaddr() -> str:
    if not 'HTTP_X_FORWARDED_FOR' in request.environ:
        return request.remote_addr
    return request.environ['HTTP_X_FORWARDED_FOR'].split(',')[-1].strip()

def log_request() -> str:
    app.logger.info(f"{request.method} {request.url} ip={req_ipaddr()} ua={request.headers.get('User-Agent')}")

@app.route('/')
def index():
    return render_template('index.html.j2', foo = "bar")

@app.route('/api/v1/mouse_move', methods=["POST"])
def api_decode_form():
    log_request()
    content_type = request.headers.get('Content-Type')
    if (content_type != 'application/json'):
        return 'Content-Type not supported!'

    json = request.json
    app.logger.info(json)
    return {}

