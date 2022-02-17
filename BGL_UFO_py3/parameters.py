# ----------------------------------------------------------------------  
# This model file was automatically created by SARAH version4.14.4 
# SARAH References: arXiv:0806.0538, arXiv:0909.2863, arXiv:1002.0840    
# (c) Florian Staub, 2011  
# ----------------------------------------------------------------------  
# File created at 15:54 on 3.6.2021   
# ----------------------------------------------------------------------  
 
 
from object_library import all_parameters,Parameter 
 
from function_library import complexconjugate,re,im,csc,sec,acsc,asec 
 
ZERO=Parameter(name='ZERO', 
                      nature='internal', 
                      type='real', 
                      value='0.0', 
                      texname='0') 
 
Md1 = 	 Parameter(name = 'Md1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0.0035, 
	 texname = '\\text{Md1}', 
	 lhablock = 'MASS', 
	 lhacode = [1]) 
 
Md2 = 	 Parameter(name = 'Md2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0.104, 
	 texname = '\\text{Md2}', 
	 lhablock = 'MASS', 
	 lhacode = [3]) 
 
Md3 = 	 Parameter(name = 'Md3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 4.2, 
	 texname = '\\text{Md3}', 
	 lhablock = 'MASS', 
	 lhacode = [5]) 
 
Mu1 = 	 Parameter(name = 'Mu1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0.0015, 
	 texname = '\\text{Mu1}', 
	 lhablock = 'MASS', 
	 lhacode = [2]) 
 
Mu2 = 	 Parameter(name = 'Mu2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 1.27, 
	 texname = '\\text{Mu2}', 
	 lhablock = 'MASS', 
	 lhacode = [4]) 
 
Mu3 = 	 Parameter(name = 'Mu3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 171.2, 
	 texname = '\\text{Mu3}', 
	 lhablock = 'MASS', 
	 lhacode = [6]) 
 
Wu3 = 	 Parameter(name = 'Wu3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 1.51, 
	 texname = '\\text{Wu3}', 
	 lhablock = 'DECAY', 
	 lhacode = [6]) 
 
Me1 = 	 Parameter(name = 'Me1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0.000511, 
	 texname = '\\text{Me1}', 
	 lhablock = 'MASS', 
	 lhacode = [11]) 
 
Me2 = 	 Parameter(name = 'Me2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0.105, 
	 texname = '\\text{Me2}', 
	 lhablock = 'MASS', 
	 lhacode = [13]) 
 
Me3 = 	 Parameter(name = 'Me3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 1.776, 
	 texname = '\\text{Me3}', 
	 lhablock = 'MASS', 
	 lhacode = [15]) 
 
Mnu1 = 	 Parameter(name = 'Mnu1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{Mnu1}', 
	 lhablock = 'MASS', 
	 lhacode = [12]) 
 
Wnu1 = 	 Parameter(name = 'Wnu1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Wnu1}', 
	 lhablock = 'DECAY', 
	 lhacode = [12]) 
 
Mnu2 = 	 Parameter(name = 'Mnu2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{Mnu2}', 
	 lhablock = 'MASS', 
	 lhacode = [14]) 
 
Wnu2 = 	 Parameter(name = 'Wnu2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Wnu2}', 
	 lhablock = 'DECAY', 
	 lhacode = [14]) 
 
Mnu3 = 	 Parameter(name = 'Mnu3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{Mnu3}', 
	 lhablock = 'MASS', 
	 lhacode = [16]) 
 
Wnu3 = 	 Parameter(name = 'Wnu3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Wnu3}', 
	 lhablock = 'DECAY', 
	 lhacode = [16]) 
 
Mnu4 = 	 Parameter(name = 'Mnu4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{Mnu4}', 
	 lhablock = 'MASS', 
	 lhacode = [8810012]) 
 
Wnu4 = 	 Parameter(name = 'Wnu4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Wnu4}', 
	 lhablock = 'DECAY', 
	 lhacode = [8810012]) 
 
Mnu5 = 	 Parameter(name = 'Mnu5', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{Mnu5}', 
	 lhablock = 'MASS', 
	 lhacode = [8810014]) 
 
Wnu5 = 	 Parameter(name = 'Wnu5', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Wnu5}', 
	 lhablock = 'DECAY', 
	 lhacode = [8810014]) 
 
Mnu6 = 	 Parameter(name = 'Mnu6', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{Mnu6}', 
	 lhablock = 'MASS', 
	 lhacode = [8810016]) 
 
Wnu6 = 	 Parameter(name = 'Wnu6', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Wnu6}', 
	 lhablock = 'DECAY', 
	 lhacode = [8810016]) 
 
Mh1 = 	 Parameter(name = 'Mh1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{Mh1}', 
	 lhablock = 'MASS', 
	 lhacode = [25]) 
 
Wh1 = 	 Parameter(name = 'Wh1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Wh1}', 
	 lhablock = 'DECAY', 
	 lhacode = [25]) 
 
Mh2 = 	 Parameter(name = 'Mh2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{Mh2}', 
	 lhablock = 'MASS', 
	 lhacode = [26]) 
 
Wh2 = 	 Parameter(name = 'Wh2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Wh2}', 
	 lhablock = 'DECAY', 
	 lhacode = [26]) 
 
Mh3 = 	 Parameter(name = 'Mh3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{Mh3}', 
	 lhablock = 'MASS', 
	 lhacode = [27]) 
 
Wh3 = 	 Parameter(name = 'Wh3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Wh3}', 
	 lhablock = 'DECAY', 
	 lhacode = [27]) 
 
MAh2 = 	 Parameter(name = 'MAh2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MAh2}', 
	 lhablock = 'MASS', 
	 lhacode = [35]) 
 
WAh2 = 	 Parameter(name = 'WAh2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WAh2}', 
	 lhablock = 'DECAY', 
	 lhacode = [35]) 

MAh3 = 	 Parameter(name = 'MAh3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MAh3}', 
	 lhablock = 'MASS', 
	 lhacode = [36]) 
 
WAh3 = 	 Parameter(name = 'WAh3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WAh3}', 
	 lhablock = 'DECAY', 
	 lhacode = [36]) 
 
MHm2 = 	 Parameter(name = 'MHm2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MHm2}', 
	 lhablock = 'MASS', 
	 lhacode = [37]) 
 
WHm2 = 	 Parameter(name = 'WHm2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WHm2}', 
	 lhablock = 'DECAY', 
	 lhacode = [37]) 
 
MZ = 	 Parameter(name = 'MZ', 
	 nature = 'external', 
	 type = 'real', 
	 value = 91.1876, 
	 texname = '\\text{MZ}', 
	 lhablock = 'MASS', 
	 lhacode = [23]) 
 
WZ = 	 Parameter(name = 'WZ', 
	 nature = 'external', 
	 type = 'real', 
	 value = 2.4952, 
	 texname = '\\text{WZ}', 
	 lhablock = 'DECAY', 
	 lhacode = [23]) 
 
WWm = 	 Parameter(name = 'WWm', 
	 nature = 'external', 
	 type = 'real', 
	 value = 2.141, 
	 texname = '\\text{WWm}', 
	 lhablock = 'DECAY', 
	 lhacode = [24]) 
 
rY1d11 = 	 Parameter(name='rY1d11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Y1d11}', 
	 lhablock = 'HMIX', 
	 lhacode = [62] ) 
 
iY1d11 = 	 Parameter(name='iY1d11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Y1d11}', 
	 lhablock = 'IMHMIX', 
	 lhacode = [62] ) 
 
rY1d12 = 	 Parameter(name='rY1d12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Y1d12}', 
	 lhablock = 'HMIX', 
	 lhacode = [63] ) 
 
iY1d12 = 	 Parameter(name='iY1d12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Y1d12}', 
	 lhablock = 'IMHMIX', 
	 lhacode = [63] ) 
 
rY1d13 = 	 Parameter(name='rY1d13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Y1d13}', 
	 lhablock = 'HMIX', 
	 lhacode = [64] ) 
 
iY1d13 = 	 Parameter(name='iY1d13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Y1d13}', 
	 lhablock = 'IMHMIX', 
	 lhacode = [64] ) 
 
rY1d21 = 	 Parameter(name='rY1d21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Y1d21}', 
	 lhablock = 'HMIX', 
	 lhacode = [65] ) 
 
iY1d21 = 	 Parameter(name='iY1d21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Y1d21}', 
	 lhablock = 'IMHMIX', 
	 lhacode = [65] ) 
 
rY1d22 = 	 Parameter(name='rY1d22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Y1d22}', 
	 lhablock = 'HMIX', 
	 lhacode = [66] ) 
 
iY1d22 = 	 Parameter(name='iY1d22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Y1d22}', 
	 lhablock = 'IMHMIX', 
	 lhacode = [66] ) 
 
rY1d23 = 	 Parameter(name='rY1d23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Y1d23}', 
	 lhablock = 'HMIX', 
	 lhacode = [67] ) 
 
iY1d23 = 	 Parameter(name='iY1d23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Y1d23}', 
	 lhablock = 'IMHMIX', 
	 lhacode = [67] ) 
 
rY2d31 = 	 Parameter(name='rY2d31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Y2d31}', 
	 lhablock = 'HMIX', 
	 lhacode = [77] ) 
 
iY2d31 = 	 Parameter(name='iY2d31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Y2d31}', 
	 lhablock = 'IMHMIX', 
	 lhacode = [77] ) 
 
rY2d32 = 	 Parameter(name='rY2d32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Y2d32}', 
	 lhablock = 'HMIX', 
	 lhacode = [78] ) 
 
iY2d32 = 	 Parameter(name='iY2d32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Y2d32}', 
	 lhablock = 'IMHMIX', 
	 lhacode = [78] ) 
 
rY2d33 = 	 Parameter(name='rY2d33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Y2d33}', 
	 lhablock = 'HMIX', 
	 lhacode = [79] ) 
 
iY2d33 = 	 Parameter(name='iY2d33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Y2d33}', 
	 lhablock = 'IMHMIX', 
	 lhacode = [79] ) 
 
rY1u11 = 	 Parameter(name='rY1u11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Y1u11}', 
	 lhablock = 'HMIX', 
	 lhacode = [44] ) 
 
iY1u11 = 	 Parameter(name='iY1u11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Y1u11}', 
	 lhablock = 'IMHMIX', 
	 lhacode = [44] ) 
 
rY1u12 = 	 Parameter(name='rY1u12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Y1u12}', 
	 lhablock = 'HMIX', 
	 lhacode = [45] ) 
 
iY1u12 = 	 Parameter(name='iY1u12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Y1u12}', 
	 lhablock = 'IMHMIX', 
	 lhacode = [45] ) 
 
rY1u21 = 	 Parameter(name='rY1u21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Y1u21}', 
	 lhablock = 'HMIX', 
	 lhacode = [47] ) 
 
iY1u21 = 	 Parameter(name='iY1u21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Y1u21}', 
	 lhablock = 'IMHMIX', 
	 lhacode = [47] ) 
 
rY1u22 = 	 Parameter(name='rY1u22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Y1u22}', 
	 lhablock = 'HMIX', 
	 lhacode = [48] ) 
 
iY1u22 = 	 Parameter(name='iY1u22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Y1u22}', 
	 lhablock = 'IMHMIX', 
	 lhacode = [48] ) 
 
rY2u33 = 	 Parameter(name='rY2u33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Y2u33}', 
	 lhablock = 'HMIX', 
	 lhacode = [61] ) 
 
iY2u33 = 	 Parameter(name='iY2u33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Y2u33}', 
	 lhablock = 'IMHMIX', 
	 lhacode = [61] ) 
 
rY1e11 = 	 Parameter(name='rY1e11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Y1e11}', 
	 lhablock = 'HMIX', 
	 lhacode = [80] ) 
 
iY1e11 = 	 Parameter(name='iY1e11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Y1e11}', 
	 lhablock = 'IMHMIX', 
	 lhacode = [80] ) 
 
rY1e12 = 	 Parameter(name='rY1e12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Y1e12}', 
	 lhablock = 'HMIX', 
	 lhacode = [81] ) 
 
iY1e12 = 	 Parameter(name='iY1e12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Y1e12}', 
	 lhablock = 'IMHMIX', 
	 lhacode = [81] ) 
 
rY1e21 = 	 Parameter(name='rY1e21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Y1e21}', 
	 lhablock = 'HMIX', 
	 lhacode = [83] ) 
 
iY1e21 = 	 Parameter(name='iY1e21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Y1e21}', 
	 lhablock = 'IMHMIX', 
	 lhacode = [83] ) 
 
rY1e22 = 	 Parameter(name='rY1e22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Y1e22}', 
	 lhablock = 'HMIX', 
	 lhacode = [84] ) 
 
iY1e22 = 	 Parameter(name='iY1e22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Y1e22}', 
	 lhablock = 'IMHMIX', 
	 lhacode = [84] ) 
 
rY2e33 = 	 Parameter(name='rY2e33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Y2e33}', 
	 lhablock = 'HMIX', 
	 lhacode = [97] ) 
 
iY2e33 = 	 Parameter(name='iY2e33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Y2e33}', 
	 lhablock = 'IMHMIX', 
	 lhacode = [97] ) 
 
rY1n11 = 	 Parameter(name='rY1n11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Y1n11}', 
	 lhablock = 'HMIX', 
	 lhacode = [98] ) 
 
iY1n11 = 	 Parameter(name='iY1n11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Y1n11}', 
	 lhablock = 'IMHMIX', 
	 lhacode = [98] ) 
 
rY1n12 = 	 Parameter(name='rY1n12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Y1n12}', 
	 lhablock = 'HMIX', 
	 lhacode = [99] ) 
 
iY1n12 = 	 Parameter(name='iY1n12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Y1n12}', 
	 lhablock = 'IMHMIX', 
	 lhacode = [99] ) 
 
rY1n21 = 	 Parameter(name='rY1n21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Y1n21}', 
	 lhablock = 'HMIX', 
	 lhacode = [101] ) 
 
iY1n21 = 	 Parameter(name='iY1n21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Y1n21}', 
	 lhablock = 'IMHMIX', 
	 lhacode = [101] ) 
 
rY1n22 = 	 Parameter(name='rY1n22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Y1n22}', 
	 lhablock = 'HMIX', 
	 lhacode = [102] ) 
 
iY1n22 = 	 Parameter(name='iY1n22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Y1n22}', 
	 lhablock = 'IMHMIX', 
	 lhacode = [102] ) 
 
rY2n33 = 	 Parameter(name='rY2n33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Y2n33}', 
	 lhablock = 'HMIX', 
	 lhacode = [115] ) 
 
iY2n33 = 	 Parameter(name='iY2n33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Y2n33}', 
	 lhablock = 'IMHMIX', 
	 lhacode = [115] ) 
 
rC13 = 	 Parameter(name='rC13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{C13}', 
	 lhablock = 'HMIX', 
	 lhacode = [136] ) 
 
iC13 = 	 Parameter(name='iC13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{C13}', 
	 lhablock = 'IMHMIX', 
	 lhacode = [136] ) 
 
rC23 = 	 Parameter(name='rC23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{C23}', 
	 lhablock = 'HMIX', 
	 lhacode = [139] ) 
 
iC23 = 	 Parameter(name='iC23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{C23}', 
	 lhablock = 'IMHMIX', 
	 lhacode = [139] ) 
 
rC31 = 	 Parameter(name='rC31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{C31}', 
	 lhablock = 'HMIX', 
	 lhacode = [140] ) 
 
iC31 = 	 Parameter(name='iC31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{C31}', 
	 lhablock = 'IMHMIX', 
	 lhacode = [140] ) 
 
rC32 = 	 Parameter(name='rC32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{C32}', 
	 lhablock = 'HMIX', 
	 lhacode = [141] ) 
 
iC32 = 	 Parameter(name='iC32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{C32}', 
	 lhablock = 'IMHMIX', 
	 lhacode = [141] ) 
 
rBB11 = 	 Parameter(name='rBB11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{BB11}', 
	 lhablock = 'HMIX', 
	 lhacode = [125] ) 
 
iBB11 = 	 Parameter(name='iBB11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{BB11}', 
	 lhablock = 'IMHMIX', 
	 lhacode = [125] ) 
 
rBB12 = 	 Parameter(name='rBB12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{BB12}', 
	 lhablock = 'HMIX', 
	 lhacode = [126] ) 
 
iBB12 = 	 Parameter(name='iBB12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{BB12}', 
	 lhablock = 'IMHMIX', 
	 lhacode = [126] ) 
 
rBB21 = 	 Parameter(name='rBB21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{BB21}', 
	 lhablock = 'HMIX', 
	 lhacode = [128] ) 
 
iBB21 = 	 Parameter(name='iBB21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{BB21}', 
	 lhablock = 'IMHMIX', 
	 lhacode = [128] ) 
 
rBB22 = 	 Parameter(name='rBB22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{BB22}', 
	 lhablock = 'HMIX', 
	 lhacode = [129] ) 
 
iBB22 = 	 Parameter(name='iBB22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{BB22}', 
	 lhablock = 'IMHMIX', 
	 lhacode = [129] ) 
 
rLam1 = 	 Parameter(name='rLam1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Lam1}', 
	 lhablock = 'HMIX', 
	 lhacode = [31] ) 
 
iLam1 = 	 Parameter(name='iLam1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Lam1}', 
	 lhablock = 'IMHMIX', 
	 lhacode = [31] ) 
 
rLam3 = 	 Parameter(name='rLam3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Lam3}', 
	 lhablock = 'HMIX', 
	 lhacode = [33] ) 
 
iLam3 = 	 Parameter(name='iLam3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Lam3}', 
	 lhablock = 'IMHMIX', 
	 lhacode = [33] ) 
 
rLam4 = 	 Parameter(name='rLam4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Lam4}', 
	 lhablock = 'HMIX', 
	 lhacode = [34] ) 
 
iLam4 = 	 Parameter(name='iLam4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Lam4}', 
	 lhablock = 'IMHMIX', 
	 lhacode = [34] ) 
 
rLam2 = 	 Parameter(name='rLam2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Lam2}', 
	 lhablock = 'HMIX', 
	 lhacode = [32] ) 
 
iLam2 = 	 Parameter(name='iLam2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Lam2}', 
	 lhablock = 'IMHMIX', 
	 lhacode = [32] ) 
 
rLam1Dash = 	 Parameter(name='rLam1Dash', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Lam1Dash}', 
	 lhablock = 'HMIX', 
	 lhacode = [35] ) 
 
iLam1Dash = 	 Parameter(name='iLam1Dash', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Lam1Dash}', 
	 lhablock = 'IMHMIX', 
	 lhacode = [35] ) 
 
rLam2Dash = 	 Parameter(name='rLam2Dash', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Lam2Dash}', 
	 lhablock = 'HMIX', 
	 lhacode = [36] ) 
 
iLam2Dash = 	 Parameter(name='iLam2Dash', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Lam2Dash}', 
	 lhablock = 'IMHMIX', 
	 lhacode = [36] ) 
 
rLam3Dash = 	 Parameter(name='rLam3Dash', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Lam3Dash}', 
	 lhablock = 'HMIX', 
	 lhacode = [37] ) 
 
iLam3Dash = 	 Parameter(name='iLam3Dash', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Lam3Dash}', 
	 lhablock = 'IMHMIX', 
	 lhacode = [37] ) 
 
rAa1 = 	 Parameter(name='rAa1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Aa1}', 
	 lhablock = 'HMIX', 
	 lhacode = [40] ) 
 
iAa1 = 	 Parameter(name='iAa1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Aa1}', 
	 lhablock = 'IMHMIX', 
	 lhacode = [40] ) 
 
rAa2 = 	 Parameter(name='rAa2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Aa2}', 
	 lhablock = 'HMIX', 
	 lhacode = [41] ) 
 
iAa2 = 	 Parameter(name='iAa2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Aa2}', 
	 lhablock = 'IMHMIX', 
	 lhacode = [41] ) 
 
rAa3 = 	 Parameter(name='rAa3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Aa3}', 
	 lhablock = 'HMIX', 
	 lhacode = [42] ) 
 
iAa3 = 	 Parameter(name='iAa3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Aa3}', 
	 lhablock = 'IMHMIX', 
	 lhacode = [42] ) 
 
rAa4 = 	 Parameter(name='rAa4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Aa4}', 
	 lhablock = 'HMIX', 
	 lhacode = [43] ) 
 
iAa4 = 	 Parameter(name='iAa4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Aa4}', 
	 lhablock = 'IMHMIX', 
	 lhacode = [43] ) 
 
v1 = 	 Parameter(name='v1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{v1}', 
	 lhablock = 'VEVS', 
	 lhacode = [2] ) 
 
v2 = 	 Parameter(name='v2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{v2}', 
	 lhablock = 'VEVS', 
	 lhacode = [3] ) 
 
v3 = 	 Parameter(name='v3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{v3}', 
	 lhablock = 'VEVS', 
	 lhacode = [4] ) 
 
rZZ11 = 	 Parameter(name='rZZ11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZZ11}', 
	 lhablock = 'ZZ', 
	 lhacode = [1, 1] ) 
 
iZZ11 = 	 Parameter(name='iZZ11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZZ11}', 
	 lhablock = 'IMZZ', 
	 lhacode = [1, 1] ) 
 
rZZ12 = 	 Parameter(name='rZZ12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZZ12}', 
	 lhablock = 'ZZ', 
	 lhacode = [1, 2] ) 
 
iZZ12 = 	 Parameter(name='iZZ12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZZ12}', 
	 lhablock = 'IMZZ', 
	 lhacode = [1, 2] ) 
 
rZZ21 = 	 Parameter(name='rZZ21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZZ21}', 
	 lhablock = 'ZZ', 
	 lhacode = [2, 1] ) 
 
iZZ21 = 	 Parameter(name='iZZ21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZZ21}', 
	 lhablock = 'IMZZ', 
	 lhacode = [2, 1] ) 
 
rZZ22 = 	 Parameter(name='rZZ22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZZ22}', 
	 lhablock = 'ZZ', 
	 lhacode = [2, 2] ) 
 
iZZ22 = 	 Parameter(name='iZZ22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZZ22}', 
	 lhablock = 'IMZZ', 
	 lhacode = [2, 2] ) 
 
ZH11 = 	 Parameter(name='ZH11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZH11}', 
	 lhablock = 'ZH_SCALARMIX', 
	 lhacode = [1, 1] ) 
 
ZH12 = 	 Parameter(name='ZH12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZH12}', 
	 lhablock = 'ZH_SCALARMIX', 
	 lhacode = [1, 2] ) 
 
ZH13 = 	 Parameter(name='ZH13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZH13}', 
	 lhablock = 'ZH_SCALARMIX', 
	 lhacode = [1, 3] ) 
 
ZH21 = 	 Parameter(name='ZH21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZH21}', 
	 lhablock = 'ZH_SCALARMIX', 
	 lhacode = [2, 1] ) 
 
ZH22 = 	 Parameter(name='ZH22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZH22}', 
	 lhablock = 'ZH_SCALARMIX', 
	 lhacode = [2, 2] ) 
 
ZH23 = 	 Parameter(name='ZH23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZH23}', 
	 lhablock = 'ZH_SCALARMIX', 
	 lhacode = [2, 3] ) 
 
ZH31 = 	 Parameter(name='ZH31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZH31}', 
	 lhablock = 'ZH_SCALARMIX', 
	 lhacode = [3, 1] ) 
 
ZH32 = 	 Parameter(name='ZH32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZH32}', 
	 lhablock = 'ZH_SCALARMIX', 
	 lhacode = [3, 2] ) 
 
ZH33 = 	 Parameter(name='ZH33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZH33}', 
	 lhablock = 'ZH_SCALARMIX', 
	 lhacode = [3, 3] ) 
 
ZA11 = 	 Parameter(name='ZA11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZA11}', 
	 lhablock = 'ZA', 
	 lhacode = [1, 1] ) 
 
ZA12 = 	 Parameter(name='ZA12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZA12}', 
	 lhablock = 'ZA', 
	 lhacode = [1, 2] ) 
 
ZA13 = 	 Parameter(name='ZA13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZA13}', 
	 lhablock = 'ZA', 
	 lhacode = [1, 3] ) 
 
ZA21 = 	 Parameter(name='ZA21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZA21}', 
	 lhablock = 'ZA', 
	 lhacode = [2, 1] ) 
 
ZA22 = 	 Parameter(name='ZA22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZA22}', 
	 lhablock = 'ZA', 
	 lhacode = [2, 2] ) 
 
ZA23 = 	 Parameter(name='ZA23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZA23}', 
	 lhablock = 'ZA', 
	 lhacode = [2, 3] ) 
 
ZA31 = 	 Parameter(name='ZA31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZA31}', 
	 lhablock = 'ZA', 
	 lhacode = [3, 1] ) 
 
ZA32 = 	 Parameter(name='ZA32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZA32}', 
	 lhablock = 'ZA', 
	 lhacode = [3, 2] ) 
 
ZA33 = 	 Parameter(name='ZA33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZA33}', 
	 lhablock = 'ZA', 
	 lhacode = [3, 3] ) 
 
rZP11 = 	 Parameter(name='rZP11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZP11}', 
	 lhablock = 'ZP', 
	 lhacode = [1, 1] ) 
 
iZP11 = 	 Parameter(name='iZP11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZP11}', 
	 lhablock = 'IMZP', 
	 lhacode = [1, 1] ) 
 
rZP12 = 	 Parameter(name='rZP12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZP12}', 
	 lhablock = 'ZP', 
	 lhacode = [1, 2] ) 
 
iZP12 = 	 Parameter(name='iZP12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZP12}', 
	 lhablock = 'IMZP', 
	 lhacode = [1, 2] ) 
 
rZP21 = 	 Parameter(name='rZP21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZP21}', 
	 lhablock = 'ZP', 
	 lhacode = [2, 1] ) 
 
iZP21 = 	 Parameter(name='iZP21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZP21}', 
	 lhablock = 'IMZP', 
	 lhacode = [2, 1] ) 
 
rZP22 = 	 Parameter(name='rZP22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZP22}', 
	 lhablock = 'ZP', 
	 lhacode = [2, 2] ) 
 
iZP22 = 	 Parameter(name='iZP22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZP22}', 
	 lhablock = 'IMZP', 
	 lhacode = [2, 2] ) 
 
rZDL11 = 	 Parameter(name='rZDL11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL11}', 
	 lhablock = 'UDLMIX', 
	 lhacode = [1, 1] ) 
 
iZDL11 = 	 Parameter(name='iZDL11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL11}', 
	 lhablock = 'IMUDLMIX', 
	 lhacode = [1, 1] ) 
 
rZDL12 = 	 Parameter(name='rZDL12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL12}', 
	 lhablock = 'UDLMIX', 
	 lhacode = [1, 2] ) 
 
iZDL12 = 	 Parameter(name='iZDL12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL12}', 
	 lhablock = 'IMUDLMIX', 
	 lhacode = [1, 2] ) 
 
rZDL13 = 	 Parameter(name='rZDL13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL13}', 
	 lhablock = 'UDLMIX', 
	 lhacode = [1, 3] ) 
 
iZDL13 = 	 Parameter(name='iZDL13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL13}', 
	 lhablock = 'IMUDLMIX', 
	 lhacode = [1, 3] ) 
 
rZDL21 = 	 Parameter(name='rZDL21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL21}', 
	 lhablock = 'UDLMIX', 
	 lhacode = [2, 1] ) 
 
iZDL21 = 	 Parameter(name='iZDL21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL21}', 
	 lhablock = 'IMUDLMIX', 
	 lhacode = [2, 1] ) 
 
rZDL22 = 	 Parameter(name='rZDL22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL22}', 
	 lhablock = 'UDLMIX', 
	 lhacode = [2, 2] ) 
 
iZDL22 = 	 Parameter(name='iZDL22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL22}', 
	 lhablock = 'IMUDLMIX', 
	 lhacode = [2, 2] ) 
 
rZDL23 = 	 Parameter(name='rZDL23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL23}', 
	 lhablock = 'UDLMIX', 
	 lhacode = [2, 3] ) 
 
iZDL23 = 	 Parameter(name='iZDL23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL23}', 
	 lhablock = 'IMUDLMIX', 
	 lhacode = [2, 3] ) 
 
rZDL31 = 	 Parameter(name='rZDL31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL31}', 
	 lhablock = 'UDLMIX', 
	 lhacode = [3, 1] ) 
 
iZDL31 = 	 Parameter(name='iZDL31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL31}', 
	 lhablock = 'IMUDLMIX', 
	 lhacode = [3, 1] ) 
 
rZDL32 = 	 Parameter(name='rZDL32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL32}', 
	 lhablock = 'UDLMIX', 
	 lhacode = [3, 2] ) 
 
iZDL32 = 	 Parameter(name='iZDL32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL32}', 
	 lhablock = 'IMUDLMIX', 
	 lhacode = [3, 2] ) 
 
rZDL33 = 	 Parameter(name='rZDL33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL33}', 
	 lhablock = 'UDLMIX', 
	 lhacode = [3, 3] ) 
 
iZDL33 = 	 Parameter(name='iZDL33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL33}', 
	 lhablock = 'IMUDLMIX', 
	 lhacode = [3, 3] ) 
 
rZDR11 = 	 Parameter(name='rZDR11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR11}', 
	 lhablock = 'UDRMIX', 
	 lhacode = [1, 1] ) 
 
iZDR11 = 	 Parameter(name='iZDR11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR11}', 
	 lhablock = 'IMUDRMIX', 
	 lhacode = [1, 1] ) 
 
rZDR12 = 	 Parameter(name='rZDR12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR12}', 
	 lhablock = 'UDRMIX', 
	 lhacode = [1, 2] ) 
 
iZDR12 = 	 Parameter(name='iZDR12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR12}', 
	 lhablock = 'IMUDRMIX', 
	 lhacode = [1, 2] ) 
 
rZDR13 = 	 Parameter(name='rZDR13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR13}', 
	 lhablock = 'UDRMIX', 
	 lhacode = [1, 3] ) 
 
iZDR13 = 	 Parameter(name='iZDR13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR13}', 
	 lhablock = 'IMUDRMIX', 
	 lhacode = [1, 3] ) 
 
rZDR21 = 	 Parameter(name='rZDR21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR21}', 
	 lhablock = 'UDRMIX', 
	 lhacode = [2, 1] ) 
 
iZDR21 = 	 Parameter(name='iZDR21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR21}', 
	 lhablock = 'IMUDRMIX', 
	 lhacode = [2, 1] ) 
 
rZDR22 = 	 Parameter(name='rZDR22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR22}', 
	 lhablock = 'UDRMIX', 
	 lhacode = [2, 2] ) 
 
iZDR22 = 	 Parameter(name='iZDR22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR22}', 
	 lhablock = 'IMUDRMIX', 
	 lhacode = [2, 2] ) 
 
rZDR23 = 	 Parameter(name='rZDR23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR23}', 
	 lhablock = 'UDRMIX', 
	 lhacode = [2, 3] ) 
 
iZDR23 = 	 Parameter(name='iZDR23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR23}', 
	 lhablock = 'IMUDRMIX', 
	 lhacode = [2, 3] ) 
 
rZDR31 = 	 Parameter(name='rZDR31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR31}', 
	 lhablock = 'UDRMIX', 
	 lhacode = [3, 1] ) 
 
iZDR31 = 	 Parameter(name='iZDR31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR31}', 
	 lhablock = 'IMUDRMIX', 
	 lhacode = [3, 1] ) 
 
rZDR32 = 	 Parameter(name='rZDR32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR32}', 
	 lhablock = 'UDRMIX', 
	 lhacode = [3, 2] ) 
 
iZDR32 = 	 Parameter(name='iZDR32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR32}', 
	 lhablock = 'IMUDRMIX', 
	 lhacode = [3, 2] ) 
 
rZDR33 = 	 Parameter(name='rZDR33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR33}', 
	 lhablock = 'UDRMIX', 
	 lhacode = [3, 3] ) 
 
iZDR33 = 	 Parameter(name='iZDR33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR33}', 
	 lhablock = 'IMUDRMIX', 
	 lhacode = [3, 3] ) 
 
rZUL11 = 	 Parameter(name='rZUL11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL11}', 
	 lhablock = 'UULMIX', 
	 lhacode = [1, 1] ) 
 
iZUL11 = 	 Parameter(name='iZUL11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL11}', 
	 lhablock = 'IMUULMIX', 
	 lhacode = [1, 1] ) 
 
rZUL12 = 	 Parameter(name='rZUL12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL12}', 
	 lhablock = 'UULMIX', 
	 lhacode = [1, 2] ) 
 
iZUL12 = 	 Parameter(name='iZUL12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL12}', 
	 lhablock = 'IMUULMIX', 
	 lhacode = [1, 2] ) 
 
rZUL13 = 	 Parameter(name='rZUL13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL13}', 
	 lhablock = 'UULMIX', 
	 lhacode = [1, 3] ) 
 
iZUL13 = 	 Parameter(name='iZUL13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL13}', 
	 lhablock = 'IMUULMIX', 
	 lhacode = [1, 3] ) 
 
rZUL21 = 	 Parameter(name='rZUL21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL21}', 
	 lhablock = 'UULMIX', 
	 lhacode = [2, 1] ) 
 
iZUL21 = 	 Parameter(name='iZUL21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL21}', 
	 lhablock = 'IMUULMIX', 
	 lhacode = [2, 1] ) 
 
rZUL22 = 	 Parameter(name='rZUL22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL22}', 
	 lhablock = 'UULMIX', 
	 lhacode = [2, 2] ) 
 
iZUL22 = 	 Parameter(name='iZUL22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL22}', 
	 lhablock = 'IMUULMIX', 
	 lhacode = [2, 2] ) 
 
rZUL23 = 	 Parameter(name='rZUL23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL23}', 
	 lhablock = 'UULMIX', 
	 lhacode = [2, 3] ) 
 
iZUL23 = 	 Parameter(name='iZUL23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL23}', 
	 lhablock = 'IMUULMIX', 
	 lhacode = [2, 3] ) 
 
rZUL31 = 	 Parameter(name='rZUL31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL31}', 
	 lhablock = 'UULMIX', 
	 lhacode = [3, 1] ) 
 
iZUL31 = 	 Parameter(name='iZUL31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL31}', 
	 lhablock = 'IMUULMIX', 
	 lhacode = [3, 1] ) 
 
rZUL32 = 	 Parameter(name='rZUL32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL32}', 
	 lhablock = 'UULMIX', 
	 lhacode = [3, 2] ) 
 
iZUL32 = 	 Parameter(name='iZUL32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL32}', 
	 lhablock = 'IMUULMIX', 
	 lhacode = [3, 2] ) 
 
rZUL33 = 	 Parameter(name='rZUL33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL33}', 
	 lhablock = 'UULMIX', 
	 lhacode = [3, 3] ) 
 
iZUL33 = 	 Parameter(name='iZUL33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL33}', 
	 lhablock = 'IMUULMIX', 
	 lhacode = [3, 3] ) 
 
rZUR11 = 	 Parameter(name='rZUR11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR11}', 
	 lhablock = 'UURMIX', 
	 lhacode = [1, 1] ) 
 
iZUR11 = 	 Parameter(name='iZUR11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR11}', 
	 lhablock = 'IMUURMIX', 
	 lhacode = [1, 1] ) 
 
rZUR12 = 	 Parameter(name='rZUR12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR12}', 
	 lhablock = 'UURMIX', 
	 lhacode = [1, 2] ) 
 
iZUR12 = 	 Parameter(name='iZUR12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR12}', 
	 lhablock = 'IMUURMIX', 
	 lhacode = [1, 2] ) 
 
rZUR13 = 	 Parameter(name='rZUR13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR13}', 
	 lhablock = 'UURMIX', 
	 lhacode = [1, 3] ) 
 
iZUR13 = 	 Parameter(name='iZUR13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR13}', 
	 lhablock = 'IMUURMIX', 
	 lhacode = [1, 3] ) 
 
rZUR21 = 	 Parameter(name='rZUR21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR21}', 
	 lhablock = 'UURMIX', 
	 lhacode = [2, 1] ) 
 
iZUR21 = 	 Parameter(name='iZUR21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR21}', 
	 lhablock = 'IMUURMIX', 
	 lhacode = [2, 1] ) 
 
rZUR22 = 	 Parameter(name='rZUR22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR22}', 
	 lhablock = 'UURMIX', 
	 lhacode = [2, 2] ) 
 
iZUR22 = 	 Parameter(name='iZUR22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR22}', 
	 lhablock = 'IMUURMIX', 
	 lhacode = [2, 2] ) 
 
rZUR23 = 	 Parameter(name='rZUR23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR23}', 
	 lhablock = 'UURMIX', 
	 lhacode = [2, 3] ) 
 
iZUR23 = 	 Parameter(name='iZUR23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR23}', 
	 lhablock = 'IMUURMIX', 
	 lhacode = [2, 3] ) 
 
rZUR31 = 	 Parameter(name='rZUR31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR31}', 
	 lhablock = 'UURMIX', 
	 lhacode = [3, 1] ) 
 
iZUR31 = 	 Parameter(name='iZUR31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR31}', 
	 lhablock = 'IMUURMIX', 
	 lhacode = [3, 1] ) 
 
rZUR32 = 	 Parameter(name='rZUR32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR32}', 
	 lhablock = 'UURMIX', 
	 lhacode = [3, 2] ) 
 
iZUR32 = 	 Parameter(name='iZUR32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR32}', 
	 lhablock = 'IMUURMIX', 
	 lhacode = [3, 2] ) 
 
rZUR33 = 	 Parameter(name='rZUR33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR33}', 
	 lhablock = 'UURMIX', 
	 lhacode = [3, 3] ) 
 
iZUR33 = 	 Parameter(name='iZUR33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR33}', 
	 lhablock = 'IMUURMIX', 
	 lhacode = [3, 3] ) 
 
rZEL11 = 	 Parameter(name='rZEL11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL11}', 
	 lhablock = 'UELMIX', 
	 lhacode = [1, 1] ) 
 
iZEL11 = 	 Parameter(name='iZEL11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL11}', 
	 lhablock = 'IMUELMIX', 
	 lhacode = [1, 1] ) 
 
rZEL12 = 	 Parameter(name='rZEL12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL12}', 
	 lhablock = 'UELMIX', 
	 lhacode = [1, 2] ) 
 
iZEL12 = 	 Parameter(name='iZEL12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL12}', 
	 lhablock = 'IMUELMIX', 
	 lhacode = [1, 2] ) 
 
rZEL13 = 	 Parameter(name='rZEL13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL13}', 
	 lhablock = 'UELMIX', 
	 lhacode = [1, 3] ) 
 
iZEL13 = 	 Parameter(name='iZEL13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL13}', 
	 lhablock = 'IMUELMIX', 
	 lhacode = [1, 3] ) 
 
rZEL21 = 	 Parameter(name='rZEL21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL21}', 
	 lhablock = 'UELMIX', 
	 lhacode = [2, 1] ) 
 
iZEL21 = 	 Parameter(name='iZEL21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL21}', 
	 lhablock = 'IMUELMIX', 
	 lhacode = [2, 1] ) 
 
rZEL22 = 	 Parameter(name='rZEL22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL22}', 
	 lhablock = 'UELMIX', 
	 lhacode = [2, 2] ) 
 
iZEL22 = 	 Parameter(name='iZEL22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL22}', 
	 lhablock = 'IMUELMIX', 
	 lhacode = [2, 2] ) 
 
rZEL23 = 	 Parameter(name='rZEL23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL23}', 
	 lhablock = 'UELMIX', 
	 lhacode = [2, 3] ) 
 
iZEL23 = 	 Parameter(name='iZEL23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL23}', 
	 lhablock = 'IMUELMIX', 
	 lhacode = [2, 3] ) 
 
rZEL31 = 	 Parameter(name='rZEL31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL31}', 
	 lhablock = 'UELMIX', 
	 lhacode = [3, 1] ) 
 
iZEL31 = 	 Parameter(name='iZEL31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL31}', 
	 lhablock = 'IMUELMIX', 
	 lhacode = [3, 1] ) 
 
rZEL32 = 	 Parameter(name='rZEL32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL32}', 
	 lhablock = 'UELMIX', 
	 lhacode = [3, 2] ) 
 
iZEL32 = 	 Parameter(name='iZEL32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL32}', 
	 lhablock = 'IMUELMIX', 
	 lhacode = [3, 2] ) 
 
rZEL33 = 	 Parameter(name='rZEL33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL33}', 
	 lhablock = 'UELMIX', 
	 lhacode = [3, 3] ) 
 
iZEL33 = 	 Parameter(name='iZEL33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL33}', 
	 lhablock = 'IMUELMIX', 
	 lhacode = [3, 3] ) 
 
rZER11 = 	 Parameter(name='rZER11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER11}', 
	 lhablock = 'UERMIX', 
	 lhacode = [1, 1] ) 
 
iZER11 = 	 Parameter(name='iZER11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER11}', 
	 lhablock = 'IMUERMIX', 
	 lhacode = [1, 1] ) 
 
rZER12 = 	 Parameter(name='rZER12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER12}', 
	 lhablock = 'UERMIX', 
	 lhacode = [1, 2] ) 
 
iZER12 = 	 Parameter(name='iZER12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER12}', 
	 lhablock = 'IMUERMIX', 
	 lhacode = [1, 2] ) 
 
rZER13 = 	 Parameter(name='rZER13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER13}', 
	 lhablock = 'UERMIX', 
	 lhacode = [1, 3] ) 
 
iZER13 = 	 Parameter(name='iZER13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER13}', 
	 lhablock = 'IMUERMIX', 
	 lhacode = [1, 3] ) 
 
rZER21 = 	 Parameter(name='rZER21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER21}', 
	 lhablock = 'UERMIX', 
	 lhacode = [2, 1] ) 
 
iZER21 = 	 Parameter(name='iZER21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER21}', 
	 lhablock = 'IMUERMIX', 
	 lhacode = [2, 1] ) 
 
rZER22 = 	 Parameter(name='rZER22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER22}', 
	 lhablock = 'UERMIX', 
	 lhacode = [2, 2] ) 
 
iZER22 = 	 Parameter(name='iZER22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER22}', 
	 lhablock = 'IMUERMIX', 
	 lhacode = [2, 2] ) 
 
rZER23 = 	 Parameter(name='rZER23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER23}', 
	 lhablock = 'UERMIX', 
	 lhacode = [2, 3] ) 
 
iZER23 = 	 Parameter(name='iZER23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER23}', 
	 lhablock = 'IMUERMIX', 
	 lhacode = [2, 3] ) 
 
rZER31 = 	 Parameter(name='rZER31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER31}', 
	 lhablock = 'UERMIX', 
	 lhacode = [3, 1] ) 
 
iZER31 = 	 Parameter(name='iZER31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER31}', 
	 lhablock = 'IMUERMIX', 
	 lhacode = [3, 1] ) 
 
rZER32 = 	 Parameter(name='rZER32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER32}', 
	 lhablock = 'UERMIX', 
	 lhacode = [3, 2] ) 
 
iZER32 = 	 Parameter(name='iZER32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER32}', 
	 lhablock = 'IMUERMIX', 
	 lhacode = [3, 2] ) 
 
rZER33 = 	 Parameter(name='rZER33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER33}', 
	 lhablock = 'UERMIX', 
	 lhacode = [3, 3] ) 
 
iZER33 = 	 Parameter(name='iZER33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER33}', 
	 lhablock = 'IMUERMIX', 
	 lhacode = [3, 3] ) 
 
rVv11 = 	 Parameter(name='rVv11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv11}', 
	 lhablock = 'ZM_SCALARMIX', 
	 lhacode = [1, 1] ) 
 
iVv11 = 	 Parameter(name='iVv11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv11}', 
	 lhablock = 'IMZM_SCALARMIX', 
	 lhacode = [1, 1] ) 
 
rVv12 = 	 Parameter(name='rVv12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv12}', 
	 lhablock = 'ZM_SCALARMIX', 
	 lhacode = [1, 2] ) 
 
iVv12 = 	 Parameter(name='iVv12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv12}', 
	 lhablock = 'IMZM_SCALARMIX', 
	 lhacode = [1, 2] ) 
 
rVv13 = 	 Parameter(name='rVv13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv13}', 
	 lhablock = 'ZM_SCALARMIX', 
	 lhacode = [1, 3] ) 
 
iVv13 = 	 Parameter(name='iVv13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv13}', 
	 lhablock = 'IMZM_SCALARMIX', 
	 lhacode = [1, 3] ) 
 
rVv14 = 	 Parameter(name='rVv14', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv14}', 
	 lhablock = 'ZM_SCALARMIX', 
	 lhacode = [1, 4] ) 
 
iVv14 = 	 Parameter(name='iVv14', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv14}', 
	 lhablock = 'IMZM_SCALARMIX', 
	 lhacode = [1, 4] ) 
 
rVv15 = 	 Parameter(name='rVv15', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv15}', 
	 lhablock = 'ZM_SCALARMIX', 
	 lhacode = [1, 5] ) 
 
iVv15 = 	 Parameter(name='iVv15', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv15}', 
	 lhablock = 'IMZM_SCALARMIX', 
	 lhacode = [1, 5] ) 
 
rVv16 = 	 Parameter(name='rVv16', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv16}', 
	 lhablock = 'ZM_SCALARMIX', 
	 lhacode = [1, 6] ) 
 
iVv16 = 	 Parameter(name='iVv16', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv16}', 
	 lhablock = 'IMZM_SCALARMIX', 
	 lhacode = [1, 6] ) 
 
rVv21 = 	 Parameter(name='rVv21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv21}', 
	 lhablock = 'ZM_SCALARMIX', 
	 lhacode = [2, 1] ) 
 
iVv21 = 	 Parameter(name='iVv21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv21}', 
	 lhablock = 'IMZM_SCALARMIX', 
	 lhacode = [2, 1] ) 
 
rVv22 = 	 Parameter(name='rVv22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv22}', 
	 lhablock = 'ZM_SCALARMIX', 
	 lhacode = [2, 2] ) 
 
iVv22 = 	 Parameter(name='iVv22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv22}', 
	 lhablock = 'IMZM_SCALARMIX', 
	 lhacode = [2, 2] ) 
 
rVv23 = 	 Parameter(name='rVv23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv23}', 
	 lhablock = 'ZM_SCALARMIX', 
	 lhacode = [2, 3] ) 
 
iVv23 = 	 Parameter(name='iVv23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv23}', 
	 lhablock = 'IMZM_SCALARMIX', 
	 lhacode = [2, 3] ) 
 
rVv24 = 	 Parameter(name='rVv24', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv24}', 
	 lhablock = 'ZM_SCALARMIX', 
	 lhacode = [2, 4] ) 
 
iVv24 = 	 Parameter(name='iVv24', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv24}', 
	 lhablock = 'IMZM_SCALARMIX', 
	 lhacode = [2, 4] ) 
 
rVv25 = 	 Parameter(name='rVv25', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv25}', 
	 lhablock = 'ZM_SCALARMIX', 
	 lhacode = [2, 5] ) 
 
iVv25 = 	 Parameter(name='iVv25', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv25}', 
	 lhablock = 'IMZM_SCALARMIX', 
	 lhacode = [2, 5] ) 
 
rVv26 = 	 Parameter(name='rVv26', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv26}', 
	 lhablock = 'ZM_SCALARMIX', 
	 lhacode = [2, 6] ) 
 
iVv26 = 	 Parameter(name='iVv26', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv26}', 
	 lhablock = 'IMZM_SCALARMIX', 
	 lhacode = [2, 6] ) 
 
rVv31 = 	 Parameter(name='rVv31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv31}', 
	 lhablock = 'ZM_SCALARMIX', 
	 lhacode = [3, 1] ) 
 
iVv31 = 	 Parameter(name='iVv31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv31}', 
	 lhablock = 'IMZM_SCALARMIX', 
	 lhacode = [3, 1] ) 
 
rVv32 = 	 Parameter(name='rVv32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv32}', 
	 lhablock = 'ZM_SCALARMIX', 
	 lhacode = [3, 2] ) 
 
iVv32 = 	 Parameter(name='iVv32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv32}', 
	 lhablock = 'IMZM_SCALARMIX', 
	 lhacode = [3, 2] ) 
 
rVv33 = 	 Parameter(name='rVv33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv33}', 
	 lhablock = 'ZM_SCALARMIX', 
	 lhacode = [3, 3] ) 
 
iVv33 = 	 Parameter(name='iVv33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv33}', 
	 lhablock = 'IMZM_SCALARMIX', 
	 lhacode = [3, 3] ) 
 
rVv34 = 	 Parameter(name='rVv34', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv34}', 
	 lhablock = 'ZM_SCALARMIX', 
	 lhacode = [3, 4] ) 
 
iVv34 = 	 Parameter(name='iVv34', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv34}', 
	 lhablock = 'IMZM_SCALARMIX', 
	 lhacode = [3, 4] ) 
 
rVv35 = 	 Parameter(name='rVv35', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv35}', 
	 lhablock = 'ZM_SCALARMIX', 
	 lhacode = [3, 5] ) 
 
iVv35 = 	 Parameter(name='iVv35', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv35}', 
	 lhablock = 'IMZM_SCALARMIX', 
	 lhacode = [3, 5] ) 
 
rVv36 = 	 Parameter(name='rVv36', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv36}', 
	 lhablock = 'ZM_SCALARMIX', 
	 lhacode = [3, 6] ) 
 
iVv36 = 	 Parameter(name='iVv36', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv36}', 
	 lhablock = 'IMZM_SCALARMIX', 
	 lhacode = [3, 6] ) 
 
rVv41 = 	 Parameter(name='rVv41', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv41}', 
	 lhablock = 'ZM_SCALARMIX', 
	 lhacode = [4, 1] ) 
 
iVv41 = 	 Parameter(name='iVv41', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv41}', 
	 lhablock = 'IMZM_SCALARMIX', 
	 lhacode = [4, 1] ) 
 
rVv42 = 	 Parameter(name='rVv42', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv42}', 
	 lhablock = 'ZM_SCALARMIX', 
	 lhacode = [4, 2] ) 
 
iVv42 = 	 Parameter(name='iVv42', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv42}', 
	 lhablock = 'IMZM_SCALARMIX', 
	 lhacode = [4, 2] ) 
 
rVv43 = 	 Parameter(name='rVv43', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv43}', 
	 lhablock = 'ZM_SCALARMIX', 
	 lhacode = [4, 3] ) 
 
iVv43 = 	 Parameter(name='iVv43', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv43}', 
	 lhablock = 'IMZM_SCALARMIX', 
	 lhacode = [4, 3] ) 
 
rVv44 = 	 Parameter(name='rVv44', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv44}', 
	 lhablock = 'ZM_SCALARMIX', 
	 lhacode = [4, 4] ) 
 
iVv44 = 	 Parameter(name='iVv44', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv44}', 
	 lhablock = 'IMZM_SCALARMIX', 
	 lhacode = [4, 4] ) 
 
rVv45 = 	 Parameter(name='rVv45', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv45}', 
	 lhablock = 'ZM_SCALARMIX', 
	 lhacode = [4, 5] ) 
 
iVv45 = 	 Parameter(name='iVv45', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv45}', 
	 lhablock = 'IMZM_SCALARMIX', 
	 lhacode = [4, 5] ) 
 
rVv46 = 	 Parameter(name='rVv46', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv46}', 
	 lhablock = 'ZM_SCALARMIX', 
	 lhacode = [4, 6] ) 
 
iVv46 = 	 Parameter(name='iVv46', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv46}', 
	 lhablock = 'IMZM_SCALARMIX', 
	 lhacode = [4, 6] ) 
 
rVv51 = 	 Parameter(name='rVv51', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv51}', 
	 lhablock = 'ZM_SCALARMIX', 
	 lhacode = [5, 1] ) 
 
iVv51 = 	 Parameter(name='iVv51', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv51}', 
	 lhablock = 'IMZM_SCALARMIX', 
	 lhacode = [5, 1] ) 
 
rVv52 = 	 Parameter(name='rVv52', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv52}', 
	 lhablock = 'ZM_SCALARMIX', 
	 lhacode = [5, 2] ) 
 
iVv52 = 	 Parameter(name='iVv52', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv52}', 
	 lhablock = 'IMZM_SCALARMIX', 
	 lhacode = [5, 2] ) 
 
rVv53 = 	 Parameter(name='rVv53', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv53}', 
	 lhablock = 'ZM_SCALARMIX', 
	 lhacode = [5, 3] ) 
 
iVv53 = 	 Parameter(name='iVv53', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv53}', 
	 lhablock = 'IMZM_SCALARMIX', 
	 lhacode = [5, 3] ) 
 
rVv54 = 	 Parameter(name='rVv54', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv54}', 
	 lhablock = 'ZM_SCALARMIX', 
	 lhacode = [5, 4] ) 
 
iVv54 = 	 Parameter(name='iVv54', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv54}', 
	 lhablock = 'IMZM_SCALARMIX', 
	 lhacode = [5, 4] ) 
 
rVv55 = 	 Parameter(name='rVv55', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv55}', 
	 lhablock = 'ZM_SCALARMIX', 
	 lhacode = [5, 5] ) 
 
iVv55 = 	 Parameter(name='iVv55', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv55}', 
	 lhablock = 'IMZM_SCALARMIX', 
	 lhacode = [5, 5] ) 
 
rVv56 = 	 Parameter(name='rVv56', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv56}', 
	 lhablock = 'ZM_SCALARMIX', 
	 lhacode = [5, 6] ) 
 
iVv56 = 	 Parameter(name='iVv56', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv56}', 
	 lhablock = 'IMZM_SCALARMIX', 
	 lhacode = [5, 6] ) 
 
rVv61 = 	 Parameter(name='rVv61', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv61}', 
	 lhablock = 'ZM_SCALARMIX', 
	 lhacode = [6, 1] ) 
 
iVv61 = 	 Parameter(name='iVv61', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv61}', 
	 lhablock = 'IMZM_SCALARMIX', 
	 lhacode = [6, 1] ) 
 
rVv62 = 	 Parameter(name='rVv62', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv62}', 
	 lhablock = 'ZM_SCALARMIX', 
	 lhacode = [6, 2] ) 
 
iVv62 = 	 Parameter(name='iVv62', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv62}', 
	 lhablock = 'IMZM_SCALARMIX', 
	 lhacode = [6, 2] ) 
 
rVv63 = 	 Parameter(name='rVv63', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv63}', 
	 lhablock = 'ZM_SCALARMIX', 
	 lhacode = [6, 3] ) 
 
iVv63 = 	 Parameter(name='iVv63', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv63}', 
	 lhablock = 'IMZM_SCALARMIX', 
	 lhacode = [6, 3] ) 
 
rVv64 = 	 Parameter(name='rVv64', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv64}', 
	 lhablock = 'ZM_SCALARMIX', 
	 lhacode = [6, 4] ) 
 
iVv64 = 	 Parameter(name='iVv64', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv64}', 
	 lhablock = 'IMZM_SCALARMIX', 
	 lhacode = [6, 4] ) 
 
rVv65 = 	 Parameter(name='rVv65', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv65}', 
	 lhablock = 'ZM_SCALARMIX', 
	 lhacode = [6, 5] ) 
 
iVv65 = 	 Parameter(name='iVv65', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv65}', 
	 lhablock = 'IMZM_SCALARMIX', 
	 lhacode = [6, 5] ) 
 
rVv66 = 	 Parameter(name='rVv66', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv66}', 
	 lhablock = 'ZM_SCALARMIX', 
	 lhacode = [6, 6] ) 
 
iVv66 = 	 Parameter(name='iVv66', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Vv66}', 
	 lhablock = 'IMZM_SCALARMIX', 
	 lhacode = [6, 6] ) 
 
aS = 	 Parameter(name='aS', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0.119, 
	 texname = '\\text{aS}', 
	 lhablock = 'SMINPUTS', 
	 lhacode = [3] ) 
 
aEWM1 = 	 Parameter(name='aEWM1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 137.035999679, 
	 texname = '\\text{aEWM1}', 
	 lhablock = 'SMINPUTS', 
	 lhacode = [1] ) 
 
Gf = 	 Parameter(name='Gf', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0.0000116639, 
	 texname = '\\text{Gf}', 
	 lhablock = 'SMINPUTS', 
	 lhacode = [2] ) 
 
Y1d11 = 	 Parameter(name='Y1d11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rY1d11 + complex(0,1)*iY1d11', 
	 texname = '\\text{Y1d11}' ) 
 
Y1d12 = 	 Parameter(name='Y1d12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rY1d12 + complex(0,1)*iY1d12', 
	 texname = '\\text{Y1d12}' ) 
 
Y1d13 = 	 Parameter(name='Y1d13', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rY1d13 + complex(0,1)*iY1d13', 
	 texname = '\\text{Y1d13}' ) 
 
Y1d21 = 	 Parameter(name='Y1d21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rY1d21 + complex(0,1)*iY1d21', 
	 texname = '\\text{Y1d21}' ) 
 
Y1d22 = 	 Parameter(name='Y1d22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rY1d22 + complex(0,1)*iY1d22', 
	 texname = '\\text{Y1d22}' ) 
 
Y1d23 = 	 Parameter(name='Y1d23', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rY1d23 + complex(0,1)*iY1d23', 
	 texname = '\\text{Y1d23}' ) 
 
Y2d31 = 	 Parameter(name='Y2d31', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rY2d31 + complex(0,1)*iY2d31', 
	 texname = '\\text{Y2d31}' ) 
 
Y2d32 = 	 Parameter(name='Y2d32', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rY2d32 + complex(0,1)*iY2d32', 
	 texname = '\\text{Y2d32}' ) 
 
Y2d33 = 	 Parameter(name='Y2d33', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rY2d33 + complex(0,1)*iY2d33', 
	 texname = '\\text{Y2d33}' ) 
 
Y1u11 = 	 Parameter(name='Y1u11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rY1u11 + complex(0,1)*iY1u11', 
	 texname = '\\text{Y1u11}' ) 
 
Y1u12 = 	 Parameter(name='Y1u12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rY1u12 + complex(0,1)*iY1u12', 
	 texname = '\\text{Y1u12}' ) 
 
Y1u21 = 	 Parameter(name='Y1u21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rY1u21 + complex(0,1)*iY1u21', 
	 texname = '\\text{Y1u21}' ) 
 
Y1u22 = 	 Parameter(name='Y1u22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rY1u22 + complex(0,1)*iY1u22', 
	 texname = '\\text{Y1u22}' ) 
 
Y2u33 = 	 Parameter(name='Y2u33', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rY2u33 + complex(0,1)*iY2u33', 
	 texname = '\\text{Y2u33}' ) 
 
Y1e11 = 	 Parameter(name='Y1e11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rY1e11 + complex(0,1)*iY1e11', 
	 texname = '\\text{Y1e11}' ) 
 
Y1e12 = 	 Parameter(name='Y1e12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rY1e12 + complex(0,1)*iY1e12', 
	 texname = '\\text{Y1e12}' ) 
 
Y1e21 = 	 Parameter(name='Y1e21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rY1e21 + complex(0,1)*iY1e21', 
	 texname = '\\text{Y1e21}' ) 
 
Y1e22 = 	 Parameter(name='Y1e22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rY1e22 + complex(0,1)*iY1e22', 
	 texname = '\\text{Y1e22}' ) 
 
Y2e33 = 	 Parameter(name='Y2e33', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rY2e33 + complex(0,1)*iY2e33', 
	 texname = '\\text{Y2e33}' ) 
 
Y1n11 = 	 Parameter(name='Y1n11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rY1n11 + complex(0,1)*iY1n11', 
	 texname = '\\text{Y1n11}' ) 
 
Y1n12 = 	 Parameter(name='Y1n12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rY1n12 + complex(0,1)*iY1n12', 
	 texname = '\\text{Y1n12}' ) 
 
Y1n21 = 	 Parameter(name='Y1n21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rY1n21 + complex(0,1)*iY1n21', 
	 texname = '\\text{Y1n21}' ) 
 
Y1n22 = 	 Parameter(name='Y1n22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rY1n22 + complex(0,1)*iY1n22', 
	 texname = '\\text{Y1n22}' ) 
 
Y2n33 = 	 Parameter(name='Y2n33', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rY2n33 + complex(0,1)*iY2n33', 
	 texname = '\\text{Y2n33}' ) 
 
C13 = 	 Parameter(name='C13', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rC13 + complex(0,1)*iC13', 
	 texname = '\\text{C13}' ) 
 
C23 = 	 Parameter(name='C23', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rC23 + complex(0,1)*iC23', 
	 texname = '\\text{C23}' ) 
 
C31 = 	 Parameter(name='C31', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rC31 + complex(0,1)*iC31', 
	 texname = '\\text{C31}' ) 
 
C32 = 	 Parameter(name='C32', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rC32 + complex(0,1)*iC32', 
	 texname = '\\text{C32}' ) 
 
BB11 = 	 Parameter(name='BB11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rBB11 + complex(0,1)*iBB11', 
	 texname = '\\text{BB11}' ) 
 
BB12 = 	 Parameter(name='BB12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rBB12 + complex(0,1)*iBB12', 
	 texname = '\\text{BB12}' ) 
 
BB21 = 	 Parameter(name='BB21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rBB21 + complex(0,1)*iBB21', 
	 texname = '\\text{BB21}' ) 
 
BB22 = 	 Parameter(name='BB22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rBB22 + complex(0,1)*iBB22', 
	 texname = '\\text{BB22}' ) 
 
Lam1 = 	 Parameter(name='Lam1', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rLam1 + complex(0,1)*iLam1', 
	 texname = '\\text{Lam1}' ) 
 
Lam3 = 	 Parameter(name='Lam3', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rLam3 + complex(0,1)*iLam3', 
	 texname = '\\text{Lam3}' ) 
 
Lam4 = 	 Parameter(name='Lam4', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rLam4 + complex(0,1)*iLam4', 
	 texname = '\\text{Lam4}' ) 
 
Lam2 = 	 Parameter(name='Lam2', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rLam2 + complex(0,1)*iLam2', 
	 texname = '\\text{Lam2}' ) 
 
Lam1Dash = 	 Parameter(name='Lam1Dash', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rLam1Dash + complex(0,1)*iLam1Dash', 
	 texname = '\\text{Lam1Dash}' ) 
 
Lam2Dash = 	 Parameter(name='Lam2Dash', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rLam2Dash + complex(0,1)*iLam2Dash', 
	 texname = '\\text{Lam2Dash}' ) 
 
Lam3Dash = 	 Parameter(name='Lam3Dash', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rLam3Dash + complex(0,1)*iLam3Dash', 
	 texname = '\\text{Lam3Dash}' ) 
 
Aa1 = 	 Parameter(name='Aa1', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rAa1 + complex(0,1)*iAa1', 
	 texname = '\\text{Aa1}' ) 
 
Aa2 = 	 Parameter(name='Aa2', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rAa2 + complex(0,1)*iAa2', 
	 texname = '\\text{Aa2}' ) 
 
Aa3 = 	 Parameter(name='Aa3', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rAa3 + complex(0,1)*iAa3', 
	 texname = '\\text{Aa3}' ) 
 
Aa4 = 	 Parameter(name='Aa4', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rAa4 + complex(0,1)*iAa4', 
	 texname = '\\text{Aa4}' ) 
 
ZZ11 = 	 Parameter(name='ZZ11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZZ11 + complex(0,1)*iZZ11', 
	 texname = '\\text{ZZ11}' ) 
 
ZZ12 = 	 Parameter(name='ZZ12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZZ12 + complex(0,1)*iZZ12', 
	 texname = '\\text{ZZ12}' ) 
 
ZZ21 = 	 Parameter(name='ZZ21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZZ21 + complex(0,1)*iZZ21', 
	 texname = '\\text{ZZ21}' ) 
 
ZZ22 = 	 Parameter(name='ZZ22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZZ22 + complex(0,1)*iZZ22', 
	 texname = '\\text{ZZ22}' ) 
 
ZP11 = 	 Parameter(name='ZP11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZP11 + complex(0,1)*iZP11', 
	 texname = '\\text{ZP11}' ) 
 
ZP12 = 	 Parameter(name='ZP12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZP12 + complex(0,1)*iZP12', 
	 texname = '\\text{ZP12}' ) 
 
ZP21 = 	 Parameter(name='ZP21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZP21 + complex(0,1)*iZP21', 
	 texname = '\\text{ZP21}' ) 
 
ZP22 = 	 Parameter(name='ZP22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZP22 + complex(0,1)*iZP22', 
	 texname = '\\text{ZP22}' ) 
 
ZDL11 = 	 Parameter(name='ZDL11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDL11 + complex(0,1)*iZDL11', 
	 texname = '\\text{ZDL11}' ) 
 
ZDL12 = 	 Parameter(name='ZDL12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDL12 + complex(0,1)*iZDL12', 
	 texname = '\\text{ZDL12}' ) 
 
ZDL13 = 	 Parameter(name='ZDL13', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDL13 + complex(0,1)*iZDL13', 
	 texname = '\\text{ZDL13}' ) 
 
ZDL21 = 	 Parameter(name='ZDL21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDL21 + complex(0,1)*iZDL21', 
	 texname = '\\text{ZDL21}' ) 
 
ZDL22 = 	 Parameter(name='ZDL22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDL22 + complex(0,1)*iZDL22', 
	 texname = '\\text{ZDL22}' ) 
 
ZDL23 = 	 Parameter(name='ZDL23', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDL23 + complex(0,1)*iZDL23', 
	 texname = '\\text{ZDL23}' ) 
 
ZDL31 = 	 Parameter(name='ZDL31', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDL31 + complex(0,1)*iZDL31', 
	 texname = '\\text{ZDL31}' ) 
 
ZDL32 = 	 Parameter(name='ZDL32', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDL32 + complex(0,1)*iZDL32', 
	 texname = '\\text{ZDL32}' ) 
 
ZDL33 = 	 Parameter(name='ZDL33', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDL33 + complex(0,1)*iZDL33', 
	 texname = '\\text{ZDL33}' ) 
 
ZDR11 = 	 Parameter(name='ZDR11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDR11 + complex(0,1)*iZDR11', 
	 texname = '\\text{ZDR11}' ) 
 
ZDR12 = 	 Parameter(name='ZDR12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDR12 + complex(0,1)*iZDR12', 
	 texname = '\\text{ZDR12}' ) 
 
ZDR13 = 	 Parameter(name='ZDR13', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDR13 + complex(0,1)*iZDR13', 
	 texname = '\\text{ZDR13}' ) 
 
ZDR21 = 	 Parameter(name='ZDR21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDR21 + complex(0,1)*iZDR21', 
	 texname = '\\text{ZDR21}' ) 
 
ZDR22 = 	 Parameter(name='ZDR22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDR22 + complex(0,1)*iZDR22', 
	 texname = '\\text{ZDR22}' ) 
 
ZDR23 = 	 Parameter(name='ZDR23', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDR23 + complex(0,1)*iZDR23', 
	 texname = '\\text{ZDR23}' ) 
 
ZDR31 = 	 Parameter(name='ZDR31', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDR31 + complex(0,1)*iZDR31', 
	 texname = '\\text{ZDR31}' ) 
 
ZDR32 = 	 Parameter(name='ZDR32', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDR32 + complex(0,1)*iZDR32', 
	 texname = '\\text{ZDR32}' ) 
 
ZDR33 = 	 Parameter(name='ZDR33', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDR33 + complex(0,1)*iZDR33', 
	 texname = '\\text{ZDR33}' ) 
 
ZUL11 = 	 Parameter(name='ZUL11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUL11 + complex(0,1)*iZUL11', 
	 texname = '\\text{ZUL11}' ) 
 
ZUL12 = 	 Parameter(name='ZUL12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUL12 + complex(0,1)*iZUL12', 
	 texname = '\\text{ZUL12}' ) 
 
ZUL13 = 	 Parameter(name='ZUL13', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUL13 + complex(0,1)*iZUL13', 
	 texname = '\\text{ZUL13}' ) 
 
ZUL21 = 	 Parameter(name='ZUL21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUL21 + complex(0,1)*iZUL21', 
	 texname = '\\text{ZUL21}' ) 
 
ZUL22 = 	 Parameter(name='ZUL22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUL22 + complex(0,1)*iZUL22', 
	 texname = '\\text{ZUL22}' ) 
 
ZUL23 = 	 Parameter(name='ZUL23', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUL23 + complex(0,1)*iZUL23', 
	 texname = '\\text{ZUL23}' ) 
 
ZUL31 = 	 Parameter(name='ZUL31', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUL31 + complex(0,1)*iZUL31', 
	 texname = '\\text{ZUL31}' ) 
 
ZUL32 = 	 Parameter(name='ZUL32', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUL32 + complex(0,1)*iZUL32', 
	 texname = '\\text{ZUL32}' ) 
 
ZUL33 = 	 Parameter(name='ZUL33', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUL33 + complex(0,1)*iZUL33', 
	 texname = '\\text{ZUL33}' ) 
 
ZUR11 = 	 Parameter(name='ZUR11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUR11 + complex(0,1)*iZUR11', 
	 texname = '\\text{ZUR11}' ) 
 
ZUR12 = 	 Parameter(name='ZUR12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUR12 + complex(0,1)*iZUR12', 
	 texname = '\\text{ZUR12}' ) 
 
ZUR13 = 	 Parameter(name='ZUR13', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUR13 + complex(0,1)*iZUR13', 
	 texname = '\\text{ZUR13}' ) 
 
ZUR21 = 	 Parameter(name='ZUR21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUR21 + complex(0,1)*iZUR21', 
	 texname = '\\text{ZUR21}' ) 
 
ZUR22 = 	 Parameter(name='ZUR22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUR22 + complex(0,1)*iZUR22', 
	 texname = '\\text{ZUR22}' ) 
 
ZUR23 = 	 Parameter(name='ZUR23', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUR23 + complex(0,1)*iZUR23', 
	 texname = '\\text{ZUR23}' ) 
 
ZUR31 = 	 Parameter(name='ZUR31', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUR31 + complex(0,1)*iZUR31', 
	 texname = '\\text{ZUR31}' ) 
 
ZUR32 = 	 Parameter(name='ZUR32', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUR32 + complex(0,1)*iZUR32', 
	 texname = '\\text{ZUR32}' ) 
 
ZUR33 = 	 Parameter(name='ZUR33', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUR33 + complex(0,1)*iZUR33', 
	 texname = '\\text{ZUR33}' ) 
 
ZEL11 = 	 Parameter(name='ZEL11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZEL11 + complex(0,1)*iZEL11', 
	 texname = '\\text{ZEL11}' ) 
 
ZEL12 = 	 Parameter(name='ZEL12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZEL12 + complex(0,1)*iZEL12', 
	 texname = '\\text{ZEL12}' ) 
 
ZEL13 = 	 Parameter(name='ZEL13', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZEL13 + complex(0,1)*iZEL13', 
	 texname = '\\text{ZEL13}' ) 
 
ZEL21 = 	 Parameter(name='ZEL21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZEL21 + complex(0,1)*iZEL21', 
	 texname = '\\text{ZEL21}' ) 
 
ZEL22 = 	 Parameter(name='ZEL22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZEL22 + complex(0,1)*iZEL22', 
	 texname = '\\text{ZEL22}' ) 
 
ZEL23 = 	 Parameter(name='ZEL23', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZEL23 + complex(0,1)*iZEL23', 
	 texname = '\\text{ZEL23}' ) 
 
ZEL31 = 	 Parameter(name='ZEL31', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZEL31 + complex(0,1)*iZEL31', 
	 texname = '\\text{ZEL31}' ) 
 
ZEL32 = 	 Parameter(name='ZEL32', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZEL32 + complex(0,1)*iZEL32', 
	 texname = '\\text{ZEL32}' ) 
 
ZEL33 = 	 Parameter(name='ZEL33', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZEL33 + complex(0,1)*iZEL33', 
	 texname = '\\text{ZEL33}' ) 
 
ZER11 = 	 Parameter(name='ZER11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZER11 + complex(0,1)*iZER11', 
	 texname = '\\text{ZER11}' ) 
 
ZER12 = 	 Parameter(name='ZER12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZER12 + complex(0,1)*iZER12', 
	 texname = '\\text{ZER12}' ) 
 
ZER13 = 	 Parameter(name='ZER13', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZER13 + complex(0,1)*iZER13', 
	 texname = '\\text{ZER13}' ) 
 
ZER21 = 	 Parameter(name='ZER21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZER21 + complex(0,1)*iZER21', 
	 texname = '\\text{ZER21}' ) 
 
ZER22 = 	 Parameter(name='ZER22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZER22 + complex(0,1)*iZER22', 
	 texname = '\\text{ZER22}' ) 
 
ZER23 = 	 Parameter(name='ZER23', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZER23 + complex(0,1)*iZER23', 
	 texname = '\\text{ZER23}' ) 
 
ZER31 = 	 Parameter(name='ZER31', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZER31 + complex(0,1)*iZER31', 
	 texname = '\\text{ZER31}' ) 
 
ZER32 = 	 Parameter(name='ZER32', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZER32 + complex(0,1)*iZER32', 
	 texname = '\\text{ZER32}' ) 
 
ZER33 = 	 Parameter(name='ZER33', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZER33 + complex(0,1)*iZER33', 
	 texname = '\\text{ZER33}' ) 
 
Vv11 = 	 Parameter(name='Vv11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVv11 + complex(0,1)*iVv11', 
	 texname = '\\text{Vv11}' ) 
 
Vv12 = 	 Parameter(name='Vv12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVv12 + complex(0,1)*iVv12', 
	 texname = '\\text{Vv12}' ) 
 
Vv13 = 	 Parameter(name='Vv13', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVv13 + complex(0,1)*iVv13', 
	 texname = '\\text{Vv13}' ) 
 
Vv14 = 	 Parameter(name='Vv14', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVv14 + complex(0,1)*iVv14', 
	 texname = '\\text{Vv14}' ) 
 
Vv15 = 	 Parameter(name='Vv15', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVv15 + complex(0,1)*iVv15', 
	 texname = '\\text{Vv15}' ) 
 
Vv16 = 	 Parameter(name='Vv16', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVv16 + complex(0,1)*iVv16', 
	 texname = '\\text{Vv16}' ) 
 
Vv21 = 	 Parameter(name='Vv21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVv21 + complex(0,1)*iVv21', 
	 texname = '\\text{Vv21}' ) 
 
Vv22 = 	 Parameter(name='Vv22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVv22 + complex(0,1)*iVv22', 
	 texname = '\\text{Vv22}' ) 
 
Vv23 = 	 Parameter(name='Vv23', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVv23 + complex(0,1)*iVv23', 
	 texname = '\\text{Vv23}' ) 
 
Vv24 = 	 Parameter(name='Vv24', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVv24 + complex(0,1)*iVv24', 
	 texname = '\\text{Vv24}' ) 
 
Vv25 = 	 Parameter(name='Vv25', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVv25 + complex(0,1)*iVv25', 
	 texname = '\\text{Vv25}' ) 
 
Vv26 = 	 Parameter(name='Vv26', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVv26 + complex(0,1)*iVv26', 
	 texname = '\\text{Vv26}' ) 
 
Vv31 = 	 Parameter(name='Vv31', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVv31 + complex(0,1)*iVv31', 
	 texname = '\\text{Vv31}' ) 
 
Vv32 = 	 Parameter(name='Vv32', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVv32 + complex(0,1)*iVv32', 
	 texname = '\\text{Vv32}' ) 
 
Vv33 = 	 Parameter(name='Vv33', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVv33 + complex(0,1)*iVv33', 
	 texname = '\\text{Vv33}' ) 
 
Vv34 = 	 Parameter(name='Vv34', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVv34 + complex(0,1)*iVv34', 
	 texname = '\\text{Vv34}' ) 
 
Vv35 = 	 Parameter(name='Vv35', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVv35 + complex(0,1)*iVv35', 
	 texname = '\\text{Vv35}' ) 
 
Vv36 = 	 Parameter(name='Vv36', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVv36 + complex(0,1)*iVv36', 
	 texname = '\\text{Vv36}' ) 
 
Vv41 = 	 Parameter(name='Vv41', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVv41 + complex(0,1)*iVv41', 
	 texname = '\\text{Vv41}' ) 
 
Vv42 = 	 Parameter(name='Vv42', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVv42 + complex(0,1)*iVv42', 
	 texname = '\\text{Vv42}' ) 
 
Vv43 = 	 Parameter(name='Vv43', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVv43 + complex(0,1)*iVv43', 
	 texname = '\\text{Vv43}' ) 
 
Vv44 = 	 Parameter(name='Vv44', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVv44 + complex(0,1)*iVv44', 
	 texname = '\\text{Vv44}' ) 
 
Vv45 = 	 Parameter(name='Vv45', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVv45 + complex(0,1)*iVv45', 
	 texname = '\\text{Vv45}' ) 
 
Vv46 = 	 Parameter(name='Vv46', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVv46 + complex(0,1)*iVv46', 
	 texname = '\\text{Vv46}' ) 
 
Vv51 = 	 Parameter(name='Vv51', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVv51 + complex(0,1)*iVv51', 
	 texname = '\\text{Vv51}' ) 
 
Vv52 = 	 Parameter(name='Vv52', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVv52 + complex(0,1)*iVv52', 
	 texname = '\\text{Vv52}' ) 
 
Vv53 = 	 Parameter(name='Vv53', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVv53 + complex(0,1)*iVv53', 
	 texname = '\\text{Vv53}' ) 
 
Vv54 = 	 Parameter(name='Vv54', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVv54 + complex(0,1)*iVv54', 
	 texname = '\\text{Vv54}' ) 
 
Vv55 = 	 Parameter(name='Vv55', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVv55 + complex(0,1)*iVv55', 
	 texname = '\\text{Vv55}' ) 
 
Vv56 = 	 Parameter(name='Vv56', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVv56 + complex(0,1)*iVv56', 
	 texname = '\\text{Vv56}' ) 
 
Vv61 = 	 Parameter(name='Vv61', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVv61 + complex(0,1)*iVv61', 
	 texname = '\\text{Vv61}' ) 
 
Vv62 = 	 Parameter(name='Vv62', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVv62 + complex(0,1)*iVv62', 
	 texname = '\\text{Vv62}' ) 
 
Vv63 = 	 Parameter(name='Vv63', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVv63 + complex(0,1)*iVv63', 
	 texname = '\\text{Vv63}' ) 
 
Vv64 = 	 Parameter(name='Vv64', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVv64 + complex(0,1)*iVv64', 
	 texname = '\\text{Vv64}' ) 
 
Vv65 = 	 Parameter(name='Vv65', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVv65 + complex(0,1)*iVv65', 
	 texname = '\\text{Vv65}' ) 
 
Vv66 = 	 Parameter(name='Vv66', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVv66 + complex(0,1)*iVv66', 
	 texname = '\\text{Vv66}' ) 
 
G = 	 Parameter(name='G', 
	 nature = 'internal', 
	 type = 'real', 
	 value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)', 
	 texname = 'G') 
 
el = 	 Parameter(name='el', 
	 nature = 'internal', 
	 type = 'real', 
	 value = '2*cmath.sqrt(1/aEWM1)*cmath.sqrt(cmath.pi)', 
	 texname = 'el') 
 
MWm = 	 Parameter(name='MWm', 
	 nature = 'internal', 
	 type = 'real', 
	 value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (MZ**2*cmath.pi)/(cmath.sqrt(2)*aEWM1*Gf)))', 
	 texname = 'MWm') 
 
TW = 	 Parameter(name='TW', 
	 nature = 'internal', 
	 type = 'real', 
	 value = 'cmath.asin(cmath.sqrt(1 - MWm**2/MZ**2))', 
	 texname = 'TW') 
 
g1 = 	 Parameter(name='g1', 
	 nature = 'internal', 
	 type = 'real', 
	 value = 'el*1./cmath.cos(TW)', 
	 texname = 'g1') 
 
g2 = 	 Parameter(name='g2', 
	 nature = 'internal', 
	 type = 'real', 
	 value = 'el*1./cmath.sin(TW)', 
	 texname = 'g2') 
 
RXiWm = 	 Parameter(name='RXiWm', 
	 nature = 'internal', 
	 type = 'real', 
	 value = '1.', 
	 texname = 'RXiWm') 
 
RXiZ = 	 Parameter(name='RXiZ', 
	 nature = 'internal', 
	 type = 'real', 
	 value = '1.', 
	 texname = 'RXiZ') 
 
HPP1 = 	 Parameter(name='HPP1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{HPP1}', 
	 lhablock = 'EFFHIGGSCOUPLINGS', 
	 lhacode = [25,22,22] ) 
 
HGG1 = 	 Parameter(name='HGG1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{HGG1}', 
	 lhablock = 'EFFHIGGSCOUPLINGS', 
	 lhacode = [25,21,21] ) 
 
HPP2 = 	 Parameter(name='HPP2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{HPP2}', 
	 lhablock = 'EFFHIGGSCOUPLINGS', 
	 lhacode = [26,22,22] ) 
 
HGG2 = 	 Parameter(name='HGG2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{HGG2}', 
	 lhablock = 'EFFHIGGSCOUPLINGS', 
	 lhacode = [26,21,21] ) 
 
HPP3 = 	 Parameter(name='HPP3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{HPP3}', 
	 lhablock = 'EFFHIGGSCOUPLINGS', 
	 lhacode = [27,22,22] ) 
 
HGG3 = 	 Parameter(name='HGG3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{HGG3}', 
	 lhablock = 'EFFHIGGSCOUPLINGS', 
	 lhacode = [27,21,21] ) 
 
APP2 = 	 Parameter(name='APP2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{APP2}', 
	 lhablock = 'EFFHIGGSCOUPLINGS', 
	 lhacode = [35,22,22] ) 
 
AGG2 = 	 Parameter(name='AGG2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{AGG2}', 
	 lhablock = 'EFFHIGGSCOUPLINGS', 
	 lhacode = [35,21,21] ) 
 
APP3 = 	 Parameter(name='APP3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{APP3}', 
	 lhablock = 'EFFHIGGSCOUPLINGS', 
	 lhacode = [36,22,22] ) 
 
AGG3 = 	 Parameter(name='AGG3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{AGG3}', 
	 lhablock = 'EFFHIGGSCOUPLINGS', 
	 lhacode = [36,21,21] ) 
 
