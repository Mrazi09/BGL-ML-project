(* ::Package:: *)

ParticleDefinitions[GaugeES] = {

(* -------------------------GaugeES Higgses ------------------------- *)

    {H10,{
        Description -> "Neutral component of the first Higgs doublet",
        PDG -> {0},
        PDG.IX -> {0},
        Mass -> Automatic,
        FeynArtsNr -> 1,
        LaTeX -> "H^0_1",
        OutputName -> "H10" }},

    {H20,{
        Description -> "Neutral component of the second Higgs doublet",
        PDG -> {0},
        PDG.IX -> {0},
        Mass -> Automatic,
        FeynArtsNr -> 3,
        LaTeX -> "H^0_2",
        OutputName -> "H20" }},

    {S0,{
        Description -> "the third Higgs singlet",
        PDG -> {0},
        PDG.IX -> {0},
        Mass -> Automatic,
        FeynArtsNr -> 5,
        LaTeX -> "S^0",
        OutputName -> "S0" }},

    {H1p,{
        Description -> "Charged component of the first Higgs doublet",
        PDG -> {0},
        PDG.IX -> {0},
        Mass -> Automatic,
        FeynArtsNr -> 2,
        LaTeX -> "H^+_1",
        OutputName -> "H1p" }},

    {H2p,{
        Description -> "Charged component of the second Higgs doublet",
        PDG -> {0},
        PDG.IX -> {0},
        Mass -> Automatic,
        FeynArtsNr -> 4,
        LaTeX -> "H^+_2",
        OutputName -> "H2p" }},



(* -------------------------GaugeES Bosons ------------------------- *)

    {VB,{Description -> "B-Boson"}},
    (*{VBp,{Description -> "B-prime-Boson",
          PDG -> {0},
          PDG.IX -> {0},
          Width -> 0,
          Mass -> 0,
          FeynArtsNr -> 6,
          LaTeX -> "B_p",
          OutputName -> "Bp" }},*)
    {VG,{Description -> "Gluon"}},
    {VWB,{Description -> "W-Bosons"}},

(* ----------------------------------GaugeES Ghosts ----------------------------- *)

    {gB,{Description -> "B-Boson Ghost"}},
    (*{gBp,{Description -> "B-prime-Boson Ghost",
        PDG -> {0},
        PDG.IX -> {0},
        Width -> 0,
        Mass -> 0,
        FeynArtsNr -> 7,
        LaTeX -> "\\eta^{B_p}",
        OutputName -> "gBp" }},*)
    {gG,{Description -> "Gluon Ghost"}},
    {gWB,{Description -> "W-Boson Ghost"}},



    {FDLd1,   {Description -> "Dirac Left Down-Quark 1",
                FeynArtsNr -> 120,
                LaTeX -> "d^1_{\\mathrm{D-L}}",
                Mass -> LesHouches,
                OutputName -> "dDL1",
                PDG -> {1},
                Width -> {0}}},

    {FDLd2,   {Description -> "Dirac Left Down-Quark 2",
                FeynArtsNr -> 121,
                LaTeX -> "d^2_{\\mathrm{D-L}}",
                Mass -> LesHouches,
                OutputName -> "dDL2",
                PDG -> {3},
                Width -> {0}}},

    {FDLd3,   {Description -> "Dirac Left Down-Quark 3",
                FeynArtsNr -> 123,
                LaTeX -> "d^3_{\\mathrm{D-L}}",
                Mass -> LesHouches,
                OutputName -> "dDL3",
                PDG -> {5},
                Width -> {0}}},

    {FDRd1,     {Description -> "Dirac Right Down-Quark 1",
                FeynArtsNr -> 124,
                LaTeX -> "d^1_{\\mathrm{D-R}}",
                Mass -> LesHouches,
                OutputName -> "dDR1",
                PDG -> {0},
                Width -> {0}}},

    {FDRd2,     {Description -> "Dirac Right Down-Quark 2",
                FeynArtsNr -> 125,
                LaTeX -> "d^2_{\\mathrm{D-R}}",
                Mass -> LesHouches,
                OutputName -> "dDR2",
                PDG -> {0},
                Width -> {0}}},

    {FDRd3,     {Description -> "Dirac Right Down-Quark 3",
                FeynArtsNr -> 126,
                LaTeX -> "d^3_{\\mathrm{D-R}}",
                Mass -> LesHouches,
                OutputName -> "dDR3",
                PDG -> {0},
                Width -> {0}}},

    {FDLu1,     {Description -> "Dirac Left Up-Quark 1",
                FeynArtsNr -> 127,
                LaTeX -> "u^1_{\\mathrm{D-L}}",
                Mass -> LesHouches,
                OutputName -> "uDL1",
                PDG -> {2},
                Width -> {0}}},

    {FDLu2,     {Description -> "Dirac Left Up-Quark 2",
                FeynArtsNr -> 128,
                LaTeX -> "u^2_{\\mathrm{D-L}}",
                Mass -> LesHouches,
                OutputName -> "uDL2",
                PDG -> {4},
                Width -> {0}}},

    {FDLu3,     {Description -> "Dirac Left Up-Quark 2",
                FeynArtsNr -> 129,
                LaTeX -> "u^2_{\\mathrm{D-L}}",
                Mass -> LesHouches,
                OutputName -> "uDL3",
                PDG -> {6},
                Width -> {0}}},

    {FDRu1,     {Description -> "Dirac Right Up-Quark 1",
                FeynArtsNr -> 130,
                LaTeX -> "u^1_{\\mathrm{D-R}}",
                Mass -> LesHouches,
                OutputName -> "uDR1",
                PDG -> {0},
                Width -> {0}}},

    {FDRu2,     {Description -> "Dirac Right Up-Quark 2",
                FeynArtsNr -> 131,
                LaTeX -> "u^2_{\\mathrm{D-R}}",
                Mass -> LesHouches,
                OutputName -> "uDR2",
                PDG -> {0},
                Width -> {0}}},

    {FDRu3,     {Description -> "Dirac Right Up-Quark 3",
                FeynArtsNr -> 132,
                LaTeX -> "u^3_{\\mathrm{D-R}}",
                Mass -> LesHouches,
                OutputName -> "uDR3",
                PDG -> {0},
                Width -> {0}}},

    {FDLe1,     {Description -> "Dirac Left Electron 1",
                FeynArtsNr -> 133,
                LaTeX -> "e^1_{\\mathrm{D-L}}",
                Mass -> LesHouches,
                OutputName -> "eDL1",
                PDG -> {11},
                Width -> {0}}},

    {FDLe2,     {Description -> "Dirac Left Electron 2",
                FeynArtsNr -> 134,
                LaTeX -> "e^2_{\\mathrm{D-L}}",
                Mass -> LesHouches,
                OutputName -> "eDL2",
                PDG -> {13},
                Width -> {0}}},

    {FDLe3,     {Description -> "Dirac Left Electron 3",
                FeynArtsNr -> 135,
                LaTeX -> "e^3_{\\mathrm{D-L}}",
                Mass -> LesHouches,
                OutputName -> "eDL3",
                PDG -> {15},
                Width -> {0}}},

    {FDRe1,     {Description -> "Dirac Right Electron 1",
                FeynArtsNr -> 136,
                LaTeX -> "e^1_{\\mathrm{D-R}}",
                Mass -> LesHouches,
                OutputName -> "eDR1",
                PDG -> {0},
                Width -> {0}}},

    {FDRe2,     {Description -> "Dirac Right Electron 2",
                FeynArtsNr -> 137,
                LaTeX -> "e^2_{\\mathrm{D-R}}",
                Mass -> LesHouches,
                OutputName -> "eDR2",
                PDG -> {0},
                Width -> {0}}},

    {FDRe3,     {Description -> "Dirac Right Electron 3",
                FeynArtsNr -> 138,
                LaTeX -> "e^3_{\\mathrm{D-R}}",
                Mass -> LesHouches,
                OutputName -> "eDR3",
                PDG -> {0},
                Width -> {0}}},

    {FDLv1,     {Description -> "Dirac Left Neutrino 1",
                FeynArtsNr -> 139,
                LaTeX -> "\\nu^1_{\\mathrm{D-L}}",
                Mass -> LesHouches,
                OutputName -> "vDL1",
                PDG -> {12},
                Width -> {0}}},

    {FDLv2,     {Description -> "Dirac Left Neutrino 2",
                FeynArtsNr -> 140,
                LaTeX -> "\\nu^2_{\\mathrm{D-L}}",
                Mass -> LesHouches,
                OutputName -> "vDL2",
                PDG -> {14},
                Width -> {0}}},

    {FDLv3,     {Description -> "Dirac Left Neutrino 3",
                FeynArtsNr -> 141,
                LaTeX -> "\\nu^3_{\\mathrm{D-L}}",
                Mass -> LesHouches,
                OutputName -> "vDL3",
                PDG -> {16},
                Width -> {0}}},

    {FDRv1 ,     {Description -> "Dirac Right Neutrino 1",
                FeynArtsNr -> 142,
                LaTeX -> "\\nu^1_{\\mathrm{D-R}}",
                Mass -> LesHouches,
                OutputName -> "vDR1",
                PDG -> {8810012},
                Width -> {0}}},

    {FDRv2 ,     {Description -> "Dirac Right Neutrino 2",
                FeynArtsNr -> 143,
                LaTeX -> "\\nu^2_{\\mathrm{D-R}}",
                Mass -> LesHouches,
                OutputName -> "vDR2",
                PDG -> {8810014},
                Width -> {0}}},

    {FDRv3 ,     {Description -> "Dirac Right Neutrino 3",
                FeynArtsNr -> 144,
                LaTeX -> "\\nu^3_{\\mathrm{D-R}}",
                Mass -> LesHouches,
                OutputName -> "vDR3",
                PDG -> {8810016},
                Width -> {0}}}

};

ParticleDefinitions[EWSB] = {

(* ---------------------------------------EWSB Higgs -----------------------------------------*)

{hh, {   Description -> "Higgs",
          PDG -> {25, 26, 27},
          Width -> {Automatic, Automatic, Automatic},
          Mass -> LesHouches,
          FeynArtsNr -> 8,
          LaTeX -> "h",
          ElectricCharge -> 0,
          OutputName -> "h" }},

{Ah, {   Description -> "Pseudo-Scalar Higgs",
          PDG -> {0, 35, 36},
          Width -> {0, 0, Automatic},
          Mass -> LesHouches,
          FeynArtsNr -> 9,
          LaTeX -> "A^0",
          ElectricCharge -> 0,
          OutputName -> "Ah" }},


{Hm, {   Description -> "Charged Higgs",
          PDG -> {0, -37},
          PDG.IX ->{0, -100000601},
          Width -> {0, Automatic},
          Mass -> LesHouches,
          FeynArtsNr -> 11,
          LaTeX -> "H^-",
          ElectricCharge -> -1,
          OutputName -> "Hm" }},

(* -----------------------------------EWSB Bosons -----------------------------------------*)

{VP,  {Description -> "Photon"}},
{VZ,  {Description -> "Z-Boson",
        Goldstone -> Ah[{1}]}},
(*{VZp,   {Description -> "Z-prime-Boson",
        PDG -> {31},
        PDG.IX ->{122000002},
        FeynArtsNr -> 9,
        ElectricCharge -> 0,
        Width -> Automatic,
        Mass -> LesHouches,
        Goldstone -> Ah[{2}],
        LaTeX -> "Z^{\\prime}",
        OutputName -> "Zp" }},*)

{VG,    {Description -> "Gluon"}},
{VWm,   {Description -> "W-Boson",
        Goldstone -> Hm[{1}]}},


(* -----------------------------------EWSB Ghosts -----------------------------------*)


{gP,  {Description -> "Photon Ghost"}},
(*{gWp,  { Description -> "Positive W+ - Boson Ghost"}},
{gWpC, { Description -> "Negative W+ - Boson Ghost" }}, *)

{gWm, {Description -> "Negative W Boson Ghost",
      PDG -> 0,
      PDG.IX -> 0,
      Mass -> Mass[VWm],
      Width -> Automatic,
      FeynArtsNr -> 10,
      ElectricCharge -> -1,
      LaTeX -> "\\eta^-",
      OutputName -> "gWm"}},
{gWmC,{Description -> "Positive W Boson Ghost",
      PDG -> 0,
      PDG.IX -> 0,
      Width -> Automatic,
      FeynArtsNr -> 14,
      ElectricCharge -> 1,
      LaTeX -> "\\eta^+",
      OutputName -> "gWp"}},

{gZ,  {Description -> "Z-Boson Ghost"}},
(*{gZp, {Description -> "Z-prime-Boson Ghost",
      PDG -> 0,
      PDG.IX -> 0,
      Mass -> Mass[VZp],
      Width -> Automatic,
      FeynArtsNr -> 12,
      ElectricCharge -> 0,
      LaTeX -> "\\eta^{Z^{\\prime}}",
      OutputName -> "gZp" }},*)
{gG,  {Description -> "Gluon Ghost"}},

(* -----------------------------------EWSB Dirac fermions -----------------------------------*)

{Fd,  {Description -> "Down-Quarks"}},
{Fu,  {Description -> "Up-Quarks"}},
{Fe,  {Description -> "Leptons" }},
{Fv,{   Description -> "Neutrinos",
            PDG ->{12,14,16,8810012,8810014,8810016},
            ElectricCharge -> 0,
            Width -> {Automatic,Automatic,Automatic,Automatic,Automatic,Automatic},
            Mass -> LesHouches,
            FeynArtsNr -> 13,
            LaTeX -> "\\nu",
            OutputName -> "nu"}}
    };

(* -----------------------------------Weyl Fermios -----------------------------------*)
WeylFermionAndIndermediate = {

    {H1,{
        Description -> "First Higgs doublet",
        LaTeX -> "H_1",
        OutputName -> "" }},

    {H2,{
        Description -> "Second Higgs doublet",
        LaTeX -> "H_2",
        OutputName -> "" }},


    {S,{
        Description -> "Higgs singlet",
        LaTeX -> "S",
        OutputName -> "" }},
(*
    {v0,{
        Description -> "Right-Neutrino 1",
        Latex -> "v^R_1"}},

    {vp,{
        Description -> "Right-Neutrino 2",
        Latex -> "v^R_2"}},

    {vm,{
        Description -> "Right-Neutrino 3",
        Latex -> "v^R_3"}},
*)
    {q1,{LaTeX -> "q_1"}},
    {q2,{LaTeX -> "q_2"}},
    {q3,{LaTeX -> "q_3"}},

    {l1,{LaTeX -> "l_1"}},
    {l2,{LaTeX -> "l_2"}},
    {l3,{LaTeX -> "l_3"}},

    {d1,{LaTeX -> "d1"}},
    {d2,{LaTeX -> "d2"}},
    {d3,{LaTeX -> "d3"}},

    {uu1,{LaTeX -> "u1"}},
    {uu2,{LaTeX -> "u2"}},
    {uu3,{LaTeX -> "u3"}},

    {ee1,{LaTeX -> "e1"}},
    {ee2,{LaTeX -> "e2"}},
    {ee3,{LaTeX -> "e3"}},

    {e1L,{LaTeX -> "e1_L" }},
    {e2L,{LaTeX -> "e2_L"}},
    {e3L,{LaTeX -> "e3_L"}},
    {e1R,{LaTeX -> "e1_R"}},
    {e2R,{LaTeX -> "e2_R"}},
    {e3R,{LaTeX -> "e3_R"}},

    {v1L,{LaTeX -> "v1_L"}},
    {v2L,{LaTeX -> "v2_L"}},
    {v3L,{LaTeX -> "v3_L"}},

    {d1L,{LaTeX -> "d1_L"}},
    {d2L,{LaTeX -> "d2_L"}},
    {d3L,{LaTeX -> "d3_L"}},
    {d1R,{LaTeX -> "d1_R"}},
    {d2R,{LaTeX -> "d2_R"}},
    {d3R,{LaTeX -> "d3_R"}},

    {u1L,{LaTeX -> "u1_L"}},
    {u2L,{LaTeX -> "u2_L"}},
    {u3L,{LaTeX -> "u3_L"}},
    {u1R,{LaTeX -> "u1_R"}},
    {u2R,{LaTeX -> "u2_R"}},
    {u3R,{LaTeX -> "u3_R"}},

    {v01R,{LaTeX -> "v1_R"}},
    {v02R,{LaTeX -> "v2_R"}},
    {v03R,{LaTeX -> "v3_R"}},


    {EL,{
        Description -> "Rotated Left Electron",
        LaTeX -> "E_L",
        OutputName -> "" }},

    {ER,{
        Description -> "Rotated Right Electron",
        LaTeX -> "E_R",
        OutputName -> "" }},

    {DL,{
        Description -> "Rotated Left Up-Quark",
        LaTeX -> "D_L",
        OutputName -> "" }},

    {DR,{
        Description -> "Rotated Right Up-Quark",
        LaTeX -> "D_R",
        OutputName -> "" }},

    {UL,{
        Description -> "Rotated Left Down-Quark",
        LaTeX -> "U_L",
        OutputName -> "" }},

    {UR,{
        Description -> "Rotated Right Down-Quark",
        LaTeX -> "U_R",
        OutputName -> "" }},

    {VL,{
        Description -> "Rotated neutrino",
        LaTeX -> "N_L",
        OutputName -> "" }},

    {sigma1, {LaTeX -> "\\sigma_1"}},
	{sigma2, {LaTeX -> "\\sigma_2"}},
	{sigma3, {LaTeX -> "\\sigma_3"}},

	{phi1, {LaTeX -> "\\phi_1"}},
	{phi2, {LaTeX -> "\\phi_2"}},
	{phi3, {LaTeX -> "\\phi_3"}}


};
