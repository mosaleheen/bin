#!/bin/bash -x

dlpoly-extract-config-coordinates -f REVCON -k 0 -p > Extract
dlpoly-relocate-config-coordinates -f Extract > Relocate
sed -i '1,5d' Relocate
head -5 ../CONFIG > head.CONFIG
cat head.CONFIG Relocate > CONFIG
rm Extract Relocate REVCON head.CONFIG
