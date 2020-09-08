#!/usr/bin/env python3
# coding=utf-8

import requests
import hashlib
from Crypto.Cipher import AES
import hmac
from binascii import b2a_hex, a2b_hex
import random
from utils.edit_db.connect_db import OperationMysql
from utils.edit_config.config import Config
import os
from utils.edit_encryption.encryption import md5_str
import datetime


a = [53, 54, 50, 97, 59, 53, 110, 121, 45, 99, 57, 51, 49, 45, 52, 98, 50, 56, 45, 97, 53, 101, 50, 55, 46, 19, 51, 52, 97, 50, 74, 16, 49, 56, 98, 54]
sg_key = bytearray(a)
ae_key = "ABCD123dJKHger34"


db_config_file = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "config_file", "db.yml")
db_peizhi = Config(db_config_file).get("skdb_config")
ams_db_config = Config(db_config_file).get("ams")


def get_aes_message(key, value):
    """
    对报文进行aes加密
    """
    # key -> sha1prng_key
    signature = hashlib.sha1(key.encode()).digest()
    signature = hashlib.sha1(signature).digest()
    aes_key = bytes.fromhex(''.join(['%02x' % i for i in signature])[:32])
    crypto = AES.new(aes_key, AES.MODE_ECB)
    # padding content with pkcs5
    block_size = AES.block_size
    append_size = block_size - len(value.encode('utf-8')) % block_size
    padding_value = value + append_size * chr(append_size)
    return ''.join(['%02x' % i for i in crypto.encrypt(str.encode(padding_value))])


def get_sign_message(key, message):
    """
    对报文签名
    """
    signature = hmac.new(key, bytes(message, encoding='utf-8'), digestmod=hashlib.sha256).digest()
    str_sig = b2a_hex(signature).decode(encoding="utf-8")
    return str_sig


def get_jiami_message(message):
    """
    获取加密后的报文
    """
    sign_message = get_sign_message(sg_key, message)
    aes_message = get_aes_message(ae_key, message)
    message_dict = {
        "sign": sign_message,
        "aes": aes_message
    }
    return message_dict


def get_rusult(url, request_date):
    message_dict = get_jiami_message(request_date)
    headers = {'cache-control': "no-cache"}
    data = message_dict.get("aes")
    querystring = {"sign": message_dict.get("sign")}
    res = requests.post(url=url, headers=headers, data=data, params=querystring, verify=False).text
    return res


def get_result_dict(url, request_date):
    context = {}
    try:
        result = get_rusult(url, request_date)
    except Exception as e:
        result = e
    context["req_url"] = url
    context["req_date"] = request_date
    context["result"] = result
    return context


def get_jiami_dict(request_date):
    context = {}
    try:
        result = get_jiami_message(request_date)
    except Exception as e:
        result = e
    context["req_date"] = request_date
    context["sign"] = result.get("sign","none")
    context["aes"] = result.get("aes","none")
    return context


# 获取红字申请编码16位
def get_zhuan_bianma_16():
    suiji = str(random.randint(99999999999999, 999999999999999))
    list_a = list(map(int, suiji))
    sub_naumer = 0
    for i in range(len(list_a)):
        sub_naumer = sub_naumer + list_a[i]
    yu_number = sub_naumer % 10
    suiji = suiji + str(yu_number)
    return suiji


def get_hztzd_dict():
    context = {}
    try:
        result = get_zhuan_bianma_16()
    except Exception as e:
        result = e
    context["hztzd"] = result
    return context


def sh_hztzd_dict(fpdm, fphm, shjg):
    context = {}
    hztzdbh = get_zhuan_bianma_16()
    try:
        op_mysql = OperationMysql(db_peizhi)
        if shjg == "tg":
            sql = "update dj_hzxxb_sq set xxbbh=%s, clbz=2 where lzfpdm=%s and lzfphm=%s ;" % (hztzdbh, fpdm, fphm)
        if shjg == "btg":
            sql = "update dj_hzxxb_sq set clbz=3,spbz='%s' where lzfpdm=%s and lzfphm=%s ;" % ("N", fpdm, fphm)
        if shjg == "dh":
            sql = "update dj_hzxxb_sq set clbz=3 where lzfpdm=%s and lzfphm=%s ;" % (fpdm, fphm)
        res = op_mysql.update(sql)
        if res == 1:
            sh_jg = "发票审核成功"
        else:
            sh_jg = "不存在此发票"
        result = "yes"
    except Exception as e:
        result = e
        sh_jg = "审核失败"
    context["fpdm"] = fpdm
    context["fphm"] = fphm
    context["sh_jg"] = sh_jg
    context["hztzdbh"] = hztzdbh
    context["result"] = result
    return context


def get_ams_ewm(dd_no):
    context = {}
    op_mysql = OperationMysql(ams_db_config)
    sql = "SELECT STORE_CODE,ORDER_NO,TOTAL_PRICE,TRANSACTION_DATE FROM `order_info` WHERE ORDER_NO ='%s' ;" % dd_no
    res = op_mysql.select(sql)[0]
    dict_dd = res
    STORE_CODE = dict_dd.get("STORE_CODE")
    ORDER_NO = dict_dd.get("ORDER_NO")
    AMT = dict_dd.get("TOTAL_PRICE")
    TRANSACTION_DATE = datetime.datetime.strftime(dict_dd.get("TRANSACTION_DATE"), '%Y%m%d')
    SIGN_str = "%s,%s,%s,%s,HERMESSCAN" % (STORE_CODE, ORDER_NO, AMT, TRANSACTION_DATE)
    SIGN_md5 = md5_str(SIGN_str).upper()
    SIGN = SIGN_md5[1:8]
    ewm = "http://dev.fapiao.com:19080/hermes-invoice/inv.html?r=%s,%s,%s,%s,%s" % (
    STORE_CODE, ORDER_NO, AMT, TRANSACTION_DATE, SIGN)
    context["dd_no"] = dd_no
    context["ewm"] = ewm
    return context








