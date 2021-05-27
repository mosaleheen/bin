#!/usr/bin/env python
# -*-coding: utf-8 -*-
 
#embedded_creator.py
#Mohammad Saleheen
#CREATED: 12-16-2020 

import sys
import os

if len(sys.argv) != 4:
    print('Number of arguments provided: ', len(sys.argv))
    print('''
    Please provide the dl_poly trajectory filename, number of
    MM metal atoms, and number of QM cluster atoms as arguments,
    in that order.
    ''')
    exit()
    
ifile = sys.argv[1]
mm_metal = int(sys.argv[2])
qm_cluster = int(sys.argv[3])
ofile = 'embedded'
zero_chg, hw_chg, om_chg = 0, 0.005564, -0.011128                           # defining the charges

fwand = open(ofile, 'w')
fwand.write('{}\n{}\n{}\n'.format('$embed', '  periodic  3', '  cell  ang'))                    # writing header info in embedded file
box_angle = 90
atom_elements = set()                                                   # empty set for storing element names
with open(ifile, 'r') as frand:
    frand.readline()                                                    # dummy header
    trjkey, pbckey, natoms, nimages, nlines = [int(item) for item in frand.readline().split()]  # keys according to HISTORY file format
    startcluster_lines = (natoms - qm_cluster) * 2 + 4 + 2              # starting of cluster lines
    frand.readline()                                                    # dummy timestamp
    xbox = float(frand.readline().split()[0])
    ybox = float(frand.readline().split()[1])
    zbox = float(frand.readline().split()[2])
    fwand.write('\t{0:0.8f}  {1:0.8f}  {2:0.8f}  {3:0.4f}  {3:0.4f}  {3:0.4f}\n'.format(xbox, ybox, zbox, box_angle))
    fwand.write('{}\n'.format('  content ang'))
    for i in range(mm_metal):                                           # getting the mm metal coordinates
        atom_name = frand.readline().split()[0]
        atom_elements.add(atom_name)
        xc, yc, zc = [float(item) for item in frand.readline().split()]
        xc = xc + xbox if xc < 0 else ( xc - xbox if xc > xbox else xc)
        yc = yc + ybox if yc < 0 else ( yc - ybox if yc > ybox else yc)
        zc = zc + zbox if zc < 0 else ( zc - zbox if zc > zbox else zc)
        fwand.write('{}\t{:0.14f}\t{:0.14f}\t{:0.14f}\n'.format(atom_name, xc, yc, zc))
    for line in frand:                                                  # getting the water coordinates
        if 'Ow' in line or 'Hw' in line or 'Om' in line:
            atom_name = line.split()[0]
            atom_elements.add(atom_name)
            xc, yc, zc = [float(item) for item in frand.readline().split()]
            xc = xc + xbox if xc < 0 else ( xc - xbox if xc > xbox else xc)
            yc = yc + ybox if yc < 0 else ( yc - ybox if yc > ybox else yc)
            zc = zc + zbox if zc < 0 else ( zc - zbox if zc > zbox else zc)
            fwand.write('{}\t{:0.14f}\t{:0.14f}\t{:0.14f}\n'.format(atom_name, xc, yc, zc))
    frand.seek(0)                                                       # rewinding and getting to the start of cluster coordinates
    for line in range(startcluster_lines):
        frand.readline()
    cluster_coords = []                                                 # empty list for storing cluster coordinates
    for i in range(qm_cluster):                                         # read the cluster coordinates, add to a list, add the atom names in a set
        atom_name = frand.readline().split()[0]
        atom_elements.add(atom_name)
        xc, yc, zc = [float(item) for item in frand.readline().split()]
        xc = xc + xbox if xc < 0 else ( xc - xbox if xc > xbox else xc)
        yc = yc + ybox if yc < 0 else ( yc - ybox if yc > ybox else yc)
        zc = zc + zbox if zc < 0 else ( zc - zbox if zc > zbox else zc)
        fwand.write('{}\t{:0.14f}\t{:0.14f}\t{:0.14f}\n'.format(atom_name, xc, yc, zc))
        cluster_coords.append('{}        {:0.14f}   {:0.14f}   {:0.14f}'.format(atom_name, xc, yc, zc))
    fwand.write('{}\n{}\n{}\n'.format('  end', '...', '  charges'))
    for element in atom_elements:
        if element=='Om':
            fwand.write('    {}\t{:0.6f}\n'.format(element, om_chg))
        elif element=='Hw':
            fwand.write('    {}\t{:0.6f}\n'.format(element, hw_chg))
        else:
            fwand.write('    {}\t{:0.6f}\n'.format(element, zero_chg))
    print(atom_elements)
    fwand.write('{}\n{}\n{}\n'.format('  end', '...', '  cluster ang'))
    for item in cluster_coords:
        fwand.write('{}\n'.format(item))
    fwand.write('{}\n'.format('  end'))
fwand.close()

