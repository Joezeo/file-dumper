from common.base_parser import BaseParser
from bs4 import BeautifulSoup


class ColorPanelHtmlParser(BaseParser):
    '''
    What's the dump files should this parser deal with
    '''
    foucs = [
        "color_panel.html"
    ]

    '''
    Every parser should add this method to process dump file content

    @param: filename: current processing file's name
    @param: file: current processing file's content
    '''

    def parse(self, filename: str, file: str) -> str:
        soup = BeautifulSoup(file, "html.parser")
        content = ""
        for tr in soup.find_all("tr"):
            td = tr.find_all("td")
            name, rgb, hex = td[1].string, td[2].string, td[3].string
            content += f"{name}(\"{name}\", \"{rgb}\", \"{hex}\"),\n"
        return content
