#include <TROOT.h>
#include <TLegend.h>
#include <TCanvas.h>
#include <TFile.h>
#include <TChain.h>
#include <TLine.h>
#include <TH1.h>
#include <TH2.h>
#include <TH3.h>
#include <TF1.h>
#include <TStyle.h>
#include <TLorentzVector.h>
#include <vector>
#include <fstream>
#include <iostream>
#include <sstream>
#include <list>
#include <string>
#include <iomanip>
#include <stdio.h>
#include <math.h>
#include <algorithm>

using std::cout;
using namespace std;
using std::endl;
using std::vector;
   

void read_txt()
{
   // ===========================
   // Data Format from 
   // ===========================
   float pt_l1          ;
   float pt_l2          ;
   float pt_jet1        ;
   float pt_jet2        ;
   float pt_jet3        ;
   float pt_jet4        ;
   float E_l1           ;
   float E_l2           ;
   float E_j1           ;
   float E_j2           ;
   float E_j3           ;
   float E_j4           ;
   float eta_l1         ;
   float eta_l2         ;
   float eta_j1         ;
   float eta_j2         ;
   float eta_j3         ;
   float eta_j4         ;
   float phi_l1         ;
   float phi_l2         ;
   float phi_j1         ;
   float phi_j2         ;
   float phi_j3         ;
   float phi_j4         ;
   float MZ             ;
   float pt_z           ;
   float eta_z          ;
   float phi_z          ;
   float M_j1j2         ;
   float M_j1j3         ;
   float M_j1j4         ;
   float M_j2j3         ;
   float M_j2j4         ;
   float M_j3j4         ;
   float pt_j1j2        ;
   float pt_j1j3        ;
   float pt_j1j4        ;
   float pt_j2j3        ;
   float pt_j2j4        ;
   float pt_j3j4        ;
   float eta_j1j2       ;
   float eta_j1j3       ;
   float eta_j1j4       ;
   float eta_j2j3       ;
   float eta_j2j4       ;
   float eta_j3j4       ;
   float phi_j1j2       ;
   float phi_j1j3       ;
   float phi_j1j4       ;
   float phi_j2j3       ;
   float phi_j2j4       ;
   float phi_j3j4       ;
   float MH2_1          ;
   float MH2_2          ;
   float MH2_3          ;
   float MH2_4          ;
   float MH2_5          ;
   float MH2_6          ;
   float MA3            ;
   float pt_A3          ;
   float eta_A3         ;
   float phi_A3         ;
   float cos_j1j2       ;
   float cos_j1j3       ;
   float cos_j1j4       ;
   float cos_j2j3       ;
   float cos_j2j4       ;
   float cos_j3j4       ;
   float cos_j1lep1     ;
   float cos_j1lep2     ;
   float cos_j2lep1     ;
   float cos_j2lep2     ;
   float cos_j3lep1     ;
   float cos_j3lep2     ;
   float cos_j4lep1     ;
   float cos_j4lep2     ;
   float cos_lep1lep2   ;
   float DR_j1j2        ;
   float DR_j1j3        ;
   float DR_j1j4        ;
   float DR_j2j3        ;
   float DR_j2j4        ;
   float DR_j3j4        ;
   float DR_j1lep1      ;
   float DR_j1lep2      ;
   float DR_j2lep1      ;
   float DR_j2lep2      ;
   float DR_j3lep1      ;
   float DR_j3lep2      ;
   float DR_j4lep1      ;
   float DR_j4lep2      ;
   float DR_lep1lep2    ;
   float DPhi_j1j2      ;
   float DPhi_j1j3      ;
   float DPhi_j1j4      ;
   float DPhi_j2j3      ;
   float DPhi_j2j4      ;
   float DPhi_j3j4      ;
   float DPhi_j1lep1    ;
   float DPhi_j1lep2    ;
   float DPhi_j2lep1    ;
   float DPhi_j2lep2    ;
   float DPhi_j3lep1    ;
   float DPhi_j3lep2    ;
   float DPhi_j4lep1    ;
   float DPhi_j4lep2    ;
   float DPhi_lep1lep2  ;
   float DTheta_j1j2    ;
   float DTheta_j1j3    ;
   float DTheta_j1j4    ;
   float DTheta_j2j3    ;
   float DTheta_j2j4    ;
   float DTheta_j3j4    ;
   float DTheta_j1lep1  ;
   float DTheta_j1lep2  ;
   float DTheta_j2lep1  ;
   float DTheta_j2lep2  ;
   float DTheta_j3lep1  ;
   float DTheta_j3lep2  ;
   float DTheta_j4lep1  ;
   float DTheta_j4lep2  ;
   float DTheta_lep1lep2;
   float xs_weight      ;

   //---------------------------------------------------------------
   // Define Input File Name
   //---------------------------------------------------------------
   int iSET = 1;           // = 1 signal file
                           // = 2 background file
   //---------------------------------------------------------------

   //---------------------------------------------------------------
   // Define Input data directory
     string dirData = "inputdata/";
   // Define Input/Output Files
   string  inpName;
   int    NumLines;
   if ( iSET ==  1 ) { inpName = "A3_single_prod_160GeV"; NumLines = 10000;}
   if ( iSET ==  2 ) { inpName = "Z_plus_jets";    NumLines =  10000;}
   //
   string inpFile  = dirData + inpName  + ".txt";
   string outFile  = dirData + inpName  + ".root"; 
   string inpClone = dirData + inpName  + ".clone_to_check.txt"; 
   cout << " " << endl;
   cout << " ----------------------------------------------------- " << endl;
   cout << " Input  File  Name: "  << inpFile  << endl;
   cout << "        File Clone: "  << inpClone << endl;
   cout << " Output File  Name: "  << outFile  << endl;
   cout << " ----------------------------------------------------- " << endl;
   //---------------------------------------------------------------


   //---------------------------------------------------------------
   // Recreate Output File
   //---------------------------------------------------------------
   TFile *hfile = TFile::Open(outFile.c_str(),"RECREATE");
   // Define TTree
   TTree *tree = new TTree("A3","A3 Single Production");
   tree->Branch("pt_l1"                 , &pt_l1                , "pt_l1/F");
   tree->Branch("pt_l2"                 , &pt_l2                , "pt_l2/F");
   tree->Branch("pt_jet1"               , &pt_jet1              , "pt_jet1/F");
   tree->Branch("pt_jet2"               , &pt_jet2              , "pt_jet2/F");
   tree->Branch("pt_jet3"               , &pt_jet3              , "pt_jet3/F");
   tree->Branch("pt_jet4"               , &pt_jet4              , "pt_jet4/F");
   tree->Branch("E_l1"                  , &E_l1                 , "E_l1/F");
   tree->Branch("E_l2"                  , &E_l2                 , "E_l2/F");
   tree->Branch("E_j1"                  , &E_j1                 , "E_j1/F");
   tree->Branch("E_j2"                  , &E_j2                 , "E_j2/F");
   tree->Branch("E_j3"                  , &E_j3                 , "E_j3/F");
   tree->Branch("E_j4"                  , &E_j4                 , "E_j4/F");
   tree->Branch("eta_l1"                , &eta_l1               , "eta_l1/F");
   tree->Branch("eta_l2"                , &eta_l2               , "eta_l2/F");
   tree->Branch("eta_j1"                , &eta_j1               , "eta_j1/F");
   tree->Branch("eta_j2"                , &eta_j2               , "eta_j2/F");
   tree->Branch("eta_j3"                , &eta_j3               , "eta_j3/F");
   tree->Branch("eta_j4"                , &eta_j4               , "eta_j4/F");
   tree->Branch("phi_l1"                , &phi_l1               , "phi_l1/F");
   tree->Branch("phi_l2"                , &phi_l2               , "phi_l2/F");
   tree->Branch("phi_j1"                , &phi_j1               , "phi_j1/F");
   tree->Branch("phi_j2"                , &phi_j2               , "phi_j2/F");
   tree->Branch("phi_j3"                , &phi_j3               , "phi_j3/F");
   tree->Branch("phi_j4"                , &phi_j4               , "phi_j4/F");
   tree->Branch("MZ"                    , &MZ                   , "MZ/F");
   tree->Branch("pt_z"                  , &pt_z                 , "pt_z/F");
   tree->Branch("eta_z"                 , &eta_z                , "eta_z/F");
   tree->Branch("phi_z"                 , &phi_z                , "phi_z/F");
   tree->Branch("M_j1j2 "               , &M_j1j2               , "M_j1j2/F");
   tree->Branch("M_j1j3 "               , &M_j1j3               , "M_j1j3/F");
   tree->Branch("M_j1j4 "               , &M_j1j4               , "M_j1j4/F");
   tree->Branch("M_j2j3 "               , &M_j2j3               , "M_j2j3/F");
   tree->Branch("M_j2j4 "               , &M_j2j4               , "M_j2j4/F");
   tree->Branch("M_j3j4 "               , &M_j3j4               , "M_j3j4/F");
   tree->Branch("pt_j1j2"               , &pt_j1j2              , "pt_j1j2/F");
   tree->Branch("pt_j1j3"               , &pt_j1j3              , "pt_j1j3/F");
   tree->Branch("pt_j1j4"               , &pt_j1j4              , "pt_j1j4/F");
   tree->Branch("pt_j2j3"               , &pt_j2j3              , "pt_j2j3/F");
   tree->Branch("pt_j2j4"               , &pt_j2j4              , "pt_j2j4/F");
   tree->Branch("pt_j3j4"               , &pt_j3j4              , "pt_j3j4/F");
   tree->Branch("eta_j1j2"              , &eta_j1j2             , "eta_j1j2/F");
   tree->Branch("eta_j1j3"              , &eta_j1j3             , "eta_j1j3/F");
   tree->Branch("eta_j1j4"              , &eta_j1j4             , "eta_j1j4/F");
   tree->Branch("eta_j2j3"              , &eta_j2j3             , "eta_j2j3/F");
   tree->Branch("eta_j2j4"              , &eta_j2j4             , "eta_j2j4/F");
   tree->Branch("eta_j3j4"              , &eta_j3j4             , "eta_j3j4/F");
   tree->Branch("phi_j1j2"              , &phi_j1j2             , "phi_j1j2/F");
   tree->Branch("phi_j1j3"              , &phi_j1j3             , "phi_j1j3/F");
   tree->Branch("phi_j1j4"              , &phi_j1j4             , "phi_j1j4/F");
   tree->Branch("phi_j2j3"              , &phi_j2j3             , "phi_j2j3/F");
   tree->Branch("phi_j2j4"              , &phi_j2j4             , "phi_j2j4/F");
   tree->Branch("phi_j3j4"              , &phi_j3j4             , "phi_j3j4/F");
   tree->Branch("MH2_1"                 , &MH2_1                , "MH2_1/F");
   tree->Branch("MH2_2"                 , &MH2_2                , "MH2_2/F");
   tree->Branch("MH2_3"                 , &MH2_3                , "MH2_3/F");
   tree->Branch("MH2_4"                 , &MH2_4                , "MH2_4/F");
   tree->Branch("MH2_5"                 , &MH2_5                , "MH2_5/F");
   tree->Branch("MH2_6"                 , &MH2_6                , "MH2_6/F");
   tree->Branch("MA3"                   , &MA3                  , "MA3/F");
   tree->Branch("pt_A3"                 , &pt_A3                , "pt_A3/F");
   tree->Branch("eta_A3"                , &eta_A3               , "eta_A3/F");
   tree->Branch("phi_A3"                , &phi_A3               , "phi_A3/F");
   tree->Branch("cos_j1j2"              , &cos_j1j2             , "cos_j1j2/F");
   tree->Branch("cos_j1j3"              , &cos_j1j3             , "cos_j1j3/F");
   tree->Branch("cos_j1j4"              , &cos_j1j4             , "cos_j1j4/F");
   tree->Branch("cos_j2j3"              , &cos_j2j3             , "cos_j2j3/F");
   tree->Branch("cos_j2j4"              , &cos_j2j4             , "cos_j2j4/F");
   tree->Branch("cos_j3j4"              , &cos_j3j4             , "cos_j3j4/F");
   tree->Branch("cos_j1lep1"            , &cos_j1lep1           , "cos_j1lep1/F");
   tree->Branch("cos_j1lep2"            , &cos_j1lep2           , "cos_j1lep2/F");
   tree->Branch("cos_j2lep1"            , &cos_j2lep1           , "cos_j2lep1/F");
   tree->Branch("cos_j2lep2"            , &cos_j2lep2           , "cos_j2lep2/F");
   tree->Branch("cos_j3lep1"            , &cos_j3lep1           , "cos_j3lep1/F");
   tree->Branch("cos_j3lep2"            , &cos_j3lep2           , "cos_j3lep2/F");
   tree->Branch("cos_j4lep1"            , &cos_j4lep1           , "cos_j4lep1/F");
   tree->Branch("cos_j4lep2"            , &cos_j4lep2           , "cos_j4lep2/F");
   tree->Branch("cos_lep1lep2"          , &cos_lep1lep2         , "cos_lep1lep2/F");
   tree->Branch("DR_j1j2"               , &DR_j1j2              , "DR_j1j2/F");
   tree->Branch("DR_j1j3"               , &DR_j1j3              , "DR_j1j3/F");
   tree->Branch("DR_j1j4"               , &DR_j1j4              , "DR_j1j4/F");
   tree->Branch("DR_j2j3"               , &DR_j2j3              , "DR_j2j3/F");
   tree->Branch("DR_j2j4"               , &DR_j2j4              , "DR_j2j4/F");
   tree->Branch("DR_j3j4"               , &DR_j3j4              , "DR_j3j4/F");
   tree->Branch("DR_j1lep1"             , &DR_j1lep1            , "DR_j1lep1/F");
   tree->Branch("DR_j1lep2"             , &DR_j1lep2            , "DR_j1lep2/F");
   tree->Branch("DR_j2lep1"             , &DR_j2lep1            , "DR_j2lep1/F");
   tree->Branch("DR_j2lep2"             , &DR_j2lep2            , "DR_j2lep2/F");
   tree->Branch("DR_j3lep1"             , &DR_j3lep1            , "DR_j3lep1/F");
   tree->Branch("DR_j3lep2"             , &DR_j3lep2            , "DR_j3lep2/F");
   tree->Branch("DR_j4lep1"             , &DR_j4lep1            , "DR_j4lep1/F");
   tree->Branch("DR_j4lep2"             , &DR_j4lep2            , "DR_j4lep2/F");
   tree->Branch("DR_lep1lep2"           , &DR_lep1lep2          , "DR_lep1lep2/F");
   tree->Branch("DPhi_j1j2"             , &DPhi_j1j2            , "DPhi_j1j2/F");
   tree->Branch("DPhi_j1j3"             , &DPhi_j1j3            , "DPhi_j1j3/F");
   tree->Branch("DPhi_j1j4"             , &DPhi_j1j4            , "DPhi_j1j4/F");
   tree->Branch("DPhi_j2j3"             , &DPhi_j2j3            , "DPhi_j2j3/F");
   tree->Branch("DPhi_j2j4"             , &DPhi_j2j4            , "DPhi_j2j4/F");
   tree->Branch("DPhi_j3j4"             , &DPhi_j3j4            , "DPhi_j3j4/F");
   tree->Branch("DPhi_j1lep1"           , &DPhi_j1lep1          , "DPhi_j1lep1/F");
   tree->Branch("DPhi_j1lep2"           , &DPhi_j1lep2          , "DPhi_j1lep2/F");
   tree->Branch("DPhi_j2lep1"           , &DPhi_j2lep1          , "DPhi_j2lep1/F");
   tree->Branch("DPhi_j2lep2"           , &DPhi_j2lep2          , "DPhi_j2lep2/F");
   tree->Branch("DPhi_j3lep1"           , &DPhi_j3lep1          , "DPhi_j3lep1/F");
   tree->Branch("DPhi_j3lep2"           , &DPhi_j3lep2          , "DPhi_j3lep2/F");
   tree->Branch("DPhi_j4lep1"           , &DPhi_j4lep1          , "DPhi_j4lep1/F");
   tree->Branch("DPhi_j4lep2"           , &DPhi_j4lep2          , "DPhi_j4lep2/F");
   tree->Branch("DPhi_lep1lep2"         , &DPhi_lep1lep2        , "DPhi_lep1lep2/F");
   tree->Branch("DTheta_j1j2"           , &DTheta_j1j2          , "DTheta_j1j2/F");
   tree->Branch("DTheta_j1j3"           , &DTheta_j1j3          , "DTheta_j1j3/F");
   tree->Branch("DTheta_j1j4"           , &DTheta_j1j4          , "DTheta_j1j4/F");
   tree->Branch("DTheta_j2j3"           , &DTheta_j2j3          , "DTheta_j2j3/F");
   tree->Branch("DTheta_j2j4"           , &DTheta_j2j4          , "DTheta_j2j4/F");
   tree->Branch("DTheta_j3j4"           , &DTheta_j3j4          , "DTheta_j3j4/F");
   tree->Branch("DTheta_j1lep1"         , &DTheta_j1lep1        , "DTheta_j1lep1/F");
   tree->Branch("DTheta_j1lep2"         , &DTheta_j1lep2        , "DTheta_j1lep2/F");
   tree->Branch("DTheta_j2lep1"         , &DTheta_j2lep1        , "DTheta_j2lep1/F");
   tree->Branch("DTheta_j2lep2"         , &DTheta_j2lep2        , "DTheta_j2lep2/F");
   tree->Branch("DTheta_j3lep1"         , &DTheta_j3lep1        , "DTheta_j3lep1/F");
   tree->Branch("DTheta_j3lep2"         , &DTheta_j3lep2        , "DTheta_j3lep2/F");
   tree->Branch("DTheta_j4lep1"         , &DTheta_j4lep1        , "DTheta_j4lep1/F");
   tree->Branch("DTheta_j4lep2"         , &DTheta_j4lep2        , "DTheta_j4lep2/F");
   tree->Branch("DTheta_lep1lep2"       , &DTheta_lep1lep2      , "DTheta_lep1lep2/F");
   tree->Branch("xs_weight"             , &xs_weight            , "xs_weight/F");

   //Input file
   ifstream in;
   in.open(inpFile.c_str());
   //Input file clone (fro cross check)
   ofstream cout(inpClone.c_str());

   //Count number of lines
   Int_t nlines =0;

   //Loop over the full available information
   //while (1) {
   while ( nlines < NumLines ) {
        // input information
        in >> pt_l1          
           >> pt_l2          
           >> pt_jet1        
           >> pt_jet2        
           >> pt_jet3        
           >> pt_jet4        
           >> E_l1           
           >> E_l2           
           >> E_j1           
           >> E_j2           
           >> E_j3           
           >> E_j4           
           >> eta_l1         
           >> eta_l2         
           >> eta_j1         
           >> eta_j2         
           >> eta_j3         
           >> eta_j4         
           >> phi_l1         
           >> phi_l2         
           >> phi_j1         
           >> phi_j2         
           >> phi_j3         
           >> phi_j4         
           >> MZ             
           >> pt_z           
           >> eta_z          
           >> phi_z          
           >> M_j1j2         
           >> M_j1j3         
           >> M_j1j4         
           >> M_j2j3         
           >> M_j2j4         
           >> M_j3j4         
           >> pt_j1j2        
           >> pt_j1j3        
           >> pt_j1j4        
           >> pt_j2j3        
           >> pt_j2j4        
           >> pt_j3j4        
           >> eta_j1j2       
           >> eta_j1j3       
           >> eta_j1j4       
           >> eta_j2j3       
           >> eta_j2j4       
           >> eta_j3j4       
           >> phi_j1j2       
           >> phi_j1j3       
           >> phi_j1j4       
           >> phi_j2j3       
           >> phi_j2j4       
           >> phi_j3j4       
           >> MH2_1          
           >> MH2_2          
           >> MH2_3          
           >> MH2_4          
           >> MH2_5          
           >> MH2_6          
           >> MA3            
           >> pt_A3          
           >> eta_A3         
           >> phi_A3         
           >> cos_j1j2       
           >> cos_j1j3       
           >> cos_j1j4       
           >> cos_j2j3       
           >> cos_j2j4       
           >> cos_j3j4       
           >> cos_j1lep1     
           >> cos_j1lep2     
           >> cos_j2lep1     
           >> cos_j2lep2     
           >> cos_j3lep1     
           >> cos_j3lep2     
           >> cos_j4lep1     
           >> cos_j4lep2     
           >> cos_lep1lep2   
           >> DR_j1j2        
           >> DR_j1j3        
           >> DR_j1j4        
           >> DR_j2j3        
           >> DR_j2j4        
           >> DR_j3j4        
           >> DR_j1lep1      
           >> DR_j1lep2      
           >> DR_j2lep1      
           >> DR_j2lep2      
           >> DR_j3lep1      
           >> DR_j3lep2      
           >> DR_j4lep1      
           >> DR_j4lep2      
           >> DR_lep1lep2    
           >> DPhi_j1j2      
           >> DPhi_j1j3      
           >> DPhi_j1j4      
           >> DPhi_j2j3      
           >> DPhi_j2j4      
           >> DPhi_j3j4      
           >> DPhi_j1lep1    
           >> DPhi_j1lep2    
           >> DPhi_j2lep1    
           >> DPhi_j2lep2    
           >> DPhi_j3lep1    
           >> DPhi_j3lep2    
           >> DPhi_j4lep1    
           >> DPhi_j4lep2    
           >> DPhi_lep1lep2  
           >> DTheta_j1j2    
           >> DTheta_j1j3    
           >> DTheta_j1j4    
           >> DTheta_j2j3    
           >> DTheta_j2j4    
           >> DTheta_j3j4    
           >> DTheta_j1lep1  
           >> DTheta_j1lep2  
           >> DTheta_j2lep1  
           >> DTheta_j2lep2  
           >> DTheta_j3lep1  
           >> DTheta_j3lep2  
           >> DTheta_j4lep1  
           >> DTheta_j4lep2  
           >> DTheta_lep1lep2
           >> xs_weight;      

	     //Check the end of file found (Avoid duplication of last line)
	     if (in.eof()) break;
        // Print out information
        cout << " " << pt_l1          
             << " " << pt_l2          
             << " " << pt_jet1        
             << " " << pt_jet2        
             << " " << pt_jet3        
             << " " << pt_jet4        
             << " " << E_l1           
             << " " << E_l2           
             << " " << E_j1           
             << " " << E_j2           
             << " " << E_j3           
             << " " << E_j4           
             << " " << eta_l1         
             << " " << eta_l2         
             << " " << eta_j1         
             << " " << eta_j2         
             << " " << eta_j3         
             << " " << eta_j4         
             << " " << phi_l1         
             << " " << phi_l2         
             << " " << phi_j1         
             << " " << phi_j2         
             << " " << phi_j3         
             << " " << phi_j4         
             << " " << MZ             
             << " " << pt_z           
             << " " << eta_z          
             << " " << phi_z          
             << " " << M_j1j2         
             << " " << M_j1j3         
             << " " << M_j1j4         
             << " " << M_j2j3         
             << " " << M_j2j4         
             << " " << M_j3j4         
             << " " << pt_j1j2        
             << " " << pt_j1j3        
             << " " << pt_j1j4        
             << " " << pt_j2j3        
             << " " << pt_j2j4        
             << " " << pt_j3j4        
             << " " << eta_j1j2       
             << " " << eta_j1j3       
             << " " << eta_j1j4       
             << " " << eta_j2j3       
             << " " << eta_j2j4       
             << " " << eta_j3j4       
             << " " << phi_j1j2       
             << " " << phi_j1j3       
             << " " << phi_j1j4       
             << " " << phi_j2j3       
             << " " << phi_j2j4       
             << " " << phi_j3j4       
             << " " << MH2_1          
             << " " << MH2_2          
             << " " << MH2_3          
             << " " << MH2_4          
             << " " << MH2_5          
             << " " << MH2_6          
             << " " << MA3            
             << " " << pt_A3          
             << " " << eta_A3         
             << " " << phi_A3         
             << " " << cos_j1j2       
             << " " << cos_j1j3       
             << " " << cos_j1j4       
             << " " << cos_j2j3       
             << " " << cos_j2j4       
             << " " << cos_j3j4       
             << " " << cos_j1lep1     
             << " " << cos_j1lep2     
             << " " << cos_j2lep1     
             << " " << cos_j2lep2     
             << " " << cos_j3lep1     
             << " " << cos_j3lep2     
             << " " << cos_j4lep1     
             << " " << cos_j4lep2     
             << " " << cos_lep1lep2   
             << " " << DR_j1j2        
             << " " << DR_j1j3        
             << " " << DR_j1j4        
             << " " << DR_j2j3        
             << " " << DR_j2j4        
             << " " << DR_j3j4        
             << " " << DR_j1lep1      
             << " " << DR_j1lep2      
             << " " << DR_j2lep1      
             << " " << DR_j2lep2      
             << " " << DR_j3lep1      
             << " " << DR_j3lep2      
             << " " << DR_j4lep1      
             << " " << DR_j4lep2      
             << " " << DR_lep1lep2    
             << " " << DPhi_j1j2      
             << " " << DPhi_j1j3      
             << " " << DPhi_j1j4      
             << " " << DPhi_j2j3      
             << " " << DPhi_j2j4      
             << " " << DPhi_j3j4      
             << " " << DPhi_j1lep1    
             << " " << DPhi_j1lep2    
             << " " << DPhi_j2lep1    
             << " " << DPhi_j2lep2    
             << " " << DPhi_j3lep1    
             << " " << DPhi_j3lep2    
             << " " << DPhi_j4lep1    
             << " " << DPhi_j4lep2    
             << " " << DPhi_lep1lep2  
             << " " << DTheta_j1j2    
             << " " << DTheta_j1j3    
             << " " << DTheta_j1j4    
             << " " << DTheta_j2j3    
             << " " << DTheta_j2j4    
             << " " << DTheta_j3j4    
             << " " << DTheta_j1lep1  
             << " " << DTheta_j1lep2  
             << " " << DTheta_j2lep1  
             << " " << DTheta_j2lep2  
             << " " << DTheta_j3lep1  
             << " " << DTheta_j3lep2  
             << " " << DTheta_j4lep1  
             << " " << DTheta_j4lep2  
             << " " << DTheta_lep1lep2
             << " " << xs_weight     
             << endl;   
	     //update number of lines
	     nlines ++;
	     //fill tree
	     tree->Fill();
   }
   //write tree      
   tree->Write();
   // close output file
   hfile->Close();
   // end
   printf(" found %d points \n",nlines );

}
