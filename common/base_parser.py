# -*- encoding: utf-8 -*-
# @date    : 2022/07/16 17:11:44
# @author  : Joe Zane
# @email   : joezane.cn@gmail.com
# @version : v1.0


class BaseParser():

    '''
    According to the filename to open a file using utf-8 charset
    and return the string content of this file.
    '''

    def openFile(self, filename) -> str:
        if filename is None:
            print("Foucus nothing.")
            return None
        return open(filename, encoding='utf-8').read()

    '''
    Judge whether the parser foucus on and processing this dump file or not.
    '''

    def foucsThis(self, filename) -> bool:
        if not hasattr(self, "foucs"):
            return
        foucs = eval('self.foucs')
        for fc in foucs:
            if fc == filename:
                return True
        return False

    '''
    Write the processing result in certain file.
    '''

    def writeResult(self, filename, content):
        split = filename.split("\\")
        filename = split[len(split) - 1].split(".")[0]
        idx = 0
        final_path = ""
        for sp in split:
            if idx < len(split) - 2:
                final_path += sp + "\\"
                idx += 1
        filename = f"{final_path}\\result\\{filename}.txt"
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
