#/usr/bin/env python
#! -*- coding: utf-8 -*-
from sys import stdin

'''This program allows you to calculate the sum of two integers'''

input_str = stdin.readline()
res = 0
if ' ' in input_str:
    input_str = input_str.replace(' ', '')

#OPERATION_1: Addition

if input_str[0].isdigit() and '+' in input_str and input_str[2].isdigit():
    res = int(input_str[0]) + int(input_str[2])
    print 'The sum is equal:', res
else:
    print 'The string is not correct'
