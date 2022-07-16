# wireshark-dumper

Parse the network paceket capture result dump file from wireshark.

### Directories

***wireshark-dumper***  
|&nbsp;--&nbsp; `dumps  ` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; where you put the dump files  
|&nbsp;--&nbsp; `result ` &nbsp;&nbsp;&nbsp; the result file is created in here  
|&nbsp;--&nbsp; `parsers` &nbsp;&nbsp; create parser classes here  
|&nbsp;--&nbsp; `common ` &nbsp;&nbsp;&nbsp; some common components  

### Usage

Create parser extend `common.base_parser.BaseParser`, and this parser class should have a method called `parse(filename) -> String` to process the dump file and return the process result and should also have the list attribute called `focus` to specify the files to be processed. Just like this:

```python
class DemoParser(BaseParser):

    '''
    What's the dump files should this parser deal with
    '''

    foucs = [
        "demo.json"
    ]

    '''
    Every parser should add this method to process dump file content

    @param: filename: current processing file's name
    @param: file: current processing file's content
    '''

    def parse(self, filename, file) -> str:
        content = "";
        # there is your customize process logic
        return content
```

### Run

The program entry was `start.py`, just python it.
