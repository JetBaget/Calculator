#/usr/bin/env python
#! -*- coding: utf-8 -*-
import argparse
import time
from os import path
import signal
import sys

#Initialisation of variables
input_str = ''
processed_str = ''
processed_list = []
operators = []
o_perands = []
number = ''
res = 0
char = ''

#version and changes date control
ver = "1.3.1"
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--version", action="store_true")
args = parser.parse_args()
if args.version:
    print ("Version: {}".format(ver))
    date_of_create = path.getmtime("calc.py")
    print ("The date of last changes: {}".format(time.ctime(date_of_create)))
    exit(0)

#Classes
class InStr_proc(): #input string processing

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

#Function for correct close
def signal_handler(signal, frame):
    print("You pressed Ctrl+C!")
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

#Function of cheking the correctness of Input
def check_input(checking_string):
    check_1 = False
    check_2 = False
    check_3 = False
    o_tor = []
    o_and = []
    str_to_list = []
    buf_1 = 0
    buf_2 = 0
    num = ''

    for char in checking_string:
        if char.isdigit() or char in '+-':
            check_1 = True
        else:
            check_1 = False
            break
    if check_1 == True:
        #print "Check_1: OK"
        str_1 = list(checking_string) 
        for char in checking_string:
            if char.isdigit():
                num += char
                if len(str_1) == 1:
                    o_and.append(number)
                    str_to_list.append(number)
                    num = ''
            else:
                if num != '':
                    o_and.append(num)
                    str_to_list.append(num)
                    o_tor.append(char)
                    str_to_list.append(char)
                    num = ''
                else:
                    o_tor.append(char)
                    str_to_list.append(char)
            str_1.pop(0)
        if len(o_tor) == len(o_and) or (len(o_and) - len(o_tor) == 1):
            check_2 = True
            #print "Check_2: OK"
            buf_1 = str_to_list[0]
            buf_2 = str_to_list[1]
            while str_to_list != []:
                if len(str_to_list) > 2:
                    if buf_1.isdigit() == buf_2.isdigit():
                        check_3 = False
                        print ("Wrong order of symbols!")
                        break
                    else:
                        if str_to_list != []:
                            buf_1 = buf_2
                            buf_2 = str_to_list.pop(0)
                            check_3 = True
                        else:
                            break
                else:
                    if buf_1.isdigit() == True and buf_2.isdigit() == False:
                        check_3 = False
                        print ("Wrong order of symbols!")
                        break
                    else:
                        check_3 = True
                        str_to_list = []
            #if check_3 == True:
                #print "Check_3: OK"
        else:
            print ("Wrong number of operators or operands!")
    else:
        print ("Wrong symbol!")
    return check_1 * check_2 * check_3

#Help and Exit
#print ("For help enter '-h' or '--help'. For exit enter '-e', '--exit'.")

#input_str = sys.stdin.readline()[:-1]

while input_str != '-e' or input_str != '--exit':
    while True:
        char = sys.stdin.read(1)
        if char == '\n':
            break
        elif char == '':
            break
        else:
            input_str += char
    if input_str == '-e' or input_str == '--exit':
        exit(0)
    elif input_str == '-h' or input_str == '--help':
        print ("---------------------------------H-E-L-P-----------------------------------------")
        print ("1. Enter the expression in format: +/- A +/- B +/- ... +/- Z")
        print ("2. Use only '-' and '+' operators")
        print ("3. To exit enter '-e' or '--exit'")
        print (" --------------------------------------------------------------------------------")
        continue
    elif input_str == '':
        break
    else:
        processed_str = InStr_proc(input_str).processor()
        processed_list = list(processed_str)
        operators = Queue()
        o_perands = Queue()
        for i in processed_str:
            if i in '+-':
                operators.enqueue(i)
                if number != '':
                    o_perands.enqueue(number)
                    number = ''
            elif i.isdigit() and len(processed_list) == 1:
                number += i
                o_perands.enqueue(number)
                number = ''
            else:
                number += i
            processed_list.pop(0)

#Calculating:
        if operators.size() == 1 and o_perands.isEmpty() is True:
            res = ''
            print (res)
        elif o_perands.size() == 1 and operators.isEmpty() is True:
            res += int(o_perands.dequeue())
            print (res)
        else:
            if check_input(processed_str) == 1:
                if operators.peek() == '-' and operators.size() == o_perands.size():
                    res -= int(o_perands.dequeue())
                    operators.dequeue()
                elif operators.peek() == '+' and operators.size() == o_perands.size():
                    res += int(o_perands.dequeue())
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
                print (res)
            else:
                break
#Prepare to a new cycle iteration        
        operators = []
        o_perands = []
        res = 0
        number = ''
        input_str = ''
