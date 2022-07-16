# -*- encoding: utf-8 -*-
#@date    : 2022/07/16 17:11:34
#@author  : Joe Zane
#@email   : joezane.cn@gmail.com
#@version : v1.0

from common.base_parser import BaseParser

class MoshJsonParser(BaseParser):
    foucs = [
        "tab_accomplish_l.json"
    ]
    def parse(self, filename):
        file = self.openFile(filename);
        print(file)
