#!/usr/bin/env python3
# coding=utf-8

from flask import Blueprint
from flask import render_template
from flask import request
from page.tool.edit_base64 import get_base_result, get_md5_result

blue = Blueprint("tool_viems", __name__)


@blue.route('/tool/base64', methods=['GET',"POST"])
def base64():
    html = ""
    method = request.method
    if method == "GET":
        html = render_template("tool.html")
    elif method == "POST":
        basereq = request.form["base"]
        req_text = request.form["req_text"]
        context = get_base_result(basereq, req_text)
        html = render_template("tool.html", **context)
    return html


@blue.route('/tool/md5', methods=['GET',"POST"])
def md5():
    html = ""
    method = request.method
    if method == "GET":
        html = render_template("tool.html")
    elif method == "POST":
        req_text = request.form["req_text"]
        context = get_md5_result(req_text)
        html = render_template("tool.html", **context)
    return html





