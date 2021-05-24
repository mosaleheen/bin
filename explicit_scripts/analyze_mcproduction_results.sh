#!/bin/bash -x

mkdir statistics
cd statistics/
cp ../{pore.out.xyz,pore.out.prp} .

# relocate xyz
~/bin/python_scripts/mc_scripts/relocate_xyz.py pore.out.xyz 49.0

# overall box water number
~/bin/python_scripts/mc_scripts/pore_water_average.py pore.out.prp 10
mv avg_10_blocks boxwater_10b
cat boxwater_10b | tail -8 | awk -F " " '{print $2}' > boxwater_last8m

# surface density of water
~/bin/python_scripts/mc_scripts/pore_density.py geometry_relocated.out.xyz 9.0 19.0
mv water_density_pore water_density_surface
~/bin/python_scripts/mc_scripts/density_avg_calculator.py water_density_surface 10
mv density_10_blocks density_surface_10b
cat density_surface_10b | tail -8 | awk -F " " '{print $3}' > surface_last8m_density

# bulk (middle) density of water
~/bin/python_scripts/mc_scripts/pore_density.py geometry_relocated.out.xyz 24.0 34.0
mv water_density_pore water_density_bulk
~/bin/python_scripts/mc_scripts/density_avg_calculator.py water_density_bulk 10
mv density_10_blocks density_bulk_10b
cat density_bulk_10b | tail -8 | awk -F " " '{print $3}' > bulk_last8m_density
cd ../
