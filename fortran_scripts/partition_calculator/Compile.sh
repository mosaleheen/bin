#! /bin/bash -x
rm *.exe
gfortran -c Constants.f90
gfortran -c PartitionProcedures.f90 
gfortran -o partition_calculator.exe PartitionMain.f90 PartitionProcedures.o Constants.o
rm *.o *.mod
