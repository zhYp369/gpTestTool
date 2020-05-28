#!/usr/bin/env python3
# coding=utf-8


from utils.edit_encryption.encryption import encode_base64, decode_base64,stringtomd5


def get_base_result(req, text):
    context = {}
    res_text = ""
    if req == "baseENcode":
        res_text = encode_base64(text)
    if req == "baseDEcode":
        res_text = decode_base64(text)
    context["base_res_text"] = res_text
    context["base_req_text"] = text
    return context


def get_md5_result(text):
    context = {}
    res_text = stringtomd5(text)
    context["md5_res_text"] = res_text
    context["md5_req_text"] = text
    return context
