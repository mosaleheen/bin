#! /bin/bash -x
rm *.o *.mod *.exe
gfortran -c ConfidenceProcedures.f90
gfortran -o confidence_calculator.exe ConfidenceMain.f90 ConfidenceProcedures.o 
rm *.o *.mod
