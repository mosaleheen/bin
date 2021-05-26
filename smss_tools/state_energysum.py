#!/usr/bin/env python
# -*-coding: utf-8 -*-
 
#state_energysum.py
#Mohammad Saleheen
#CREATED: 12-16-2020 
#calculate total energy of states

import sys
import os

if len(sys.argv) != 4:
    print('Number of arguments provided: ', len(sys.argv))
    print('''
    Please provide the path to the energy files from peecm, turbomole, and the 
    meanfield dlpoly calculation as arguments, in that order. For example, path
    to peecm energy file can be 01_peecm/energy.
    ''')
    exit()

ifile_peecm = sys.argv[1]
ifile_turbo = sys.argv[2]
ifile_poly  = sys.argv[3]
ofile = 'state_energy'

fwand = open(ofile, 'w')
if os.path.exists(ifile_peecm):
    with open(ifile_peecm, 'r') as frand:
        dummy = frand.readline()
        scf_peecm = float(frand.readline().split()[1]) 
if os.path.exists(ifile_turbo): 
    with open(ifile_turbo, 'r') as frand:
        dummy = frand.readline()
        scf_turbo = float(frand.readline().split()[1])
if os.path.exists(ifile_poly):
    with open(ifile_poly, 'r') as frand:
        meanfield_dlpoly = float(frand.readline())
state_energy = scf_peecm - scf_turbo + meanfield_dlpoly
fwand.write('{:0.15f}\n'.format(state_energy))
fwand.close()
