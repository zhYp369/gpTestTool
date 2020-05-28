#!/usr/bin/env python3
# coding=utf-8

from flask import Blueprint, request
from flask import render_template
from page.zdyt.edit_date import get_result_dict, get_jiami_dict, get_hztzd_dict, sh_hztzd_dict


blue = Blueprint("zdyt_viems", __name__)


@blue.route('/zdyt/apitest', methods=['GET', 'POST'])
def apitest():

    method = request.method

    if method == "GET":
        html = render_template("zdyt/zdyt.html")

    elif method == 'POST':
        req_url = request.form["req_url"]
        req_date = request.form["request_data"]
        context = get_result_dict(req_url, req_date)
        html = render_template("zdyt/zdyt.html", **context)

    else:
        html = "<h1>请求方式错误</h1>"
    return html


@blue.route('/zdyt/get_jm', methods=['GET', 'POST'])
def get_jm():

    method = request.method

    if method == "GET":
        html = render_template("zdyt/zdyt_jm.html")

    elif method == 'POST':
        req_date = request.form["request_data"]
        context = get_jiami_dict(req_date)
        html = render_template("zdyt/zdyt_jm.html", **context)

    else:
        html = "<h1>请求方式错误</h1>"
    return html


@blue.route('/zdyt/get_hztzd', methods=['GET', 'POST'])
def get_hztzd():
    context = get_hztzd_dict()
    html = render_template("zdyt/zdyt_hztzd.html", **context)
    return html


@blue.route('/zdyt/hztzd_sh', methods=['GET', 'POST'])
def hztzd_sh():

    method = request.method

    if method == "GET":
        html = render_template("zdyt/zdyt_hztzd_sh.html")

    elif method == 'POST':
        fpdm = request.form["fpdm"]
        fphm = request.form["fphm"]
        shjg = request.form["shjg"]
        context = sh_hztzd_dict(fpdm, fphm, shjg)
        html = render_template("zdyt/zdyt_hztzd_sh.html", **context)
    else:
        html = "<h1>请求方式错误</h1>"
    return html












