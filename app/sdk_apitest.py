#!/usr/bin/env python
# coding=utf-8

"""
@author: zhangyp
@project: gpTestTool
@file: sdk_apitest
@time: 2020/6/28 9:56
@desc: 
"""



from flask import Blueprint, request, Response
from flask import render_template
from page.xin_sk.editofd import ofd_zhuan_base64
import base64
from utils.edit_date.edit_num import get_time


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


#流式读取
@blue.route('/sdk/down_ofdfile', methods=['GET', 'POST'])
def down_ofdfile():
    method = request.method
    if method == "GET":
        html = render_template("sdkapi/download_ofd.html")
        return html
    elif method == 'POST':
        ofdbase64 = request.form["ofdbase64"]
        ofd_file_path = r"/opt/var/app/data/Tooldata/test.ofd"
        # ofd_file_path = r"C:\Users\zhangyp\Desktop\ofd\test.ofd"
        ofd_file_name = get_time("%Y%m%d%H%M%S")+"test.ofd"
        with open(ofd_file_path, "wb") as f:
            f.write(base64.decodebytes(ofdbase64.encode(encoding="utf-8")))
        def send_file():
            with open(ofd_file_path, 'rb') as targetfile:
                while 1:
                    data = targetfile.read(20 * 1024 * 1024)  # 每次读取20M
                    if not data:
                        break
                    yield data
        response = Response(send_file(), content_type='application/octet-stream')
        response.headers["Content-disposition"] = 'attachment; filename=%s' % ofd_file_name  # 如果不加上这行代码，导致下图的问题
        return response

