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
            content += f"C_{idx}({idx}, \"{color}\"),\n"
            idx += 1
        return content
