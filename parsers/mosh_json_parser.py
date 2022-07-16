# -*- encoding: utf-8 -*-
# @date    : 2022/07/16 17:11:34
# @author  : Joe Zane
# @email   : joezane.cn@gmail.com
# @version : v1.0

import json

from tokenize import String
from common.base_parser import BaseParser


class MoshJsonParser(BaseParser):

    '''
    What's the dump files should this parser deal with
    '''
    foucs = [
        "tab_accomplish_l.json"
    ]

    '''
    Every parser should add this method to process dump file content
    '''

    def parse(self, filename) -> String:
        file_content = self.openFile(filename)
        file_json = json.loads(file_content)
        content = ""
        for udp_packet in file_json:
            source_layers = udp_packet["_source"]["layers"]
            # 0:client-server 1:server-client
            if source_layers["ssyncp"]["ssyncp.direction"] == "0":
                content += "\"" + \
                    source_layers["udp"]["udp.payload"] + "\"" + ",\n"

        content = content[:len(content)-2]
        return content
