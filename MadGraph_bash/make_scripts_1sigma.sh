#!/bin/bash
cd ./Updated_benchmarks
rm -r Folder_1sigma 2> /dev/null
mkdir Folder_1sigma 2> /dev/null

cd Folder_1sigma
mkdir Point_{1..25}



for i in {1..25}; do
cd /home/jpedropino@UA.PT/Workstation/DeepPheNo/Vasileios_Benchmarks/Updated_benchmarks/Folder_1sigma/Point_$i/
rm -r Folder_commands_$i.sh 2> /dev/null
touch Folder_commands_$i.sh 2> /dev/null
echo "import model THDMSBGL -modelname" >> Folder_commands_$i.sh
echo "define iq = u1 u1bar d1 d1bar u2 u2bar d2 d2bar g" >> Folder_commands_$i.sh
echo "define j = u1 u1bar d1 d1bar u2 u2bar d2 d2bar g d3 d3bar" >> Folder_commands_$i.sh
echo "define l+ = e1 e2bar" >> Folder_commands_$i.sh
echo "define l- = e1 e2" >> Folder_commands_$i.sh
echo "generate iq iq > ah2 h2, (ah2 > j j), (h2 > ah2 z, ah2 > j j, z > l+ l-)" >> Folder_commands_$i.sh
echo "output /home/jpedropino@UA.PT/Workstation/MadGraph/MG5_aMC_v2_7_0/2-Signal-1sigma/ah3_$i " >> Folder_commands_$i.sh
echo "exit" >> Folder_commands_$i.sh
done



for i in {1..25}; do
cd /home/jpedropino@UA.PT/Workstation/DeepPheNo/Vasileios_Benchmarks/Updated_benchmarks/Folder_1sigma/Point_$i/
rm -r Production_commands_$i.sh 2> /dev/null
touch Production_commands_$i.sh 2> /dev/null
echo "#!/bin/bash" >> Production_commands_$i.sh
echo " " >> Production_commands_$i.sh
echo "#SBATCH -n 1" >> Production_commands_$i.sh
echo "#SBATCH --cpus-per-task=1" >> Production_commands_$i.sh
echo "#SBATCH --time=9-00:00:00" >> Production_commands_$i.sh
echo "#SBATCH --mem-per-cpu=5500mb" >> Production_commands_$i.sh
echo "#SBATCH --mail-type=ALL" >> Production_commands_$i.sh
echo "#SBATCH --mail-user=jpedropino@ua.pt" >> Production_commands_$i.sh  
echo " " >> Production_commands_$i.sh
echo "cd /home/jpedropino@UA.PT/Workstation/MadGraph/MG5_aMC_v2_7_0" >> Production_commands_$i.sh
echo "/home/jpedropino@UA.PT/Workstation/MadGraph/MG5_aMC_v2_7_0/bin/mg5_aMC /home/jpedropino@UA.PT/Workstation/DeepPheNo/Vasileios_Benchmarks/Updated_benchmarks/Folder_1sigma/Point_$i/Folder_commands_$i.sh 
" >> Production_commands_$i.sh
echo " " >> Production_commands_$i.sh
echo "cd /home/jpedropino@UA.PT/Workstation/MadGraph/MG5_aMC_v2_7_0" >> Production_commands_$i.sh
echo "/home/jpedropino@UA.PT/Workstation/MadGraph/MG5_aMC_v2_7_0/bin/mg5_aMC /home/jpedropino@UA.PT/Workstation/DeepPheNo/Vasileios_Benchmarks/Updated_benchmarks/Folder_1sigma/Point_$i/Scan_commands_$i.sh " >> Production_commands_$i.sh
echo "cd /home/jpedropino@UA.PT/Workstation/MadGraph/MG5_aMC_v2_7_0/2-Signal-1sigma/ah3_$i/bin" >> Production_commands_$i.sh
echo "./cleanall" >> Production_commands_$i.sh
done



for i in {1..25}; do
cd /home/jpedropino@UA.PT/Workstation/DeepPheNo/Vasileios_Benchmarks/Updated_benchmarks/Folder_1sigma/Point_$i/
rm -r Scan_commands_$i.sh 2> /dev/null
touch Scan_commands_$i.sh 2> /dev/null
echo "import model THDMSBGL -modelname" >> Scan_commands_$i.sh
echo "launch 2-Signal-1sigma/ah3_$i" >> Scan_commands_$i.sh
echo "set nevents 1000" >> Scan_commands_$i.sh
echo "set ebeam1 7000" >> Scan_commands_$i.sh
echo "set ebeam2 7000" >> Scan_commands_$i.sh
echo "/home/jpedropino@UA.PT/Workstation/DeepPheNo/Vasileios_Benchmarks/Updated_benchmarks/1sigma/restrict_default_$i.dat" >> Scan_commands_$i.sh
done



for i in {1..25}; do
cd /home/jpedropino@UA.PT/Workstation/DeepPheNo/Vasileios_Benchmarks/Updated_benchmarks/Folder_1sigma/Point_$i/
rm -r Submit_job_$i.sh 2> /dev/null
touch Submit_job_$i.sh 2> /dev/null
echo "#!/bin/bash" >> Submit_job_$i.sh
echo " " >> Submit_job_$i.sh
echo "#SBATCH -n 1" >> Submit_job_$i.sh 
echo "#SBATCH --cpus-per-task=1" >> Submit_job_$i.sh 
echo "#SBATCH --time=9-00:00:00" >> Submit_job_$i.sh 
echo "#SBATCH --mem-per-cpu=5500mb" >> Submit_job_$i.sh 
echo "#SBATCH --mail-type=ALL" >> Submit_job_$i.sh
echo "#SBATCH --mail-user=jpedropino@ua.pt" >> Submit_job_$i.sh  
echo " " >> Submit_job_$i.sh
echo "cd /home/jpedropino@UA.PT/Workstation/DeepPheNo/Vasileios_Benchmarks/Updated_benchmarks/Folder_1sigma/Point_$i" >> Submit_job_$i.sh 
echo "chmod +x Folder_commands_$i.sh Production_commands_$i.sh Scan_commands_$i.sh" >> Submit_job_$i.sh 
echo "sbatch ./Production_commands_$i.sh" >> Submit_job_$i.sh 
done



for i in {1..25}; do
cd /home/jpedropino@UA.PT/Workstation/DeepPheNo/Vasileios_Benchmarks/Updated_benchmarks/Folder_1sigma/Point_$i/
chmod +x Submit_job_$i.sh
./Submit_job_$i.sh
done





















