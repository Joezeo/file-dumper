# -*- encoding: utf-8 -*-
# @date    : 2022/07/16 17:11:34
# @author  : Joe Zane
# @email   : joezane.cn@gmail.com
# @version : v1.0

import json

from common.base_parser import BaseParser


class WiresharkUdpPayloadParser(BaseParser):

    '''
    What's the dump files should this parser deal with
    '''
    foucs = [
        "mosh_udp_playload_*.json"
    ]

    '''
    Every parser should add this method to process dump file content

    @param: filename: current processing file's name
    @param: file: current processing file's content
    '''

    def parse(self, filename: str, file: str) -> str:
        file_json = json.loads(file)
        server, client = "\nserver:\n", "client:\n"

        for udp_packet in file_json:
            source_layers = udp_packet["_source"]["layers"]
            # 0:client-server 1:server-client
            if ("ssyncp" in source_layers
                    and source_layers["ssyncp"]["ssyncp.direction"] == "0") \
                    or ("ssyncp" not in source_layers
                        and source_layers["ip"]["ip.src"] == "26.26.26.1"):
                client += f"\"{source_layers['udp']['udp.payload']}\",\n"
            if ("ssyncp" in source_layers
                    and source_layers["ssyncp"]["ssyncp.direction"] == "1") \
                    or ("ssyncp" not in source_layers
                        and source_layers["ip"]["ip.dst"] == "26.26.26.1"):
                server += f"\"{source_layers['udp']['udp.payload']}\",\n"

        content = client[:len(client) - 2] + server[:len(server) - 2]
        return content
