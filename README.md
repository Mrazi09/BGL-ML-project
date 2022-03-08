# BGL-ML-project
Codes and data for the BGL-ML research project, which corresponds to the paper: "Collider phenomenology of new scalars from multi-Higgs models" by myself (João Pedro Pino Gonçalves) and collaborators (António Morais, António Onofre, Pedro Ferreira, Felipe F. Freitas, Vasileios Vatellis and Roman Pasechnik). arXiv:00000.0000

**Refs**: Some references for direct searches at the LHC that were relevant for the paper

**Param_Cards_MG5**: Parameters cards to be used in MadGraph, for all 1sigma and 2sigma benchmark points 

**TMVA**: Contains the C macros to run the TMVA analysis. Contains some data inside, but the data samples are are very small and they are only meant for testing purposes !!!! In the **Data** folder, there are some .csv's with greater statistics. Requires ROOT to run. Containts do_read, which converts .txt files to ROOT tuples. Contains do_TMVA_A3_single_prod_root6, which runs the TMVA code

**Root analysis**: Contains jupyter notebooks for the analysis. A3_singleproduction.ipynb contains the main root analysis based on PyROOT (jet selection based on pT). It reads a root file generated by Delphes and extract data. It also contains some plotting codes. To_txt.ipynb contains the main code for converting .csv files into .txt files needed for the ROOT TMVA framework. There is also some plotting codes for the TMVA root output. PyROOT_JetMatching.ipynb contains the notebook here we match the jets to the original fields using only kinematic information.

**BGL_UFO_py3**: Contains the UFO files, as well as an example parameter card (restrict_default.dat) to run Monte Carlo simulations in MadGraph. Python3 version

**BGL_UFO_py3**: Contains the UFO files, as well as an example parameter card (restrict_default.dat) to run Monte Carlo simulations in MadGraph. Python2 version

**MadGraph_bash**: Contains some example scripts to run MadGraph. They are designed to run in Aveiro's local computer cluster. make_scripts_1sigma.sh contains the code to get the cross-section for each of the 1sigma points for the signal topology. Inside the Signal folder, it contains the main codes to run MadGraph+Pythia8+Delphes chain for the signal, and inside Folders_1.sh it contains the MadGraph syntax for event generation. Equivalently, inside the Z_plus_jets folder we have the codes for the Z plus jets background. The MadGraph syntax is the Folders.sh file.
There is also run_\*.sh codes which were used to simulate 1 million events for z+jets and signal. The code generated 10 samples, each with 100k events

**Data**: Contains .csv tables with the data used in the analysis. Corresponds to the events that survive the cuts from the 1M points generated.





For additional information or questions, feel free to contact me by email (jpedropino@ua.pt or johnppg5@gmail.com)
