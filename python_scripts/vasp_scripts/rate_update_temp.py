#!/usr/bin/env python
# -*-coding: utf-8 -*-
#Mohammad Saleheen
#CREATED: 11-02-2020

# The purpose of this code is to update the temperature dependent rate constants
# in the MATLAB model ode and function file. Doing this manually is annoying
# and error prone.

import sys
import os
import glob

ifile_ode = 'ODEGua_Pt.m'                       # input ode file
ofile_ode = 'new_ode.m'                         # output ode file
ifile_func = 'Guaiacol_Pt.m'                    # input function file
ofile_func = 'new_function.m'                   # output function file

if len(sys.argv) != 2:
    print('Number of arguments provided: ', len(sys.argv))
    print('''
    Please provide the number of forward or reverse rate constants 
    as an argument. You have to change the name of the input files
    within the code if you need to.
            ''')
    exit()

rate_constants = int(sys.argv[1])               # provide the number of rate constants for the reaction mechanism
fwd_file = glob.glob('kf*')[0]                  # this assumes the forward rate constants are listed in filename that starts with kf*
rev_file = glob.glob('kr*')[0]                  # reverse rate constants listed in file kb*

with open(fwd_file,'r') as fw_read:
    fcons_lines = fw_read.readlines()           # store the forward rate constants
with open(rev_file,'r') as fr_read:
    rcons_lines = fr_read.readlines()           # store the reverse rate constants

fwand = open(ofile_ode,'w')                     # replace the rate constants of model ode file with the.. 
with open(ifile_ode,'r') as frand:              # temperature updated rate constants
    for line in frand:
        for j in range(rate_constants+1):
            data_f = 'k'+str(j)+'f'+'='
            data_b = 'k'+str(j)+'b'+'='
            if data_f in line:
                line = line.replace(line.split()[1],fcons_lines[j-1].strip())
                break
            if data_b in line:
                line = line.replace(line.split()[1],rcons_lines[j-1].strip())
                break
        fwand.write(line)
fwand.close()

fwand = open(ofile_func,'w')                    # replace the rate constants of model function file with the ...=
with open(ifile_func,'r') as frand:             # temperature updated rate constants                                   
    for line in frand:                                                       
        for j in range(rate_constants+1):                                     
            data_f = 'k'+str(j)+'f'+'='                                       
            data_b = 'k'+str(j)+'b'+'='                                       
            if data_f in line:                                                
                line = line.replace(line.split()[1],fcons_lines[j-1].strip()) 
                break                                                         
            if data_b in line:                                                
                line = line.replace(line.split()[1],rcons_lines[j-1].strip()) 
                break                                                         
        fwand.write(line)                                                      
fwand.close()                                                                                                                                  

