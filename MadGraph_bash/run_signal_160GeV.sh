#!/bin/bash

cd /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/
rm -r Folder_commands_160GeV.sh 2> /dev/null
touch Folder_commands_160GeV.sh 2> /dev/null
echo "import model THDMSBGL -modelname" >> Folder_commands_160GeV.sh
echo "define iq = u1 u1bar d1 d1bar u2 u2bar d2 d2bar g" >> Folder_commands_160GeV.sh
echo "define j = u1 u1bar d1 d1bar u2 u2bar d2 d2bar g d3 d3bar" >> Folder_commands_160GeV.sh
echo "define l+ = e1bar e2bar" >> Folder_commands_160GeV.sh
echo "define l- = e1 e2" >> Folder_commands_160GeV.sh
echo "generate iq iq > ah2 h2, (ah2 > j j), (h2 > ah2 z, ah2 > j j, z > l+ l-)" >> Folder_commands_160GeV.sh
echo "output /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/160GeV" >> Folder_commands_160GeV.sh
echo "exit" >> Folder_commands_160GeV.sh


rm -r Production_commands_160GeV.sh 2> /dev/null
touch Production_commands_160GeV.sh 2> /dev/null
echo "#!/bin/bash" >> Production_commands_160GeV.sh
echo " " >> Production_commands_160GeV.sh
echo "cd /home/felipe/MG5_aMC_v2_7_2_py3" >> Production_commands_160GeV.sh
echo "/home/felipe/MG5_aMC_v2_7_2_py3/bin/mg5_aMC /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/Folder_commands_160GeV.sh" >> Production_commands_160GeV.sh
echo " " >> Production_commands_160GeV.sh
echo "cd /home/felipe/MG5_aMC_v2_7_2_py3" >> Production_commands_160GeV.sh
echo "/home/felipe/MG5_aMC_v2_7_2_py3/bin/mg5_aMC /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/Scan_commands_160GeV.sh" >> Production_commands_160GeV.sh
echo "cd /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/160GeV/bin" >> Production_commands_160GeV.sh
echo "./cleanall" >> Production_commands_160GeV.sh


#Ten samples with 100k events each ---> 1M total
rm -r Scan_commands_160GeV.sh 2> /dev/null
touch Scan_commands_160GeV.sh 2> /dev/null
echo "!cp /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/160GeV/Cards/pythia8_card_default.dat /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/160GeV/Cards/pythia8_card.dat" >> Scan_commands_160GeV.sh
echo "!cp /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/160GeV/Cards/delphes_card_ATLAS.dat /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/160GeV/Cards/delphes_card.dat" >> Scan_commands_160GeV.sh
echo "launch /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/160GeV" >> Scan_commands_160GeV.sh
echo "set nevents 100000" >> Scan_commands_160GeV.sh
echo "set ebeam1 7000" >> Scan_commands_160GeV.sh
echo "set ebeam2 7000" >> Scan_commands_160GeV.sh
echo "/media/felipe/EXTERNAL_USB/1-BGL-ML_roots/restrict_default_160GeV.dat" >> Scan_commands_160GeV.sh
echo "exit" >> Scan_commands_160GeV.sh
echo "!cd /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/160GeV/Events/run_01" >> Scan_commands_160GeV.sh
echo "!find . -name \"*.hepmc.gz\" -type f -delete" >> Scan_commands_160GeV.sh
echo "!find . -name \"*.hepmc\" -type f -delete" >> Scan_commands_160GeV.sh
echo "!File=\$(find . -name \"*.root\" -type f)" >> Scan_commands_160GeV.sh
echo "!mv \$File Signal_160_1.root" >> Scan_commands_160GeV.sh
echo "launch /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/160GeV" >> Scan_commands_160GeV.sh
echo "set nevents 100000" >> Scan_commands_160GeV.sh
echo "set ebeam1 7000" >> Scan_commands_160GeV.sh
echo "set ebeam2 7000" >> Scan_commands_160GeV.sh
echo "exit" >> Scan_commands_160GeV.sh
echo "!cd /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/160GeV/Events/run_02" >> Scan_commands_160GeV.sh
echo "!find . -name \"*.hepmc.gz\" -type f -delete" >> Scan_commands_160GeV.sh
echo "!find . -name \"*.hepmc\" -type f -delete" >> Scan_commands_160GeV.sh
echo "!File=\$(find . -name \"*.root\" -type f)" >> Scan_commands_160GeV.sh
echo "!mv \$File Signal_160_2.root" >> Scan_commands_160GeV.sh
echo "launch /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/160GeV" >> Scan_commands_160GeV.sh
echo "set nevents 100000" >> Scan_commands_160GeV.sh
echo "set ebeam1 7000" >> Scan_commands_160GeV.sh
echo "set ebeam2 7000" >> Scan_commands_160GeV.sh
echo "exit" >> Scan_commands_160GeV.sh
echo "!cd /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/160GeV/Events/run_03" >> Scan_commands_160GeV.sh
echo "!find . -name \"*.hepmc.gz\" -type f -delete" >> Scan_commands_160GeV.sh
echo "!find . -name \"*.hepmc\" -type f -delete" >> Scan_commands_160GeV.sh
echo "!File=\$(find . -name \"*.root\" -type f)" >> Scan_commands_160GeV.sh
echo "!mv \$File Signal_160_3.root" >> Scan_commands_160GeV.sh
echo "launch /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/160GeV" >> Scan_commands_160GeV.sh
echo "set nevents 100000" >> Scan_commands_160GeV.sh
echo "set ebeam1 7000" >> Scan_commands_160GeV.sh
echo "set ebeam2 7000" >> Scan_commands_160GeV.sh
echo "exit" >> Scan_commands_160GeV.sh
echo "!cd /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/160GeV/Events/run_04" >> Scan_commands_160GeV.sh
echo "!find . -name \"*.hepmc.gz\" -type f -delete" >> Scan_commands_160GeV.sh
echo "!find . -name \"*.hepmc\" -type f -delete" >> Scan_commands_160GeV.sh
echo "!File=\$(find . -name \"*.root\" -type f)" >> Scan_commands_160GeV.sh
echo "!mv \$File Signal_160_4.root" >> Scan_commands_160GeV.sh
echo "launch /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/160GeV" >> Scan_commands_160GeV.sh
echo "set nevents 100000" >> Scan_commands_160GeV.sh
echo "set ebeam1 7000" >> Scan_commands_160GeV.sh
echo "set ebeam2 7000" >> Scan_commands_160GeV.sh
echo "exit" >> Scan_commands_160GeV.sh
echo "!cd /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/160GeV/Events/run_05" >> Scan_commands_160GeV.sh
echo "!find . -name \"*.hepmc.gz\" -type f -delete" >> Scan_commands_160GeV.sh
echo "!find . -name \"*.hepmc\" -type f -delete" >> Scan_commands_160GeV.sh
echo "!File=\$(find . -name \"*.root\" -type f)" >> Scan_commands_160GeV.sh
echo "!mv \$File Signal_160_5.root" >> Scan_commands_160GeV.sh
echo "launch /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/160GeV" >> Scan_commands_160GeV.sh
echo "set nevents 100000" >> Scan_commands_160GeV.sh
echo "set ebeam1 7000" >> Scan_commands_160GeV.sh
echo "set ebeam2 7000" >> Scan_commands_160GeV.sh
echo "exit" >> Scan_commands_160GeV.sh
echo "!cd /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/160GeV/Events/run_06" >> Scan_commands_160GeV.sh
echo "!find . -name \"*.hepmc.gz\" -type f -delete" >> Scan_commands_160GeV.sh
echo "!find . -name \"*.hepmc\" -type f -delete" >> Scan_commands_160GeV.sh
echo "!File=\$(find . -name \"*.root\" -type f)" >> Scan_commands_160GeV.sh
echo "!mv \$File Signal_160_6.root" >> Scan_commands_160GeV.sh
echo "launch /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/160GeV" >> Scan_commands_160GeV.sh
echo "set nevents 100000" >> Scan_commands_160GeV.sh
echo "set ebeam1 7000" >> Scan_commands_160GeV.sh
echo "set ebeam2 7000" >> Scan_commands_160GeV.sh
echo "exit" >> Scan_commands_160GeV.sh
echo "!cd /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/160GeV/Events/run_07" >> Scan_commands_160GeV.sh
echo "!find . -name \"*.hepmc.gz\" -type f -delete" >> Scan_commands_160GeV.sh
echo "!find . -name \"*.hepmc\" -type f -delete" >> Scan_commands_160GeV.sh
echo "!File=\$(find . -name \"*.root\" -type f)" >> Scan_commands_160GeV.sh
echo "!mv \$File Signal_160_7.root" >> Scan_commands_160GeV.sh
echo "launch /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/160GeV" >> Scan_commands_160GeV.sh
echo "set nevents 100000" >> Scan_commands_160GeV.sh
echo "set ebeam1 7000" >> Scan_commands_160GeV.sh
echo "set ebeam2 7000" >> Scan_commands_160GeV.sh
echo "exit" >> Scan_commands_160GeV.sh
echo "!cd /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/160GeV/Events/run_08" >> Scan_commands_160GeV.sh
echo "!find . -name \"*.hepmc.gz\" -type f -delete" >> Scan_commands_160GeV.sh
echo "!find . -name \"*.hepmc\" -type f -delete" >> Scan_commands_160GeV.sh
echo "!File=\$(find . -name \"*.root\" -type f)" >> Scan_commands_160GeV.sh
echo "!mv \$File Signal_160_8.root" >> Scan_commands_160GeV.sh
echo "launch /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/160GeV" >> Scan_commands_160GeV.sh
echo "set nevents 100000" >> Scan_commands_160GeV.sh
echo "set ebeam1 7000" >> Scan_commands_160GeV.sh
echo "set ebeam2 7000" >> Scan_commands_160GeV.sh
echo "exit" >> Scan_commands_160GeV.sh
echo "!cd /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/160GeV/Events/run_09" >> Scan_commands_160GeV.sh
echo "!find . -name \"*.hepmc.gz\" -type f -delete" >> Scan_commands_160GeV.sh
echo "!find . -name \"*.hepmc\" -type f -delete" >> Scan_commands_160GeV.sh
echo "!File=\$(find . -name \"*.root\" -type f)" >> Scan_commands_160GeV.sh
echo "!mv \$File Signal_160_9.root" >> Scan_commands_160GeV.sh
echo "launch /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/160GeV" >> Scan_commands_160GeV.sh
echo "set nevents 100000" >> Scan_commands_160GeV.sh
echo "set ebeam1 7000" >> Scan_commands_160GeV.sh
echo "set ebeam2 7000" >> Scan_commands_160GeV.sh
echo "exit" >> Scan_commands_160GeV.sh
echo "!cd /media/felipe/EXTERNAL_USB/1-BGL-ML_roots/160GeV/Events/run_10" >> Scan_commands_160GeV.sh
echo "!find . -name \"*.hepmc.gz\" -type f -delete" >> Scan_commands_160GeV.sh
echo "!find . -name \"*.hepmc\" -type f -delete" >> Scan_commands_160GeV.sh
echo "!File=\$(find . -name \"*.root\" -type f)" >> Scan_commands_160GeV.sh
echo "!mv \$File Signal_160_10.root" >> Scan_commands_160GeV.sh


rm -r Submit_job_160GeV.sh 2> /dev/null
touch Submit_job_160GeV.sh 2> /dev/null
echo "#!/bin/bash" >> Submit_job_160GeV.sh
echo " " >> Submit_job_160GeV.sh
echo "cd /media/felipe/EXTERNAL_USB/1-BGL-ML_roots" >> Submit_job_160GeV.sh 
echo "chmod +x Folder_commands_160GeV.sh Production_commands_160GeV.sh Scan_commands_160GeV.sh" >> Submit_job_160GeV.sh 
echo "./Production_commands_160GeV.sh" >> Submit_job_160GeV.sh 


chmod +x Submit_job_160GeV.sh
./Submit_job_160GeV.sh

