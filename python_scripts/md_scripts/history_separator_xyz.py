#!/usr/bin/env python
# -*-coding: utf-8 -*-

#history_separator_xyz.py
#Mohammad Saleheen
#CREATED: 12-16-2020

import sys

if len(sys.argv) != 2:
    print('Number of arguments provided: ', len(sys.argv))
    print('''
    Please provide the dl_poly trajectory filename as argument.
    ''')
    exit()

ifile = sys.argv[1]

with open(ifile, 'r') as frand:
    frand.readline()                                                    # dummy header
    trjkey, pbckey, natoms, nimages, nlines = [int(item) for item in frand.readline().split()]  # keys accroding to HISTORY file writing
    for image in range(nimages):                                        # loop thorugh conformations
        index = str(image + 1).rjust(5,'0')                             # formatting file index for writing with 0 padding
        ofile = 'image-' + index
        fwand = open(ofile, 'w')
        fwand.write('{}\n'.format(natoms))
        timestamp, time = frand.readline().split()[0:2]
        fwand.write('{}\t{}\n'.format(timestamp, time))
        xbox = float(frand.readline().split()[0])
        ybox = float(frand.readline().split()[1])
        zbox = float(frand.readline().split()[2])
        for line in range(natoms):                                   # loop through atoms
            atom_name = frand.readline().split()[0]
            xc, yc, zc = [float(item) for item in frand.readline().split()]
            xc = xc + xbox if xc < 0 else ( xc - xbox if xc > xbox else xc)
            yc = yc + ybox if yc < 0 else ( yc - ybox if yc > ybox else yc)
            zc = zc + zbox if zc < 0 else ( zc - zbox if zc > zbox else zc)
            fwand.write('{}\t{:0.14f}\t{:0.14f}\t{:0.14f}\n'.format(atom_name, xc, yc, zc))
        fwand.close()

