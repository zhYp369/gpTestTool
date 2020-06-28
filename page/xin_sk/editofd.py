
import base64
import requests
from utils.edit_date.edit_json import type_to_json, jiexi_json


def ofdbase64_zhuan_imgbase64(f ,url):
    """
    调接口ofdbase64的数据转图片base64的数据
    :param ofdbase64:
    :return:
    """
    # 读取odf文件的bety数据
    base64str = f.read()

    # bety数据加密成base64字符串
    bs64_b = base64.b64encode(base64str)
    bs64_str = bytes.decode(bs64_b)

    # 请求接口的headers
    headers = {
        'content-type': 'application/octet-stream',
        'Content-Type': 'text/plain'
    }

    # 请求转换图片接口
    response = requests.request("POST", url, headers=headers, data=bs64_str).text

    # 将返回数据转换json格式，提取文件数据列表，带清单的可能是list
    res_json = type_to_json(response)
    data = jiexi_json(res_json, "DATAS.DATA")

    data_list = []  # 定义一个列表用来放图片base64数据

    # 将base64加到列表
    if isinstance(data, list):          # 带清单返回列表
        for i in range(len(data)):
            img = data[i].get("IMG")
            data_list.append(img)
    else:                               # 不带清单，返回单个文件数据
        img = data.get("IMG")
        data_list.append(img)

    context = {"result": data_list}
    return context


def ofd_zhuan_base64(f):
    """
        调接口ofdbase64的数据转图片base64的数据
        :param ofdbase64:
        :return:
        """
    # 读取odf文件的bety数据
    base64str = f.read()
    # bety数据加密成base64字符串
    bs64_b = base64.b64encode(base64str)
    bs64_str = bytes.decode(bs64_b)
    context = {"result": bs64_str}
    return context