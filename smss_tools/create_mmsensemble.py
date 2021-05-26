#!/usr/bin/env python
# -*-coding: utf-8 -*-

#create_mmsensemble.py
#Mohammad Saleheen
#CREATED: 12-20-2020

import sys

if len(sys.argv) != 2:
    print('''
    Please provide the input SMSS_MATCH filename that contains
    the matching coordinates between cluster, poscar, and mm atoms,
    in that order, as an argument.
    ''')
    exit()

ifile = sys.argv[1]
ofile = 'MMS_ENSEMBLE'

fwand = open(ofile, 'w')
fwand.write('$MMS_SHIFTS\n')
shift = 0
with open(ifile, 'r') as frand:
    dummy_head = frand.readline()
    for line in frand:
        clusterid, poscarid, mmid = line.split()
        fwand.write('\t{}\t{}\t{:0.14f}\t{:0.14f}\t{:0.14f}\n'.format(clusterid, mmid, shift, shift, shift))
fwand.close()
