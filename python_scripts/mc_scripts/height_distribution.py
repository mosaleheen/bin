#!/usr/bin/env python     
# -*-coding: utf-8 -*-
 
#height_distribution.py
#Mohammad Saleheen
#CREATED: 11-09-2020

import sys
import numpy as np

if len(sys.argv) != 4:
    print('Number of arguments provided: ',len(sys.argv))
    print('''
        Please provide the relocated input xyz file, overall box height,
        and average density as arguments to the script, in that order.
        ''')
    exit()

infile = sys.argv[1]                            # input xyz file
zbox = float(sys.argv[2])                              # total box height        
avg_density = float(sys.argv[3])                       # average density
interval_size = 0.1                     
zlow = 6.9                                      # top of the catalyst surface    
zhigh = zlow + interval_size
interval_bins = int(((zbox-zlow)/0.1))          
ofile = 'normalized_height_distribution'
mc_steps = 0
with open (infile, 'r') as frand:               # counting the number of mc steps in relocated xyz file
    for line in frand:
        if 'MC_STEP' in line:
            mc_steps += 1   
print('Number of MC steps:', mc_steps)
fwand = open (ofile, 'w')                  
fwand.write ('{}\t{}\t{}\t{}\t{}\t{}\n'.format('height', '#nmol', '#avgmols', '#avgdensity', '#normalizedmols', '#densitynorm'))

nmol = [0.0]*interval_bins                      # number of water molecules (to be calculated) within each interval
zlength = [zhigh]                               # creating a list of zhigh for printing's sake

with open (infile, 'r') as frand:
    for i in range(interval_bins):
        print('Working on interval bin: ', i)
        for line in frand:
            if line.startswith('O'):
                atom, xcoord, ycoord, zcoord = line.strip().split()
                if (float(zcoord) >= zlow) and (float(zcoord) < zhigh):
                        nmol[i] = nmol[i] + 1.0
        frand.seek(0)
        zlow = round(zlow + 0.1, 2)
        zhigh = round(zhigh + 0.1, 2)
        zlength.append(zhigh)
    avgmols = [ x / float(mc_steps) for x in nmol]                      # number of water molecules within 1 conformation
    avgdensity = [ p * avg_density for p in avgmols]
    normalizedmols = [ y / np.mean(avgmols[170:270]) for y in avgmols]  # number of water molecules normalized such that middle 10 angstrom is 1.0
    densitynorm = [ z * avg_density for z in normalizedmols]            # density
for i in range(interval_bins):
    fwand.write('{}\t{:0.2f}\t{:0.2f}\t\t{:0.2f}\t\t{:0.2f}\t\t{:0.2f}\n'.format(zlength[i], nmol[i], avgmols[i], avgdensity[i], normalizedmols[i], densitynorm[i]))
fwand.close()
