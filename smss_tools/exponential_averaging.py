#!/usr/bin/env python
# -*-coding: utf-8 -*-

#exponential_averaging.py
#Mohammad Saleheen
#CREATED: 12-21-2020
#Comments: 
# zwanzig equation works as -kb*T*ln<exp(-(E2-E1)/kb*T)> which does not 
# exactly equate to kb*T*ln<exp(E2-E1)/kb*T)>, i.e., -ve of forward 
# exponential is not exactly equal to reverse exponential, hence, 
# reverse exponential averaging is performed separately. It should be
# kept in mind that DeltaF file contains always Ufinal - Uinitial, 
# both in forward and reverse expoential cases, due to the architecture
# of the BAR code.

import numpy as np
import sys
from constants import boltzman_ev as kb
from constants import hartree_ev  as ha_ev

if len(sys.argv) != 3:
    print('''
    Please provide the direction of exponential averaging
    (forward/reverse) and the temperature as arguments, in 
    that order.
    ''')
    exit()

direction = sys.argv[1]
temperature  = float(sys.argv[2])
ifile = 'MMS_REPLAY_Dlpoly_initial'
ffile = 'MMS_REPLAY_Dlpoly_final'
ofile_diff   = 'DeltaF'
ofile_energy = 'zwanzig_average'

# read the energies listed in MMS_REPLAY_Dlpoly_initial
energy_i = []
with open (ifile, 'r') as frand:
    for line in frand:
        if '$energy' in line:
            energy_i.append(line.split()[2])
# read the energies listed in MMS_REPLAY_Dlpoly_final
energy_f = []
with open (ffile, 'r') as frand:
    for line in frand:
        if '$energy' in line:
            energy_f.append(line.split()[2])

exponential = []
if len(energy_i) == len(energy_f):
    fwand = open(ofile_diff, 'w')
    fwand.write('\t{}\n'.format('Ufinal - Uinitial'))
    fwand.write('\t{}\n'.format('================='))
    for i in range(len(energy_i)):
        ediff = float(energy_f[i]) - float(energy_i[i])
        fwand.write('\t{:0.15f}\n'.format(ediff))
        if direction == 'forward':
            exponential.append(np.exp( - (ediff * ha_ev) / (kb * temperature)))
        elif direction == 'reverse':
            exponential.append(np.exp( (ediff * ha_ev) / (kb * temperature)))
        else:
            print('Exponential averaging directions can only be forward or reverse')
    fwand.close()
    fwand = open(ofile_energy, 'w')
    zwanzig = - kb * temperature * np.log(np.mean(exponential))
    fwand.write('{:0.18f}\n'.format(zwanzig))
else:
    print('''
    Number of energies in initial and final MMS_REPLAY files
    do not match. Please check the calculation.
    ''')
    exit()

