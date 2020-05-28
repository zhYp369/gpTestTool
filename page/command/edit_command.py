#!/usr/bin/env python3
# coding=utf-8

from utils.edit_file.edit_ymal import get_yaml_data
from utils.edit_os.edit_path import get_updir
import os


self_file = os.path.abspath(__file__)
command_file = os.path.join(get_updir(3, self_file), "ymal", "command.yml")
test_file = os.path.join(get_updir(3, self_file), "ymal", "testfile.yml")


def edit_command():
    commane_dict = get_yaml_data(command_file)
    return commane_dict


def edit_testfile():
    commane_dict = get_yaml_data(test_file)
    return commane_dict


