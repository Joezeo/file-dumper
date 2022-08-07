from common.base_parser import BaseParser


class KeyBoardStringTxtParser(BaseParser):
    '''
    What's the dump files should this parser deal with
    '''
    foucs = [
        "keyboard_string.txt"
    ]

    '''
    Every parser should add this method to process dump file content

    @param: filename: current processing file's name
    @param: file: current processing file's content
    '''

    def parse(self, filename: str, file: str) -> str:
        content = ""
        for line in file.split("\n"):
            sp = line.split("\t")
            field = sp[0].replace(" ", "_").replace("(", "")\
                .replace(")", "").replace("/", "_").upper()
            code = "\"" + sp[2] + "\"" if sp[2] != "--" else "null"
            code = code.replace("(", "").replace(")", "")
            shiftCode = "\"" + sp[3] + "\"" if sp[3] != "--" else "null"
            shiftCode = shiftCode.replace("(", "").replace(")", "")
            ctrlCode = "\"" + sp[4] + "\"" if sp[4] != "--" else "null"
            ctrlCode = ctrlCode.replace("(", "").replace(")", "")
            altCode = "\"" + sp[5] + "\"" if sp[5] != "--" else "null"
            altCode = altCode.replace("(", "").replace(")", "")
            content += f"{field}(\"{sp[1]}\", {code}, {shiftCode}, " +\
                f"{ctrlCode}, {altCode}),\n"
            print(field)
        return content
