#!/usr/bin/env python
# -*-coding: utf-8 -*-

#pore_density.py
#Mohammad Saleheen
#CREATED: 11-05-2020

import sys

if len(sys.argv) != 4:
    print('Number of arguments provided: ', len(sys.argv))
    print('''
    Please provide the relocated xyz file, the lowest zlength and the
    highest z length of the box between which the density has to be
    calculated, in that order Please make sure the x and y dimensions
    of the box are correctly specified in the code.
    ''')
    exit()

ifile = sys.argv[1]
zlower_lim = float(sys.argv[2])
zupper_lim = float(sys.argv[3])
ofile = 'water_density_pore'
avogadro = 6.022140857e+23
m3to_ang3 = 1e+30
molecular_weight = 18
kiloto_standard = 1000
xbox, ybox = 33.3309, 28.8657
middle_box_volm = xbox * ybox * (zupper_lim - zlower_lim)

total_steps = 0
with open(ifile, 'r') as frand:
    for index, line in enumerate(frand):
        if "MC_STEP" in line:
            total_steps += 1

fwand = open(ofile, 'w')
fwand.write('{}\t{}\t{}\n'.format('#Step','#Water', 'Density(kg/m3)'))

frand = open(ifile, 'r')
for i in range(total_steps):
    print('Working on MC step: ', i)
    atom_count=int(frand.readline())
    step_count=frand.readline().strip().split()
    oxygen_count = 0
    for j in range(atom_count):
        line = frand.readline()
        if line.startswith('O'):
            atom, xcoord, ycoord, zcoord = line.split()
            if (float(zcoord) >= zlower_lim) and (float(zcoord) <= zupper_lim):
                oxygen_count = oxygen_count + 1
    image_density = (oxygen_count*molecular_weight*m3to_ang3)/(avogadro*kiloto_standard*middle_box_volm)
    print('{}\t  {}\t{:0.2f}'.format(step_count[1], oxygen_count, image_density))
    fwand.write('{}\t  {}\t{:0.2f}\n'.format(step_count[1], oxygen_count, image_density))
frand.close()
fwand.close()
