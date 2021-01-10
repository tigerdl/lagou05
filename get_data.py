# -*- coding: utf-8 -*-
# @Time : 2021/1/10 6:36 下午
# @Author : lidong
# @File : get_data.py

import os

import yaml

file_path = os.path.dirname(os.path.abspath(__file__)) + "/calculator.yml"

def get_yaml_data():
    with open(file_path) as f:
        data = yaml.safe_load(f)["data"]
        print(1,data)
        return [data]
