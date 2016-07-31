#/usr/bin/env python
#! -*- coding: utf-8 -*-
import argparse
import time
from os import path
from sys import stdin

#Initialisation of variables
input_str = stdin.readline()
processed_str = ''
operators = []
o_perands = []
number = ''
res = 0

#Version and changes date control
ver = "1.2"
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--version", action="store_true")
args = parser.parse_args()
if args.version:
    print ("Version: {}".format(ver))
    date_of_create = path.getmtime("calc.py")
    print ("The date of last changes: {}".format(time.ctime(date_of_create)))
    exit(0)

#Classes
class InStr_proc():

    def __init__(self, string):
        self.string = string

    def processor(self):
        if ' ' in self.string:
            self.string = self.string.replace(' ', '')
            return self.string
        else:
            return self.string

class Queue():

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)
 
    def peek(self):
        return self.items[0]

#Input string processing
processed_str = InStr_proc(input_str).processor()
operators = Queue()
o_perands = Queue()

#Cheking the correctness of Input

for i in processed_str:
    if i in '+-':
        operators.enqueue(i)
        if number != '':
            o_perands.enqueue(number)
        number = ''
    elif i.isdigit():
        number += i
    else:
        o_perands.enqueue(number)

#Calculating
if operators.peek() == '-' and operators.size() == o_perands.size():
    res -= int(o_perands.dequeue())
    operators.dequeue()
else:
    res += int(o_perands.dequeue())
while o_perands.isEmpty() != True:
    if operators.peek() == '+':
        res += int(o_perands.dequeue())
        operators.dequeue()
    elif operators.peek() == '-':
        res -= int(o_perands.dequeue())
        operators.dequeue()

print res
