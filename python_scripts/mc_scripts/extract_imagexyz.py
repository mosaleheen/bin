#!/usr/bin/env python
# -*-coding: utf-8 -*-
 
#extract_imagexyz.py
#Mohammad Saleheen
#CREATED: 11-05-2020 

import sys

if len(sys.argv) != 4:
    print('Number of arguments provided: ', len(sys.argv))
    print('''
    Please provide the relocated xyz file of MC calculation, the 
    nth mc step geometry to be extracted, and total number of geometries
    to be extracted from that point on as arguments, in that order.
    For example, using 1000000 100 as arguments would extract 1000000th
    step geometry and the next 99 geometries. One can use 1 as the
    second argument to extract only the nth geometry.
    ''')
    exit()
    
ifile = sys.argv[1]
extraction_step = sys.argv[2]
steps_to_extract = int(sys.argv[3])
if steps_to_extract <= 0:
    print('You have to specifiy a positive integer as the 3rd argument')
    exit()
ofile_extract = 'mcimage_'+ extraction_step + '_' + str(steps_to_extract) + '.xyz'

total_steps = 0
match_step = 0
with open(ifile, 'r') as frand:
    for index, line in enumerate(frand):
        if "MC_STEP" in line:
            total_steps += 1
            step_number = line.split()[1]
            if extraction_step == step_number: 
                match_step = index                     
print('Total number of MC steps: ', total_steps)
frand.close()

frand = open(ifile, 'r')
fwand = open(ofile_extract, 'w')
for i, line in enumerate(frand):
    if i==match_step-1:
        print('Extracting MC step geometry: ', extraction_step)
        step_acount=int(line.strip())
        fwand.write('{}\n'.format(str(step_acount)))
        for j in range(step_acount + 1):
            fwand.write('{}\n'.format(frand.readline().strip()))
        for k in range(steps_to_extract - 1):
            try:
                atom_count = int(frand.readline().strip())
                fwand.write('{}\n'.format(str(atom_count)))
                for l in range(atom_count + 1):
                    fwand.write('{}\n'.format(frand.readline().strip()))
            except:
                print('There are only {} steps to extract'.format(k + 1))
                break
frand.close()
fwand.close()

