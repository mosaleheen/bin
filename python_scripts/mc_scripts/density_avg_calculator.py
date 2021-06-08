#!/usr/bin/env python
# -*-coding: utf-8 -*-

#number_block_average.py
#Mohammad Saleheen
#CREATED: 10-19-2020

import sys
import numpy as np

try:
    infile = sys.argv[1]                        # specify propoerty input file as first argument
    n_blocks = int(sys.argv[2])                 # specify number of blocks for averaging as second argument
    ofile = 'density_'+str(n_blocks)+'_blocks'
    count = 0
    with open (infile, 'r') as frand:           
        for line in frand:
            count += 1
    count = count - 1                           # omitting the header lines of to count lines of property file 
    steps_in_blocks = int(count/n_blocks)     
    print('Number of steps in each block:', steps_in_blocks)
    fwand = open (ofile, 'w')                   # open the output file and header as necessary
    fwand.write ('{}\t{}\t{}\n'.format('steps', 'nmol', 'density'))
    with open (infile, 'r') as frand:
        frand.readline().strip()                # ignore the header lines
        for j in range(n_blocks):
            nmol = []
            density = []
            for k in range(steps_in_blocks):
                line = frand.readline().strip()
                steps = int(float(line.split()[0]))
                nmol.append(float(line.split()[1]))
                density.append(float(line.split()[2]))
            print('{}\t{}\t{:0.2f}\n'.format(steps, np.mean(nmol), np.mean(density)))
            fwand.write('{}\t{:0.2f}\t{:0.2f}\n'.format(steps, np.mean(nmol), np.mean(density)))
    fwand.close()
except:
    print('''
    Please provide the input file as first argument and number of blocks
    required for averaging properties as a second argument
    ''')
