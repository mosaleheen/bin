#! /bin/bash -x

rm *.exe
gfortran -c Constants.f90
gfortran -c BARProcedures.f90 
gfortran -o bar_calculator.exe BARMain.f90 BARProcedures.o Constants.o
rm *.o *.mod
