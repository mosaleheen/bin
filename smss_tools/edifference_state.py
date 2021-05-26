#!/usr/bin/env python
# -*-coding: utf-8 -*-
 
#ediff_states.py
#Mohammad Saleheen
#CREATED: 12-16-2020 
#Purpose: calculate the energy difference between the two state

import sys
import os
from constants import hartree_ev as ha_to_ev

if len(sys.argv) != 3:
    print('Number of arguments provided: ', len(sys.argv))
    print('''
    Please provide the path to the state energy files for both state II and  
    state III as arguments, in that order.
    ''')
    exit()

ifile_stateii = sys.argv[1]
ifile_stateiii = sys.argv[2]
ofile = 'ediff_stateii_iii'

fwand = open(ofile, 'w')
if os.path.exists(ifile_stateii):
    with open(ifile_stateii, 'r') as frand:
        stateii_energy = float(frand.readline()) 
if os.path.exists(ifile_stateiii): 
    with open(ifile_stateiii, 'r') as frand:
        stateiii_energy = float(frand.readline())
diff_energy = (stateiii_energy - stateii_energy) * ha_to_ev
fwand.write('{:0.15f}\n'.format(diff_energy))
fwand.close()
