#!/usr/bin/env python3
title = "Brainfuck Interpreter by Matthew Watt"
version = 1.0

import requests, argparse, os, re, ast, numpy as np
from time import sleep

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

parser = argparse.ArgumentParser(description='Interpret brainfuck code.')
parser.add_argument('files', metavar='f', type=str, nargs=1,help='the file to interpret')

fileName = parser.parse_args().files[0]
pointer = 0 # pointer position to zero
output = ""
command = ""

byteList = [0]

def refresh():
    cls()
    print(title, "- Version", version, '\nFile:', fileName, '\n', byteList,"\nPointer:",pointer,"\nCommand",command,"\nOutput:",output)

refresh()

with open(fileName, 'r') as file:
        data = file.read().replace('\n', '')
        subs = {'[^>+-\[\]<>.,]+': '', '[0-9a-zA-Z/]+': '', '\,': '0,', '\]': '],', '\.': '1,', '\-': '2,', '\+': '3,', '\<': '4,', '\>': '5,',}
        for sub in subs:
            data = re.sub(sub, subs[sub], data)

        commandList = ast.literal_eval("[" + data + "]") 

def depth(l):
    if isinstance(l, list):
        return 1 + max(depth(item) for item in l)
    else:
        return 0

layers = depth(commandList)

httpState = 0

def controlCommand(command):
    global byteList, pointer, output
    print("Machine control command program output")
    if command == 0:
        print("null")
    elif command == 1:
        print("start of heading")
        httpsState = 0
    elif command == 2:
        print("start of text")
        httpsState = 1
    elif command == 3:
        print("end of text")
        httpsState = 0
    elif command == 4:
        print("end of transmission")
        httpsState = 0
    elif command == 6:
        print("acknowledge")
    elif command == 10:
        print("new line")
    elif command == 21:
        print("negative acknowledge")
    else:
        print("unused ASCII command")


def runCommand(command):
    global byteList, pointer, output
    if command == 0:
        userInput = input()
        byteList[pointer] = ord(userInput[0])
    elif command == 1:
        if byteList[pointer] > 31 and byteList[pointer] < 127:
            output += chr(byteList[pointer])
        elif byteList[pointer] < 32:
            controlCommand(byteList[pointer])
    elif command == 2:
        byteList[pointer] -= 1
        if byteList[pointer] < 0:
            byteList[pointer] = 255 # roll over instead of allowing negative (keep within one byte) - assumed feature of bf
    elif command == 3:
        byteList[pointer] += 1
        if byteList[pointer] > 255:
            byteList[pointer] = 0 # roll over instead of allowing 256 (keep within one byte) - assumed feature of bf
    elif command == 4:
        pointer -= 1
        if pointer < 0:
            byteList.insert(0, 0) # allow array to extend to the left (non-standard bf feature)
    elif command == 5:
        pointer += 1
        if len(byteList) < pointer + 1:
            byteList.append(0)

    refresh()

def loopControl(command):
    if isinstance(command, int):
        runCommand(command)
    elif isinstance(command, list):
        while byteList[pointer] > 0:
            for subCommand in command:
                loopControl(subCommand)

for command in commandList:
    loopControl(command)

cls()
print(title, "- Version", version, '\nFile:', fileName, '\n', byteList,"\n\n\nOutput:",output)
