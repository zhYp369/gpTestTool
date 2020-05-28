#!/usr/bin/env python3
# coding=utf-8

import base64
import hashlib
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
from urllib.parse import quote_plus


def stringtomd5(originstr):
    """将string转化为MD5"""
    originstr = str.encode(originstr, encoding='UTF-8')
    signaturemd5 = hashlib.md5()
    signaturemd5.update(originstr)
    return signaturemd5.hexdigest()


# md5加密
def md5_str(str1):
    hl = hashlib.md5()
    hl.update(str1.encode(encoding='utf-8'))
    str_md5 = hl.hexdigest()
    return str_md5


# base64加密
def encode_base64(encodeStrTest):
    encodeStrTest = base64.encodebytes(encodeStrTest.encode(encoding="utf-8"))
    encodeStrTest = encodeStrTest.decode(encoding="utf-8")
    return encodeStrTest


# base64解密
def decode_base64(decodeStrTest):
    decodeStrTest = decodeStrTest.encode(encoding="utf-8")
    decodeStrTest = base64.decodebytes(decodeStrTest)
    decodeStrTest = decodeStrTest.decode(encoding="utf-8")
    return decodeStrTest


# 秘钥字符不够16不够16，大于16补够16倍数
def pad_key(key):
    while len(key) % 16 != 0:
        key += b' '
    return key


# 加密字符不够16不够16，大于16补够16倍数
def pad(text):
    while len(text) % 16 != 0:
        text += b' '
    return text


# 对字符aes进行加密
def en_ase_str(key, text):
    key = key.encode(encoding="utf-8")
    text = text.encode(encoding="utf-8")
    # text = pad(text)
    # key = pad_key(key)
    # 进行加密算法，模式ECB模式，把叠加完16位的秘钥传进来
    aes = AES.new(key, AES.MODE_ECB)
    encrypted_text = aes.encrypt(text)
    encrypted_text = b2a_hex(encrypted_text).decode(encoding="utf-8")
    return encrypted_text


# 对字符进行aes加密
def de_ase_str(key, text):
    key = key.encode(encoding="utf-8")
    text = text.encode(encoding="utf-8")
    text = a2b_hex(text)
    key = pad_key(key)
    aes = AES.new(key, AES.MODE_ECB)
    decrypted_text = aes.decrypt(text)
    decrypted_text = decrypted_text.rstrip(b" ")
    return decrypted_text.decode(encoding="utf-8")


# 对url进行参数urlencode
def url_encode(value):
    value = quote_plus(value, encoding="utf-8")
    return value


def convert_n_bytes(n, b):
    bits = b * 8
    return (n + 2 ** (bits - 1)) % 2 ** bits - 2 ** (bits - 1)


def convert_4_bytes(n):
    return convert_n_bytes(n, 4)


def getHashCode(s):
    h = 0
    n = len(s)
    for i, c in enumerate(s):
        h = h + ord(c) * 31 ** (n - 1 - i)
    return convert_4_bytes(h)












