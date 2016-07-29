#/usr/bin/env python
#! -*- coding: utf-8 -*-
__version__ = "1.1"

from sys import stdin

input_str = stdin.readline()
res = 0
if ' ' in input_str:
    input_str = input_str.replace(' ', '')

#OPERATION_1: Addition

if input_str[0].isdigit() and '+' in input_str and input_str[2].isdigit():
    res = int(input_str[0]) + int(input_str[2])
    print res
else:
    print 'The string is not correct'
