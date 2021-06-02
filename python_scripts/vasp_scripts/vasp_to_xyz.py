#!/usr/bin/env python     
# -*-coding: utf-8 -*-
 
#vasp_to_xyz.py
#Mohammad Saleheen
#CREATED: 11-19-2020
import sys

if len(sys.argv) != 2:
    print('Number of arguments provided: ', len(sys.argv))
    print('''
        Please provide the name of the VASP coordinate file, number of
        different types of atoms as an argument, in that order.
        For example, if you have benzene adsorbed on a Pt surface, the 
        argument will be 3.
        ''')
    exit()

ifile = sys.argv[1]
type_atoms = int(sys.argv[2])
ofile = 'output.xyz'
atom_name= []
atom_count=[]

frand = open(ifile, 'r')
fwand = open(ofile, 'w')
head = frand.readline()                                                 #dummy header line
frand.readline()                                                        #dummy
xbox = float(frand.readline().split()[0])
ybox = float(frand.readline().split()[1])
zbox = float(frand.readline().split()[2])

atom_specifier_line = frand.readline()
for i in range(type_atoms):
    atom_name.append(atom_specifier_line.split()[i])

atom_count_line = frand.readline()
for i in range(type_atoms):
    atom_count.append(int(atom_count_line.split()[i]))

catalyst, atom_1, atom_2, atom_3 = frand.readline().split()
nmetal, ncarbon, noxygen, nhydrogen = frand.readline().split()

total_atoms = sum(atom_count)
frand.readline()                                                        #dummy
frand.readline()                                                        #dummy
fwand.write('{}\n'.format(str(total_atoms)))
fwand.write('{}\n'.format(head))


for i in range(int(nmetal)):
    xc, yc, zc, relax_x, relax_y, relax_z = frand.readline().split()
    xc = float(xc) * xbox
    yc = float(yc) * ybox
    zc = float(zc) * zbox
    fwand.write('{}\t{:0.8f}\t{:0.8f}\t{:0.8f}\n'.format('Pd', xc, yc, zc))
for i in range(int(ncarbon)):
    xc, yc, zc, relax_x, relax_y, relax_z = frand.readline().split()
    xc = float(xc) * xbox
    yc = float(yc) * ybox
    zc = float(zc) * zbox
    fwand.write('{}\t{:0.8f}\t{:0.8f}\t{:0.8f}\n'.format(atom_1, xc, yc, zc))
for i in range(int(noxygen)):
    xc, yc, zc, relax_x, relax_y, relax_z = frand.readline().split()
    xc = float(xc) * xbox
    yc = float(yc) * ybox
    zc = float(zc) * zbox
    fwand.write('{}\t{:0.8f}\t{:0.8f}\t{:0.8f}\n'.format(atom_2, xc, yc, zc))
for i in range(int(nhydrogen)):
    xc, yc, zc, relax_x, relax_y, relax_z = frand.readline().split()
    xc = float(xc) * xbox
    yc = float(yc) * ybox
    zc = float(zc) * zbox
    fwand.write('{}\t{:0.8f}\t{:0.8f}\t{:0.8f}\n'.format(atom_3, xc, yc, zc))
frand.close()
fwand.close()
