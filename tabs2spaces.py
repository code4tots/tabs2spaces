#!/usr/bin/env python
# usage: ./tabs2spaces.py [sourcefilename] [optional:destfilename=sourcefilename] [optional:tabworth=4]
# e.g. : ./tabs2spaces.py example.py 2
# If tabworth is not specified, it defaults to 4
# Converts all tabs in a file to spaces.

# WARNING:::: Another pitfall of this program is that your destination file can't be interpretable as an integer. It it can, it is assumed the argument was meant to specify tab worth.

# WARNING:::: it will even turn tabs in literals into spaces. IT WILL TURN ALL TABS IN YOUR FILE INTO SPACES!!
DEFAULT_TAB_WORTH = 4

def convert(sourcefilename, destfilename, tabworth):
    f = open(sourcefilename,'r')
    text = f.read()
    f.close()
    text = text.replace('\t',' ' * tabworth)
    f = open(destfilename,'w')
    f.write(text)
    f.close()

def main():
    from sys import argv
    argc = len(argv)
    if   argc == 1 or argc > 4:
        print('usage: ./tabs2spaces.py [sourcefilename] [optional:destfilename=sourcefilename] [optional:tabworth=4]')
    elif argc == 2:
        convert(argv[1],argv[1],DEFAULT_TAB_WORTH)
    elif argc == 3:
        destfilename = argv[1]
        try:
            tab_worth = int(argv[2])
        except:
            tab_worth = DEFAULT_TAB_WORTH
            destfilename = argv[2]
        convert(argv[1],destfilename,tab_worth)
    elif argc == 4:
        convert(argv[1],argv[2],int(argv[3]))
        
if __name__ == '__main__':
    main()
