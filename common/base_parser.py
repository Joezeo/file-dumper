# -*- encoding: utf-8 -*-
#@date    : 2022/07/16 17:11:44
#@author  : Joe Zane
#@email   : joezane.cn@gmail.com
#@version : v1.0

from tokenize import String


class BaseParser:
    def openFile(self, filename) -> String:
        if filename == None:
            print("Foucus nothing.")
            return None;
        return "Open file: " + filename;
    def foucsThis(self, filename) -> bool:
        if not hasattr(self, "foucs"):
            return;
        foucs = eval('self.foucs')
        for fc in foucs:
            if fc == filename:
                return True;
        return False;