import sys
import os.path
from pathlib import Path
from itertools import groupby
from html.parser import HTMLParser

# Extending the HTMLParser
class InhParser(HTMLParser):
    def __init__(self):
        print('Calling initializer of InhParser class inherited from HTMLParser')
        # initialize the base class
        HTMLParser.__init__(self)
    
    # Calling the read method will return the parsed data
    def read(self, data):
        # clear the current output before re-use
        self._lines = []
        # re-set the parser's state before re-use
        self.reset()
        self.feed(data)
        return ''.join(self._lines)
    # Overriding original handle_data method.
    def handle_data(self, d):
        self._lines.append(d)

# Checking whether it is the main file or not.
if __name__ == "__main__":
    if len(sys.argv) == 3:
        input_file = sys.argv[1]
        print('Input File ', input_file)
        output_file_path = sys.argv[2]
        print('Output file path', output_file_path)
        resolved_file = Path(input_file).resolve()
        lines = list()
        if resolved_file.is_file():
            print('Input file is proper, Working/processing on it.')
            # Parsing the subtitle file source code from stackoverflow
            # https://stackoverflow.com/a/23620587/3629379
            with open(resolved_file, 'r') as file:
                # Here [2:] is cropping the first two elements from the list
                """
                # Ex: For parsed data [['1\n',
                        '00:02:17,440 --> 00:02:20,375\n',
                        "<font color="#E5E5E5">okay the next segment is going</font><font color="#CCCCCC"> to</font>"]
                        ]
                    getting list(g)[2:], cropping first two elements, returns
                    "<font color="#E5E5E5">okay the next segment is going</font><font color="#CCCCCC"> to</font>"]
                        """
                res = [list(g)[2:] for b,g in groupby(file, lambda x: bool(x.strip())) if b]
            
            # res is list of lists
            #print(res[:3])
            """
            [['<font color="#E5E5E5">okay the next segment is going</font><font color="#CCCCCC"> to</font>\n'], 
            ['introduce some of<font color="#CCCCCC"> the linguistic</font>\n'], 
            ['background as well<font color="#E5E5E5"> as some of the</font>\n']]
            """

            # Using List compression and concatinating list of lists to list of strings
            elLst = [''.join(st for st in el) for el in res]
            #print(elLst[:3])
            """
            ['<font color="#E5E5E5">okay the next segment is going</font><font color="#CCCCCC"> to</font>\n', 
                'introduce some of<font color="#CCCCCC"> the linguistic</font>\n', 
                'background as well<font color="#E5E5E5"> as some of the</font>\n']
            """
            # Initializing object for overridden parser
            parser = InhParser()
            # Using Concatinating Strings to compress the list of strings
            finalStr = ''.join(el for el in elLst)
            
            # Calling parser.read with the generated final string
            finaldata = parser.read(finalStr)
            
            # Writing Parsed data to File
            output_file = open(output_file_path,"w")
            output_file.write(finaldata)
            output_file.close()
            print('Processing done and saved to output file.')
        else:
            print('Input file doesnt exists')
    else:
        print('Please pass the input file to parse and output file to write.')
