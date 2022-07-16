# -*- encoding: utf-8 -*-
#@date    : 2022/07/16 17:11:23
#@author  : Joe Zane
#@email   : joezane.cn@gmail.com
#@version : v1.0

import os
import sys

abs_project_path = os.path.dirname(__file__)
sys.path.append(os.path.join(abs_project_path, "common"))
sys.path.append(os.path.join(abs_project_path, "parser"))

from parsers.mosh_json_parser import MoshJsonParser

base_file_path = "./dumps"

if __name__ == '__main__':
    parser = MoshJsonParser()
    for filename in os.listdir(base_file_path):
        if parser.foucsThis(filename=filename):
            parser.parse(filename=filename)
