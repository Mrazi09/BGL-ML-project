#!/bin/bash
#SBATCH -n 1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=10500mb
#SBATCH --mail-type=ALL
#SBATCH --mail-user=jpedropino@ua.pt

cd /home/jpedropino@UA.PT/Workstation/MadGraph/MG5_aMC_v2_7_0
./bin/mg5_aMC /home/jpedropino@UA.PT/Workstation/1-BGL-collider-project/Folders_1.sh
cd /home/jpedropino@UA.PT/Workstation/MadGraph/MG5_aMC_v2_7_0
./bin/mg5_aMC /home/jpedropino@UA.PT/Workstation/1-BGL-collider-project/Scan_1.sh

cd /home/jpedropino@UA.PT/Workstation/MadGraph/MG5_aMC_v2_7_0/1-BGL_signal/bin
./cleanall

cd /home/jpedropino@UA.PT/Workstation/MadGraph/MG5_aMC_v2_7_0/1-BGL_signal/VLQs-SHUT/Events/run_01
find . -name "*.hepmc.gz" -type f -delete
find . -name "*.hepmc" -type f -delete
File=$(find . -name "*.root" -type f)
mv $File 1-BGL_signal.root

