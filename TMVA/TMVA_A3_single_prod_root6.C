// @(#)root/tmva $Id$
/**********************************************************************************
 * Project   : TMVA - a ROOT-integrated toolkit for multivariate data analysis    *
 * Package   : TMVA                                                               *
 * Root Macro:TMVA_Combinatorial_ttH                                              *
 *                                                                                *
 * This macro provides examples for the training and testing of the               *
 * TMVA classifiers.                                                              *
 *                                                                                *
 * As input data is used a toy-MC sample consisting of four Gaussian-distributed  *
 * and linearly correlated input variables.                                       *
 *                                                                                *
 * The methods to be used can be switched on and off by means of booleans, or     *
 * via the prompt command, for example:                                           *
 *                                                                                *
 *    root -l ./TMVA_Combinatorial_ttH.C\(\"Fisher,Likelihood\"\)                 *
 *                                                                                *
 * (note that the backslashes are mandatory)                                      *
 * If no method given, a default set of classifiers is used.                      *
 *                                                                                *
 * The output file "TMVA.root" can be analysed with the use of dedicated          *
 * macros (simply say: root -l <macro.C>), which can be conveniently              *
 * invoked through a GUI that will appear at the end of the run of this macro.    *
 * Launch the GUI via the command:                                                *
 *                                                                                *
 *    root -l ./TMVAGui.C                                                         *
 *                                                                                *
 **********************************************************************************/

#include <cstdlib>
#include <iostream>
#include <map>
#include <string>
#include <vector>

#include "TChain.h"
#include "TFile.h"
#include "TTree.h"
#include "TString.h"
#include "TObjString.h"
#include "TSystem.h"
#include "TROOT.h"
// TMVA 
#include "TMVA/Tools.h"
#include "TMVA/Reader.h"
using namespace TMVA;

#include "TMVA/Factory.h"
#include "TMVA/DataLoader.h"
#include "TMVA/Tools.h"
#include "TMVA/TMVAGui.h"

void TMVA_A3_single_prod_root6( TString myMethodList = "" )
{
   // The explicit loading of the shared libTMVA is done in TMVAlogon.C, defined in .rootrc
   // if you use your private .rootrc, or run from a different directory, please copy the
   // corresponding lines from .rootrc

   // methods to be processed can be given as an argument; use format:
   //
   // mylinux~> root -l TMVA_Combinatorial_ttH.C\(\"myMethod1,myMethod2,myMethod3\"\)
   //
   // if you like to use a method via the plugin mechanism, we recommend using
   //
   // mylinux~> root -l TMVA_Combinatorial_ttH.C\(\"P_myMethod\"\)
   // (an example is given for using the BDT as plugin (see below),
   // but of course the real application is when you write your own
   // method based)

   //---------------------------------------------------------------
   // This loads the library
   TMVA::Tools::Instance();

   // to get access to the GUI and all tmva macros
   //TString tmva_dir(TString(gRootDir) + "/tmva");
   //if(gSystem->Getenv("TMVASYS"))
   //   tmva_dir = TString(gSystem->Getenv("TMVASYS"));
   // gROOT->SetMacroPath(tmva_dir + "/test/:" + gROOT->GetMacroPath() );
    //gROOT->SetMacroPath("/usr/local/root/tmva/test/");
    //gROOT->ProcessLine(".L /usr/local/root/tmva/test/TMVAGui.C");


   // Default MVA methods to be trained + tested
   std::map<std::string,int> Use;

   // --- Cut optimisation
   Use["Cuts"]            = 0;
   Use["CutsD"]           = 0;
   Use["CutsPCA"]         = 0;
   Use["CutsGA"]          = 0;
   Use["CutsSA"]          = 0;
   // 
   // --- 1-dimensional likelihood ("naive Bayes estimator")
   Use["Likelihood"]      = 1;
   Use["LikelihoodD"]     = 0; // the "D" extension indicates decorrelated input variables (see option strings)
   Use["LikelihoodPCA"]   = 0; // the "PCA" extension indicates PCA-transformed input variables (see option strings)
   Use["LikelihoodKDE"]   = 0;
   Use["LikelihoodMIX"]   = 0;
   //
   // --- Mutidimensional likelihood and Nearest-Neighbour methods
   Use["PDERS"]           = 0;
   Use["PDERSD"]          = 0;
   Use["PDERSPCA"]        = 0;
   Use["PDEFoam"]         = 0;
   Use["PDEFoamBoost"]    = 0; // uses generalised MVA method boosting
   Use["KNN"]             = 0; // k-nearest neighbour method
   //
   // --- Linear Discriminant Analysis
   Use["LD"]              = 0; // Linear Discriminant identical to Fisher
   Use["Fisher"]          = 1;
   Use["FisherG"]         = 1;
   Use["BoostedFisher"]   = 1; // uses generalised MVA method boosting
   Use["HMatrix"]         = 0;
   //
   // --- Function Discriminant analysis
   Use["FDA_GA"]          = 0; // minimisation of user-defined function using Genetics Algorithm
   Use["FDA_SA"]          = 0;
   Use["FDA_MC"]          = 0;
   Use["FDA_MT"]          = 0;
   Use["FDA_GAMT"]        = 0;
   Use["FDA_MCMT"]        = 0;
   //
   // --- Neural Networks (all are feed-forward Multilayer Perceptrons)
   Use["MLP"]             = 0; // Recommended ANN
   Use["MLPBFGS"]         = 0; // Recommended ANN with optional training method
   Use["MLPBNN"]          = 0; // Recommended ANN with BFGS training method and bayesian regulator
   Use["CFMlpANN"]        = 0; // Depreciated ANN from ALEPH
   Use["TMlpANN"]         = 0; // ROOT's own ANN
   //
#ifdef R__HAS_TMVAGPU
   Use["DNN_GPU"]         = 1; // CUDA-accelerated DNN training.
#else
   Use["DNN_GPU"]         = 0;
#endif

#ifdef R__HAS_TMVACPU
   Use["DNN_CPU"]         = 1; // Multi-core accelerated DNN.
#else
   Use["DNN_CPU"]         = 0;
#endif
   // --- Support Vector Machine 
   Use["SVM"]             = 1;
   // 
   // --- Boosted Decision Trees
   Use["BDT"]             = 1; // uses Adaptive Boost
   Use["BDTG"]            = 1; // uses Gradient Boost
   Use["BDTB"]            = 1; // uses Bagging
   Use["BDTD"]            = 1; // decorrelation + Adaptive Boost
   Use["BDTF"]            = 1; // allow usage of fisher discriminant for node splitting 
   // 
   // --- Friedman's RuleFit method, ie, an optimised series of cuts ("rules")
   Use["RuleFit"]         = 1;
   // ---------------------------------------------------------------

   std::cout << std::endl;
   std::cout << "==> Start TMVA_A3_single_prod" << std::endl;

   // Select methods (don't look at this code - not of interest)
   if (myMethodList != "") {
      for (std::map<std::string,int>::iterator it = Use.begin(); it != Use.end(); it++) it->second = 0;

      std::vector<TString> mlist = TMVA::gTools().SplitString( myMethodList, ',' );
      for (UInt_t i=0; i<mlist.size(); i++) {
         std::string regMethod(mlist[i]);

         if (Use.find(regMethod) == Use.end()) {
            std::cout << "Method \"" << regMethod << "\" not known in TMVA under this name. Choose among the following:" << std::endl;
            for (std::map<std::string,int>::iterator it = Use.begin(); it != Use.end(); it++) std::cout << it->first << " ";
            std::cout << std::endl;
            return;
         }
         Use[regMethod] = 1;
      }
   }

    // --------------------------------------------------------------------------------------------------

    // ====================================================================================
    // ---                      Here the preparation phase begins                       ---
    // ---                     Reading Signal and Background Files                      ---
    // ====================================================================================

    // ====================================================================================
    // Define the set of variables wanted
    // ====================================================================================
    // NOTE: Make sure the varaibles are exactly the ones in the analysis
    //         iVarSet=    1  First set of variables 
    // ====================================================================================   
    int iVarSet  =    1; 
    // extension for input and output files
    TString extIn, extIn2, extOut; 
    // define which mass to look at
    string MassX = "314p99GeV";
    string type;
    // ----------------------------------------------------
    // Define extensions (if wanted) for output files names
    // ----------------------------------------------------
        if ( iVarSet ==     1 ) {extIn=""; }  // best test from angular distributions
    // ====================================================================================


    // Create a ROOT output file where TMVA will store ntuples, histograms, etc.
    TString outfileName( "TMVA_A3_single_prod_"+MassX+".root" );
    TFile* outputFile = TFile::Open( outfileName, "RECREATE" );

    // Create the factory object. Later you can choose the methods
    // whose performance you'd like to investigate. The factory is
    // the only TMVA object you have to interact with
    //
    // The first argument is the base of the name of all the
    // weightfiles in the directory weight/
    //
    // The second argument is the output file for the training results
    // All TMVA output can be suppressed by removing the "!" (not) in
    // front of the "Silent" argument in the option string
    TMVA::Factory *factory = new TMVA::Factory( "TMVA_A3_single_prod", outputFile,
                                               "!V:!Silent:Color:DrawProgressBar:Transformations=I;:AnalysisType=Classification" );
    

    // Transformations=I;D;P;G,D


    TMVA::DataLoader *dataloader=new TMVA::DataLoader("dataset");
    // If you wish to modify default settings
    // (please check "src/Config.h" to see all available global options)
    //    (TMVA::gConfig().GetVariablePlotting()).fTimesRMS = 8.0;
    //    (TMVA::gConfig().GetIONames()).fWeightFileDir = "myWeightDirectory";
    // Set bins for PDFs = 20
    (TMVA::gConfig().GetVariablePlotting()).fNbinsMVAoutput   = 50; 
    (TMVA::gConfig().GetVariablePlotting()).fNbins1D          = 50; 
    (TMVA::gConfig().GetVariablePlotting()).fNbinsXOfROCCurve = 50; 

    // Define the input variables that shall be used for the MVA training
    // note that you may also use variable expressions, such as: "3*var1/var2*abs(var3)"
    // [all types of expressions that can also be parsed by TTree::Draw( "expression" )]

    // ====================================================================================
    // ====================================================================================
    // ---                              Define TMVA Variables                           ---
    // ====================================================================================
    // ====================================================================================

    // ====================================
    // Set of variables for Masses mX0>=40GeV
    // ====================================
    if ( iVarSet == 1 ) {
        // selected variables
   dataloader->AddVariable("p_{T}(l_{1}):=pt_l1"                 , 'F');
   dataloader->AddVariable("p_{T}(l_{2}):=pt_l2"                 , 'F');
   dataloader->AddVariable("p_{T}(j_{1}):=pt_jet1"               , 'F');
   dataloader->AddVariable("p_{T}(j_{2}):=pt_jet2"               , 'F');
   dataloader->AddVariable("p_{T}(j_{3}):=pt_jet3"               , 'F');
   dataloader->AddVariable("p_{T}(j_{4}):=pt_jet4"               , 'F');
   dataloader->AddVariable("E(l_{1}):=E_l1"                  , 'F');
   dataloader->AddVariable("E(l_{2}):=E_l2"                  , 'F');
   dataloader->AddVariable("E(j_{1}):=E_j1"                  , 'F');
   dataloader->AddVariable("E(j_{2}):=E_j2"                  , 'F');
   dataloader->AddVariable("E(j_{3}):=E_j3"                  , 'F');
   dataloader->AddVariable("E(j_{4}):=E_j4"                  , 'F');
   dataloader->AddVariable("#eta(l_{1}):=eta_l1"                , 'F');
   dataloader->AddVariable("#eta(l_{2}):=eta_l2"                , 'F');
   dataloader->AddVariable("#eta(j_{1}):=eta_j1"                , 'F');
   dataloader->AddVariable("#eta(j_{2}):=eta_j2"                , 'F');
   dataloader->AddVariable("#eta(j_{3}):=eta_j3"                , 'F');
   dataloader->AddVariable("#eta(j_{4}):=eta_j4"                , 'F');
   dataloader->AddVariable("#phi(l_{1}):=phi_l1"                , 'F');
   dataloader->AddVariable("#phi(l_{2}):=phi_l2"                , 'F');
   dataloader->AddVariable("#phi(j_{1}):=phi_j1"                , 'F');
   dataloader->AddVariable("#phi(j_{2}):=phi_j2"                , 'F');
   dataloader->AddVariable("#phi(j_{3}):=phi_j3"                , 'F');
   dataloader->AddVariable("#phi(j_{4}):=phi_j4"                , 'F');
   dataloader->AddVariable("M(Z):=MZ"                    , 'F');
   dataloader->AddVariable("p_{T}(Z):=pt_z"                  , 'F');
   dataloader->AddVariable("#eta(Z):=eta_z"                 , 'F');
   dataloader->AddVariable("#phi(Z):=phi_z"                 , 'F');
   dataloader->AddVariable("M(j_{1},j_{2}):=M_j1j2 "               , 'F');
   dataloader->AddVariable("M(j_{1},j_{3}):=M_j1j3 "               , 'F');
   dataloader->AddVariable("M(j_{1},j_{4}):=M_j1j4 "               , 'F');
   dataloader->AddVariable("M(j_{2},j_{3}):=M_j2j3 "               , 'F');
   dataloader->AddVariable("M(j_{2},j_{4}):=M_j2j4 "               , 'F');
   dataloader->AddVariable("M(j_{3},j_{4}):=M_j3j4 "               , 'F');
   dataloader->AddVariable("p_{T}(j_{1},j_{2}):=pt_j1j2"               , 'F');
   dataloader->AddVariable("p_{T}(j_{1},j_{3}):=pt_j1j3"               , 'F');
   dataloader->AddVariable("p_{T}(j_{1},j_{4}):=pt_j1j4"               , 'F');
   dataloader->AddVariable("p_{T}(j_{2},j_{3}):=pt_j2j3"               , 'F');
   dataloader->AddVariable("p_{T}(j_{2},j_{4}):=pt_j2j4"               , 'F');
   dataloader->AddVariable("p_{T}(j_{3},j_{4}):=pt_j3j4"               , 'F');
   dataloader->AddVariable("#eta(j_{1},j_{2}):=eta_j1j2"              , 'F');
   dataloader->AddVariable("#eta(j_{1},j_{3}):=eta_j1j3"              , 'F');
   dataloader->AddVariable("#eta(j_{1},j_{4}):=eta_j1j4"              , 'F');
   dataloader->AddVariable("#eta(j_{2},j_{3}):=eta_j2j3"              , 'F');
   dataloader->AddVariable("#eta(j_{2},j_{4}):=eta_j2j4"              , 'F');
   dataloader->AddVariable("#eta(j_{3},j_{4}):=eta_j3j4"              , 'F');
   dataloader->AddVariable("#phi(j_{1},j_{2}):=phi_j1j2"              , 'F');
   dataloader->AddVariable("#phi(j_{1},j_{3}):=phi_j1j3"              , 'F');
   dataloader->AddVariable("#phi(j_{1},j_{4}):=phi_j1j4"              , 'F');
   dataloader->AddVariable("#phi(j_{2},j_{3}):=phi_j2j3"              , 'F');
   dataloader->AddVariable("#phi(j_{2},j_{4}):=phi_j2j4"              , 'F');
   dataloader->AddVariable("#phi(j_{3},j_{4}):=phi_j3j4"              , 'F');
   dataloader->AddVariable("M(H_{2,1}):=MH2_1"                 , 'F');
   dataloader->AddVariable("M(H_{2,2}):=MH2_2"                 , 'F');
   dataloader->AddVariable("M(H_{2,3}):=MH2_3"                 , 'F');
   dataloader->AddVariable("M(H_{2,4}):=MH2_4"                 , 'F');
   dataloader->AddVariable("M(H_{2,5}):=MH2_5"                 , 'F');
   dataloader->AddVariable("M(H_{2,6}):=MH2_6"                 , 'F');
   dataloader->AddVariable("M(A_{3}):=MA3"                   , 'F');
   dataloader->AddVariable("p_{T}(A_{3}):=pt_A3"                 , 'F');
   dataloader->AddVariable("#eta(A_{3}):=eta_A3"                , 'F');
   dataloader->AddVariable("#phi(A_{3}):=phi_A3"                , 'F');
   dataloader->AddVariable("cos(j_{1},j_{2}):=cos_j1j2"              , 'F');
   dataloader->AddVariable("cos(j_{1},j_{3}):=cos_j1j3"              , 'F');
   dataloader->AddVariable("cos(j_{1},j_{4}):=cos_j1j4"              , 'F');
   dataloader->AddVariable("cos(j_{2},j_{3}):=cos_j2j3"              , 'F');
   dataloader->AddVariable("cos(j_{2},j_{4}):=cos_j2j4"              , 'F');
   dataloader->AddVariable("cos(j_{3},j_{4}):=cos_j3j4"              , 'F');
   dataloader->AddVariable("cos(j_{1},l_{1}):=cos_j1lep1"            , 'F');
   dataloader->AddVariable("cos(j_{1},l_{2}):=cos_j1lep2"            , 'F');
   dataloader->AddVariable("cos(j_{2},l_{1}):=cos_j2lep1"            , 'F');
   dataloader->AddVariable("cos(j_{2},l_{2}):=cos_j2lep2"            , 'F');
   dataloader->AddVariable("cos(j_{3},l_{1}):=cos_j3lep1"            , 'F');
   dataloader->AddVariable("cos(j_{3},l_{2}):=cos_j3lep2"            , 'F');
   dataloader->AddVariable("cos(j_{4},l_{1}):=cos_j4lep1"            , 'F');
   dataloader->AddVariable("cos(j_{4},l_{2}):=cos_j4lep2"            , 'F');
   dataloader->AddVariable("cos(l_{1},l_{2}):=cos_lep1lep2"          , 'F');
   dataloader->AddVariable("#Delta R(j_{1},j_{2}):=DR_j1j2"               , 'F');
   dataloader->AddVariable("#Delta R(j_{1},j_{3}):=DR_j1j3"               , 'F');
   dataloader->AddVariable("#Delta R(j_{1},j_{4}):=DR_j1j4"               , 'F');
   dataloader->AddVariable("#Delta R(j_{2},j_{3}):=DR_j2j3"               , 'F');
   dataloader->AddVariable("#Delta R(j_{2},j_{4}):=DR_j2j4"               , 'F');
   dataloader->AddVariable("#Delta R(j_{3},j_{4}):=DR_j3j4"               , 'F');
   dataloader->AddVariable("#Delta R(j_{1},l_{1}):=DR_j1lep1"             , 'F');
   dataloader->AddVariable("#Delta R(j_{1},l_{2}):=DR_j1lep2"             , 'F');
   dataloader->AddVariable("#Delta R(j_{2},l_{1}):=DR_j2lep1"             , 'F');
   dataloader->AddVariable("#Delta R(j_{2},l_{2}):=DR_j2lep2"             , 'F');
   dataloader->AddVariable("#Delta R(j_{3},l_{1}):=DR_j3lep1"             , 'F');
   dataloader->AddVariable("#Delta R(j_{3},l_{2}):=DR_j3lep2"             , 'F');
   dataloader->AddVariable("#Delta R(j_{4},l_{1}):=DR_j4lep1"             , 'F');
   dataloader->AddVariable("#Delta R(j_{4},l_{2}):=DR_j4lep2"             , 'F');
   dataloader->AddVariable("#Delta R(l_{1},l_{2}):=DR_lep1lep2"           , 'F');
   dataloader->AddVariable("#Delta #phi (j_{1},j_{2}):=DPhi_j1j2"             , 'F');
   dataloader->AddVariable("#Delta #phi (j_{1},j_{3}):=DPhi_j1j3"             , 'F');
   dataloader->AddVariable("#Delta #phi (j_{1},j_{4}):=DPhi_j1j4"             , 'F');
   dataloader->AddVariable("#Delta #phi (j_{2},j_{3}):=DPhi_j2j3"             , 'F');
   dataloader->AddVariable("#Delta #phi (j_{2},j_{4}):=DPhi_j2j4"             , 'F');
   dataloader->AddVariable("#Delta #phi (j_{3},j_{4}):=DPhi_j3j4"             , 'F');
   dataloader->AddVariable("#Delta #phi (j_{1},l_{1}):=DPhi_j1lep1"           , 'F');
   dataloader->AddVariable("#Delta #phi (j_{1},l_{2}):=DPhi_j1lep2"           , 'F');
   dataloader->AddVariable("#Delta #phi (j_{2},l_{1}):=DPhi_j2lep1"           , 'F');
   dataloader->AddVariable("#Delta #phi (j_{2},l_{2}):=DPhi_j2lep2"           , 'F');
   dataloader->AddVariable("#Delta #phi (j_{3},l_{1}):=DPhi_j3lep1"           , 'F');
   dataloader->AddVariable("#Delta #phi (j_{3},l_{2}):=DPhi_j3lep2"           , 'F');
   dataloader->AddVariable("#Delta #phi (j_{4},l_{1}):=DPhi_j4lep1"           , 'F');
   dataloader->AddVariable("#Delta #phi (j_{4},l_{2}):=DPhi_j4lep2"           , 'F');
   dataloader->AddVariable("#Delta #phi (l_{1},l_{2}):=DPhi_lep1lep2"         , 'F');
   dataloader->AddVariable("#Delta #theta (j_{1},j_{2}):=DTheta_j1j2"           , 'F');
   dataloader->AddVariable("#Delta #theta (j_{1},j_{3}):=DTheta_j1j3"           , 'F');
   dataloader->AddVariable("#Delta #theta (j_{1},j_{4}):=DTheta_j1j4"           , 'F');
   dataloader->AddVariable("#Delta #theta (j_{2},j_{3}):=DTheta_j2j3"           , 'F');
   dataloader->AddVariable("#Delta #theta (j_{2},j_{4}):=DTheta_j2j4"           , 'F');
   dataloader->AddVariable("#Delta #theta (j_{3},j_{4}):=DTheta_j3j4"           , 'F');
   dataloader->AddVariable("#Delta #theta (j_{1},l_{1}):=DTheta_j1lep1"         , 'F');
   dataloader->AddVariable("#Delta #theta (j_{1},l_{2}):=DTheta_j1lep2"         , 'F');
   dataloader->AddVariable("#Delta #theta (j_{2},l_{1}):=DTheta_j2lep1"         , 'F');
   dataloader->AddVariable("#Delta #theta (j_{2},l_{2}):=DTheta_j2lep2"         , 'F');
   dataloader->AddVariable("#Delta #theta (j_{3},l_{1}):=DTheta_j3lep1"         , 'F');
   dataloader->AddVariable("#Delta #theta (j_{3},l_{2}):=DTheta_j3lep2"         , 'F');
   dataloader->AddVariable("#Delta #theta (j_{4},l_{1}):=DTheta_j4lep1"         , 'F');
   dataloader->AddVariable("#Delta #theta (j_{4},l_{2}):=DTheta_j4lep2"         , 'F');
   dataloader->AddVariable("#Delta #theta (l_{1},l_{2}):=DTheta_lep1lep2"       , 'F');
    }

    // ====================================================================================
    // Read training and test data from Signal and Background Files
    // ====================================================================================
    TString sigFileName;
    TString bck1FileName;
    // 1) Signal file
       // for masses above 40GeV
       if ( iVarSet == 1 ) sigFileName = "inputdata/A3_single_prod_160GeV.root";
       TFile*  sigFile = TFile::Open( sigFileName, "READ" );
       std::cout << "--- TMVA: Using Signal     input file: " << sigFile->GetName() << std::endl;    
    // 2) Background file
       if ( iVarSet == 1 ) bck1FileName = "inputdata/Z_plus_jets.root";
       TFile*  bck1File = TFile::Open( bck1FileName, "READ" );
       std::cout << "--- TMVA: Using Background input file: " << bck1File->GetName() << std::endl;
    // ====================================================================================
    
    // --- Register the training and test trees for Signal and Background
    TTree *signal     =  (TTree*)sigFile->Get("A3");
    TTree *background = (TTree*)bck1File->Get("A3");

    // global event weights per tree (see below for setting event-wise weights)
    Double_t signalWeight     = 1.0;
    Double_t backgroundWeight = 1.0;
   
    // You can add an arbitrary number of signal or background trees
    dataloader->AddSignalTree    ( signal,     signalWeight     );
    dataloader->AddBackgroundTree( background, backgroundWeight );
   
    // To give different trees for training and testing, do as follows:
    //    factory->AddSignalTree( signalTrainingTree, signalTrainWeight, "Training" );
    //    factory->AddSignalTree( signalTestTree,     signalTestWeight,  "Test" );
   
    // Use the following code instead of the above two or four lines to add signal and background
    // training and test events "by hand"
    // NOTE that in this case one should not give expressions (such as "var1+var2") in the input
    //      variable definition, but simply compute the expression before adding the event
    //
    //     // --- begin ----------------------------------------------------------
    //     std::vector<Double_t> vars( 4 ); // vector has size of number of input variables
    //     Float_t  treevars[4], weight;
    //
    //     // Signal
    //     for (UInt_t ivar=0; ivar<4; ivar++) signal->SetBranchAddress( Form( "var%i", ivar+1 ), &(treevars[ivar]) );
    //     for (UInt_t i=0; i<signal->GetEntries(); i++) {
    //        signal->GetEntry(i);
    //        for (UInt_t ivar=0; ivar<4; ivar++) vars[ivar] = treevars[ivar];
    //        // add training and test events; here: first half is training, second is testing
    //        // note that the weight can also be event-wise
    //        if (i < signal->GetEntries()/2.0) factory->AddSignalTrainingEvent( vars, signalWeight );
    //        else                              factory->AddSignalTestEvent    ( vars, signalWeight );
    //     }
    //
    //     // Background (has event weights)
    //     background->SetBranchAddress( "weight", &weight );
    //     for (UInt_t ivar=0; ivar<4; ivar++) background->SetBranchAddress( Form( "var%i", ivar+1 ), &(treevars[ivar]) );
    //     for (UInt_t i=0; i<background->GetEntries(); i++) {
    //        background->GetEntry(i);
    //        for (UInt_t ivar=0; ivar<4; ivar++) vars[ivar] = treevars[ivar];
    //        // add training and test events; here: first half is training, second is testing
    //        // note that the weight can also be event-wise
    //        if (i < background->GetEntries()/2) factory->AddBackgroundTrainingEvent( vars, backgroundWeight*weight );
    //        else                                factory->AddBackgroundTestEvent    ( vars, backgroundWeight*weight );
    //     }
    // --- end ------------------------------------------------------------
    //
    // --- end of tree registration

    // Set individual event weights (the variables must exist in the original TTree)
    //    for signal    : factory->SetSignalWeightExpression    ("weight1*weight2");
    //    for background: factory->SetBackgroundWeightExpression("weight1*weight2");
    //factory->SetSignalWeightExpression( "NewNtuWeight" );
    //factory->SetBackgroundWeightExpression( "NewNtuWeight" );

    // Apply additional cuts on the signal and background samples (can be different)
    TCut mycuts = ""; // for example: TCut mycuts = "abs(var1)<0.5 && abs(var2-0.5)<1";
    TCut mycutb = ""; // for example: TCut mycutb = "abs(var1)<0.5";

    // Tell the factory how to use the training and testing events
    //
    // If no numbers of events are given, half of the events in the tree are used
    // for training, and the other half for testing:
    //    factory->PrepareTrainingAndTestTree( mycut, "SplitMode=random:!V" );
    // To also specify the number of testing events, use:
    //    factory->PrepareTrainingAndTestTree( mycut,
    //                                         "NSigTrain=3000:NBkgTrain=3000:NSigTest=3000:NBkgTest=3000:SplitMode=Random:!V" );
    dataloader->PrepareTrainingAndTestTree( mycuts, mycutb,
                                        "nTrain_Signal=0:nTrain_Background=0:SplitMode=Random:NormMode=NumEvents:!V" );
/*
    // ---- Book MVA methods
    //
    // Please lookup the various method configuration options in the corresponding cxx files, eg:
    // src/MethoCuts.cxx, etc, or here: http://tmva.sourceforge.net/optionRef.html
    // it is possible to preset ranges in the option string in which the cut optimisation should be done:
    // "...:CutRangeMin[2]=-1:CutRangeMax[2]=1"...", where [2] is the third input variable

    // Cut optimisation
    if (Use["Cuts"])
      factory->BookMethod( dataloader, TMVA::Types::kCuts, "Cuts",
                           "!H:!V:FitMethod=MC:EffSel:SampleSize=200000:VarProp=FSmart" );

    if (Use["CutsD"])
      factory->BookMethod( dataloader, TMVA::Types::kCuts, "CutsD",
                           "!H:!V:FitMethod=MC:EffSel:SampleSize=200000:VarProp=FSmart:VarTransform=Decorrelate" );

    if (Use["CutsPCA"])
      factory->BookMethod( dataloader, TMVA::Types::kCuts, "CutsPCA",
                           "!H:!V:FitMethod=MC:EffSel:SampleSize=200000:VarProp=FSmart:VarTransform=PCA" );

    if (Use["CutsGA"])
      factory->BookMethod( dataloader, TMVA::Types::kCuts, "CutsGA",
                           "H:!V:FitMethod=GA:CutRangeMin[0]=-10:CutRangeMax[0]=10:VarProp[1]=FMax:EffSel:Steps=30:Cycles=3:PopSize=400:SC_steps=10:SC_rate=5:SC_factor=0.95" );

    if (Use["CutsSA"])
      factory->BookMethod( dataloader, TMVA::Types::kCuts, "CutsSA",
                           "!H:!V:FitMethod=SA:EffSel:MaxCalls=150000:KernelTemp=IncAdaptive:InitialTemp=1e+6:MinTemp=1e-6:Eps=1e-10:UseDefaultScale" );

    // Likelihood ("naive Bayes estimator")
    if (Use["Likelihood"])
      factory->BookMethod( dataloader, TMVA::Types::kLikelihood, "Likelihood",
                           "H:!V:TransformOutput:PDFInterpol=Spline2:NSmoothSig[0]=20:NSmoothBkg[0]=20:NSmoothBkg[1]=10:NSmooth=1:NAvEvtPerBin=50" );

    // Decorrelated likelihood
    if (Use["LikelihoodD"])
      factory->BookMethod( dataloader, TMVA::Types::kLikelihood, "LikelihoodD",
                           "!H:!V:TransformOutput:PDFInterpol=Spline2:NSmoothSig[0]=20:NSmoothBkg[0]=20:NSmooth=5:NAvEvtPerBin=50:VarTransform=Decorrelate" );

    // PCA-transformed likelihood
    if (Use["LikelihoodPCA"])
      factory->BookMethod( dataloader, TMVA::Types::kLikelihood, "LikelihoodPCA",
                           "!H:!V:!TransformOutput:PDFInterpol=Spline2:NSmoothSig[0]=20:NSmoothBkg[0]=20:NSmooth=5:NAvEvtPerBin=50:VarTransform=PCA" ); 

    // Use a kernel density estimator to approximate the PDFs
    if (Use["LikelihoodKDE"])
      factory->BookMethod( dataloader, TMVA::Types::kLikelihood, "LikelihoodKDE",
                           "!H:!V:!TransformOutput:PDFInterpol=KDE:KDEtype=Gauss:KDEiter=Adaptive:KDEFineFactor=0.3:KDEborder=None:NAvEvtPerBin=50" ); 

    // Use a variable-dependent mix of splines and kernel density estimator
    if (Use["LikelihoodMIX"])
      factory->BookMethod( dataloader, TMVA::Types::kLikelihood, "LikelihoodMIX",
                           "!H:!V:!TransformOutput:PDFInterpolSig[0]=KDE:PDFInterpolBkg[0]=KDE:PDFInterpolSig[1]=KDE:PDFInterpolBkg[1]=KDE:PDFInterpolSig[2]=Spline2:PDFInterpolBkg[2]=Spline2:PDFInterpolSig[3]=Spline2:PDFInterpolBkg[3]=Spline2:KDEtype=Gauss:KDEiter=Nonadaptive:KDEborder=None:NAvEvtPerBin=50" ); 

    // Test the multi-dimensional probability density estimator
    // here are the options strings for the MinMax and RMS methods, respectively:
    //      "!H:!V:VolumeRangeMode=MinMax:DeltaFrac=0.2:KernelEstimator=Gauss:GaussSigma=0.3" );
    //      "!H:!V:VolumeRangeMode=RMS:DeltaFrac=3:KernelEstimator=Gauss:GaussSigma=0.3" );
    if (Use["PDERS"])
      factory->BookMethod( dataloader, TMVA::Types::kPDERS, "PDERS",
                           "!H:!V:NormTree=T:VolumeRangeMode=Adaptive:KernelEstimator=Gauss:GaussSigma=0.3:NEventsMin=400:NEventsMax=600" );

    if (Use["PDERSD"])
      factory->BookMethod( dataloader, TMVA::Types::kPDERS, "PDERSD",
                           "!H:!V:VolumeRangeMode=Adaptive:KernelEstimator=Gauss:GaussSigma=0.3:NEventsMin=400:NEventsMax=600:VarTransform=Decorrelate" );

    if (Use["PDERSPCA"])
      factory->BookMethod( dataloader, TMVA::Types::kPDERS, "PDERSPCA",
                           "!H:!V:VolumeRangeMode=Adaptive:KernelEstimator=Gauss:GaussSigma=0.3:NEventsMin=400:NEventsMax=600:VarTransform=PCA" );

    // Multi-dimensional likelihood estimator using self-adapting phase-space binning
    if (Use["PDEFoam"])
      factory->BookMethod( dataloader, TMVA::Types::kPDEFoam, "PDEFoam",
                           "!H:!V:SigBgSeparate=F:TailCut=0.001:VolFrac=0.0666:nActiveCells=500:nSampl=2000:nBin=5:Nmin=100:Kernel=None:Compress=T" );

    if (Use["PDEFoamBoost"])
      factory->BookMethod( dataloader, TMVA::Types::kPDEFoam, "PDEFoamBoost",
                           "!H:!V:Boost_Num=30:Boost_Transform=linear:SigBgSeparate=F:MaxDepth=4:UseYesNoCell=T:DTLogic=MisClassificationError:FillFoamWithOrigWeights=F:TailCut=0:nActiveCells=500:nBin=20:Nmin=400:Kernel=None:Compress=T" );

    // K-Nearest Neighbour classifier (KNN)
    if (Use["KNN"])
      factory->BookMethod( dataloader, TMVA::Types::kKNN, "KNN",
                           "H:nkNN=20:ScaleFrac=0.8:SigmaFact=1.0:Kernel=Gaus:UseKernel=F:UseWeight=T:!Trim" );

    // H-Matrix (chi2-squared) method
    if (Use["HMatrix"])
      factory->BookMethod( dataloader, TMVA::Types::kHMatrix, "HMatrix", "!H:!V:VarTransform=None" );

    // Linear discriminant (same as Fisher discriminant)
    if (Use["LD"])
      factory->BookMethod( dataloader, TMVA::Types::kLD, "LD", "H:!V:VarTransform=None:CreateMVAPdfs:PDFInterpolMVAPdf=Spline2:NbinsMVAPdf=50:NsmoothMVAPdf=10" );

    // Fisher discriminant (same as LD)
    if (Use["Fisher"])
      factory->BookMethod( dataloader, TMVA::Types::kFisher, "Fisher", "H:!V:Fisher:VarTransform=None:CreateMVAPdfs:PDFInterpolMVAPdf=Spline2:NbinsMVAPdf=50:NsmoothMVAPdf=10" );

    // Fisher with Gauss-transformed input variables
    if (Use["FisherG"])
      factory->BookMethod( dataloader, TMVA::Types::kFisher, "FisherG", "H:!V:VarTransform=Gauss" );

    // Composite classifier: ensemble (tree) of boosted Fisher classifiers
    if (Use["BoostedFisher"])
      factory->BookMethod( dataloader, TMVA::Types::kFisher, "BoostedFisher", 
                           "H:!V:Boost_Num=20:Boost_Transform=log:Boost_Type=AdaBoost:Boost_AdaBoostBeta=0.2:!Boost_DetailedMonitoring" );

    // Function discrimination analysis (FDA) -- test of various fitters - the recommended one is Minuit (or GA or SA)
    if (Use["FDA_MC"])
      factory->BookMethod( dataloader, TMVA::Types::kFDA, "FDA_MC",
                           "H:!V:Formula=(0)+(1)*x0+(2)*x1+(3)*x2+(4)*x3:ParRanges=(-1,1);(-10,10);(-10,10);(-10,10);(-10,10):FitMethod=MC:SampleSize=100000:Sigma=0.1" );

    if (Use["FDA_GA"]) // can also use Simulated Annealing (SA) algorithm (see Cuts_SA options])
      factory->BookMethod( dataloader, TMVA::Types::kFDA, "FDA_GA",
                           "H:!V:Formula=(0)+(1)*x0+(2)*x1+(3)*x2+(4)*x3:ParRanges=(-1,1);(-10,10);(-10,10);(-10,10);(-10,10):FitMethod=GA:PopSize=300:Cycles=3:Steps=20:Trim=True:SaveBestGen=1" );

    if (Use["FDA_SA"]) // can also use Simulated Annealing (SA) algorithm (see Cuts_SA options])
      factory->BookMethod( dataloader, TMVA::Types::kFDA, "FDA_SA",
                           "H:!V:Formula=(0)+(1)*x0+(2)*x1+(3)*x2+(4)*x3:ParRanges=(-1,1);(-10,10);(-10,10);(-10,10);(-10,10):FitMethod=SA:MaxCalls=15000:KernelTemp=IncAdaptive:InitialTemp=1e+6:MinTemp=1e-6:Eps=1e-10:UseDefaultScale" );

    if (Use["FDA_MT"])
      factory->BookMethod( dataloader, TMVA::Types::kFDA, "FDA_MT",
                           "H:!V:Formula=(0)+(1)*x0+(2)*x1+(3)*x2+(4)*x3:ParRanges=(-1,1);(-10,10);(-10,10);(-10,10);(-10,10):FitMethod=MINUIT:ErrorLevel=1:PrintLevel=-1:FitStrategy=2:UseImprove:UseMinos:SetBatch" );

    if (Use["FDA_GAMT"])
      factory->BookMethod( dataloader, TMVA::Types::kFDA, "FDA_GAMT",
                           "H:!V:Formula=(0)+(1)*x0+(2)*x1+(3)*x2+(4)*x3:ParRanges=(-1,1);(-10,10);(-10,10);(-10,10);(-10,10):FitMethod=GA:Converger=MINUIT:ErrorLevel=1:PrintLevel=-1:FitStrategy=0:!UseImprove:!UseMinos:SetBatch:Cycles=1:PopSize=5:Steps=5:Trim" );

    if (Use["FDA_MCMT"])
      factory->BookMethod( dataloader, TMVA::Types::kFDA, "FDA_MCMT",
                           "H:!V:Formula=(0)+(1)*x0+(2)*x1+(3)*x2+(4)*x3:ParRanges=(-1,1);(-10,10);(-10,10);(-10,10);(-10,10):FitMethod=MC:Converger=MINUIT:ErrorLevel=1:PrintLevel=-1:FitStrategy=0:!UseImprove:!UseMinos:SetBatch:SampleSize=20" );

    // TMVA ANN: MLP (recommended ANN) -- all ANNs in TMVA are Multilayer Perceptrons
    if (Use["MLP"])
      factory->BookMethod( dataloader, TMVA::Types::kMLP, "MLP", "H:!V:NeuronType=tanh:VarTransform=N:NCycles=600:HiddenLayers=N+5:TestRate=5:!UseRegulator" );

    if (Use["MLPBFGS"])
      factory->BookMethod( dataloader, TMVA::Types::kMLP, "MLPBFGS", "H:!V:NeuronType=tanh:VarTransform=N:NCycles=600:HiddenLayers=N+5:TestRate=5:TrainingMethod=BFGS:!UseRegulator" );

    if (Use["MLPBNN"])
      factory->BookMethod( dataloader, TMVA::Types::kMLP, "MLPBNN", "H:!V:NeuronType=tanh:VarTransform=N:NCycles=600:HiddenLayers=N+5:TestRate=5:TrainingMethod=BFGS:UseRegulator" ); // BFGS training with bayesian regulators

    // CF(Clermont-Ferrand)ANN
    if (Use["CFMlpANN"])
      factory->BookMethod( dataloader, TMVA::Types::kCFMlpANN, "CFMlpANN", "!H:!V:NCycles=2000:HiddenLayers=N+1,N"  ); // n_cycles:#nodes:#nodes:...  

    // Tmlp(Root)ANN
    if (Use["TMlpANN"])
      factory->BookMethod( dataloader, TMVA::Types::kTMlpANN, "TMlpANN", "!H:!V:NCycles=200:HiddenLayers=N+1,N:LearningMethod=BFGS:ValidationFraction=0.3"  ); // n_cycles:#nodes:#nodes:...

    // Support Vector Machine
    if (Use["SVM"])
      factory->BookMethod( dataloader, TMVA::Types::kSVM, "SVM", "Gamma=0.25:Tol=0.001:VarTransform=Norm" );

    // Boosted Decision Trees
    if (Use["BDTG"]) // Gradient Boost
      factory->BookMethod( dataloader, TMVA::Types::kBDT, "BDTG",
                           "!H:!V:NTrees=1000:MinNodeSize=2.5%:BoostType=Grad:Shrinkage=0.10:UseBaggedBoost:BaggedSampleFraction=0.5:nCuts=20:MaxDepth=2" );

    if (Use["BDT"])  // Adaptive Boost
      factory->BookMethod( dataloader, TMVA::Types::kBDT, "BDT",
                           "!H:!V:NTrees=850:MinNodeSize=2.5%:MaxDepth=3:BoostType=AdaBoost:AdaBoostBeta=0.5:UseBaggedBoost:BaggedSampleFraction=0.5:SeparationType=GiniIndex:nCuts=20" );

    if (Use["BDTB"]) // Bagging
      factory->BookMethod( dataloader, TMVA::Types::kBDT, "BDTB",
                           "!H:!V:NTrees=400:BoostType=Bagging:SeparationType=GiniIndex:nCuts=20" );

    if (Use["BDTD"]) // Decorrelation + Adaptive Boost
      factory->BookMethod( dataloader, TMVA::Types::kBDT, "BDTD",
                           "!H:!V:NTrees=400:MinNodeSize=5%:MaxDepth=3:BoostType=AdaBoost:SeparationType=GiniIndex:nCuts=20:VarTransform=Decorrelate" );
    
    if (Use["BDTF"])  // Allow Using Fisher discriminant in node splitting for (strong) linearly correlated variables
      factory->BookMethod( dataloader, TMVA::Types::kBDT, "BDTMitFisher",
                           "!H:!V:NTrees=50:MinNodeSize=2.5%:UseFisherCuts:MaxDepth=3:BoostType=AdaBoost:AdaBoostBeta=0.5:SeparationType=GiniIndex:nCuts=20" );

    // RuleFit -- TMVA implementation of Friedman's method
    if (Use["RuleFit"])
      factory->BookMethod( dataloader, TMVA::Types::kRuleFit, "RuleFit",
                           "H:!V:RuleFitModule=RFTMVA:Model=ModRuleLinear:MinImp=0.001:RuleMinDist=0.001:NTrees=20:fEventsMin=0.01:fEventsMax=0.5:GDTau=-1.0:GDTauPrec=0.01:GDStep=0.01:GDNSteps=10000:GDErrScale=1.02" );
*/ 

   // ### Book MVA methods
   //
   // Please lookup the various method configuration options in the corresponding cxx files, eg:
   // src/MethoCuts.cxx, etc, or here: http://tmva.sourceforge.net/optionRef.html
   // it is possible to preset ranges in the option string in which the cut optimisation should be done:
   // "...:CutRangeMin[2]=-1:CutRangeMax[2]=1"...", where [2] is the third input variable

   // Cut optimisation
   if (Use["Cuts"])
      factory->BookMethod( dataloader, TMVA::Types::kCuts, "Cuts",
                           "!H:!V:FitMethod=MC:EffSel:SampleSize=200000:VarProp=FSmart" );

   if (Use["CutsD"])
      factory->BookMethod( dataloader, TMVA::Types::kCuts, "CutsD",
                           "!H:!V:FitMethod=MC:EffSel:SampleSize=200000:VarProp=FSmart:VarTransform=Decorrelate" );

   if (Use["CutsPCA"])
      factory->BookMethod( dataloader, TMVA::Types::kCuts, "CutsPCA",
                           "!H:!V:FitMethod=MC:EffSel:SampleSize=200000:VarProp=FSmart:VarTransform=PCA" );

   if (Use["CutsGA"])
      factory->BookMethod( dataloader, TMVA::Types::kCuts, "CutsGA",
                           "H:!V:FitMethod=GA:CutRangeMin[0]=-10:CutRangeMax[0]=10:VarProp[1]=FMax:EffSel:Steps=30:Cycles=3:PopSize=400:SC_steps=10:SC_rate=5:SC_factor=0.95" );

   if (Use["CutsSA"])
      factory->BookMethod( dataloader, TMVA::Types::kCuts, "CutsSA",
                           "!H:!V:FitMethod=SA:EffSel:MaxCalls=150000:KernelTemp=IncAdaptive:InitialTemp=1e+6:MinTemp=1e-6:Eps=1e-10:UseDefaultScale" );

   // Likelihood ("naive Bayes estimator")
   if (Use["Likelihood"])
      factory->BookMethod( dataloader, TMVA::Types::kLikelihood, "Likelihood",
                           "H:!V:TransformOutput:PDFInterpol=Spline2:NSmoothSig[0]=20:NSmoothBkg[0]=20:NSmoothBkg[1]=10:NSmooth=1:NAvEvtPerBin=50" );

   // Decorrelated likelihood
   if (Use["LikelihoodD"])
      factory->BookMethod( dataloader, TMVA::Types::kLikelihood, "LikelihoodD",
                           "!H:!V:TransformOutput:PDFInterpol=Spline2:NSmoothSig[0]=20:NSmoothBkg[0]=20:NSmooth=5:NAvEvtPerBin=50:VarTransform=Decorrelate" );

   // PCA-transformed likelihood
   if (Use["LikelihoodPCA"])
      factory->BookMethod( dataloader, TMVA::Types::kLikelihood, "LikelihoodPCA",
                           "!H:!V:!TransformOutput:PDFInterpol=Spline2:NSmoothSig[0]=20:NSmoothBkg[0]=20:NSmooth=5:NAvEvtPerBin=50:VarTransform=PCA" );

   // Use a kernel density estimator to approximate the PDFs
   if (Use["LikelihoodKDE"])
      factory->BookMethod( dataloader, TMVA::Types::kLikelihood, "LikelihoodKDE",
                           "!H:!V:!TransformOutput:PDFInterpol=KDE:KDEtype=Gauss:KDEiter=Adaptive:KDEFineFactor=0.3:KDEborder=None:NAvEvtPerBin=50" );

   // Use a variable-dependent mix of splines and kernel density estimator
   if (Use["LikelihoodMIX"])
      factory->BookMethod( dataloader, TMVA::Types::kLikelihood, "LikelihoodMIX",
                           "!H:!V:!TransformOutput:PDFInterpolSig[0]=KDE:PDFInterpolBkg[0]=KDE:PDFInterpolSig[1]=KDE:PDFInterpolBkg[1]=KDE:PDFInterpolSig[2]=Spline2:PDFInterpolBkg[2]=Spline2:PDFInterpolSig[3]=Spline2:PDFInterpolBkg[3]=Spline2:KDEtype=Gauss:KDEiter=Nonadaptive:KDEborder=None:NAvEvtPerBin=50" );

   // Test the multi-dimensional probability density estimator
   // here are the options strings for the MinMax and RMS methods, respectively:
   //
   //      "!H:!V:VolumeRangeMode=MinMax:DeltaFrac=0.2:KernelEstimator=Gauss:GaussSigma=0.3" );
   //      "!H:!V:VolumeRangeMode=RMS:DeltaFrac=3:KernelEstimator=Gauss:GaussSigma=0.3" );
   if (Use["PDERS"])
      factory->BookMethod( dataloader, TMVA::Types::kPDERS, "PDERS",
                           "!H:!V:NormTree=T:VolumeRangeMode=Adaptive:KernelEstimator=Gauss:GaussSigma=0.3:NEventsMin=400:NEventsMax=600" );

   if (Use["PDERSD"])
      factory->BookMethod( dataloader, TMVA::Types::kPDERS, "PDERSD",
                           "!H:!V:VolumeRangeMode=Adaptive:KernelEstimator=Gauss:GaussSigma=0.3:NEventsMin=400:NEventsMax=600:VarTransform=Decorrelate" );

   if (Use["PDERSPCA"])
      factory->BookMethod( dataloader, TMVA::Types::kPDERS, "PDERSPCA",
                           "!H:!V:VolumeRangeMode=Adaptive:KernelEstimator=Gauss:GaussSigma=0.3:NEventsMin=400:NEventsMax=600:VarTransform=PCA" );

   // Multi-dimensional likelihood estimator using self-adapting phase-space binning
   if (Use["PDEFoam"])
      factory->BookMethod( dataloader, TMVA::Types::kPDEFoam, "PDEFoam",
                           "!H:!V:SigBgSeparate=F:TailCut=0.001:VolFrac=0.0666:nActiveCells=500:nSampl=2000:nBin=5:Nmin=100:Kernel=None:Compress=T" );

   if (Use["PDEFoamBoost"])
      factory->BookMethod( dataloader, TMVA::Types::kPDEFoam, "PDEFoamBoost",
                           "!H:!V:Boost_Num=30:Boost_Transform=linear:SigBgSeparate=F:MaxDepth=4:UseYesNoCell=T:DTLogic=MisClassificationError:FillFoamWithOrigWeights=F:TailCut=0:nActiveCells=500:nBin=20:Nmin=400:Kernel=None:Compress=T" );

   // K-Nearest Neighbour classifier (KNN)
   if (Use["KNN"])
      factory->BookMethod( dataloader, TMVA::Types::kKNN, "KNN",
                           "H:nkNN=20:ScaleFrac=0.8:SigmaFact=1.0:Kernel=Gaus:UseKernel=F:UseWeight=T:!Trim" );

   // H-Matrix (chi2-squared) method
   if (Use["HMatrix"])
      factory->BookMethod( dataloader, TMVA::Types::kHMatrix, "HMatrix", "!H:!V:VarTransform=None" );

   // Linear discriminant (same as Fisher discriminant)
   if (Use["LD"])
      factory->BookMethod( dataloader, TMVA::Types::kLD, "LD", "H:!V:VarTransform=None:CreateMVAPdfs:PDFInterpolMVAPdf=Spline2:NbinsMVAPdf=50:NsmoothMVAPdf=10" );

   // Fisher discriminant (same as LD)
   if (Use["Fisher"])
      factory->BookMethod( dataloader, TMVA::Types::kFisher, "Fisher", "H:!V:Fisher:VarTransform=None:CreateMVAPdfs:PDFInterpolMVAPdf=Spline2:NbinsMVAPdf=50:NsmoothMVAPdf=10" );

   // Fisher with Gauss-transformed input variables
   if (Use["FisherG"])
      factory->BookMethod( dataloader, TMVA::Types::kFisher, "FisherG", "H:!V:VarTransform=Gauss" );

   // Composite classifier: ensemble (tree) of boosted Fisher classifiers
   if (Use["BoostedFisher"])
      factory->BookMethod( dataloader, TMVA::Types::kFisher, "BoostedFisher",
                           "H:!V:Boost_Num=20:Boost_Transform=log:Boost_Type=AdaBoost:Boost_AdaBoostBeta=0.2:!Boost_DetailedMonitoring" );

   // Function discrimination analysis (FDA) -- test of various fitters - the recommended one is Minuit (or GA or SA)
   if (Use["FDA_MC"])
      factory->BookMethod( dataloader, TMVA::Types::kFDA, "FDA_MC",
                           "H:!V:Formula=(0)+(1)*x0+(2)*x1+(3)*x2+(4)*x3:ParRanges=(-1,1);(-10,10);(-10,10);(-10,10);(-10,10):FitMethod=MC:SampleSize=100000:Sigma=0.1" );

   if (Use["FDA_GA"]) // can also use Simulated Annealing (SA) algorithm (see Cuts_SA options])
      factory->BookMethod( dataloader, TMVA::Types::kFDA, "FDA_GA",
                           "H:!V:Formula=(0)+(1)*x0+(2)*x1+(3)*x2+(4)*x3:ParRanges=(-1,1);(-10,10);(-10,10);(-10,10);(-10,10):FitMethod=GA:PopSize=100:Cycles=2:Steps=5:Trim=True:SaveBestGen=1" );

   if (Use["FDA_SA"]) // can also use Simulated Annealing (SA) algorithm (see Cuts_SA options])
      factory->BookMethod( dataloader, TMVA::Types::kFDA, "FDA_SA",
                           "H:!V:Formula=(0)+(1)*x0+(2)*x1+(3)*x2+(4)*x3:ParRanges=(-1,1);(-10,10);(-10,10);(-10,10);(-10,10):FitMethod=SA:MaxCalls=15000:KernelTemp=IncAdaptive:InitialTemp=1e+6:MinTemp=1e-6:Eps=1e-10:UseDefaultScale" );

   if (Use["FDA_MT"])
      factory->BookMethod( dataloader, TMVA::Types::kFDA, "FDA_MT",
                           "H:!V:Formula=(0)+(1)*x0+(2)*x1+(3)*x2+(4)*x3:ParRanges=(-1,1);(-10,10);(-10,10);(-10,10);(-10,10):FitMethod=MINUIT:ErrorLevel=1:PrintLevel=-1:FitStrategy=2:UseImprove:UseMinos:SetBatch" );

   if (Use["FDA_GAMT"])
      factory->BookMethod( dataloader, TMVA::Types::kFDA, "FDA_GAMT",
                           "H:!V:Formula=(0)+(1)*x0+(2)*x1+(3)*x2+(4)*x3:ParRanges=(-1,1);(-10,10);(-10,10);(-10,10);(-10,10):FitMethod=GA:Converger=MINUIT:ErrorLevel=1:PrintLevel=-1:FitStrategy=0:!UseImprove:!UseMinos:SetBatch:Cycles=1:PopSize=5:Steps=5:Trim" );

   if (Use["FDA_MCMT"])
      factory->BookMethod( dataloader, TMVA::Types::kFDA, "FDA_MCMT",
                           "H:!V:Formula=(0)+(1)*x0+(2)*x1+(3)*x2+(4)*x3:ParRanges=(-1,1);(-10,10);(-10,10);(-10,10);(-10,10):FitMethod=MC:Converger=MINUIT:ErrorLevel=1:PrintLevel=-1:FitStrategy=0:!UseImprove:!UseMinos:SetBatch:SampleSize=20" );

   // TMVA ANN: MLP (recommended ANN) -- all ANNs in TMVA are Multilayer Perceptrons
   if (Use["MLP"])
      factory->BookMethod( dataloader, TMVA::Types::kMLP, "MLP", "H:!V:NeuronType=tanh:VarTransform=N:NCycles=600:HiddenLayers=N+5:TestRate=5:!UseRegulator" );

   if (Use["MLPBFGS"])
      factory->BookMethod( dataloader, TMVA::Types::kMLP, "MLPBFGS", "H:!V:NeuronType=tanh:VarTransform=N:NCycles=600:HiddenLayers=N+5:TestRate=5:TrainingMethod=BFGS:!UseRegulator" );

   if (Use["MLPBNN"])
      factory->BookMethod( dataloader, TMVA::Types::kMLP, "MLPBNN", "H:!V:NeuronType=tanh:VarTransform=N:NCycles=60:HiddenLayers=N+5:TestRate=5:TrainingMethod=BFGS:UseRegulator" ); // BFGS training with bayesian regulators


   // Multi-architecture DNN implementation.
   if (Use["DNN_CPU"] or Use["DNN_GPU"]) {
      // General layout.
      TString layoutString ("Layout=TANH|128,TANH|128,TANH|128,LINEAR");

      // Training strategies.
      TString training0("LearningRate=1e-2,Momentum=0.9,Repetitions=1,"
                        "ConvergenceSteps=30,BatchSize=150,TestRepetitions=10,"
                        "WeightDecay=1e-4,Regularization=None,"
                        "DropConfig=0.0+0.5+0.5+0.5, Multithreading=True");
      TString training1("LearningRate=1e-2,Momentum=0.9,Repetitions=1,"
                        "ConvergenceSteps=20,BatchSize=150,TestRepetitions=10,"
                        "WeightDecay=1e-4,Regularization=L2,"
                        "DropConfig=0.0+0.0+0.0+0.0, Multithreading=True");
      TString training2("LearningRate=1e-3,Momentum=0.0,Repetitions=1,"
                        "ConvergenceSteps=20,BatchSize=150,TestRepetitions=10,"
                        "WeightDecay=1e-4,Regularization=L2,"
                        "DropConfig=0.0+0.0+0.0+0.0, Multithreading=True");
      TString trainingStrategyString ("TrainingStrategy=");
      trainingStrategyString += training0 + "|" + training1 + "|" + training2;

      // General Options.
      TString dnnOptions ("!H:V:ErrorStrategy=CROSSENTROPY:VarTransform=N:"
                          "WeightInitialization=XAVIERUNIFORM");
      dnnOptions.Append (":"); dnnOptions.Append (layoutString);
      dnnOptions.Append (":"); dnnOptions.Append (trainingStrategyString);

      // Cuda implementation.
      if (Use["DNN_GPU"]) {
         TString gpuOptions = dnnOptions + ":Architecture=GPU";
         factory->BookMethod(dataloader, TMVA::Types::kDL, "DNN_GPU", gpuOptions);
      }
      // Multi-core CPU implementation.
      if (Use["DNN_CPU"]) {
         TString cpuOptions = dnnOptions + ":Architecture=CPU";
         factory->BookMethod(dataloader, TMVA::Types::kDL, "DNN_CPU", cpuOptions);
      }
   }


   // CF(Clermont-Ferrand)ANN
   if (Use["CFMlpANN"])
      factory->BookMethod( dataloader, TMVA::Types::kCFMlpANN, "CFMlpANN", "!H:!V:NCycles=200:HiddenLayers=N+1,N"  ); // n_cycles:#nodes:#nodes:...

   // Tmlp(Root)ANN
   if (Use["TMlpANN"])
      factory->BookMethod( dataloader, TMVA::Types::kTMlpANN, "TMlpANN", "!H:!V:NCycles=200:HiddenLayers=N+1,N:LearningMethod=BFGS:ValidationFraction=0.3"  ); // n_cycles:#nodes:#nodes:...

   // Support Vector Machine
   if (Use["SVM"])
      factory->BookMethod( dataloader, TMVA::Types::kSVM, "SVM", "Gamma=0.25:Tol=0.001:VarTransform=Norm" );

   // Boosted Decision Trees
   if (Use["BDTG"]) // Gradient Boost
      factory->BookMethod( dataloader, TMVA::Types::kBDT, "BDTG",
                           "!H:!V:NTrees=1000:MinNodeSize=2.5%:BoostType=Grad:Shrinkage=0.10:UseBaggedBoost:BaggedSampleFraction=0.5:nCuts=20:MaxDepth=2" );

   if (Use["BDT"])  // Adaptive Boost
      factory->BookMethod( dataloader, TMVA::Types::kBDT, "BDT",
                           "!H:!V:NTrees=850:MinNodeSize=2.5%:MaxDepth=3:BoostType=AdaBoost:AdaBoostBeta=0.5:UseBaggedBoost:BaggedSampleFraction=0.5:SeparationType=GiniIndex:nCuts=20" );

   if (Use["BDTB"]) // Bagging
      factory->BookMethod( dataloader, TMVA::Types::kBDT, "BDTB",
                           "!H:!V:NTrees=400:BoostType=Bagging:SeparationType=GiniIndex:nCuts=20" );

   if (Use["BDTD"]) // Decorrelation + Adaptive Boost
      factory->BookMethod( dataloader, TMVA::Types::kBDT, "BDTD",
                           "!H:!V:NTrees=400:MinNodeSize=5%:MaxDepth=3:BoostType=AdaBoost:SeparationType=GiniIndex:nCuts=20:VarTransform=Decorrelate" );

   if (Use["BDTF"])  // Allow Using Fisher discriminant in node splitting for (strong) linearly correlated variables
      factory->BookMethod( dataloader, TMVA::Types::kBDT, "BDTF",
                           "!H:!V:NTrees=50:MinNodeSize=2.5%:UseFisherCuts:MaxDepth=3:BoostType=AdaBoost:AdaBoostBeta=0.5:SeparationType=GiniIndex:nCuts=20" );

   // RuleFit -- TMVA implementation of Friedman's method
   if (Use["RuleFit"])
      factory->BookMethod( dataloader, TMVA::Types::kRuleFit, "RuleFit",
                           "H:!V:RuleFitModule=RFTMVA:Model=ModRuleLinear:MinImp=0.001:RuleMinDist=0.001:NTrees=20:fEventsMin=0.01:fEventsMax=0.5:GDTau=-1.0:GDTauPrec=0.01:GDStep=0.01:GDNSteps=10000:GDErrScale=1.02" );



    // For an example of the category classifier usage, see: TMVA_Combinatorial_ttHCategory

    // --------------------------------------------------------------------------------------------------

    // ---- Now you can optimize the setting (configuration) of the MVAs using the set of training events

    // ---- STILL EXPERIMENTAL and only implemented for BDT's !
    // factory->OptimizeAllMethods("SigEffAt001","Scan");
    // factory->OptimizeAllMethods("ROCIntegral","FitGA");

    // --------------------------------------------------------------------------------------------------

    // ---- Now you can tell the factory to train, test, and evaluate the MVAs

    // Train MVAs using the set of training events
    factory->TrainAllMethods();

    // ---- Evaluate all MVAs using the set of test events
    factory->TestAllMethods();

    // ----- Evaluate and compare performance of all configured MVAs
    factory->EvaluateAllMethods();

    // --------------------------------------------------------------

    // Save the output
    outputFile->Close();

    std::cout << "==> Wrote root file: " << outputFile->GetName() << std::endl;
    std::cout << "==> TMVA_Combinatorial_ttH is done!" << std::endl;

    delete factory;
    delete dataloader;

    // Launch the GUI for the root macros
    if (!gROOT->IsBatch()) TMVAGui( outfileName );
}
