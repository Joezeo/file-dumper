# -*- encoding: utf-8 -*-
# @date    : 2022/07/16 17:11:23
# @author  : Joe Zane
# @email   : joezane.cn@gmail.com
# @version : v1.0

import inspect
import os
import sys
import pkgutil
import logging
from concurrent.futures import ThreadPoolExecutor

source_file_path = "dumps"
result_file_path = "result"
abs_project_path = os.path.dirname(__file__)
parsers_path_set = []
theard_pool = ThreadPoolExecutor(
    max_workers=10,
    thread_name_prefix="parser.thread."
)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

sys.path.append(os.path.join(abs_project_path, "common"))
sys.path.append(os.path.join(abs_project_path, "parsers"))
for importer, modname, ispkg in pkgutil.walk_packages(
    path=[os.path.join(abs_project_path, "parsers")],
    prefix="parsers.",
    onerror=lambda x: None
):
    exec('from ' + modname + ' import *')
    parsers_path_set.append(modname)


def _start_parser(parser, filename) -> None:
    file = parser._open_file(filename)
    content = parser.parse(filename, file)
    parser._write_result(os.path.join(abs_dump_file_path, filename), content)


if __name__ == '__main__':
    parser_set = []
    for parser_path in parsers_path_set:
        mod = sys.modules[parser_path]
        members = inspect.getmembers(mod, inspect.isclass)
        for (name, clazz) in members:
            if (name == "BaseParser"):
                continue
            parser_set.append(
                clazz(abs_project_path, source_file_path, result_file_path)
            )

    abs_dump_file_path = os.path.join(abs_project_path, source_file_path)
    for filename in os.listdir(abs_dump_file_path):
        for parser in parser_set:
            if parser._foucs_this(filename=filename):
                theard_pool.submit(_start_parser, parser, filename)
