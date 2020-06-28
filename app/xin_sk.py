#!/usr/bin/env python3
# coding=utf-8

from flask import Blueprint, request
from flask import render_template
from page.xin_sk.editofd import ofdbase64_zhuan_imgbase64



blue = Blueprint("xin_sk_viems", __name__)


@blue.route('/xin_sk/ofdtransferomg', methods=['GET', 'POST'])
def ofdtransferomg():

    method = request.method
    if method == "GET":
        context = {}
    elif method == 'POST':
        f = request.files['file']
        url = request.form["url"]
        if ".ofd" == f.filename[-4:]:
            context = ofdbase64_zhuan_imgbase64(f, url)
        else:
            context = {"error": "上传文件格式不正确"}
        context["url"] = url
    else:
        context = {"error": "请求方式错误"}
    context["qqurl"] = "http://172.25.2.106:52101/fpt-pdfTransfer/ofdTransfer.do?method=ofd2png"
    html = render_template("xinsk/up_ofd.html", **context)
    return html
















