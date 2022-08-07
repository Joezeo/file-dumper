from common.base_parser import BaseParser


class Color256TxtParser(BaseParser):
    '''
    What's the dump files should this parser deal with
    '''
    foucs = [
        "color_256.txt"
    ]

    '''
    Every parser should add this method to process dump file content

    @param: filename: current processing file's name
    @param: file: current processing file's content
    '''

    def parse(self, filename: str, file: str) -> str:
        content = ""
        idx = 0
        for color in file.split("\n"):
            rgb = self.hex_to_rgb(color)
            content += f"C_{idx}({idx}, \"{color}\", \"{rgb}\"),\n"
            idx += 1
        return content

    def hex_to_rgb(self, value: str) -> str:
        v = value.lstrip('#')
        s = "{}".format(tuple(int(v[i:i+2], 16) for i in (0, 2, 4)))
        s = s.replace(",", "").replace("(", "").replace(")", "")
        return s
