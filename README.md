# wireshark-dumper
Parse the network paceket capture result dump file from wireshark. 

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
    '''
    def parse(self, filename) -> String:
        content = "";
        # there is your customize process logic
        return content
```

### Directories
wireshark-dumper  
|&nbsp;--&nbsp; `parsers` &nbsp; put the parser classes  
|&nbsp;--&nbsp; `common` &nbsp;&nbsp;&nbsp; some common components  
|&nbsp;--&nbsp; `dumps` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; where you put the dump files  
|&nbsp;--&nbsp; `result` &nbsp;&nbsp;&nbsp; the result file is created in here

### Run
The program entry was `start.py`, just python it.
