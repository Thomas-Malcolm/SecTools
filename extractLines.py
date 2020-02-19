#!/usr/bin/python3

import sys


def printHelp():
    print("=======================================")
    print("extractLines.py does exactly what it sounds like - it extracts lines from a file, strips newlines and tabs (very static atm, but can just edit code) and prints to stdout")

    print("=======================================")
    print("Usage: \n")
    print("-h/--help        print help information")
    print("-f               specify input file")
    print("-s               starting line (def: 0)")
    print("-e               ending line (def: EOF)")

    print("=======================================")

args = sys.argv

fileName = None
startLine = None # Default 0
endLine = None   # Default EOF


for i,entry in enumerate(args):
    if entry == '-h' or entry == '--help':
        printHelp()
        exit()
    elif entry == '-f':
        fileName = args[i + 1]
    elif entry == '-s':
        try:
            startLine = int(args[i + 1])
        except ValueError:
            print("Incorrect usage, start line can only be an int")
    elif entry == '-e':
        try:
            endLine = int(args[i + 1])
        except ValueError:
            print("Incorrect usage, end line can only be an int")

if fileName is None or not isinstance(fileName, str):
    print("Incorrect usage. Specify file name (-f)")
    exit()


with open(fileName, "r") as ass:
    lines = []
    for i,line in enumerate(ass):
        lines.append(line.strip('\n'))


    if startLine is None:
        startLine = 0
    if endLine is None:
        endLine = len(lines)
        
        
    toOut = ""

    for i in range(startLine,endLine):
        toOut += lines[i].strip('\n').strip('\t').strip('\t').strip('\t').strip('  ')


    print(toOut)



