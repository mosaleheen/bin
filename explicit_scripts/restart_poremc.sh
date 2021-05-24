#!/bin/bash -x

mkdir restart/
cd restart/
cp -r ../* .
sed -i "s/add_to_config.*/checkpoint pore.out.chk/g" pore.inp
sed -i "s/run.*/run 20000000/g" pore.inp
sed -i "s/equilibration.*/production  500/g" pore.inp
cd ../
