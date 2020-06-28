#!/usr/bin/env python3
# coding=utf-8

from flask import Blueprint, request
from flask import render_template
from page.zdyt.edit_date import get_ams_ewm


blue = Blueprint("ams_viems", __name__)


@blue.route('/ams/get_ewm', methods=['GET', 'POST'])
def get_ewm():

    method = request.method

    if method == "GET":
        html = render_template("ams/get_ewm.html")
    elif method == 'POST':
        dd_no = request.form["dd_no"]
        context = get_ams_ewm(dd_no)
        html = render_template("ams/get_ewm.html", **context)
    else:
        html = "<h1>请求方式错误</h1>"
    return html












