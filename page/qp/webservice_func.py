#!/usr/bin/env python3
# coding=utf-8


from suds.client import Client
from suds.xsd.doctor import Import, ImportDoctor
from utils.edit_file.edit_ymal import get_yaml_data
from utils.edit_file.edit_ymal import path_qp_yml


url_list = get_yaml_data(path_qp_yml).get("cdk").get("plugins")

# Fix missing types with ImportDoctor
plugins_list = []
for i in url_list:
    imp = Import(i)
    plugins_list.append(ImportDoctor(imp))


# 车队卡
def cdk_req(url, func, in0, in1):
    client = Client(url=url, plugins=plugins_list)
    respon = client.service["CardInvoiceDataServiceHttpPort"][func](in0, in1)
    return respon


# loyalty
def loyalty_req(url, func, in0, in1):
    client = Client(url=url)
    respon = client.service["EInvoiceRequestServiceHttpPort"][func](in0, in1)
    return respon
