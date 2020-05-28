#!/usr/bin/env python3
# coding=utf-8

from page.qp.webservice_func import cdk_req
from utils.edit_date.edit_json import type_to_json, update_json_value, jsonToXml
from utils.edit_date.edit_num import get_time, get_random


def update_global(glo_date):
    values = ""
    global_date = type_to_json(glo_date)
    RequestNumber = "LAT-REQ" + get_time("%Y%m%d%H%M%S") + get_random(5)
    sendtime = get_time("%Y-%m-%dT%H:%M:%S")
    global_date = update_json_value(global_date, "GlobalInfo.requestNumber", RequestNumber)
    glo_date = update_json_value(global_date, "GlobalInfo.sendTime", sendtime)
    for values in glo_date.values():
        values = values
    return values


def update_reqdate(req_date):
    values = ""
    req_date = type_to_json(req_date)
    for values in req_date.values():
        values = values
    return values


def get_result_dict(req_url, req_method, glo_xml_date, req_xml_date):
    context = {}
    gol_data = update_global(glo_xml_date)
    req_date = update_reqdate(req_xml_date)
    try:
        result = cdk_req(req_url, req_method, gol_data, req_date)
    except Exception as e:
        result = e
    context["req_url"] = req_url
    context["req_method"] = req_method
    context["glo_date"] = glo_xml_date
    context["req_date"] = req_xml_date
    context["result"] = result
    return context
