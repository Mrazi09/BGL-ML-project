#!/bin/bash

cd /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/
rm -r Folder_commands_Zjets.sh 2> /dev/null
touch Folder_commands_Zjets.sh 2> /dev/null
echo "define j = g u c d s u~ c~ d~ s~ b b~" >> Folder_commands_Zjets.sh
echo "generate p p > z, (z > l+ l-)" >> Folder_commands_Zjets.sh
echo "add process p p > z j, (z > l+ l-)" >> Folder_commands_Zjets.sh
echo "add process p p > z j j, (z > l+ l-)" >> Folder_commands_Zjets.sh
echo "add process p p > z j j j, (z > l+ l-)" >> Folder_commands_Zjets.sh
echo "add process p p > z j j j j, (z > l+ l-)" >> Folder_commands_Zjets.sh
echo "output /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/Z_plus_jets" >> Folder_commands_Zjets.sh
echo "exit" >> Folder_commands_Zjets.sh


rm -r Production_commands_Zjets.sh 2> /dev/null
touch Production_commands_Zjets.sh 2> /dev/null
echo "#!/bin/bash" >> Production_commands_Zjets.sh
echo " " >> Production_commands_Zjets.sh
echo "cd /home/felipe/MG5_aMC_v2_7_2_py3" >> Production_commands_Zjets.sh
echo "/home/felipe/MG5_aMC_v2_7_2_py3/bin/mg5_aMC /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/Folder_commands_Zjets.sh" >> Production_commands_Zjets.sh
echo " " >> Production_commands_Zjets.sh
echo "cd /home/felipe/MG5_aMC_v2_7_2_py3" >> Production_commands_Zjets.sh
echo "/home/felipe/MG5_aMC_v2_7_2_py3/bin/mg5_aMC /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/Scan_commands_Zjets.sh" >> Production_commands_Zjets.sh
echo "cd /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/Z_plus_jets/bin" >> Production_commands_Zjets.sh
echo "./cleanall" >> Production_commands_Zjets.sh


#Ten samples with 100k events each ---> 1M total
rm -r Scan_commands_Zjets.sh 2> /dev/null
touch Scan_commands_Zjets.sh 2> /dev/null
echo "!cp /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/Z_plus_jets/Cards/pythia8_card_default.dat /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/Z_plus_jets/Cards/pythia8_card.dat" >> Scan_commands_Zjets.sh
echo "!cp /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/Z_plus_jets/Cards/delphes_card_ATLAS.dat /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/Z_plus_jets/Cards/delphes_card.dat" >> Scan_commands_Zjets.sh
echo "launch /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/Z_plus_jets" >> Scan_commands_Zjets.sh
echo "set nevents 100000" >> Scan_commands_Zjets.sh
echo "set ebeam1 7000" >> Scan_commands_Zjets.sh
echo "set ebeam2 7000" >> Scan_commands_Zjets.sh
echo "exit" >> Scan_commands_Zjets.sh
echo "!cd /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/Z_plus_jets/Events/run_01" >> Scan_commands_Zjets.sh
echo "!find . -name \"*.hepmc.gz\" -type f -delete" >> Scan_commands_Zjets.sh
echo "!find . -name \"*.hepmc\" -type f -delete" >> Scan_commands_Zjets.sh
echo "!File=\$(find . -name \"*.root\" -type f)" >> Scan_commands_Zjets.sh
echo "!mv \$File Z_plus_jets_1.root" >> Scan_commands_Zjets.sh
echo "launch /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/Z_plus_jets" >> Scan_commands_Zjets.sh
echo "set nevents 100000" >> Scan_commands_Zjets.sh
echo "set ebeam1 7000" >> Scan_commands_Zjets.sh
echo "set ebeam2 7000" >> Scan_commands_Zjets.sh
echo "exit" >> Scan_commands_Zjets.sh
echo "!cd /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/Z_plus_jets/Events/run_02" >> Scan_commands_Zjets.sh
echo "!find . -name \"*.hepmc.gz\" -type f -delete" >> Scan_commands_Zjets.sh
echo "!find . -name \"*.hepmc\" -type f -delete" >> Scan_commands_Zjets.sh
echo "!File=\$(find . -name \"*.root\" -type f)" >> Scan_commands_Zjets.sh
echo "!mv \$File Z_plus_jets_2.root" >> Scan_commands_Zjets.sh
echo "launch /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/Z_plus_jets" >> Scan_commands_Zjets.sh
echo "set nevents 100000" >> Scan_commands_Zjets.sh
echo "set ebeam1 7000" >> Scan_commands_Zjets.sh
echo "set ebeam2 7000" >> Scan_commands_Zjets.sh
echo "exit" >> Scan_commands_Zjets.sh
echo "!cd /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/Z_plus_jets/Events/run_03" >> Scan_commands_Zjets.sh
echo "!find . -name \"*.hepmc.gz\" -type f -delete" >> Scan_commands_Zjets.sh
echo "!find . -name \"*.hepmc\" -type f -delete" >> Scan_commands_Zjets.sh
echo "!File=\$(find . -name \"*.root\" -type f)" >> Scan_commands_Zjets.sh
echo "!mv \$File Z_plus_jets_3.root" >> Scan_commands_Zjets.sh
echo "launch /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/Z_plus_jets" >> Scan_commands_Zjets.sh
echo "set nevents 100000" >> Scan_commands_Zjets.sh
echo "set ebeam1 7000" >> Scan_commands_Zjets.sh
echo "set ebeam2 7000" >> Scan_commands_Zjets.sh
echo "exit" >> Scan_commands_Zjets.sh
echo "!cd /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/Z_plus_jets/Events/run_04" >> Scan_commands_Zjets.sh
echo "!find . -name \"*.hepmc.gz\" -type f -delete" >> Scan_commands_Zjets.sh
echo "!find . -name \"*.hepmc\" -type f -delete" >> Scan_commands_Zjets.sh
echo "!File=\$(find . -name \"*.root\" -type f)" >> Scan_commands_Zjets.sh
echo "!mv \$File Z_plus_jets_4.root" >> Scan_commands_Zjets.sh
echo "launch /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/Z_plus_jets" >> Scan_commands_Zjets.sh
echo "set nevents 100000" >> Scan_commands_Zjets.sh
echo "set ebeam1 7000" >> Scan_commands_Zjets.sh
echo "set ebeam2 7000" >> Scan_commands_Zjets.sh
echo "exit" >> Scan_commands_Zjets.sh
echo "!cd /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/Z_plus_jets/Events/run_05" >> Scan_commands_Zjets.sh
echo "!find . -name \"*.hepmc.gz\" -type f -delete" >> Scan_commands_Zjets.sh
echo "!find . -name \"*.hepmc\" -type f -delete" >> Scan_commands_Zjets.sh
echo "!File=\$(find . -name \"*.root\" -type f)" >> Scan_commands_Zjets.sh
echo "!mv \$File Z_plus_jets_5.root" >> Scan_commands_Zjets.sh
echo "launch /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/Z_plus_jets" >> Scan_commands_Zjets.sh
echo "set nevents 100000" >> Scan_commands_Zjets.sh
echo "set ebeam1 7000" >> Scan_commands_Zjets.sh
echo "set ebeam2 7000" >> Scan_commands_Zjets.sh
echo "exit" >> Scan_commands_Zjets.sh
echo "!cd /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/Z_plus_jets/Events/run_06" >> Scan_commands_Zjets.sh
echo "!find . -name \"*.hepmc.gz\" -type f -delete" >> Scan_commands_Zjets.sh
echo "!find . -name \"*.hepmc\" -type f -delete" >> Scan_commands_Zjets.sh
echo "!File=\$(find . -name \"*.root\" -type f)" >> Scan_commands_Zjets.sh
echo "!mv \$File Z_plus_jets_6.root" >> Scan_commands_Zjets.sh
echo "launch /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/Z_plus_jets" >> Scan_commands_Zjets.sh
echo "set nevents 100000" >> Scan_commands_Zjets.sh
echo "set ebeam1 7000" >> Scan_commands_Zjets.sh
echo "set ebeam2 7000" >> Scan_commands_Zjets.sh
echo "exit" >> Scan_commands_Zjets.sh
echo "!cd /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/Z_plus_jets/Events/run_07" >> Scan_commands_Zjets.sh
echo "!find . -name \"*.hepmc.gz\" -type f -delete" >> Scan_commands_Zjets.sh
echo "!find . -name \"*.hepmc\" -type f -delete" >> Scan_commands_Zjets.sh
echo "!File=\$(find . -name \"*.root\" -type f)" >> Scan_commands_Zjets.sh
echo "!mv \$File Z_plus_jets_7.root" >> Scan_commands_Zjets.sh
echo "launch /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/Z_plus_jets" >> Scan_commands_Zjets.sh
echo "set nevents 100000" >> Scan_commands_Zjets.sh
echo "set ebeam1 7000" >> Scan_commands_Zjets.sh
echo "set ebeam2 7000" >> Scan_commands_Zjets.sh
echo "exit" >> Scan_commands_Zjets.sh
echo "!cd /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/Z_plus_jets/Events/run_08" >> Scan_commands_Zjets.sh
echo "!find . -name \"*.hepmc.gz\" -type f -delete" >> Scan_commands_Zjets.sh
echo "!find . -name \"*.hepmc\" -type f -delete" >> Scan_commands_Zjets.sh
echo "!File=\$(find . -name \"*.root\" -type f)" >> Scan_commands_Zjets.sh
echo "!mv \$File Z_plus_jets_8.root" >> Scan_commands_Zjets.sh
echo "launch /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/Z_plus_jets" >> Scan_commands_Zjets.sh
echo "set nevents 100000" >> Scan_commands_Zjets.sh
echo "set ebeam1 7000" >> Scan_commands_Zjets.sh
echo "set ebeam2 7000" >> Scan_commands_Zjets.sh
echo "exit" >> Scan_commands_Zjets.sh
echo "!cd /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/Z_plus_jets/Events/run_09" >> Scan_commands_Zjets.sh
echo "!find . -name \"*.hepmc.gz\" -type f -delete" >> Scan_commands_Zjets.sh
echo "!find . -name \"*.hepmc\" -type f -delete" >> Scan_commands_Zjets.sh
echo "!File=\$(find . -name \"*.root\" -type f)" >> Scan_commands_Zjets.sh
echo "!mv \$File Z_plus_jets_9.root" >> Scan_commands_Zjets.sh
echo "launch /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/Z_plus_jets" >> Scan_commands_Zjets.sh
echo "set nevents 100000" >> Scan_commands_Zjets.sh
echo "set ebeam1 7000" >> Scan_commands_Zjets.sh
echo "set ebeam2 7000" >> Scan_commands_Zjets.sh
echo "exit" >> Scan_commands_Zjets.sh
echo "!cd /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/Z_plus_jets/Events/run_10" >> Scan_commands_Zjets.sh
echo "!find . -name \"*.hepmc.gz\" -type f -delete" >> Scan_commands_Zjets.sh
echo "!find . -name \"*.hepmc\" -type f -delete" >> Scan_commands_Zjets.sh
echo "!File=\$(find . -name \"*.root\" -type f)" >> Scan_commands_Zjets.sh
echo "!mv \$File Z_plus_jets_10.root" >> Scan_commands_Zjets.sh


rm -r Submit_job_Zjets.sh 2> /dev/null
touch Submit_job_Zjets.sh 2> /dev/null
echo "#!/bin/bash" >> Submit_job_Zjets.sh
echo " " >> Submit_job_Zjets.sh
echo "cd /media/felipe/EXTERNAL_USB/1-BGL-ML_roots" >> Submit_job_Zjets.sh 
echo "chmod +x Folder_commands_Zjets.sh Production_commands_Zjets.sh Scan_commands_Zjets.sh" >> Submit_job_Zjets.sh 
echo "./Production_commands_Zjets.sh" >> Submit_job_Zjets.sh 


chmod +x Submit_job_Zjets.sh
./Submit_job_Zjets.sh

