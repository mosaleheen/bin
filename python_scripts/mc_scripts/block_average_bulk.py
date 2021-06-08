#!/usr/bin/env python
# -*-coding: utf-8 -*-

#block_averaging_mc.py
#Mohammad Saleheen
#CREATED: 10-19-2020
#average bulk water density, number of mols, and pressure over specified number of blocks
#from an MC simulation output

import sys
import numpy as np

if len(sys.argv) != 5:
    print('Number of arguments provided: ', len(sys.argv))
    print('''
    Please provide the name of the output bulk property file, total
    number of MC steps performed, number of blocks over which the property
    has to be averaged, and the MC property printing interval in the 
    output property file as arguments, in that order.
    ''')
    exit()

ofile           = sys.argv[1]
total_mc_steps  = int(sys.argv[2])          # number of mc steps
n_blocks        = int(sys.argv[3])          # specify number of blocks for averaging as an argument
mc_prp_interval = int(sys.argv[4])          # number of steps skipped in mc property output
steps_in_blocks = int(total_mc_steps / (n_blocks * mc_prp_interval))

fwand = open ('blockavg_'+str(n_blocks), 'w')
fwand.write ('{}\t{}\t{}\t{}\n'.format("steps","nmol","pressure","density"))
with open (ofile, 'r') as frand:
    for i in range(4):                      # reading header lines
        frand.readline()
    for j in range(n_blocks):
        nmol = []
        pressure = []
        density = []
        for k in range(steps_in_blocks):
            line = frand.readline()
            steps = int(float(line.split()[0]))
            nmol.append(float(line.split()[3]))
            pressure.append(float(line.split()[4]))
            density.append(float(line.split()[-1]))
        fwand.write('{}\t{:0.2f}\t{:0.2f}\t{:0.2f}\n'.format(steps, np.mean(nmol), np.mean(pressure), np.mean(density)))
    fwand.close()
