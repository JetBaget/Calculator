#/usr/bin/env python
#! -*- coding: utf-8 -*-
from sys import stdin

'''This program allows you to calculate the sum of two integers'''

input_str = stdin.read()
res = 0

#OPERATION_1: Addition

split_input_str = input_str.split()

if split_input_str[0].isdigit() and split_input_str[1] == '+'\
 and split_input_str[2].isdigit():
    res = int(split_input_str[0]) + int(split_input_str[2])
    print 'The sum is equal:', res
else:
    print 'The string is not correct'
