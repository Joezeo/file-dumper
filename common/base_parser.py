# -*- encoding: utf-8 -*-
# @date    : 2022/07/16 17:11:44
# @author  : Joe Zane
# @email   : joezane.cn@gmail.com
# @version : v1.0

import logging

logger = logging.getLogger(__name__)


class BaseParser:
    def __init__(self, project_path: str, source_path: str, result_path: str):
        self._project_path = project_path
        self._source_path = source_path
        self._result_path = result_path

    '''
    According to the filename to open a file using utf-8 charset
    and return the string content of this file.
    '''

    def _open_file(self, filename: str) -> str:
        if filename is None:
            logger.warning("filename is none.")
            return None
        filename = f"{self._project_path}\\{self._source_path}\\{filename}"
        logger.info(f"starting reading file: {filename}")
        return open(filename, encoding='utf-8').read()

    '''
    Judge whether the parser foucus on and processing this dump file or not.
    '''

    def _foucs_this(self, filename: str) -> bool:
        if not hasattr(self, "foucs"):
            return
        foucs = eval('self.foucs')
        for focus in foucs:
            if "*" in focus:
                if focus[0] == "*" or focus[-1] == "*":
                    continue
                s = focus.split("*")
                if (s[0] in filename) and (s[1] is None or s[1] in filename) \
                        and focus.index(s[0][-1]) < focus.index(s[1][0]):
                    return True
            elif focus == filename:
                return True
        return False

    '''
    Write the processing result in certain file.
    '''

    def _write_result(self, filename: str, content: str) -> None:
        split = filename.split("\\")
        filename = split[len(split) - 1].split(".")[0]
        filename = f"{self._project_path}\\{self._result_path}\\{filename}.txt"
        logger.info(f"writing processing result to file: {filename}")
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
