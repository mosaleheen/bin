#!/bin/bash -x

mkdir restart/
cd restart/
cp ../* .
mv REVCON CONFIG
mv REVIVE REVOLD
sed -i "s/#restart noscale.*/restart/g" CONTROL
cd ../
