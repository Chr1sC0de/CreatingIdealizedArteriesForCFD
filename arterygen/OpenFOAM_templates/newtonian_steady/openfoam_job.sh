#!/bin/bash
#PBS -l ncpus=32
#PBS -l mem=64GB
#PBS -l jobfs=400GB
#PBS -l walltime=10:00:00
#PBS -l software=openFOAM
#PBS -l wd

# Unload modules.
module rm openmpi intel-cc intel-fc

# Load modules.
module load OpenFOAM/7
# decompose the case into the desired number of cores
decomposePar
mpirun simpleFoam -parallel > $PBS_JOBID.log
# reconstruct the case
reconstructPar
# now remove the processor folders to save space
rm -rf processor*