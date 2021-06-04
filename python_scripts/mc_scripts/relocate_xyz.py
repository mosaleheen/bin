#!/usr/bin/env python
# -*-coding: utf-8 -*-

#relocate_xyz.py
#Mohammad Saleheen
#CREATED: 11-05-2020

import sys

if len(sys.argv) != 3:
    print('Number of arguments provided: ', len(sys.argv))
    print('''
    Please provide the xyz file of MC calculation, and the height
    of the simulation box as arguments, in that order.
    ''')
    exit()

ifile = sys.argv[1]
zbox = float(sys.argv[2])
ofile = 'geometry_relocated.out.xyz'
xbox, ybox = 33.3309, 28.8657

total_steps = 0
with open(ifile, 'r') as frand:
    for index, line in enumerate(frand):
        if "MC_STEP" in line:
            total_steps += 1
print('Total number of MC steps: ', total_steps)
frand.close()

fwand = open(ofile, 'w')
frand = open(ifile, 'r')
for i in range(total_steps):
    atom_count = int(frand.readline())
    step_count = frand.readline().strip()
    print('Working on MC Step: ', i)
    fwand.write('{}\n{}\n'.format(atom_count, step_count))
    for j in range(atom_count):
        atom, xcoord, ycoord, zcoord = frand.readline().split()
        xcoord = float(xcoord) + xbox if float(xcoord) < 0 else xcoord
        ycoord = float(ycoord) + ybox if float(ycoord) < 0 else ycoord
        zcoord = float(zcoord) + zbox if float(zcoord) < 0 else zcoord
        fwand.write('{}\t{}\t{}\t{}\n'.format(atom, xcoord, ycoord, zcoord))
frand.close()
fwand.close()

