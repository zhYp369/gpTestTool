import yaml
import os
#!/usr/bin/env python3
# coding=utf-8

from utils.edit_os.edit_path import get_updir

_file = os.path.abspath(__file__)
app_path = get_updir(3, _file)

path_qp_yml = os.path.join(app_path, "ymal", "qp.yml")


def get_yaml_data(yaml_file):
    with open(yaml_file, 'r', encoding="utf-8") as f:
        file_data = f.read()
    data = yaml.load(file_data, Loader=yaml.FullLoader)
    return data



