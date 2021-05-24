#!/bin/bash -x

mkdir first_run
mv * first_run/
mv first_run/restart .
cp first_run/{CONFIG,FIELD,HISTORY} .
cp restart/OUTPUT .
cp restart/HISTORY HISTORY-last

step=`grep timestep HISTORY | tail -1 | awk -F " " '{print $2}'`
lstep=$(($step+1000))
line=`grep -n "timestep    $lstep" HISTORY-last | awk -F ":" '{print $1}'`
sed -n "$line,$ p" HISTORY-last > test
mv test HISTORY-last
cat HISTORY-last >> HISTORY
sed -i '1,2d' HISTORY
head -2 ../../image_010/HISTORY > header
cat HISTORY >> header
mv header HISTORY

