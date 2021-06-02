#!/usr/bin/env python
# -*-coding: utf-8 -*-
 
#history_divider.py
#Mohammad Saleheen
#CREATED: 12-16-2020 

import sys

if len(sys.argv) != 3:
    print('Number of arguments provided: ', len(sys.argv))
    print('''
    Please provide the name of the input trajectory file and the 
    number of equidistant images to collect from the trajectory.
    ''')
    exit()

ifile = sys.argv[1]
collect_image = int(sys.argv[2])
ofile = 'HISTORY-' + str(collect_image)
fwand = open(ofile, 'w')
with open(ifile, 'r') as frand:
    header_line = frand.readline()                                        # header line                                          
    trjkey, pbckey, natoms, nimages, nlines = frand.readline().split()    # keys accroding to HISTORY file writing
    conflines = (int(natoms) * 2) + 4                                     # number of lines for each conformation
    collect_lines = collect_image * conflines + 2                         # number of lines to be collected in the new HISTORY file
    fwand.write(header_line)                                                                                               
    fwand.write('{}\t{}\t{}\t{}\t{}\n'.format(trjkey, pbckey, natoms, collect_image, collect_lines)) # writing the header info
    skip_images = int(int(nimages)/collect_image) - 1                    # -1 is to count the number of images within intervals
    skip_lines = skip_images * conflines                                  # number of lines to be skipped
    for loop in range(collect_image):
        for line in range(conflines):
            line_content = frand.readline()
            fwand.write(line_content)
        for line in range(skip_lines):
            frand.readline()
    fwand.close()

