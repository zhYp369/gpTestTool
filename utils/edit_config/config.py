#!/usr/bin/env python
# coding=utf-8

"""
读取配置。这里配置文件用的yaml，也可用其他如XML,INI等，需在file_reader中添加相应的Reader进行处理。
"""
import os
from utils.edit_config.file_reader import YamlReader

# 通过当前文件的绝对路径，其父级目录一定是框架的base目录，然后确定各层的绝对路径。如果你的结构不同，可自行修改。
# 之前直接拼接的路径，修改了一下，用现在下面这种方法，可以支持linux和windows等不同的平台，也建议大家多用os.path.split()和os.path.join()，不要直接+'\\xxx\\ss'这样
BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
CONFIG_FILE = os.path.join(BASE_PATH, 'config')
DATA_PATH = os.path.join(BASE_PATH, 'data')
DRIVER_PATH = os.path.join(BASE_PATH, 'drivers')
LOG_PATH = os.path.join(BASE_PATH, 'log')
REPORT_PATH = os.path.join(BASE_PATH, 'report')
UP_file_path=os.path.join(DATA_PATH,'up_file')
EXE_PATH=os.path.join(UP_file_path,'up_exe')
ZIYUAN_PATH=os.path.join(UP_file_path,"up_ziyuan")
APK_PATH=os.path.join(ZIYUAN_PATH,'apk')
MP4_PATH=os.path.join(ZIYUAN_PATH,'mp4')
TUPIAN_PATH=os.path.join(ZIYUAN_PATH,'tupian')
XLSX_PATH=os.path.join(DATA_PATH,"ceshiyongli")



class Config:
    def __init__(self, config_name):
        config=os.path.join(CONFIG_FILE,config_name)
        self.config = YamlReader(config).data

    def get(self, element, index=0):
        """
        yaml是可以通过'---'分节的。用YamlReader读取返回的是一个list，第一项是默认的节，如果有多个节，可以传入index来获取。
        这样我们其实可以把框架相关的配置放在默认节，其他的关于项目的配置放在其他节中。可以在框架中实现多个项目的测试。
        """
        return self.config[index].get(element)