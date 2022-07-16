# -*- encoding: utf-8 -*-
# @date    : 2022/07/16 17:11:23
# @author  : Joe Zane
# @email   : joezane.cn@gmail.com
# @version : v1.0

import inspect
import os
import sys
import pkgutil

abs_project_path = os.path.dirname(__file__)
sys.path.append(os.path.join(abs_project_path, "common"))
sys.path.append(os.path.join(abs_project_path, "parsers"))

parsers_path_set = []

for importer, modname, ispkg in pkgutil.walk_packages(path=[os.path.join(abs_project_path, "parsers")],
                                                      prefix="parsers.",
                                                      onerror=lambda x: None):
    exec('from ' + modname + ' import *')
    parsers_path_set.append(modname)


base_file_path = "dumps"

if __name__ == '__main__':
    parser_set = []
    for parser_path in parsers_path_set:
        mod = sys.modules[parser_path]
        members = inspect.getmembers(mod, inspect.isclass)
        for (name, clazz) in members:
            if (name == "BaseParser"): continue
            parser_set.append(clazz())

    abs_dump_file_path = os.path.join(abs_project_path, base_file_path);
    for filename in os.listdir(abs_dump_file_path):
        for parser in parser_set:
            if parser.foucsThis(filename=filename):
                content = parser.parse(filename=os.path.join(abs_dump_file_path, filename))
                parser.writeResult(filename, content)
