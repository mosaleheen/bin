#!/usr/bin/env python
# -*-coding: utf-8 -*-
 
#history_divider.py
#Mohammad Saleheen
#CREATED: 12-16-2020 

import sys

if len(sys.argv) != 4:
    print('Number of arguments provided: ', len(sys.argv))
    print('''
    Please provide the number of bins to divide the history, 
    number of images to collect in each bins, and number of
    images to skip between bins as arguments, in that order.
    ''')
    exit()

ifile = 'HISTORY'    
nbins = int(sys.argv[1])
icollect  = int(sys.argv[2])
iskip = int(sys.argv[3])

with open(ifile, 'r') as frand:
    header_line = frand.readline()                                        # header line                                          
    trjkey, pbckey, natoms, nimages, nlines = frand.readline().split()  # keys accroding to HISTORY file writing
    conflines = (int(natoms) * 2) + 4                                        # number of lines for each conformation
    collect_lines = icollect * conflines                                # number of lines to be collected
    skip_lines = iskip * conflines                                      # number of lines to be skipped
    for bins in range(nbins):
        ofile = 'HISTORY.' + str(bins + 1) 
        fwand = open(ofile, 'w')
        fwand.write(header_line)
        fwand.write('{}\t{}\t{}\t{}\t{}\n'.format(trjkey, pbckey, natoms, icollect, collect_lines+2)) # writing the header info
        for line in range(collect_lines):
            line_content = frand.readline()
            fwand.write(line_content)
        for line in range(skip_lines):
            frand.readline()
        fwand.close()

