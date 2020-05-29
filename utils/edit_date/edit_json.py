#!/usr/bin/env python3
# coding=utf-8

import decimal
import json
import xmltodict


# 校验json里面是否有对应的key
def key_excit_json(json_1, key):
    json_1 = json.dumps(json_1)
    keylsit = key.split(".")
    if keylsit[-1] in json_1:
        return True
    else:
        return False


# 将数据格式转换为json
def type_to_json(response):
    if response[0] == "{":  # 字符串转换json
        response = json.loads(response)
    elif response[0] == "<":  # xml转换json
        xml = xmltodict.parse(response)
        response = json.dumps(xml, indent=1)
        response = json.loads(response)
        if key_excit_json(response, "RESPONSE"):
            response = response["RESPONSE"]
    else:
        raise Exception("传入的数据不能转换json格式")
    return response


def get_list_dict(str_list):
    str_list1 = []
    for i in range(len(str_list)):
        for (key, value) in str_list[i].items():
            if isinstance(value, bytes):
                value = str(value, encoding='utf-8')
                str_list[i][key] = value
            if isinstance(value, decimal.Decimal):
                value = str(value)
                str_list[i][key] = value
        str_list1.append(str_list[i])
    return str_list1


# 将json格式转换为xml
def jsonToXml(js):
    convertXml = ''
    try:
        convertXml = xmltodict.unparse(js, encoding='utf-8')
    except:
        convertXml = xmltodict.unparse({'request': js}, encoding='utf-8')
    finally:
        return convertXml


# 更新json的数据
def update_json_value(json_data, key, value):
    key_ = key.split(".")
    key_length = len(key_)
    i = 0
    json_data = dict(json_data)
    a = json_data
    while i < key_length:
        if i + 1 == key_length:
            a[key_[i]] = value
            i = i + 1
        else:
            a = a[key_[i]]
            i = i + 1
    return json_data


# 解析返回的json获得关键key值
def jiexi_json(json_data, key):
    a = key.split(".")
    value = json_data
    for i in a:
        value = value[i]
    return value











