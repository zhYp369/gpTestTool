#!/usr/bin/env python
# coding=utf-8

"""
@author: zhangyp
@project: gpTestTool
@file: sdk_apitest
@time: 2020/6/28 9:56
@desc: 
"""



from flask import Blueprint, request
from flask import render_template
from page.xin_sk.editofd import ofd_zhuan_base64


blue = Blueprint("sdk_viems", __name__)

@blue.route('/sdk/ofdtransbase64', methods=['GET', 'POST'])
def ofdtransbase64():

    method = request.method
    if method == "GET":
        context = {}
    elif method == 'POST':
        f = request.files['file']
        if ".ofd" == f.filename[-4:]:
            context = ofd_zhuan_base64(f)
        else:
            context = {"result": "上传文件格式不正确"}
    else:
        context = {"result": "请求方式错误"}
    html = render_template("sdkapi/ofd_tran_base.html", **context)
    return html
