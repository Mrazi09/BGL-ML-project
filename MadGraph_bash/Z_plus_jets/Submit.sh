#!/bin/bash

#SBATCH -n 1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=10500mb
#SBATCH --mail-type=ALL
#SBATCH --mail-user=jpedropino@ua.pt

cd /home/jpedropino@UA.PT/Workstation/1-BGL-collider-project
sbatch ./Production.sh 2> /dev/null
