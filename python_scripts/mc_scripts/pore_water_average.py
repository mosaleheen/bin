#!/usr/bin/env python
# -*-coding: utf-8 -*-

#number_block_average.py
#Mohammad Saleheen
#CREATED: 10-19-2020

import sys
import numpy as np

if len(sys.argv) != 3:
    print('Number of arguments provided: ', len(sys.argv))
    print('''
    Please provide input property file from MC calculation and 
    number of blocks desired for block averaging as arguments,
    in that order
            ''')
    exit()

infile = sys.argv[1]                        # specify propoerty input file as first argument
n_blocks = int(sys.argv[2])                 # specify number of blocks for averaging as second argument
ofile = 'avg_'+str(n_blocks)+'_blocks'
count = 0
with open (infile, 'r') as frand:           
    for line in frand:
        count += 1
count = count - 3                           # omitting the header lines of to count lines of property file 
steps_in_blocks = int(count/n_blocks)     
print('Number of steps in each block:', steps_in_blocks)
fwand = open (ofile, 'w')                   # open the output file and header as necessary
fwand.write ('{}\t{}\n'.format("steps","nmol"))
with open (infile, 'r') as frand:
    for i in range(3):
        frand.readline().strip()            # ignore the header lines
    for j in range(n_blocks):
        print('Working on block: ', j)
        nmol = []
        for k in range(steps_in_blocks):
            line = frand.readline()
            steps = int(float(line.split()[0]))
            nmol.append(float(line.split()[4]))
        fwand.write('{}\t{:0.2f}\n'.format(steps, np.mean(nmol)))
fwand.close()
