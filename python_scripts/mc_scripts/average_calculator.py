#!/usr/bin/env python
# -*-coding: utf-8 -*-

#average_calculator.py
#Mohammad Saleheen
#CREATED: 11-19-2020
import numpy as np
import sys

if len(sys.argv) != 2:
    print('Number of arguments provided: ', len(sys.argv))
    print('''
    Please provide input property filename to calculate 
    property average.
    ''')
    exit()
infile = sys.argv[1]
prop = []
with open (infile, 'r') as frand:
    for line in frand:
        prop.append(float(line))
print('{:0.4f}'.format(np.mean(prop)))
