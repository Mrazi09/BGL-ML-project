(* ::Package:: *)

ParameterDefinitions = {

{g1,        { Description -> "Hypercharge-Coupling"}},

{g2,        { Description -> "Left-Coupling"}},

{g3,        { Description -> "Strong-Coupling"}},

(*{g4,        { Description -> "BGL-Coupling",
							LaTeX -> "g_4",
							Dependence -> None,
							LesHouches -> {HMIX,60},
							OutputName-> g4   }},

{g14,        { Description -> "BGL-Coupling 2",
							LaTeX -> "g_14",
							Dependence -> None,
							LesHouches -> {HMIX,61},
							OutputName-> g14   }},

{g41,        { Description -> "BGL-Coupling 3",
							LaTeX -> "g_41",
							Dependence -> None,
							LesHouches -> {HMIX,62},
							OutputName-> g41   }},*)

{AlphaS,    {Description -> "Alpha Strong"}},
{e,         { Description -> "electric charge"}},

{Gf,        { Description -> "Fermi's constant"}},
{aEWinv,    { Description -> "inverse weak coupling constant at mZ"}},

(*-----------------------------------------------------------------------------------------------*)
(*Yukawa terms*)
(*Up-type quark Yukawa terms:*)
{Y1u11,       { Description -> "Up-Yukawa1-Coupling-11",
			        LaTeX -> "Y_{1,11}^u",
							Dependence -> None,
              LesHouches -> {HMIX,44},
              OutputName-> Y1u11            }},

{Y1u12,       { Description -> "Up-Yukawa1-Coupling-12",
              LaTeX -> "Y_{1,12}^u",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
              LesHouches -> {HMIX,45},
              OutputName-> Y1u12            }},
(*
{Y1u13,       { Description -> "Up-Yukawa1-Coupling-13",
              LaTeX -> "Y_{1,13}^u",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
              LesHouches -> {HMIX,46},
              OutputName-> Y1u13            }},
*)
{Y1u21,       { Description -> "Up-Yukawa1-Coupling21",
							LaTeX -> "Y_{1,21}^u",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,47},
							OutputName-> Y1u21            }},

{Y1u22,       { Description -> "Up-Yukawa1-Coupling22",
							LaTeX -> "Y_{1,22}^u",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,48},
							OutputName-> Y1u22            }},
(*
{Y1u23,       { Description -> "Up-Yukawa1-Coupling23",
							LaTeX -> "Y_{1,23}^u",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,49},
							OutputName-> Y1u23            }},
*)(*
{Y1u31,       { Description -> "Up-Yukawa1-Coupling31",
							LaTeX -> "Y_{1,31}^u",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,50},
							OutputName-> Y1u31            }},
{Y1u32,       { Description -> "Up-Yukawa1-Coupling32",
							LaTeX -> "Y_{1,32}^u",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,51},
							OutputName-> Y1u32            }},
{Y1u33,       { Description -> "Up-Yukawa1-Coupling33",
							LaTeX -> "Y_{1,33}^u",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,52},
							OutputName-> Y1u33            }},
*)(*
{Y2u11,       { Description -> "Up-Yukawa2-Coupling11",
							LaTeX -> "Y_{2,11}^u",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,53},
							OutputName-> Y2u11            }},

{Y2u12,       { Description -> "Up-Yukawa2-Coupling12",
							LaTeX -> "Y_{2,12}^u",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,54},
							OutputName-> Y2u12            }},

{Y2u13,       { Description -> "Up-Yukawa2-Coupling13",
							LaTeX -> "Y_{2,13}^u",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,55},
							OutputName-> Y2u13            }},


{Y2u21,       { Description -> "Up-Yukawa2-Coupling21",
							LaTeX -> "Y_{2,21}^u",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,56},
							OutputName-> Y2u21            }},


{Y2u22,       { Description -> "Up-Yukawa2-Coupling22",
							LaTeX -> "Y_{2,22}^u",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,57},
							OutputName-> Y2u22            }},


{Y2u23,       { Description -> "Up-Yukawa2-Coupling23",
							LaTeX -> "Y_{2,23}^u",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,58},
							OutputName-> Y2u23            }},


{Y2u31,       { Description -> "Up-Yukawa2-Coupling31",
							LaTeX -> "Y_{2,31}^u",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,59},
							OutputName-> Y2u31            }},


{Y2u32,       { Description -> "Up-Yukawa2-Coupling32",
							LaTeX -> "Y_{2,32}^u",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,60},
							OutputName-> Y2u32            }},
*)
{Y2u33,       { Description -> "Up-Yukawa2-Coupling33",
							LaTeX -> "Y_{2,33}^u",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,61},
							OutputName-> Y2u33            }},

(*-------------------------------------------------------------------------------------------------*)
(*Down-type quark Yukawa terms*)
{Y1d11,       { Description -> "Down-Yukawa1-Coupling11",
							LaTeX -> "Y_{1,11}^d",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,62},
							OutputName-> Y1d11            }},

{Y1d12,       { Description -> "Down-Yukawa1-Coupling12",
							LaTeX -> "Y_{1,12}^d",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,63},
							OutputName-> Y1d12            }},

{Y1d13,       { Description -> "Down-Yukawa1-Coupling13",
							LaTeX -> "Y_{1,13}^d",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,64},
							OutputName-> Y1d13            }},

{Y1d21,       { Description -> "Down-Yukawa1-Coupling21",
							LaTeX -> "Y_{1,21}^d",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,65},
							OutputName-> Y1d21            }},

{Y1d22,       { Description -> "Down-Yukawa1-Coupling22",
							LaTeX -> "Y_{1,22}^d",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,66},
							OutputName-> Y1d22            }},

{Y1d23,       { Description -> "Down-Yukawa1-Coupling23",
							LaTeX -> "Y_{1,23}^d",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,67},
							OutputName-> Y1d23            }},
(*
{Y1d31,       { Description -> "Down-Yukawa1-Coupling31",
							LaTeX -> "Y_{1,31}^d",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,68},
							OutputName-> Y1d31            }},

{Y1d32,       { Description -> "Down-Yukawa1-Coupling32",
							LaTeX -> "Y_{1,32}^d",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,69},
							OutputName-> Y1d32            }},

{Y1d33,       { Description -> "Down-Yukawa1-Coupling33",
							LaTeX -> "Y_{1,33}^d",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,70},
							OutputName-> Y1d33            }},
*)(*
{Y2d11,       { Description -> "Down-Yukawa2-Coupling11",
							LaTeX -> "Y_{2,11}^d",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,71},
							OutputName-> Y2d11            }},

{Y2d12,       { Description -> "Down-Yukawa2-Coupling12",
							LaTeX -> "Y_{2,12}^d",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,72},
							OutputName-> Y2d12            }},

{Y2d13,       { Description -> "Down-Yukawa2-Coupling13",
							LaTeX -> "Y_{2,13}^d",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,73},
							OutputName-> Y2d13            }},

{Y2d21,       { Description -> "Down-Yukawa2-Coupling21",
							LaTeX -> "Y_{2,21}^d",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,74},
							OutputName-> Y2d21            }},

{Y2d22,       { Description -> "Down-Yukawa2-Coupling22",
							LaTeX -> "Y_{2,22}^d",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,75},
							OutputName-> Y2d22            }},

{Y2d23,       { Description -> "Down-Yukawa2-Coupling23",
							LaTeX -> "Y_{2,23}^d",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,76},
							OutputName-> Y2d23            }},
*)
{Y2d31,       { Description -> "Down-Yukawa2-Coupling31",
							LaTeX -> "Y_{2,31}^d",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,77},
							OutputName-> Y2d31            }},

{Y2d32,       { Description -> "Down-Yukawa2-Coupling32",
							LaTeX -> "Y_{2,32}^d",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,78},
							OutputName-> Y2d32            }},

{Y2d33,       { Description -> "Down-Yukawa2-Coupling33",
							LaTeX -> "Y_{2,33}^d",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,79},
							OutputName-> Y2d33            }},
(*-------------------------------------------------------------------------------------------*)
(*Charged-lepton Yukawa terms*)

{Y1e11,       { Description -> "Charged-Lepton-Yukawa1-Coupling11",
							LaTeX -> "Y_{1,11}^e",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,80},
							OutputName-> Y1e11            }},

{Y1e12,       { Description -> "Charged-Lepton-Yukawa1-Coupling12",
							LaTeX -> "Y_{1,12}^e",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,81},
							OutputName-> Y1e12            }},
(*
{Y1e13,       { Description -> "Charged-Lepton-Yukawa1-Coupling13",
							LaTeX -> "Y_{1,13}^e",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,82},
							OutputName-> Y1e13            }},
*)
{Y1e21,       { Description -> "Charged-Lepton-Yukawa1-Coupling21",
							LaTeX -> "Y_{1,21}^e",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,83},
							OutputName-> Y1e21            }},

{Y1e22,       { Description -> "Charged-Lepton-Yukawa1-Coupling22",
							LaTeX -> "Y_{1,22}^e",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,84},
							OutputName-> Y1e22            }},
(*
{Y1e23,       { Description -> "Charged-Lepton-Yukawa1-Coupling23",
							LaTeX -> "Y_{1,23}^e",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,85},
							OutputName-> Y1e23            }},

{Y1e31,       { Description -> "Charged-Lepton-Yukawa1-Coupling31",
							LaTeX -> "Y_{1,31}^e",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,86},
							OutputName-> Y1e31            }},

{Y1e32,       { Description -> "Charged-Lepton-Yukawa1-Coupling32",
							LaTeX -> "Y_{1,32}^e",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,87},
							OutputName-> Y1e32            }},

{Y1e33,       { Description -> "Charged-Lepton-Yukawa1-Coupling33",
							LaTeX -> "Y_{1,33}^e",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,88},
							OutputName-> Y1e33           }},
*)(*
{Y2e11,       { Description -> "Charged-Lepton-Yukawa2-Coupling11",
							LaTeX -> "Y_{2,11}^e",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,89},
							OutputName-> Y2e11            }},

{Y2e12,       { Description -> "Charged-Lepton-Yukawa2-Coupling12",
							LaTeX -> "Y_{2,12}^e",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,90},
							OutputName-> Y2e12            }},

{Y2e13,       { Description -> "Charged-Lepton-Yukawa2-Coupling13",
							LaTeX -> "Y_{2,13}^e",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,91},
							OutputName-> Y2e13            }},

{Y2e21,       { Description -> "Charged-Lepton-Yukawa2-Coupling21",
							LaTeX -> "Y_{2,21}^e",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,92},
							OutputName-> Y2e21            }},

{Y2e22,       { Description -> "Charged-Lepton-Yukawa2-Coupling22",
							LaTeX -> "Y_{2,22}^e",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,93},
							OutputName-> Y2e22            }},

{Y2e23,       { Description -> "Charged-Lepton-Yukawa2-Coupling23",
							LaTeX -> "Y_{2,23}^e",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,94},
							OutputName-> Y2e23           }},

{Y2e31,       { Description -> "Charged-Lepton-Yukawa2-Coupling31",
							LaTeX -> "Y_{2,31}^e",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,95},
							OutputName-> Y2e31            }},

{Y2e32,       { Description -> "Charged-Lepton-Yukawa2-Coupling32",
							LaTeX -> "Y_{2,32}^e",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,96},
							OutputName-> Y2e32            }},
*)
{Y2e33,       { Description -> "Charged-Lepton-Yukawa2-Coupling33",
							LaTeX -> "Y_{2,33}^e",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,97},
							OutputName-> Y2e33            }},

(*---------------------------------------------------------------------------------------------------*)
(*Neutrino Yukawa terms*)
{Y1n11,       { Description -> "Neutrino-Yukawa1-Coupling11",
							LaTeX -> "Y_{1,11}^n",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,98},
							OutputName-> Y1n11            }},

{Y1n12,       { Description -> "Neutrino-Yukawa1-Coupling12",
							LaTeX -> "Y_{1,12}^n",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,99},
							OutputName-> Y1n12            }},
(*
{Y1n13,       { Description -> "Neutrino-Yukawa1-Coupling13",
							LaTeX -> "Y_{1,13}^n",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,100},
							OutputName-> Y1n13           }},
*)
{Y1n21,       { Description -> "Neutrino-Yukawa1-Coupling21",
							LaTeX -> "Y_{1,21}^n",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,101},
							OutputName-> Y1n21            }},

{Y1n22,       { Description -> "Neutrino-Yukawa1-Coupling22",
							LaTeX -> "Y_{1,22}^n",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,102},
							OutputName-> Y1n22            }},
(*
{Y1n23,       { Description -> "Neutrino-Yukawa1-Coupling23",
							LaTeX -> "Y_{1,23}^n",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,103},
							OutputName-> Y1n23            }},

{Y1n31,       { Description -> "Neutrino-Yukawa1-Coupling31",
							LaTeX -> "Y_{1,31}^n",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,104},
							OutputName-> Y1n31            }},

{Y1n32,       { Description -> "Neutrino-Yukawa1-Coupling32",
							LaTeX -> "Y_{1,32}^n",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,105},
							OutputName-> Y1n32            }},

{Y1n33,       { Description -> "Neutrino-Yukawa1-Coupling33",
							LaTeX -> "Y_{1,33}^n",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,106},
							OutputName-> Y1n33            }},
*)(*
{Y2n11,       { Description -> "Neutrino-Yukawa2-Coupling11",
							LaTeX -> "Y_{2,11}^n",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,107},
							OutputName-> Y2n11            }},

{Y2n12,       { Description -> "Neutrino-Yukawa2-Coupling12",
							LaTeX -> "Y_{2,12}^n",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,108},
							OutputName-> Y2n12            }},

{Y2n13,       { Description -> "Neutrino-Yukawa2-Coupling13",
							LaTeX -> "Y_{2,13}^n",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,109},
							OutputName-> Y2n13            }},

{Y2n21,       { Description -> "Neutrino-Yukawa2-Coupling21",
							LaTeX -> "Y_{2,21}^n",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,110},
							OutputName-> Y2n21            }},

{Y2n22,       { Description -> "Neutrino-Yukawa2-Coupling22",
							LaTeX -> "Y_{2,22}^n",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,111},
							OutputName-> Y2n22            }},

{Y2n23,       { Description -> "Neutrino-Yukawa2-Coupling23",
							LaTeX -> "Y_{2,23}^n",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,112},
							OutputName-> Y2n23            }},

{Y2n31,       { Description -> "Neutrino-Yukawa2-Coupling31",
							LaTeX -> "Y_{2,31}^n",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,113},
							OutputName-> Y2n31            }},

{Y2n32,       { Description -> "Neutrino-Yukawa2-Coupling32",
							LaTeX -> "Y_{2,32}^n",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,114},
							OutputName-> Y2n32            }},
*)
{Y2n33,       { Description -> "Neutrino-Yukawa2-Coupling33",
							LaTeX -> "Y_{2,33}^n",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,115},
							OutputName-> Y2n33            }},

(*--------------------------------------------------------------------------------------*)
(*Majorana couplings*)
(*
{A11,       { Description -> "Majorana-Coupling-A11",
							LaTeX -> "A_{11}",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,116},
							OutputName-> A11            }},

{A12,       { Description -> "Majorana-Coupling-A12",
							LaTeX -> "A_{12}",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,117},
							OutputName-> A12            }},

{A13,       { Description -> "Majorana-Coupling-A13",
							LaTeX -> "A_{13}",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,118},
							OutputName-> A13           }},

{A21,       { Description -> "Majorana-Coupling-A21",
							LaTeX -> "A_{21}",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,119},
							OutputName-> A21            }},

{A22,       { Description -> "Majorana-Coupling-A22",
							LaTeX -> "A_{22}",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,120},
							OutputName-> A22            }},

{A23,       { Description -> "Majorana-Coupling-A23",
							LaTeX -> "A_{23}",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,121},
							OutputName-> A23            }},

{A31,       { Description -> "Majorana-Coupling-A31",
							LaTeX -> "A_{31}",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,122},
							OutputName-> A31            }},

{A32,       { Description -> "Majorana-Coupling-A32",
							LaTeX -> "A_{32}",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,123},
							OutputName-> A32            }},

{A33,       { Description -> "Majorana-Coupling-A33",
							LaTeX -> "A_{33}",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,124},
							OutputName-> A33            }},
*)
(*-----------------------------------------------------------------------------------------*)
(*Majorana-like couplings*)

{BB11,       { Description -> "Majorana-Like-Coupling-B11",
							LaTeX -> "B_{11}",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,125},
							OutputName-> BB11            }},

{BB12,       { Description -> "Majorana-Like-Coupling-B12",
							LaTeX -> "B_{12}",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,126},
							OutputName-> BB12            }},
(*
{BB13,       { Description -> "Majorana-Like-Coupling-B13",
							LaTeX -> "B_{13}",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,127},
							OutputName-> BB13            }},
*)
{BB21,       { Description -> "Majorana-Like-Coupling-B21",
							LaTeX -> "B_{21}",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,128},
							OutputName-> BB21            }},

{BB22,       { Description -> "Majorana-Like-Coupling-B22",
							LaTeX -> "B_{22}",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,129},
							OutputName-> BB22            }},
(*
{B23,       { Description -> "Majorana-Like-Coupling-B23",
							LaTeX -> "B_{23}",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,130},
							OutputName-> B23            }},

{B31,       { Description -> "Majorana-Like-Coupling-B31",
							LaTeX -> "B_{31}",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,131},
							OutputName-> B31            }},

{B32,       { Description -> "Majorana-Like-Coupling-B32",
							LaTeX -> "B_{32}",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,132},
							OutputName-> B32            }},

{B33,       { Description -> "Majorana-Like-Coupling-B33",
							LaTeX -> "B_{33}",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,133},
							OutputName-> B33            }},

{C11,       { Description -> "Majorana-Like-Coupling-C11",
							LaTeX -> "C_{11}",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,134},
							OutputName-> C11            }},

{C12,       { Description -> "Majorana-Like-Coupling-C12",
							LaTeX -> "C_{12}",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,135},
							OutputName-> C12            }},
*)
{C13,       { Description -> "Majorana-Like-Coupling-C13",
							LaTeX -> "C_{13}",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,136},
							OutputName-> C13            }},
(*
{C21,       { Description -> "Majorana-Like-Coupling-C21",
							LaTeX -> "C_{21}",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,137},
							OutputName-> C21            }},

{C22,       { Description -> "Majorana-Like-Coupling-C22",
							LaTeX -> "C_{22}",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,138},
							OutputName-> C22            }},
*)
{C23,       { Description -> "Majorana-Like-Coupling-C23",
							LaTeX -> "C_{23}",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,139},
							OutputName-> C23            }},

{C31,       { Description -> "Majorana-Like-Coupling-C31",
							LaTeX -> "C_{31}",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,140},
							OutputName-> C31            }},

{C32,       { Description -> "Majorana-Like-Coupling-C32",
							LaTeX -> "C_{32}",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,141},
							OutputName-> C32            }},
(*
{C33,       { Description -> "Majorana-Like-Coupling-C33",
							LaTeX -> "C_{33}",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
							LesHouches -> {HMIX,142},
							OutputName-> C33            }},
*)
(*------------------------------------------------------------------------------------------------*)
(*Potential Couplings*)

{Lambda1,    {Description -> "Lambda1",
							LaTeX -> "\\lambda_1",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
              OutputName -> Lam1,
              LesHouches -> {HMIX,31}}},

{Lambda2,    {Description -> "Lambda2",
							LaTeX -> "\\lambda_2",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
              OutputName -> Lam2,
              LesHouches -> {HMIX,32}}},
{Lambda3,    { Description -> "Lambda3",
							LaTeX -> "\\lambda_3",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
              OutputName -> Lam3,
              LesHouches -> {HMIX,33}}},
{Lambda4,    { Description -> "Lambda4",
							LaTeX -> "\\lambda_4",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
              OutputName -> Lam4,
              LesHouches -> {HMIX,34}}},
{Lambda1Dash,    { Description -> "Lambda1Dash",
							LaTeX -> "\\lambda_1'",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
              OutputName -> Lam1Dash,
              LesHouches -> {HMIX,35}}},

{Lambda2Dash,    { Description -> "Lambda2Dash",
							LaTeX -> "\\lambda_2'",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
              OutputName -> Lam2Dash,
              LesHouches -> {HMIX,36}}},

{Lambda3Dash,    { Description -> "Lambda3Dash",
							LaTeX -> "\\lambda_3'",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
              OutputName -> Lam3Dash,
              LesHouches -> {HMIX,37}}},

{Mu3,    { Description -> "Mu3",
							LaTeX -> "\\mu_3",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
              OutputName -> Mu3,
              LesHouches -> {HMIX,38}}},

{Mub,    { Description -> "Mub",
							LaTeX -> "\\mu_b",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
              OutputName -> Mub,
              LesHouches -> {HMIX,39}}},


{Aa1,    { Description -> "Aa1",
							LaTeX -> "a_1",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
              OutputName -> Aa1,
              LesHouches -> {HMIX,40}}},

{Aa2,    { Description -> "Aa2",
							LaTeX -> "a_2",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
              OutputName -> Aa2,
              LesHouches -> {HMIX,41}}},

{Aa3,    { Description -> "Aa3",
							LaTeX -> "a_3",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
              OutputName -> Aa3,
              LesHouches -> {HMIX,42}}},

{Aa4,    { Description -> "Aa4",
							LaTeX -> "a_4",
							Dependence -> None,
							DependenceNum -> None,
							DependenceSPheno -> None,
              OutputName -> Aa4,
              LesHouches -> {HMIX,43}}},

{Mu1,    {   Description -> "Mu1",
							LaTeX -> "\\mu_1",
              OutputName -> Mu1,
              Real ->True,
              LesHouches -> {HMIX,20}}},

{Mu2,    {   Description -> "Mu2",
							LaTeX -> "\\mu_2",
              OutputName -> Mu2,
              Real ->True,
              LesHouches -> {HMIX,21}}},

{MuDash,    {   Description -> "MuDash",
							LaTeX -> "\\mu'",
              OutputName -> MuDash,
              Real ->True,
              LesHouches -> {HMIX,22}}},


 (*----------------------------------------*)
 (* Vacuum expectation values              *)
 (*----------------------------------------*)

{v1,       { Description -> "VEV1",
			       LaTeX -> "v_1",
			       Real ->True,
						DependenceNum -> None,
            Value -> None,
            LesHouches -> {VEVS,2},
            OutputName-> v1         }},

{v2,       { Description -> "VEV2",
			       LaTeX -> "v_2",
			       Real ->True,
						DependenceNum -> None,
            Value -> None,
            LesHouches ->  {VEVS,3},
            OutputName-> v2         }},

{v3,       { Description -> "VEV3",
            LaTeX -> "v_3",
            Real ->True,
						DependenceNum -> None,
            Value -> None,
            LesHouches ->  {VEVS,4},
            OutputName-> v3         }},

{v,        { Description -> "EW-VEV",
			       LaTeX -> "v",
            Dependence ->  None,
            Real -> True,
            (*DependenceNum -> Sqrt[4*Mass[VWm]^2/(g2^2)],*)
            DependenceSPheno -> Sqrt[v1^2 + v2^2 ],
            Value -> None,
            LesHouches -> {VEVS,1},
            OutputName-> v      }},

(*----------------------------------------*)
(* Mixing matrices (Higgs sector)         *)
(*----------------------------------------*)



{ZH,{		Description -> "Scalar-Mixing-Matrix",
						Dependence -> None,
						DependenceNum -> None,
						DependenceOptional -> None,
						DependenceSPheno -> None,
						Real -> True,
						LesHouches -> ZH_SCALARMIX,
						LaTeX -> "Z^H",
						OutputName -> ZH}},



{ZA,{   Description->"Pseudo-Scalar-Mixing-Matrix",
                 Dependence -> None,
                 DependenceOptional -> None,
                 DependenceNum -> None,
								 LesHouches -> ZA,
								 OutputName-> ZA    }},

{ZP,{  Description->"Higgs-Charged-Mixing-Matrix",
								Dependence -> None,
								DependenceOptional -> None,
								DependenceNum -> None,
								LesHouches -> ZP,
							  OutputName-> ZP }},

{ZZ, {Description -> "Photon-Z Mixing Matrix",
               Dependence -> None,
               DependenceOptional -> None,
               DependenceNum -> None,
							 LesHouches -> ZZ,
							 OutputName-> ZZ   }},

{ZW, {Description -> "W Mixing Matrix" }},



{Vv, { Description->"Neutrinos-Mixing-Matrix",
								Dependence -> None,
								DependenceNum -> None,
								DependenceOptional -> None,
								DependenceSPheno -> None,
								LesHouches -> ZM_SCALARMIX,
								LaTeX -> "V^v",
								OutputName -> Vv}},

(*----------------------------------------*)
(* Mixing Angles                          *)
(*----------------------------------------*)

{\[Beta],   { Description -> "Higgs sector mixing angle"  ,
							LaTeX -> "\\Beta",
			 	      DependenceNum -> ArcTan[TanBeta],
							Real -> True,
							LesHouches -> {HMIX, 1},
							OutputName-> Beta } },

{TanBeta,   { Description -> "TanBeta",
							LaTeX -> "\\tan(\\Beta)",
							Real ->True,
                            DependenceNum -> v2/v1,
							LesHouches -> {HMIX,2},
							OutputName-> TanBeta   }},
{\[Alpha],  { Description -> "Scalar mixing angle" }},

{ThetaW,   { Description -> "Weinberg-Angle"}},
{ThetWp,   { Description -> "Weinberg-prime-Angle"}},




{Vu,        {Description ->"Left-Up-Mixing-Matrix"}},
{Vd,        {Description ->"Left-Down-Mixing-Matrix"}},
{Uu,        {Description ->"Right-Up-Mixing-Matrix"}},
{Ud,        {Description ->"Right-Down-Mixing-Matrix"}},
{Ve,        {Description ->"Left-Lepton-Mixing-Matrix"}},
{Ue,        {Description ->"Right-Lepton-Mixing-Matrix"}}

 };
