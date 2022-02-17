from object_library import all_couplings,Coupling 
from cmath import exp 
from function_library import complexconjugate,re,im,csc,sec,acsc,asec 
 
 
GC_1 = Coupling(name = 'GC_1',
	 value = '(ZA12*(ZA11*ZA13*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)) + ZA13*(2*v1*ZA13*(Aa3 + Aa4 - complexconjugate(Aa3) - complexconjugate(Aa4)) + ZA11*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA13*(2*(v2*ZA11 - v1*ZA12)*ZA13*(-Aa3 - Aa4 + complexconjugate(Aa3) + complexconjugate(Aa4)) + ZA12*(2*v1*ZA13*(Aa3 + Aa4 - complexconjugate(Aa3) - complexconjugate(Aa4)) + ZA11*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + ZA11*(2*v2*ZA13*(-Aa3 - Aa4 + complexconjugate(Aa3) + complexconjugate(Aa4)) + ZA12*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA11*(ZA12*ZA13*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)) + ZA13*(2*v2*ZA13*(-Aa3 - Aa4 + complexconjugate(Aa3) + complexconjugate(Aa4)) + ZA12*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))))/4.', 
	 order = {'QED':1} ) 
 
GC_2 = Coupling(name = 'GC_2',
	 value = '(ZA12*(ZA11*ZA23*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)) + ZA13*(2*v1*ZA23*(Aa3 + Aa4 - complexconjugate(Aa3) - complexconjugate(Aa4)) + ZA21*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA13*(2*ZA13*(v2*ZA21 - v1*ZA22)*(-Aa3 - Aa4 + complexconjugate(Aa3) + complexconjugate(Aa4)) + ZA12*(2*v1*ZA23*(Aa3 + Aa4 - complexconjugate(Aa3) - complexconjugate(Aa4)) + ZA21*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + ZA11*(2*v2*ZA23*(-Aa3 - Aa4 + complexconjugate(Aa3) + complexconjugate(Aa4)) + ZA22*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA11*(ZA12*ZA23*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)) + ZA13*(2*v2*ZA23*(-Aa3 - Aa4 + complexconjugate(Aa3) + complexconjugate(Aa4)) + ZA22*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))))/4.', 
	 order = {'QED':1} ) 
 
GC_3 = Coupling(name = 'GC_3',
	 value = '(ZA12*(ZA11*ZA33*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)) + ZA13*(2*v1*ZA33*(Aa3 + Aa4 - complexconjugate(Aa3) - complexconjugate(Aa4)) + ZA31*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA13*(2*ZA13*(v2*ZA31 - v1*ZA32)*(-Aa3 - Aa4 + complexconjugate(Aa3) + complexconjugate(Aa4)) + ZA12*(2*v1*ZA33*(Aa3 + Aa4 - complexconjugate(Aa3) - complexconjugate(Aa4)) + ZA31*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + ZA11*(2*v2*ZA33*(-Aa3 - Aa4 + complexconjugate(Aa3) + complexconjugate(Aa4)) + ZA32*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA11*(ZA12*ZA33*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)) + ZA13*(2*v2*ZA33*(-Aa3 - Aa4 + complexconjugate(Aa3) + complexconjugate(Aa4)) + ZA32*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))))/4.', 
	 order = {'QED':1} ) 
 
GC_4 = Coupling(name = 'GC_4',
	 value = '(ZA12*(ZA21*ZA23*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)) + ZA23*(2*v1*ZA23*(Aa3 + Aa4 - complexconjugate(Aa3) - complexconjugate(Aa4)) + ZA21*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA13*(2*(v2*ZA21 - v1*ZA22)*ZA23*(-Aa3 - Aa4 + complexconjugate(Aa3) + complexconjugate(Aa4)) + ZA22*(2*v1*ZA23*(Aa3 + Aa4 - complexconjugate(Aa3) - complexconjugate(Aa4)) + ZA21*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + ZA21*(2*v2*ZA23*(-Aa3 - Aa4 + complexconjugate(Aa3) + complexconjugate(Aa4)) + ZA22*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA11*(ZA22*ZA23*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)) + ZA23*(2*v2*ZA23*(-Aa3 - Aa4 + complexconjugate(Aa3) + complexconjugate(Aa4)) + ZA22*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))))/4.', 
	 order = {'QED':1} ) 
 
GC_5 = Coupling(name = 'GC_5',
	 value = '(ZA12*(ZA21*ZA33*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)) + ZA23*(2*v1*ZA33*(Aa3 + Aa4 - complexconjugate(Aa3) - complexconjugate(Aa4)) + ZA31*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA13*(2*ZA23*(v2*ZA31 - v1*ZA32)*(-Aa3 - Aa4 + complexconjugate(Aa3) + complexconjugate(Aa4)) + ZA22*(2*v1*ZA33*(Aa3 + Aa4 - complexconjugate(Aa3) - complexconjugate(Aa4)) + ZA31*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + ZA21*(2*v2*ZA33*(-Aa3 - Aa4 + complexconjugate(Aa3) + complexconjugate(Aa4)) + ZA32*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA11*(ZA22*ZA33*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)) + ZA23*(2*v2*ZA33*(-Aa3 - Aa4 + complexconjugate(Aa3) + complexconjugate(Aa4)) + ZA32*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))))/4.', 
	 order = {'QED':1} ) 
 
GC_6 = Coupling(name = 'GC_6',
	 value = '(ZA12*(ZA31*ZA33*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)) + ZA33*(2*v1*ZA33*(Aa3 + Aa4 - complexconjugate(Aa3) - complexconjugate(Aa4)) + ZA31*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA13*(2*(v2*ZA31 - v1*ZA32)*ZA33*(-Aa3 - Aa4 + complexconjugate(Aa3) + complexconjugate(Aa4)) + ZA32*(2*v1*ZA33*(Aa3 + Aa4 - complexconjugate(Aa3) - complexconjugate(Aa4)) + ZA31*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + ZA31*(2*v2*ZA33*(-Aa3 - Aa4 + complexconjugate(Aa3) + complexconjugate(Aa4)) + ZA32*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA11*(ZA32*ZA33*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)) + ZA33*(2*v2*ZA33*(-Aa3 - Aa4 + complexconjugate(Aa3) + complexconjugate(Aa4)) + ZA32*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))))/4.', 
	 order = {'QED':1} ) 
 
GC_7 = Coupling(name = 'GC_7',
	 value = '(ZA22*(ZA21*ZA23*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)) + ZA23*(2*v1*ZA23*(Aa3 + Aa4 - complexconjugate(Aa3) - complexconjugate(Aa4)) + ZA21*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA23*(2*(v2*ZA21 - v1*ZA22)*ZA23*(-Aa3 - Aa4 + complexconjugate(Aa3) + complexconjugate(Aa4)) + ZA22*(2*v1*ZA23*(Aa3 + Aa4 - complexconjugate(Aa3) - complexconjugate(Aa4)) + ZA21*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + ZA21*(2*v2*ZA23*(-Aa3 - Aa4 + complexconjugate(Aa3) + complexconjugate(Aa4)) + ZA22*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA21*(ZA22*ZA23*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)) + ZA23*(2*v2*ZA23*(-Aa3 - Aa4 + complexconjugate(Aa3) + complexconjugate(Aa4)) + ZA22*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))))/4.', 
	 order = {'QED':1} ) 
 
GC_8 = Coupling(name = 'GC_8',
	 value = '(ZA22*(ZA21*ZA33*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)) + ZA23*(2*v1*ZA33*(Aa3 + Aa4 - complexconjugate(Aa3) - complexconjugate(Aa4)) + ZA31*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA23*(2*ZA23*(v2*ZA31 - v1*ZA32)*(-Aa3 - Aa4 + complexconjugate(Aa3) + complexconjugate(Aa4)) + ZA22*(2*v1*ZA33*(Aa3 + Aa4 - complexconjugate(Aa3) - complexconjugate(Aa4)) + ZA31*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + ZA21*(2*v2*ZA33*(-Aa3 - Aa4 + complexconjugate(Aa3) + complexconjugate(Aa4)) + ZA32*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA21*(ZA22*ZA33*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)) + ZA23*(2*v2*ZA33*(-Aa3 - Aa4 + complexconjugate(Aa3) + complexconjugate(Aa4)) + ZA32*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))))/4.', 
	 order = {'QED':1} ) 
 
GC_9 = Coupling(name = 'GC_9',
	 value = '(ZA22*(ZA31*ZA33*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)) + ZA33*(2*v1*ZA33*(Aa3 + Aa4 - complexconjugate(Aa3) - complexconjugate(Aa4)) + ZA31*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA23*(2*(v2*ZA31 - v1*ZA32)*ZA33*(-Aa3 - Aa4 + complexconjugate(Aa3) + complexconjugate(Aa4)) + ZA32*(2*v1*ZA33*(Aa3 + Aa4 - complexconjugate(Aa3) - complexconjugate(Aa4)) + ZA31*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + ZA31*(2*v2*ZA33*(-Aa3 - Aa4 + complexconjugate(Aa3) + complexconjugate(Aa4)) + ZA32*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA21*(ZA32*ZA33*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)) + ZA33*(2*v2*ZA33*(-Aa3 - Aa4 + complexconjugate(Aa3) + complexconjugate(Aa4)) + ZA32*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))))/4.', 
	 order = {'QED':1} ) 
 
GC_10 = Coupling(name = 'GC_10',
	 value = '(ZA32*(ZA31*ZA33*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)) + ZA33*(2*v1*ZA33*(Aa3 + Aa4 - complexconjugate(Aa3) - complexconjugate(Aa4)) + ZA31*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA33*(2*(v2*ZA31 - v1*ZA32)*ZA33*(-Aa3 - Aa4 + complexconjugate(Aa3) + complexconjugate(Aa4)) + ZA32*(2*v1*ZA33*(Aa3 + Aa4 - complexconjugate(Aa3) - complexconjugate(Aa4)) + ZA31*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + ZA31*(2*v2*ZA33*(-Aa3 - Aa4 + complexconjugate(Aa3) + complexconjugate(Aa4)) + ZA32*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA31*(ZA32*ZA33*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)) + ZA33*(2*v2*ZA33*(-Aa3 - Aa4 + complexconjugate(Aa3) + complexconjugate(Aa4)) + ZA32*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))))/4.', 
	 order = {'QED':1} ) 
 
GC_11 = Coupling(name = 'GC_11',
	 value = '1./4.*complex(0,1)*(ZA13*(ZA12*(2*v1*ZH13*(Aa3 - Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH11*(cmath.sqrt(2)*Aa1 - cmath.sqrt(2)*Aa2 + 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + ZA11*(2*v2*ZH13*(-Aa3 + Aa4 - complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH12*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4))) + 2*ZA13*(-4*v3*ZH13*complexconjugate(Lam1Dash) + ZH11*(Aa3*v2 + Aa4*v2 + v2*complexconjugate(Aa3) + v2*complexconjugate(Aa4) - 2*v1*complexconjugate(Lam2Dash)) + ZH12*(Aa3*v1 + Aa4*v1 + v1*complexconjugate(Aa3) + v1*complexconjugate(Aa4) - 2*v2*complexconjugate(Lam3Dash)))) - ZA12*(ZA11*ZH13*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZA13*(2*v1*ZH13*(-Aa3 + Aa4 - complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH11*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4))) + 4*ZA12*(2*v2*ZH12*complexconjugate(Lam2) + v3*ZH13*complexconjugate(Lam3Dash) + v1*ZH11*(complexconjugate(Lam3) + complexconjugate(Lam4)))) - ZA11*(ZA12*ZH13*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZA13*(2*v2*ZH13*(Aa3 - Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH12*(cmath.sqrt(2)*Aa1 - cmath.sqrt(2)*Aa2 + 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + 4*ZA11*(2*v1*ZH11*complexconjugate(Lam1) + v3*ZH13*complexconjugate(Lam2Dash) + v2*ZH12*(complexconjugate(Lam3) + complexconjugate(Lam4)))))', 
	 order = {'QED':1} ) 
 
GC_12 = Coupling(name = 'GC_12',
	 value = '1./4.*complex(0,1)*(ZA13*(ZA12*(2*v1*ZH23*(Aa3 - Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH21*(cmath.sqrt(2)*Aa1 - cmath.sqrt(2)*Aa2 + 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + ZA11*(2*v2*ZH23*(-Aa3 + Aa4 - complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH22*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4))) + 2*ZA13*(-4*v3*ZH23*complexconjugate(Lam1Dash) + ZH21*(Aa3*v2 + Aa4*v2 + v2*complexconjugate(Aa3) + v2*complexconjugate(Aa4) - 2*v1*complexconjugate(Lam2Dash)) + ZH22*(Aa3*v1 + Aa4*v1 + v1*complexconjugate(Aa3) + v1*complexconjugate(Aa4) - 2*v2*complexconjugate(Lam3Dash)))) - ZA12*(ZA11*ZH23*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZA13*(2*v1*ZH23*(-Aa3 + Aa4 - complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH21*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4))) + 4*ZA12*(2*v2*ZH22*complexconjugate(Lam2) + v3*ZH23*complexconjugate(Lam3Dash) + v1*ZH21*(complexconjugate(Lam3) + complexconjugate(Lam4)))) - ZA11*(ZA12*ZH23*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZA13*(2*v2*ZH23*(Aa3 - Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH22*(cmath.sqrt(2)*Aa1 - cmath.sqrt(2)*Aa2 + 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + 4*ZA11*(2*v1*ZH21*complexconjugate(Lam1) + v3*ZH23*complexconjugate(Lam2Dash) + v2*ZH22*(complexconjugate(Lam3) + complexconjugate(Lam4)))))', 
	 order = {'QED':1} ) 
 
GC_13 = Coupling(name = 'GC_13',
	 value = '1./4.*complex(0,1)*(ZA13*(ZA12*(2*v1*ZH33*(Aa3 - Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH31*(cmath.sqrt(2)*Aa1 - cmath.sqrt(2)*Aa2 + 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + ZA11*(2*v2*ZH33*(-Aa3 + Aa4 - complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH32*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4))) + 2*ZA13*(-4*v3*ZH33*complexconjugate(Lam1Dash) + ZH31*(Aa3*v2 + Aa4*v2 + v2*complexconjugate(Aa3) + v2*complexconjugate(Aa4) - 2*v1*complexconjugate(Lam2Dash)) + ZH32*(Aa3*v1 + Aa4*v1 + v1*complexconjugate(Aa3) + v1*complexconjugate(Aa4) - 2*v2*complexconjugate(Lam3Dash)))) - ZA12*(ZA11*ZH33*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZA13*(2*v1*ZH33*(-Aa3 + Aa4 - complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH31*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4))) + 4*ZA12*(2*v2*ZH32*complexconjugate(Lam2) + v3*ZH33*complexconjugate(Lam3Dash) + v1*ZH31*(complexconjugate(Lam3) + complexconjugate(Lam4)))) - ZA11*(ZA12*ZH33*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZA13*(2*v2*ZH33*(Aa3 - Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH32*(cmath.sqrt(2)*Aa1 - cmath.sqrt(2)*Aa2 + 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + 4*ZA11*(2*v1*ZH31*complexconjugate(Lam1) + v3*ZH33*complexconjugate(Lam2Dash) + v2*ZH32*(complexconjugate(Lam3) + complexconjugate(Lam4)))))', 
	 order = {'QED':1} ) 
 
GC_14 = Coupling(name = 'GC_14',
	 value = '1./4.*complex(0,1)*(ZA13*(ZA22*(2*v1*ZH13*(Aa3 - Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH11*(cmath.sqrt(2)*Aa1 - cmath.sqrt(2)*Aa2 + 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + ZA21*(2*v2*ZH13*(-Aa3 + Aa4 - complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH12*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4))) + 2*ZA23*(-4*v3*ZH13*complexconjugate(Lam1Dash) + ZH11*(Aa3*v2 + Aa4*v2 + v2*complexconjugate(Aa3) + v2*complexconjugate(Aa4) - 2*v1*complexconjugate(Lam2Dash)) + ZH12*(Aa3*v1 + Aa4*v1 + v1*complexconjugate(Aa3) + v1*complexconjugate(Aa4) - 2*v2*complexconjugate(Lam3Dash)))) - ZA12*(ZA21*ZH13*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZA23*(2*v1*ZH13*(-Aa3 + Aa4 - complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH11*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4))) + 4*ZA22*(2*v2*ZH12*complexconjugate(Lam2) + v3*ZH13*complexconjugate(Lam3Dash) + v1*ZH11*(complexconjugate(Lam3) + complexconjugate(Lam4)))) - ZA11*(ZA22*ZH13*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZA23*(2*v2*ZH13*(Aa3 - Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH12*(cmath.sqrt(2)*Aa1 - cmath.sqrt(2)*Aa2 + 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + 4*ZA21*(2*v1*ZH11*complexconjugate(Lam1) + v3*ZH13*complexconjugate(Lam2Dash) + v2*ZH12*(complexconjugate(Lam3) + complexconjugate(Lam4)))))', 
	 order = {'QED':1} ) 
 
GC_15 = Coupling(name = 'GC_15',
	 value = '1./4.*complex(0,1)*(ZA13*(ZA22*(2*v1*ZH23*(Aa3 - Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH21*(cmath.sqrt(2)*Aa1 - cmath.sqrt(2)*Aa2 + 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + ZA21*(2*v2*ZH23*(-Aa3 + Aa4 - complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH22*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4))) + 2*ZA23*(-4*v3*ZH23*complexconjugate(Lam1Dash) + ZH21*(Aa3*v2 + Aa4*v2 + v2*complexconjugate(Aa3) + v2*complexconjugate(Aa4) - 2*v1*complexconjugate(Lam2Dash)) + ZH22*(Aa3*v1 + Aa4*v1 + v1*complexconjugate(Aa3) + v1*complexconjugate(Aa4) - 2*v2*complexconjugate(Lam3Dash)))) - ZA12*(ZA21*ZH23*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZA23*(2*v1*ZH23*(-Aa3 + Aa4 - complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH21*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4))) + 4*ZA22*(2*v2*ZH22*complexconjugate(Lam2) + v3*ZH23*complexconjugate(Lam3Dash) + v1*ZH21*(complexconjugate(Lam3) + complexconjugate(Lam4)))) - ZA11*(ZA22*ZH23*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZA23*(2*v2*ZH23*(Aa3 - Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH22*(cmath.sqrt(2)*Aa1 - cmath.sqrt(2)*Aa2 + 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + 4*ZA21*(2*v1*ZH21*complexconjugate(Lam1) + v3*ZH23*complexconjugate(Lam2Dash) + v2*ZH22*(complexconjugate(Lam3) + complexconjugate(Lam4)))))', 
	 order = {'QED':1} ) 
 
GC_16 = Coupling(name = 'GC_16',
	 value = '1./4.*complex(0,1)*(ZA13*(ZA22*(2*v1*ZH33*(Aa3 - Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH31*(cmath.sqrt(2)*Aa1 - cmath.sqrt(2)*Aa2 + 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + ZA21*(2*v2*ZH33*(-Aa3 + Aa4 - complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH32*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4))) + 2*ZA23*(-4*v3*ZH33*complexconjugate(Lam1Dash) + ZH31*(Aa3*v2 + Aa4*v2 + v2*complexconjugate(Aa3) + v2*complexconjugate(Aa4) - 2*v1*complexconjugate(Lam2Dash)) + ZH32*(Aa3*v1 + Aa4*v1 + v1*complexconjugate(Aa3) + v1*complexconjugate(Aa4) - 2*v2*complexconjugate(Lam3Dash)))) - ZA12*(ZA21*ZH33*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZA23*(2*v1*ZH33*(-Aa3 + Aa4 - complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH31*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4))) + 4*ZA22*(2*v2*ZH32*complexconjugate(Lam2) + v3*ZH33*complexconjugate(Lam3Dash) + v1*ZH31*(complexconjugate(Lam3) + complexconjugate(Lam4)))) - ZA11*(ZA22*ZH33*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZA23*(2*v2*ZH33*(Aa3 - Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH32*(cmath.sqrt(2)*Aa1 - cmath.sqrt(2)*Aa2 + 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + 4*ZA21*(2*v1*ZH31*complexconjugate(Lam1) + v3*ZH33*complexconjugate(Lam2Dash) + v2*ZH32*(complexconjugate(Lam3) + complexconjugate(Lam4)))))', 
	 order = {'QED':1} ) 
 
GC_17 = Coupling(name = 'GC_17',
	 value = '1./4.*complex(0,1)*(ZA13*(ZA32*(2*v1*ZH13*(Aa3 - Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH11*(cmath.sqrt(2)*Aa1 - cmath.sqrt(2)*Aa2 + 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + ZA31*(2*v2*ZH13*(-Aa3 + Aa4 - complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH12*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4))) + 2*ZA33*(-4*v3*ZH13*complexconjugate(Lam1Dash) + ZH11*(Aa3*v2 + Aa4*v2 + v2*complexconjugate(Aa3) + v2*complexconjugate(Aa4) - 2*v1*complexconjugate(Lam2Dash)) + ZH12*(Aa3*v1 + Aa4*v1 + v1*complexconjugate(Aa3) + v1*complexconjugate(Aa4) - 2*v2*complexconjugate(Lam3Dash)))) - ZA12*(ZA31*ZH13*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZA33*(2*v1*ZH13*(-Aa3 + Aa4 - complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH11*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4))) + 4*ZA32*(2*v2*ZH12*complexconjugate(Lam2) + v3*ZH13*complexconjugate(Lam3Dash) + v1*ZH11*(complexconjugate(Lam3) + complexconjugate(Lam4)))) - ZA11*(ZA32*ZH13*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZA33*(2*v2*ZH13*(Aa3 - Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH12*(cmath.sqrt(2)*Aa1 - cmath.sqrt(2)*Aa2 + 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + 4*ZA31*(2*v1*ZH11*complexconjugate(Lam1) + v3*ZH13*complexconjugate(Lam2Dash) + v2*ZH12*(complexconjugate(Lam3) + complexconjugate(Lam4)))))', 
	 order = {'QED':1} ) 
 
GC_18 = Coupling(name = 'GC_18',
	 value = '1./4.*complex(0,1)*(ZA13*(ZA32*(2*v1*ZH23*(Aa3 - Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH21*(cmath.sqrt(2)*Aa1 - cmath.sqrt(2)*Aa2 + 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + ZA31*(2*v2*ZH23*(-Aa3 + Aa4 - complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH22*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4))) + 2*ZA33*(-4*v3*ZH23*complexconjugate(Lam1Dash) + ZH21*(Aa3*v2 + Aa4*v2 + v2*complexconjugate(Aa3) + v2*complexconjugate(Aa4) - 2*v1*complexconjugate(Lam2Dash)) + ZH22*(Aa3*v1 + Aa4*v1 + v1*complexconjugate(Aa3) + v1*complexconjugate(Aa4) - 2*v2*complexconjugate(Lam3Dash)))) - ZA12*(ZA31*ZH23*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZA33*(2*v1*ZH23*(-Aa3 + Aa4 - complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH21*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4))) + 4*ZA32*(2*v2*ZH22*complexconjugate(Lam2) + v3*ZH23*complexconjugate(Lam3Dash) + v1*ZH21*(complexconjugate(Lam3) + complexconjugate(Lam4)))) - ZA11*(ZA32*ZH23*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZA33*(2*v2*ZH23*(Aa3 - Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH22*(cmath.sqrt(2)*Aa1 - cmath.sqrt(2)*Aa2 + 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + 4*ZA31*(2*v1*ZH21*complexconjugate(Lam1) + v3*ZH23*complexconjugate(Lam2Dash) + v2*ZH22*(complexconjugate(Lam3) + complexconjugate(Lam4)))))', 
	 order = {'QED':1} ) 
 
GC_19 = Coupling(name = 'GC_19',
	 value = '1./4.*complex(0,1)*(ZA13*(ZA32*(2*v1*ZH33*(Aa3 - Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH31*(cmath.sqrt(2)*Aa1 - cmath.sqrt(2)*Aa2 + 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + ZA31*(2*v2*ZH33*(-Aa3 + Aa4 - complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH32*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4))) + 2*ZA33*(-4*v3*ZH33*complexconjugate(Lam1Dash) + ZH31*(Aa3*v2 + Aa4*v2 + v2*complexconjugate(Aa3) + v2*complexconjugate(Aa4) - 2*v1*complexconjugate(Lam2Dash)) + ZH32*(Aa3*v1 + Aa4*v1 + v1*complexconjugate(Aa3) + v1*complexconjugate(Aa4) - 2*v2*complexconjugate(Lam3Dash)))) - ZA12*(ZA31*ZH33*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZA33*(2*v1*ZH33*(-Aa3 + Aa4 - complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH31*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4))) + 4*ZA32*(2*v2*ZH32*complexconjugate(Lam2) + v3*ZH33*complexconjugate(Lam3Dash) + v1*ZH31*(complexconjugate(Lam3) + complexconjugate(Lam4)))) - ZA11*(ZA32*ZH33*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZA33*(2*v2*ZH33*(Aa3 - Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH32*(cmath.sqrt(2)*Aa1 - cmath.sqrt(2)*Aa2 + 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + 4*ZA31*(2*v1*ZH31*complexconjugate(Lam1) + v3*ZH33*complexconjugate(Lam2Dash) + v2*ZH32*(complexconjugate(Lam3) + complexconjugate(Lam4)))))', 
	 order = {'QED':1} ) 
 
GC_20 = Coupling(name = 'GC_20',
	 value = '1./4.*complex(0,1)*(ZA23*(ZA22*(2*v1*ZH13*(Aa3 - Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH11*(cmath.sqrt(2)*Aa1 - cmath.sqrt(2)*Aa2 + 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + ZA21*(2*v2*ZH13*(-Aa3 + Aa4 - complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH12*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4))) + 2*ZA23*(-4*v3*ZH13*complexconjugate(Lam1Dash) + ZH11*(Aa3*v2 + Aa4*v2 + v2*complexconjugate(Aa3) + v2*complexconjugate(Aa4) - 2*v1*complexconjugate(Lam2Dash)) + ZH12*(Aa3*v1 + Aa4*v1 + v1*complexconjugate(Aa3) + v1*complexconjugate(Aa4) - 2*v2*complexconjugate(Lam3Dash)))) - ZA22*(ZA21*ZH13*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZA23*(2*v1*ZH13*(-Aa3 + Aa4 - complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH11*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4))) + 4*ZA22*(2*v2*ZH12*complexconjugate(Lam2) + v3*ZH13*complexconjugate(Lam3Dash) + v1*ZH11*(complexconjugate(Lam3) + complexconjugate(Lam4)))) - ZA21*(ZA22*ZH13*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZA23*(2*v2*ZH13*(Aa3 - Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH12*(cmath.sqrt(2)*Aa1 - cmath.sqrt(2)*Aa2 + 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + 4*ZA21*(2*v1*ZH11*complexconjugate(Lam1) + v3*ZH13*complexconjugate(Lam2Dash) + v2*ZH12*(complexconjugate(Lam3) + complexconjugate(Lam4)))))', 
	 order = {'QED':1} ) 
 
GC_21 = Coupling(name = 'GC_21',
	 value = '1./4.*complex(0,1)*(ZA23*(ZA22*(2*v1*ZH23*(Aa3 - Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH21*(cmath.sqrt(2)*Aa1 - cmath.sqrt(2)*Aa2 + 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + ZA21*(2*v2*ZH23*(-Aa3 + Aa4 - complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH22*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4))) + 2*ZA23*(-4*v3*ZH23*complexconjugate(Lam1Dash) + ZH21*(Aa3*v2 + Aa4*v2 + v2*complexconjugate(Aa3) + v2*complexconjugate(Aa4) - 2*v1*complexconjugate(Lam2Dash)) + ZH22*(Aa3*v1 + Aa4*v1 + v1*complexconjugate(Aa3) + v1*complexconjugate(Aa4) - 2*v2*complexconjugate(Lam3Dash)))) - ZA22*(ZA21*ZH23*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZA23*(2*v1*ZH23*(-Aa3 + Aa4 - complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH21*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4))) + 4*ZA22*(2*v2*ZH22*complexconjugate(Lam2) + v3*ZH23*complexconjugate(Lam3Dash) + v1*ZH21*(complexconjugate(Lam3) + complexconjugate(Lam4)))) - ZA21*(ZA22*ZH23*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZA23*(2*v2*ZH23*(Aa3 - Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH22*(cmath.sqrt(2)*Aa1 - cmath.sqrt(2)*Aa2 + 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + 4*ZA21*(2*v1*ZH21*complexconjugate(Lam1) + v3*ZH23*complexconjugate(Lam2Dash) + v2*ZH22*(complexconjugate(Lam3) + complexconjugate(Lam4)))))', 
	 order = {'QED':1} ) 
 
GC_22 = Coupling(name = 'GC_22',
	 value = '1./4.*complex(0,1)*(ZA23*(ZA22*(2*v1*ZH33*(Aa3 - Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH31*(cmath.sqrt(2)*Aa1 - cmath.sqrt(2)*Aa2 + 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + ZA21*(2*v2*ZH33*(-Aa3 + Aa4 - complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH32*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4))) + 2*ZA23*(-4*v3*ZH33*complexconjugate(Lam1Dash) + ZH31*(Aa3*v2 + Aa4*v2 + v2*complexconjugate(Aa3) + v2*complexconjugate(Aa4) - 2*v1*complexconjugate(Lam2Dash)) + ZH32*(Aa3*v1 + Aa4*v1 + v1*complexconjugate(Aa3) + v1*complexconjugate(Aa4) - 2*v2*complexconjugate(Lam3Dash)))) - ZA22*(ZA21*ZH33*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZA23*(2*v1*ZH33*(-Aa3 + Aa4 - complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH31*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4))) + 4*ZA22*(2*v2*ZH32*complexconjugate(Lam2) + v3*ZH33*complexconjugate(Lam3Dash) + v1*ZH31*(complexconjugate(Lam3) + complexconjugate(Lam4)))) - ZA21*(ZA22*ZH33*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZA23*(2*v2*ZH33*(Aa3 - Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH32*(cmath.sqrt(2)*Aa1 - cmath.sqrt(2)*Aa2 + 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + 4*ZA21*(2*v1*ZH31*complexconjugate(Lam1) + v3*ZH33*complexconjugate(Lam2Dash) + v2*ZH32*(complexconjugate(Lam3) + complexconjugate(Lam4)))))', 
	 order = {'QED':1} ) 
 
GC_23 = Coupling(name = 'GC_23',
	 value = '1./4.*complex(0,1)*(ZA23*(ZA32*(2*v1*ZH13*(Aa3 - Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH11*(cmath.sqrt(2)*Aa1 - cmath.sqrt(2)*Aa2 + 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + ZA31*(2*v2*ZH13*(-Aa3 + Aa4 - complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH12*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4))) + 2*ZA33*(-4*v3*ZH13*complexconjugate(Lam1Dash) + ZH11*(Aa3*v2 + Aa4*v2 + v2*complexconjugate(Aa3) + v2*complexconjugate(Aa4) - 2*v1*complexconjugate(Lam2Dash)) + ZH12*(Aa3*v1 + Aa4*v1 + v1*complexconjugate(Aa3) + v1*complexconjugate(Aa4) - 2*v2*complexconjugate(Lam3Dash)))) - ZA22*(ZA31*ZH13*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZA33*(2*v1*ZH13*(-Aa3 + Aa4 - complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH11*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4))) + 4*ZA32*(2*v2*ZH12*complexconjugate(Lam2) + v3*ZH13*complexconjugate(Lam3Dash) + v1*ZH11*(complexconjugate(Lam3) + complexconjugate(Lam4)))) - ZA21*(ZA32*ZH13*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZA33*(2*v2*ZH13*(Aa3 - Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH12*(cmath.sqrt(2)*Aa1 - cmath.sqrt(2)*Aa2 + 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + 4*ZA31*(2*v1*ZH11*complexconjugate(Lam1) + v3*ZH13*complexconjugate(Lam2Dash) + v2*ZH12*(complexconjugate(Lam3) + complexconjugate(Lam4)))))', 
	 order = {'QED':1} ) 
 
GC_24 = Coupling(name = 'GC_24',
	 value = '1./4.*complex(0,1)*(ZA23*(ZA32*(2*v1*ZH23*(Aa3 - Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH21*(cmath.sqrt(2)*Aa1 - cmath.sqrt(2)*Aa2 + 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + ZA31*(2*v2*ZH23*(-Aa3 + Aa4 - complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH22*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4))) + 2*ZA33*(-4*v3*ZH23*complexconjugate(Lam1Dash) + ZH21*(Aa3*v2 + Aa4*v2 + v2*complexconjugate(Aa3) + v2*complexconjugate(Aa4) - 2*v1*complexconjugate(Lam2Dash)) + ZH22*(Aa3*v1 + Aa4*v1 + v1*complexconjugate(Aa3) + v1*complexconjugate(Aa4) - 2*v2*complexconjugate(Lam3Dash)))) - ZA22*(ZA31*ZH23*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZA33*(2*v1*ZH23*(-Aa3 + Aa4 - complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH21*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4))) + 4*ZA32*(2*v2*ZH22*complexconjugate(Lam2) + v3*ZH23*complexconjugate(Lam3Dash) + v1*ZH21*(complexconjugate(Lam3) + complexconjugate(Lam4)))) - ZA21*(ZA32*ZH23*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZA33*(2*v2*ZH23*(Aa3 - Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH22*(cmath.sqrt(2)*Aa1 - cmath.sqrt(2)*Aa2 + 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + 4*ZA31*(2*v1*ZH21*complexconjugate(Lam1) + v3*ZH23*complexconjugate(Lam2Dash) + v2*ZH22*(complexconjugate(Lam3) + complexconjugate(Lam4)))))', 
	 order = {'QED':1} ) 
 
GC_25 = Coupling(name = 'GC_25',
	 value = '1./4.*complex(0,1)*(ZA23*(ZA32*(2*v1*ZH33*(Aa3 - Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH31*(cmath.sqrt(2)*Aa1 - cmath.sqrt(2)*Aa2 + 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + ZA31*(2*v2*ZH33*(-Aa3 + Aa4 - complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH32*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4))) + 2*ZA33*(-4*v3*ZH33*complexconjugate(Lam1Dash) + ZH31*(Aa3*v2 + Aa4*v2 + v2*complexconjugate(Aa3) + v2*complexconjugate(Aa4) - 2*v1*complexconjugate(Lam2Dash)) + ZH32*(Aa3*v1 + Aa4*v1 + v1*complexconjugate(Aa3) + v1*complexconjugate(Aa4) - 2*v2*complexconjugate(Lam3Dash)))) - ZA22*(ZA31*ZH33*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZA33*(2*v1*ZH33*(-Aa3 + Aa4 - complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH31*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4))) + 4*ZA32*(2*v2*ZH32*complexconjugate(Lam2) + v3*ZH33*complexconjugate(Lam3Dash) + v1*ZH31*(complexconjugate(Lam3) + complexconjugate(Lam4)))) - ZA21*(ZA32*ZH33*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZA33*(2*v2*ZH33*(Aa3 - Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH32*(cmath.sqrt(2)*Aa1 - cmath.sqrt(2)*Aa2 + 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + 4*ZA31*(2*v1*ZH31*complexconjugate(Lam1) + v3*ZH33*complexconjugate(Lam2Dash) + v2*ZH32*(complexconjugate(Lam3) + complexconjugate(Lam4)))))', 
	 order = {'QED':1} ) 
 
GC_26 = Coupling(name = 'GC_26',
	 value = '1./4.*complex(0,1)*(ZA33*(ZA32*(2*v1*ZH13*(Aa3 - Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH11*(cmath.sqrt(2)*Aa1 - cmath.sqrt(2)*Aa2 + 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + ZA31*(2*v2*ZH13*(-Aa3 + Aa4 - complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH12*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4))) + 2*ZA33*(-4*v3*ZH13*complexconjugate(Lam1Dash) + ZH11*(Aa3*v2 + Aa4*v2 + v2*complexconjugate(Aa3) + v2*complexconjugate(Aa4) - 2*v1*complexconjugate(Lam2Dash)) + ZH12*(Aa3*v1 + Aa4*v1 + v1*complexconjugate(Aa3) + v1*complexconjugate(Aa4) - 2*v2*complexconjugate(Lam3Dash)))) - ZA32*(ZA31*ZH13*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZA33*(2*v1*ZH13*(-Aa3 + Aa4 - complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH11*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4))) + 4*ZA32*(2*v2*ZH12*complexconjugate(Lam2) + v3*ZH13*complexconjugate(Lam3Dash) + v1*ZH11*(complexconjugate(Lam3) + complexconjugate(Lam4)))) - ZA31*(ZA32*ZH13*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZA33*(2*v2*ZH13*(Aa3 - Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH12*(cmath.sqrt(2)*Aa1 - cmath.sqrt(2)*Aa2 + 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + 4*ZA31*(2*v1*ZH11*complexconjugate(Lam1) + v3*ZH13*complexconjugate(Lam2Dash) + v2*ZH12*(complexconjugate(Lam3) + complexconjugate(Lam4)))))', 
	 order = {'QED':1} ) 
 
GC_27 = Coupling(name = 'GC_27',
	 value = '1./4.*complex(0,1)*(ZA33*(ZA32*(2*v1*ZH23*(Aa3 - Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH21*(cmath.sqrt(2)*Aa1 - cmath.sqrt(2)*Aa2 + 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + ZA31*(2*v2*ZH23*(-Aa3 + Aa4 - complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH22*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4))) + 2*ZA33*(-4*v3*ZH23*complexconjugate(Lam1Dash) + ZH21*(Aa3*v2 + Aa4*v2 + v2*complexconjugate(Aa3) + v2*complexconjugate(Aa4) - 2*v1*complexconjugate(Lam2Dash)) + ZH22*(Aa3*v1 + Aa4*v1 + v1*complexconjugate(Aa3) + v1*complexconjugate(Aa4) - 2*v2*complexconjugate(Lam3Dash)))) - ZA32*(ZA31*ZH23*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZA33*(2*v1*ZH23*(-Aa3 + Aa4 - complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH21*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4))) + 4*ZA32*(2*v2*ZH22*complexconjugate(Lam2) + v3*ZH23*complexconjugate(Lam3Dash) + v1*ZH21*(complexconjugate(Lam3) + complexconjugate(Lam4)))) - ZA31*(ZA32*ZH23*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZA33*(2*v2*ZH23*(Aa3 - Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH22*(cmath.sqrt(2)*Aa1 - cmath.sqrt(2)*Aa2 + 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + 4*ZA31*(2*v1*ZH21*complexconjugate(Lam1) + v3*ZH23*complexconjugate(Lam2Dash) + v2*ZH22*(complexconjugate(Lam3) + complexconjugate(Lam4)))))', 
	 order = {'QED':1} ) 
 
GC_28 = Coupling(name = 'GC_28',
	 value = '1./4.*complex(0,1)*(ZA33*(ZA32*(2*v1*ZH33*(Aa3 - Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH31*(cmath.sqrt(2)*Aa1 - cmath.sqrt(2)*Aa2 + 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + ZA31*(2*v2*ZH33*(-Aa3 + Aa4 - complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH32*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4))) + 2*ZA33*(-4*v3*ZH33*complexconjugate(Lam1Dash) + ZH31*(Aa3*v2 + Aa4*v2 + v2*complexconjugate(Aa3) + v2*complexconjugate(Aa4) - 2*v1*complexconjugate(Lam2Dash)) + ZH32*(Aa3*v1 + Aa4*v1 + v1*complexconjugate(Aa3) + v1*complexconjugate(Aa4) - 2*v2*complexconjugate(Lam3Dash)))) - ZA32*(ZA31*ZH33*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZA33*(2*v1*ZH33*(-Aa3 + Aa4 - complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH31*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4))) + 4*ZA32*(2*v2*ZH32*complexconjugate(Lam2) + v3*ZH33*complexconjugate(Lam3Dash) + v1*ZH31*(complexconjugate(Lam3) + complexconjugate(Lam4)))) - ZA31*(ZA32*ZH33*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZA33*(2*v2*ZH33*(Aa3 - Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH32*(cmath.sqrt(2)*Aa1 - cmath.sqrt(2)*Aa2 + 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + 4*ZA31*(2*v1*ZH31*complexconjugate(Lam1) + v3*ZH33*complexconjugate(Lam2Dash) + v2*ZH32*(complexconjugate(Lam3) + complexconjugate(Lam4)))))', 
	 order = {'QED':1} ) 
 
GC_29 = Coupling(name = 'GC_29',
	 value = '(ZA11*(ZH12*ZH13*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)) + ZH13*(2*v2*ZH13*(Aa3 + Aa4 - complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH12*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA13*(2*(v2*ZH11 + v1*ZH12)*ZH13*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH12*(2*v1*ZH13*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH11*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + ZH11*(2*v2*ZH13*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH12*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA12*(ZH11*ZH13*(-(cmath.sqrt(2)*Aa1) - cmath.sqrt(2)*Aa2 - 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZH13*(2*v1*ZH13*(-Aa3 - Aa4 + complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH11*(-(cmath.sqrt(2)*Aa1) - cmath.sqrt(2)*Aa2 - 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)))))/4.', 
	 order = {'QED':1} ) 
 
GC_30 = Coupling(name = 'GC_30',
	 value = '(ZA11*(ZH12*ZH23*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)) + ZH13*(2*v2*ZH23*(Aa3 + Aa4 - complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH22*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA13*(2*ZH13*(v2*ZH21 + v1*ZH22)*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH12*(2*v1*ZH23*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH21*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + ZH11*(2*v2*ZH23*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH22*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA12*(ZH11*ZH23*(-(cmath.sqrt(2)*Aa1) - cmath.sqrt(2)*Aa2 - 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZH13*(2*v1*ZH23*(-Aa3 - Aa4 + complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH21*(-(cmath.sqrt(2)*Aa1) - cmath.sqrt(2)*Aa2 - 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)))))/4.', 
	 order = {'QED':1} ) 
 
GC_31 = Coupling(name = 'GC_31',
	 value = '(ZA11*(ZH12*ZH33*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)) + ZH13*(2*v2*ZH33*(Aa3 + Aa4 - complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH32*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA13*(2*ZH13*(v2*ZH31 + v1*ZH32)*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH12*(2*v1*ZH33*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH31*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + ZH11*(2*v2*ZH33*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH32*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA12*(ZH11*ZH33*(-(cmath.sqrt(2)*Aa1) - cmath.sqrt(2)*Aa2 - 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZH13*(2*v1*ZH33*(-Aa3 - Aa4 + complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH31*(-(cmath.sqrt(2)*Aa1) - cmath.sqrt(2)*Aa2 - 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)))))/4.', 
	 order = {'QED':1} ) 
 
GC_32 = Coupling(name = 'GC_32',
	 value = '(ZA11*(ZH22*ZH23*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)) + ZH23*(2*v2*ZH23*(Aa3 + Aa4 - complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH22*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA13*(2*(v2*ZH21 + v1*ZH22)*ZH23*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH22*(2*v1*ZH23*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH21*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + ZH21*(2*v2*ZH23*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH22*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA12*(ZH21*ZH23*(-(cmath.sqrt(2)*Aa1) - cmath.sqrt(2)*Aa2 - 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZH23*(2*v1*ZH23*(-Aa3 - Aa4 + complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH21*(-(cmath.sqrt(2)*Aa1) - cmath.sqrt(2)*Aa2 - 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)))))/4.', 
	 order = {'QED':1} ) 
 
GC_33 = Coupling(name = 'GC_33',
	 value = '(ZA11*(ZH22*ZH33*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)) + ZH23*(2*v2*ZH33*(Aa3 + Aa4 - complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH32*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA13*(2*ZH23*(v2*ZH31 + v1*ZH32)*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH22*(2*v1*ZH33*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH31*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + ZH21*(2*v2*ZH33*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH32*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA12*(ZH21*ZH33*(-(cmath.sqrt(2)*Aa1) - cmath.sqrt(2)*Aa2 - 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZH23*(2*v1*ZH33*(-Aa3 - Aa4 + complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH31*(-(cmath.sqrt(2)*Aa1) - cmath.sqrt(2)*Aa2 - 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)))))/4.', 
	 order = {'QED':1} ) 
 
GC_34 = Coupling(name = 'GC_34',
	 value = '(ZA11*(ZH32*ZH33*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)) + ZH33*(2*v2*ZH33*(Aa3 + Aa4 - complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH32*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA13*(2*(v2*ZH31 + v1*ZH32)*ZH33*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH32*(2*v1*ZH33*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH31*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + ZH31*(2*v2*ZH33*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH32*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA12*(ZH31*ZH33*(-(cmath.sqrt(2)*Aa1) - cmath.sqrt(2)*Aa2 - 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZH33*(2*v1*ZH33*(-Aa3 - Aa4 + complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH31*(-(cmath.sqrt(2)*Aa1) - cmath.sqrt(2)*Aa2 - 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)))))/4.', 
	 order = {'QED':1} ) 
 
GC_35 = Coupling(name = 'GC_35',
	 value = '(ZA21*(ZH12*ZH13*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)) + ZH13*(2*v2*ZH13*(Aa3 + Aa4 - complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH12*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA23*(2*(v2*ZH11 + v1*ZH12)*ZH13*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH12*(2*v1*ZH13*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH11*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + ZH11*(2*v2*ZH13*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH12*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA22*(ZH11*ZH13*(-(cmath.sqrt(2)*Aa1) - cmath.sqrt(2)*Aa2 - 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZH13*(2*v1*ZH13*(-Aa3 - Aa4 + complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH11*(-(cmath.sqrt(2)*Aa1) - cmath.sqrt(2)*Aa2 - 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)))))/4.', 
	 order = {'QED':1} ) 
 
GC_36 = Coupling(name = 'GC_36',
	 value = '(ZA21*(ZH12*ZH23*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)) + ZH13*(2*v2*ZH23*(Aa3 + Aa4 - complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH22*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA23*(2*ZH13*(v2*ZH21 + v1*ZH22)*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH12*(2*v1*ZH23*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH21*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + ZH11*(2*v2*ZH23*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH22*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA22*(ZH11*ZH23*(-(cmath.sqrt(2)*Aa1) - cmath.sqrt(2)*Aa2 - 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZH13*(2*v1*ZH23*(-Aa3 - Aa4 + complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH21*(-(cmath.sqrt(2)*Aa1) - cmath.sqrt(2)*Aa2 - 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)))))/4.', 
	 order = {'QED':1} ) 
 
GC_37 = Coupling(name = 'GC_37',
	 value = '(ZA21*(ZH12*ZH33*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)) + ZH13*(2*v2*ZH33*(Aa3 + Aa4 - complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH32*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA23*(2*ZH13*(v2*ZH31 + v1*ZH32)*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH12*(2*v1*ZH33*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH31*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + ZH11*(2*v2*ZH33*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH32*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA22*(ZH11*ZH33*(-(cmath.sqrt(2)*Aa1) - cmath.sqrt(2)*Aa2 - 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZH13*(2*v1*ZH33*(-Aa3 - Aa4 + complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH31*(-(cmath.sqrt(2)*Aa1) - cmath.sqrt(2)*Aa2 - 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)))))/4.', 
	 order = {'QED':1} ) 
 
GC_38 = Coupling(name = 'GC_38',
	 value = '(ZA21*(ZH22*ZH23*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)) + ZH23*(2*v2*ZH23*(Aa3 + Aa4 - complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH22*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA23*(2*(v2*ZH21 + v1*ZH22)*ZH23*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH22*(2*v1*ZH23*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH21*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + ZH21*(2*v2*ZH23*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH22*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA22*(ZH21*ZH23*(-(cmath.sqrt(2)*Aa1) - cmath.sqrt(2)*Aa2 - 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZH23*(2*v1*ZH23*(-Aa3 - Aa4 + complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH21*(-(cmath.sqrt(2)*Aa1) - cmath.sqrt(2)*Aa2 - 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)))))/4.', 
	 order = {'QED':1} ) 
 
GC_39 = Coupling(name = 'GC_39',
	 value = '(ZA21*(ZH22*ZH33*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)) + ZH23*(2*v2*ZH33*(Aa3 + Aa4 - complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH32*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA23*(2*ZH23*(v2*ZH31 + v1*ZH32)*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH22*(2*v1*ZH33*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH31*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + ZH21*(2*v2*ZH33*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH32*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA22*(ZH21*ZH33*(-(cmath.sqrt(2)*Aa1) - cmath.sqrt(2)*Aa2 - 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZH23*(2*v1*ZH33*(-Aa3 - Aa4 + complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH31*(-(cmath.sqrt(2)*Aa1) - cmath.sqrt(2)*Aa2 - 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)))))/4.', 
	 order = {'QED':1} ) 
 
GC_40 = Coupling(name = 'GC_40',
	 value = '(ZA21*(ZH32*ZH33*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)) + ZH33*(2*v2*ZH33*(Aa3 + Aa4 - complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH32*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA23*(2*(v2*ZH31 + v1*ZH32)*ZH33*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH32*(2*v1*ZH33*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH31*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + ZH31*(2*v2*ZH33*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH32*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA22*(ZH31*ZH33*(-(cmath.sqrt(2)*Aa1) - cmath.sqrt(2)*Aa2 - 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZH33*(2*v1*ZH33*(-Aa3 - Aa4 + complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH31*(-(cmath.sqrt(2)*Aa1) - cmath.sqrt(2)*Aa2 - 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)))))/4.', 
	 order = {'QED':1} ) 
 
GC_41 = Coupling(name = 'GC_41',
	 value = '(ZA31*(ZH12*ZH13*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)) + ZH13*(2*v2*ZH13*(Aa3 + Aa4 - complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH12*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA33*(2*(v2*ZH11 + v1*ZH12)*ZH13*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH12*(2*v1*ZH13*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH11*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + ZH11*(2*v2*ZH13*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH12*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA32*(ZH11*ZH13*(-(cmath.sqrt(2)*Aa1) - cmath.sqrt(2)*Aa2 - 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZH13*(2*v1*ZH13*(-Aa3 - Aa4 + complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH11*(-(cmath.sqrt(2)*Aa1) - cmath.sqrt(2)*Aa2 - 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)))))/4.', 
	 order = {'QED':1} ) 
 
GC_42 = Coupling(name = 'GC_42',
	 value = '(ZA31*(ZH12*ZH23*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)) + ZH13*(2*v2*ZH23*(Aa3 + Aa4 - complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH22*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA33*(2*ZH13*(v2*ZH21 + v1*ZH22)*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH12*(2*v1*ZH23*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH21*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + ZH11*(2*v2*ZH23*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH22*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA32*(ZH11*ZH23*(-(cmath.sqrt(2)*Aa1) - cmath.sqrt(2)*Aa2 - 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZH13*(2*v1*ZH23*(-Aa3 - Aa4 + complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH21*(-(cmath.sqrt(2)*Aa1) - cmath.sqrt(2)*Aa2 - 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)))))/4.', 
	 order = {'QED':1} ) 
 
GC_43 = Coupling(name = 'GC_43',
	 value = '(ZA31*(ZH12*ZH33*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)) + ZH13*(2*v2*ZH33*(Aa3 + Aa4 - complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH32*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA33*(2*ZH13*(v2*ZH31 + v1*ZH32)*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH12*(2*v1*ZH33*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH31*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + ZH11*(2*v2*ZH33*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH32*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA32*(ZH11*ZH33*(-(cmath.sqrt(2)*Aa1) - cmath.sqrt(2)*Aa2 - 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZH13*(2*v1*ZH33*(-Aa3 - Aa4 + complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH31*(-(cmath.sqrt(2)*Aa1) - cmath.sqrt(2)*Aa2 - 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)))))/4.', 
	 order = {'QED':1} ) 
 
GC_44 = Coupling(name = 'GC_44',
	 value = '(ZA31*(ZH22*ZH23*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)) + ZH23*(2*v2*ZH23*(Aa3 + Aa4 - complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH22*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA33*(2*(v2*ZH21 + v1*ZH22)*ZH23*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH22*(2*v1*ZH23*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH21*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + ZH21*(2*v2*ZH23*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH22*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA32*(ZH21*ZH23*(-(cmath.sqrt(2)*Aa1) - cmath.sqrt(2)*Aa2 - 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZH23*(2*v1*ZH23*(-Aa3 - Aa4 + complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH21*(-(cmath.sqrt(2)*Aa1) - cmath.sqrt(2)*Aa2 - 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)))))/4.', 
	 order = {'QED':1} ) 
 
GC_45 = Coupling(name = 'GC_45',
	 value = '(ZA31*(ZH22*ZH33*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)) + ZH23*(2*v2*ZH33*(Aa3 + Aa4 - complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH32*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA33*(2*ZH23*(v2*ZH31 + v1*ZH32)*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH22*(2*v1*ZH33*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH31*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + ZH21*(2*v2*ZH33*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH32*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA32*(ZH21*ZH33*(-(cmath.sqrt(2)*Aa1) - cmath.sqrt(2)*Aa2 - 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZH23*(2*v1*ZH33*(-Aa3 - Aa4 + complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH31*(-(cmath.sqrt(2)*Aa1) - cmath.sqrt(2)*Aa2 - 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)))))/4.', 
	 order = {'QED':1} ) 
 
GC_46 = Coupling(name = 'GC_46',
	 value = '(ZA31*(ZH32*ZH33*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)) + ZH33*(2*v2*ZH33*(Aa3 + Aa4 - complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH32*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 - cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA33*(2*(v2*ZH31 + v1*ZH32)*ZH33*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH32*(2*v1*ZH33*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH31*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4))) + ZH31*(2*v2*ZH33*(-Aa3 + Aa4 + complexconjugate(Aa3) - complexconjugate(Aa4)) + ZH32*(-(cmath.sqrt(2)*Aa1) + cmath.sqrt(2)*Aa2 - 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) - cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) - 2*v3*complexconjugate(Aa4)))) + ZA32*(ZH31*ZH33*(-(cmath.sqrt(2)*Aa1) - cmath.sqrt(2)*Aa2 - 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + ZH33*(2*v1*ZH33*(-Aa3 - Aa4 + complexconjugate(Aa3) + complexconjugate(Aa4)) + ZH31*(-(cmath.sqrt(2)*Aa1) - cmath.sqrt(2)*Aa2 - 2*Aa3*v3 - 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)))))/4.', 
	 order = {'QED':1} ) 
 
GC_47 = Coupling(name = 'GC_47',
	 value = '(-(ZP12*((cmath.sqrt(2)*Aa1 - cmath.sqrt(2)*Aa2 + 2*Aa3*v3 - 2*Aa4*v3)*ZA13 + v2*ZA11*complexconjugate(Lam4) - v1*ZA12*complexconjugate(Lam4))*complexconjugate(ZP11)) - ZP11*(ZA13*(-(cmath.sqrt(2)*complexconjugate(Aa1)) + cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) - v2*ZA11*complexconjugate(Lam4) + v1*ZA12*complexconjugate(Lam4))*complexconjugate(ZP12))/2.', 
	 order = {'QED':1} ) 
 
GC_48 = Coupling(name = 'GC_48',
	 value = '(-(ZP12*((cmath.sqrt(2)*Aa1 - cmath.sqrt(2)*Aa2 + 2*Aa3*v3 - 2*Aa4*v3)*ZA13 + v2*ZA11*complexconjugate(Lam4) - v1*ZA12*complexconjugate(Lam4))*complexconjugate(ZP21)) - ZP11*(ZA13*(-(cmath.sqrt(2)*complexconjugate(Aa1)) + cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) - v2*ZA11*complexconjugate(Lam4) + v1*ZA12*complexconjugate(Lam4))*complexconjugate(ZP22))/2.', 
	 order = {'QED':1} ) 
 
GC_49 = Coupling(name = 'GC_49',
	 value = '(-(ZP22*((cmath.sqrt(2)*Aa1 - cmath.sqrt(2)*Aa2 + 2*Aa3*v3 - 2*Aa4*v3)*ZA13 + v2*ZA11*complexconjugate(Lam4) - v1*ZA12*complexconjugate(Lam4))*complexconjugate(ZP11)) - ZP21*(ZA13*(-(cmath.sqrt(2)*complexconjugate(Aa1)) + cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) - v2*ZA11*complexconjugate(Lam4) + v1*ZA12*complexconjugate(Lam4))*complexconjugate(ZP12))/2.', 
	 order = {'QED':1} ) 
 
GC_50 = Coupling(name = 'GC_50',
	 value = '(-(ZP22*((cmath.sqrt(2)*Aa1 - cmath.sqrt(2)*Aa2 + 2*Aa3*v3 - 2*Aa4*v3)*ZA13 + v2*ZA11*complexconjugate(Lam4) - v1*ZA12*complexconjugate(Lam4))*complexconjugate(ZP21)) - ZP21*(ZA13*(-(cmath.sqrt(2)*complexconjugate(Aa1)) + cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) - v2*ZA11*complexconjugate(Lam4) + v1*ZA12*complexconjugate(Lam4))*complexconjugate(ZP22))/2.', 
	 order = {'QED':1} ) 
 
GC_51 = Coupling(name = 'GC_51',
	 value = '(-(ZP12*((cmath.sqrt(2)*Aa1 - cmath.sqrt(2)*Aa2 + 2*Aa3*v3 - 2*Aa4*v3)*ZA23 + v2*ZA21*complexconjugate(Lam4) - v1*ZA22*complexconjugate(Lam4))*complexconjugate(ZP11)) - ZP11*(ZA23*(-(cmath.sqrt(2)*complexconjugate(Aa1)) + cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) - v2*ZA21*complexconjugate(Lam4) + v1*ZA22*complexconjugate(Lam4))*complexconjugate(ZP12))/2.', 
	 order = {'QED':1} ) 
 
GC_52 = Coupling(name = 'GC_52',
	 value = '(-(ZP12*((cmath.sqrt(2)*Aa1 - cmath.sqrt(2)*Aa2 + 2*Aa3*v3 - 2*Aa4*v3)*ZA23 + v2*ZA21*complexconjugate(Lam4) - v1*ZA22*complexconjugate(Lam4))*complexconjugate(ZP21)) - ZP11*(ZA23*(-(cmath.sqrt(2)*complexconjugate(Aa1)) + cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) - v2*ZA21*complexconjugate(Lam4) + v1*ZA22*complexconjugate(Lam4))*complexconjugate(ZP22))/2.', 
	 order = {'QED':1} ) 
 
GC_53 = Coupling(name = 'GC_53',
	 value = '(-(ZP22*((cmath.sqrt(2)*Aa1 - cmath.sqrt(2)*Aa2 + 2*Aa3*v3 - 2*Aa4*v3)*ZA23 + v2*ZA21*complexconjugate(Lam4) - v1*ZA22*complexconjugate(Lam4))*complexconjugate(ZP11)) - ZP21*(ZA23*(-(cmath.sqrt(2)*complexconjugate(Aa1)) + cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) - v2*ZA21*complexconjugate(Lam4) + v1*ZA22*complexconjugate(Lam4))*complexconjugate(ZP12))/2.', 
	 order = {'QED':1} ) 
 
GC_54 = Coupling(name = 'GC_54',
	 value = '(-(ZP22*((cmath.sqrt(2)*Aa1 - cmath.sqrt(2)*Aa2 + 2*Aa3*v3 - 2*Aa4*v3)*ZA23 + v2*ZA21*complexconjugate(Lam4) - v1*ZA22*complexconjugate(Lam4))*complexconjugate(ZP21)) - ZP21*(ZA23*(-(cmath.sqrt(2)*complexconjugate(Aa1)) + cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) - v2*ZA21*complexconjugate(Lam4) + v1*ZA22*complexconjugate(Lam4))*complexconjugate(ZP22))/2.', 
	 order = {'QED':1} ) 
 
GC_55 = Coupling(name = 'GC_55',
	 value = '(-(ZP12*((cmath.sqrt(2)*Aa1 - cmath.sqrt(2)*Aa2 + 2*Aa3*v3 - 2*Aa4*v3)*ZA33 + v2*ZA31*complexconjugate(Lam4) - v1*ZA32*complexconjugate(Lam4))*complexconjugate(ZP11)) - ZP11*(ZA33*(-(cmath.sqrt(2)*complexconjugate(Aa1)) + cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) - v2*ZA31*complexconjugate(Lam4) + v1*ZA32*complexconjugate(Lam4))*complexconjugate(ZP12))/2.', 
	 order = {'QED':1} ) 
 
GC_56 = Coupling(name = 'GC_56',
	 value = '(-(ZP12*((cmath.sqrt(2)*Aa1 - cmath.sqrt(2)*Aa2 + 2*Aa3*v3 - 2*Aa4*v3)*ZA33 + v2*ZA31*complexconjugate(Lam4) - v1*ZA32*complexconjugate(Lam4))*complexconjugate(ZP21)) - ZP11*(ZA33*(-(cmath.sqrt(2)*complexconjugate(Aa1)) + cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) - v2*ZA31*complexconjugate(Lam4) + v1*ZA32*complexconjugate(Lam4))*complexconjugate(ZP22))/2.', 
	 order = {'QED':1} ) 
 
GC_57 = Coupling(name = 'GC_57',
	 value = '(-(ZP22*((cmath.sqrt(2)*Aa1 - cmath.sqrt(2)*Aa2 + 2*Aa3*v3 - 2*Aa4*v3)*ZA33 + v2*ZA31*complexconjugate(Lam4) - v1*ZA32*complexconjugate(Lam4))*complexconjugate(ZP11)) - ZP21*(ZA33*(-(cmath.sqrt(2)*complexconjugate(Aa1)) + cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) - v2*ZA31*complexconjugate(Lam4) + v1*ZA32*complexconjugate(Lam4))*complexconjugate(ZP12))/2.', 
	 order = {'QED':1} ) 
 
GC_58 = Coupling(name = 'GC_58',
	 value = '(-(ZP22*((cmath.sqrt(2)*Aa1 - cmath.sqrt(2)*Aa2 + 2*Aa3*v3 - 2*Aa4*v3)*ZA33 + v2*ZA31*complexconjugate(Lam4) - v1*ZA32*complexconjugate(Lam4))*complexconjugate(ZP21)) - ZP21*(ZA33*(-(cmath.sqrt(2)*complexconjugate(Aa1)) + cmath.sqrt(2)*complexconjugate(Aa2) - 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) - v2*ZA31*complexconjugate(Lam4) + v1*ZA32*complexconjugate(Lam4))*complexconjugate(ZP22))/2.', 
	 order = {'QED':1} ) 
 
GC_59 = Coupling(name = 'GC_59',
	 value = '1./4.*complex(0,1)*(-(ZH13*(ZH11*(ZH12*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v3*ZH11*complexconjugate(Lam2Dash) + 2*ZH13*(Aa3*v2 + Aa4*v2 + v2*complexconjugate(Aa3) + v2*complexconjugate(Aa4) + 2*v1*complexconjugate(Lam2Dash))) + 2*ZH13*(12*v3*ZH13*complexconjugate(Lam1Dash) + ZH11*(Aa3*v2 + Aa4*v2 + v2*complexconjugate(Aa3) + v2*complexconjugate(Aa4) + 2*v1*complexconjugate(Lam2Dash)) + ZH12*(Aa3*v1 + Aa4*v1 + v1*complexconjugate(Aa3) + v1*complexconjugate(Aa4) + 2*v2*complexconjugate(Lam3Dash))) + ZH12*(ZH11*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v3*ZH12*complexconjugate(Lam3Dash) + 2*ZH13*(Aa3*v1 + Aa4*v1 + v1*complexconjugate(Aa3) + v1*complexconjugate(Aa4) + 2*v2*complexconjugate(Lam3Dash))))) - ZH12*(ZH13*(ZH11*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v3*ZH12*complexconjugate(Lam3Dash) + 2*ZH13*(Aa3*v1 + Aa4*v1 + v1*complexconjugate(Aa3) + v1*complexconjugate(Aa4) + 2*v2*complexconjugate(Lam3Dash))) + 4*ZH12*(6*v2*ZH12*complexconjugate(Lam2) + v3*ZH13*complexconjugate(Lam3Dash) + v1*ZH11*(complexconjugate(Lam3) + complexconjugate(Lam4))) + ZH11*(ZH13*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v2*ZH11*(complexconjugate(Lam3) + complexconjugate(Lam4)) + 4*v1*ZH12*(complexconjugate(Lam3) + complexconjugate(Lam4)))) - ZH11*(ZH13*(ZH12*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v3*ZH11*complexconjugate(Lam2Dash) + 2*ZH13*(Aa3*v2 + Aa4*v2 + v2*complexconjugate(Aa3) + v2*complexconjugate(Aa4) + 2*v1*complexconjugate(Lam2Dash))) + ZH12*(ZH13*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v2*ZH11*(complexconjugate(Lam3) + complexconjugate(Lam4)) + 4*v1*ZH12*(complexconjugate(Lam3) + complexconjugate(Lam4))) + 4*ZH11*(6*v1*ZH11*complexconjugate(Lam1) + v3*ZH13*complexconjugate(Lam2Dash) + v2*ZH12*(complexconjugate(Lam3) + complexconjugate(Lam4)))))', 
	 order = {'QED':1} ) 
 
GC_60 = Coupling(name = 'GC_60',
	 value = '1./4.*complex(0,1)*(-(ZH13*(ZH11*(ZH22*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v3*ZH21*complexconjugate(Lam2Dash) + 2*ZH23*(Aa3*v2 + Aa4*v2 + v2*complexconjugate(Aa3) + v2*complexconjugate(Aa4) + 2*v1*complexconjugate(Lam2Dash))) + 2*ZH13*(12*v3*ZH23*complexconjugate(Lam1Dash) + ZH21*(Aa3*v2 + Aa4*v2 + v2*complexconjugate(Aa3) + v2*complexconjugate(Aa4) + 2*v1*complexconjugate(Lam2Dash)) + ZH22*(Aa3*v1 + Aa4*v1 + v1*complexconjugate(Aa3) + v1*complexconjugate(Aa4) + 2*v2*complexconjugate(Lam3Dash))) + ZH12*(ZH21*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v3*ZH22*complexconjugate(Lam3Dash) + 2*ZH23*(Aa3*v1 + Aa4*v1 + v1*complexconjugate(Aa3) + v1*complexconjugate(Aa4) + 2*v2*complexconjugate(Lam3Dash))))) - ZH12*(ZH13*(ZH21*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v3*ZH22*complexconjugate(Lam3Dash) + 2*ZH23*(Aa3*v1 + Aa4*v1 + v1*complexconjugate(Aa3) + v1*complexconjugate(Aa4) + 2*v2*complexconjugate(Lam3Dash))) + 4*ZH12*(6*v2*ZH22*complexconjugate(Lam2) + v3*ZH23*complexconjugate(Lam3Dash) + v1*ZH21*(complexconjugate(Lam3) + complexconjugate(Lam4))) + ZH11*(ZH23*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v2*ZH21*(complexconjugate(Lam3) + complexconjugate(Lam4)) + 4*v1*ZH22*(complexconjugate(Lam3) + complexconjugate(Lam4)))) - ZH11*(ZH13*(ZH22*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v3*ZH21*complexconjugate(Lam2Dash) + 2*ZH23*(Aa3*v2 + Aa4*v2 + v2*complexconjugate(Aa3) + v2*complexconjugate(Aa4) + 2*v1*complexconjugate(Lam2Dash))) + ZH12*(ZH23*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v2*ZH21*(complexconjugate(Lam3) + complexconjugate(Lam4)) + 4*v1*ZH22*(complexconjugate(Lam3) + complexconjugate(Lam4))) + 4*ZH11*(6*v1*ZH21*complexconjugate(Lam1) + v3*ZH23*complexconjugate(Lam2Dash) + v2*ZH22*(complexconjugate(Lam3) + complexconjugate(Lam4)))))', 
	 order = {'QED':1} ) 
 
GC_61 = Coupling(name = 'GC_61',
	 value = '1./4.*complex(0,1)*(-(ZH13*(ZH11*(ZH32*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v3*ZH31*complexconjugate(Lam2Dash) + 2*ZH33*(Aa3*v2 + Aa4*v2 + v2*complexconjugate(Aa3) + v2*complexconjugate(Aa4) + 2*v1*complexconjugate(Lam2Dash))) + 2*ZH13*(12*v3*ZH33*complexconjugate(Lam1Dash) + ZH31*(Aa3*v2 + Aa4*v2 + v2*complexconjugate(Aa3) + v2*complexconjugate(Aa4) + 2*v1*complexconjugate(Lam2Dash)) + ZH32*(Aa3*v1 + Aa4*v1 + v1*complexconjugate(Aa3) + v1*complexconjugate(Aa4) + 2*v2*complexconjugate(Lam3Dash))) + ZH12*(ZH31*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v3*ZH32*complexconjugate(Lam3Dash) + 2*ZH33*(Aa3*v1 + Aa4*v1 + v1*complexconjugate(Aa3) + v1*complexconjugate(Aa4) + 2*v2*complexconjugate(Lam3Dash))))) - ZH12*(ZH13*(ZH31*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v3*ZH32*complexconjugate(Lam3Dash) + 2*ZH33*(Aa3*v1 + Aa4*v1 + v1*complexconjugate(Aa3) + v1*complexconjugate(Aa4) + 2*v2*complexconjugate(Lam3Dash))) + 4*ZH12*(6*v2*ZH32*complexconjugate(Lam2) + v3*ZH33*complexconjugate(Lam3Dash) + v1*ZH31*(complexconjugate(Lam3) + complexconjugate(Lam4))) + ZH11*(ZH33*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v2*ZH31*(complexconjugate(Lam3) + complexconjugate(Lam4)) + 4*v1*ZH32*(complexconjugate(Lam3) + complexconjugate(Lam4)))) - ZH11*(ZH13*(ZH32*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v3*ZH31*complexconjugate(Lam2Dash) + 2*ZH33*(Aa3*v2 + Aa4*v2 + v2*complexconjugate(Aa3) + v2*complexconjugate(Aa4) + 2*v1*complexconjugate(Lam2Dash))) + ZH12*(ZH33*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v2*ZH31*(complexconjugate(Lam3) + complexconjugate(Lam4)) + 4*v1*ZH32*(complexconjugate(Lam3) + complexconjugate(Lam4))) + 4*ZH11*(6*v1*ZH31*complexconjugate(Lam1) + v3*ZH33*complexconjugate(Lam2Dash) + v2*ZH32*(complexconjugate(Lam3) + complexconjugate(Lam4)))))', 
	 order = {'QED':1} ) 
 
GC_62 = Coupling(name = 'GC_62',
	 value = '1./4.*complex(0,1)*(-(ZH13*(ZH21*(ZH22*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v3*ZH21*complexconjugate(Lam2Dash) + 2*ZH23*(Aa3*v2 + Aa4*v2 + v2*complexconjugate(Aa3) + v2*complexconjugate(Aa4) + 2*v1*complexconjugate(Lam2Dash))) + 2*ZH23*(12*v3*ZH23*complexconjugate(Lam1Dash) + ZH21*(Aa3*v2 + Aa4*v2 + v2*complexconjugate(Aa3) + v2*complexconjugate(Aa4) + 2*v1*complexconjugate(Lam2Dash)) + ZH22*(Aa3*v1 + Aa4*v1 + v1*complexconjugate(Aa3) + v1*complexconjugate(Aa4) + 2*v2*complexconjugate(Lam3Dash))) + ZH22*(ZH21*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v3*ZH22*complexconjugate(Lam3Dash) + 2*ZH23*(Aa3*v1 + Aa4*v1 + v1*complexconjugate(Aa3) + v1*complexconjugate(Aa4) + 2*v2*complexconjugate(Lam3Dash))))) - ZH12*(ZH23*(ZH21*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v3*ZH22*complexconjugate(Lam3Dash) + 2*ZH23*(Aa3*v1 + Aa4*v1 + v1*complexconjugate(Aa3) + v1*complexconjugate(Aa4) + 2*v2*complexconjugate(Lam3Dash))) + 4*ZH22*(6*v2*ZH22*complexconjugate(Lam2) + v3*ZH23*complexconjugate(Lam3Dash) + v1*ZH21*(complexconjugate(Lam3) + complexconjugate(Lam4))) + ZH21*(ZH23*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v2*ZH21*(complexconjugate(Lam3) + complexconjugate(Lam4)) + 4*v1*ZH22*(complexconjugate(Lam3) + complexconjugate(Lam4)))) - ZH11*(ZH23*(ZH22*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v3*ZH21*complexconjugate(Lam2Dash) + 2*ZH23*(Aa3*v2 + Aa4*v2 + v2*complexconjugate(Aa3) + v2*complexconjugate(Aa4) + 2*v1*complexconjugate(Lam2Dash))) + ZH22*(ZH23*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v2*ZH21*(complexconjugate(Lam3) + complexconjugate(Lam4)) + 4*v1*ZH22*(complexconjugate(Lam3) + complexconjugate(Lam4))) + 4*ZH21*(6*v1*ZH21*complexconjugate(Lam1) + v3*ZH23*complexconjugate(Lam2Dash) + v2*ZH22*(complexconjugate(Lam3) + complexconjugate(Lam4)))))', 
	 order = {'QED':1} ) 
 
GC_63 = Coupling(name = 'GC_63',
	 value = '1./4.*complex(0,1)*(-(ZH13*(ZH21*(ZH32*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v3*ZH31*complexconjugate(Lam2Dash) + 2*ZH33*(Aa3*v2 + Aa4*v2 + v2*complexconjugate(Aa3) + v2*complexconjugate(Aa4) + 2*v1*complexconjugate(Lam2Dash))) + 2*ZH23*(12*v3*ZH33*complexconjugate(Lam1Dash) + ZH31*(Aa3*v2 + Aa4*v2 + v2*complexconjugate(Aa3) + v2*complexconjugate(Aa4) + 2*v1*complexconjugate(Lam2Dash)) + ZH32*(Aa3*v1 + Aa4*v1 + v1*complexconjugate(Aa3) + v1*complexconjugate(Aa4) + 2*v2*complexconjugate(Lam3Dash))) + ZH22*(ZH31*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v3*ZH32*complexconjugate(Lam3Dash) + 2*ZH33*(Aa3*v1 + Aa4*v1 + v1*complexconjugate(Aa3) + v1*complexconjugate(Aa4) + 2*v2*complexconjugate(Lam3Dash))))) - ZH12*(ZH23*(ZH31*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v3*ZH32*complexconjugate(Lam3Dash) + 2*ZH33*(Aa3*v1 + Aa4*v1 + v1*complexconjugate(Aa3) + v1*complexconjugate(Aa4) + 2*v2*complexconjugate(Lam3Dash))) + 4*ZH22*(6*v2*ZH32*complexconjugate(Lam2) + v3*ZH33*complexconjugate(Lam3Dash) + v1*ZH31*(complexconjugate(Lam3) + complexconjugate(Lam4))) + ZH21*(ZH33*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v2*ZH31*(complexconjugate(Lam3) + complexconjugate(Lam4)) + 4*v1*ZH32*(complexconjugate(Lam3) + complexconjugate(Lam4)))) - ZH11*(ZH23*(ZH32*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v3*ZH31*complexconjugate(Lam2Dash) + 2*ZH33*(Aa3*v2 + Aa4*v2 + v2*complexconjugate(Aa3) + v2*complexconjugate(Aa4) + 2*v1*complexconjugate(Lam2Dash))) + ZH22*(ZH33*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v2*ZH31*(complexconjugate(Lam3) + complexconjugate(Lam4)) + 4*v1*ZH32*(complexconjugate(Lam3) + complexconjugate(Lam4))) + 4*ZH21*(6*v1*ZH31*complexconjugate(Lam1) + v3*ZH33*complexconjugate(Lam2Dash) + v2*ZH32*(complexconjugate(Lam3) + complexconjugate(Lam4)))))', 
	 order = {'QED':1} ) 
 
GC_64 = Coupling(name = 'GC_64',
	 value = '1./4.*complex(0,1)*(-(ZH13*(ZH31*(ZH32*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v3*ZH31*complexconjugate(Lam2Dash) + 2*ZH33*(Aa3*v2 + Aa4*v2 + v2*complexconjugate(Aa3) + v2*complexconjugate(Aa4) + 2*v1*complexconjugate(Lam2Dash))) + 2*ZH33*(12*v3*ZH33*complexconjugate(Lam1Dash) + ZH31*(Aa3*v2 + Aa4*v2 + v2*complexconjugate(Aa3) + v2*complexconjugate(Aa4) + 2*v1*complexconjugate(Lam2Dash)) + ZH32*(Aa3*v1 + Aa4*v1 + v1*complexconjugate(Aa3) + v1*complexconjugate(Aa4) + 2*v2*complexconjugate(Lam3Dash))) + ZH32*(ZH31*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v3*ZH32*complexconjugate(Lam3Dash) + 2*ZH33*(Aa3*v1 + Aa4*v1 + v1*complexconjugate(Aa3) + v1*complexconjugate(Aa4) + 2*v2*complexconjugate(Lam3Dash))))) - ZH12*(ZH33*(ZH31*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v3*ZH32*complexconjugate(Lam3Dash) + 2*ZH33*(Aa3*v1 + Aa4*v1 + v1*complexconjugate(Aa3) + v1*complexconjugate(Aa4) + 2*v2*complexconjugate(Lam3Dash))) + 4*ZH32*(6*v2*ZH32*complexconjugate(Lam2) + v3*ZH33*complexconjugate(Lam3Dash) + v1*ZH31*(complexconjugate(Lam3) + complexconjugate(Lam4))) + ZH31*(ZH33*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v2*ZH31*(complexconjugate(Lam3) + complexconjugate(Lam4)) + 4*v1*ZH32*(complexconjugate(Lam3) + complexconjugate(Lam4)))) - ZH11*(ZH33*(ZH32*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v3*ZH31*complexconjugate(Lam2Dash) + 2*ZH33*(Aa3*v2 + Aa4*v2 + v2*complexconjugate(Aa3) + v2*complexconjugate(Aa4) + 2*v1*complexconjugate(Lam2Dash))) + ZH32*(ZH33*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v2*ZH31*(complexconjugate(Lam3) + complexconjugate(Lam4)) + 4*v1*ZH32*(complexconjugate(Lam3) + complexconjugate(Lam4))) + 4*ZH31*(6*v1*ZH31*complexconjugate(Lam1) + v3*ZH33*complexconjugate(Lam2Dash) + v2*ZH32*(complexconjugate(Lam3) + complexconjugate(Lam4)))))', 
	 order = {'QED':1} ) 
 
GC_65 = Coupling(name = 'GC_65',
	 value = '1./4.*complex(0,1)*(-(ZH23*(ZH21*(ZH22*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v3*ZH21*complexconjugate(Lam2Dash) + 2*ZH23*(Aa3*v2 + Aa4*v2 + v2*complexconjugate(Aa3) + v2*complexconjugate(Aa4) + 2*v1*complexconjugate(Lam2Dash))) + 2*ZH23*(12*v3*ZH23*complexconjugate(Lam1Dash) + ZH21*(Aa3*v2 + Aa4*v2 + v2*complexconjugate(Aa3) + v2*complexconjugate(Aa4) + 2*v1*complexconjugate(Lam2Dash)) + ZH22*(Aa3*v1 + Aa4*v1 + v1*complexconjugate(Aa3) + v1*complexconjugate(Aa4) + 2*v2*complexconjugate(Lam3Dash))) + ZH22*(ZH21*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v3*ZH22*complexconjugate(Lam3Dash) + 2*ZH23*(Aa3*v1 + Aa4*v1 + v1*complexconjugate(Aa3) + v1*complexconjugate(Aa4) + 2*v2*complexconjugate(Lam3Dash))))) - ZH22*(ZH23*(ZH21*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v3*ZH22*complexconjugate(Lam3Dash) + 2*ZH23*(Aa3*v1 + Aa4*v1 + v1*complexconjugate(Aa3) + v1*complexconjugate(Aa4) + 2*v2*complexconjugate(Lam3Dash))) + 4*ZH22*(6*v2*ZH22*complexconjugate(Lam2) + v3*ZH23*complexconjugate(Lam3Dash) + v1*ZH21*(complexconjugate(Lam3) + complexconjugate(Lam4))) + ZH21*(ZH23*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v2*ZH21*(complexconjugate(Lam3) + complexconjugate(Lam4)) + 4*v1*ZH22*(complexconjugate(Lam3) + complexconjugate(Lam4)))) - ZH21*(ZH23*(ZH22*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v3*ZH21*complexconjugate(Lam2Dash) + 2*ZH23*(Aa3*v2 + Aa4*v2 + v2*complexconjugate(Aa3) + v2*complexconjugate(Aa4) + 2*v1*complexconjugate(Lam2Dash))) + ZH22*(ZH23*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v2*ZH21*(complexconjugate(Lam3) + complexconjugate(Lam4)) + 4*v1*ZH22*(complexconjugate(Lam3) + complexconjugate(Lam4))) + 4*ZH21*(6*v1*ZH21*complexconjugate(Lam1) + v3*ZH23*complexconjugate(Lam2Dash) + v2*ZH22*(complexconjugate(Lam3) + complexconjugate(Lam4)))))', 
	 order = {'QED':1} ) 
 
GC_66 = Coupling(name = 'GC_66',
	 value = '1./4.*complex(0,1)*(-(ZH23*(ZH21*(ZH32*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v3*ZH31*complexconjugate(Lam2Dash) + 2*ZH33*(Aa3*v2 + Aa4*v2 + v2*complexconjugate(Aa3) + v2*complexconjugate(Aa4) + 2*v1*complexconjugate(Lam2Dash))) + 2*ZH23*(12*v3*ZH33*complexconjugate(Lam1Dash) + ZH31*(Aa3*v2 + Aa4*v2 + v2*complexconjugate(Aa3) + v2*complexconjugate(Aa4) + 2*v1*complexconjugate(Lam2Dash)) + ZH32*(Aa3*v1 + Aa4*v1 + v1*complexconjugate(Aa3) + v1*complexconjugate(Aa4) + 2*v2*complexconjugate(Lam3Dash))) + ZH22*(ZH31*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v3*ZH32*complexconjugate(Lam3Dash) + 2*ZH33*(Aa3*v1 + Aa4*v1 + v1*complexconjugate(Aa3) + v1*complexconjugate(Aa4) + 2*v2*complexconjugate(Lam3Dash))))) - ZH22*(ZH23*(ZH31*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v3*ZH32*complexconjugate(Lam3Dash) + 2*ZH33*(Aa3*v1 + Aa4*v1 + v1*complexconjugate(Aa3) + v1*complexconjugate(Aa4) + 2*v2*complexconjugate(Lam3Dash))) + 4*ZH22*(6*v2*ZH32*complexconjugate(Lam2) + v3*ZH33*complexconjugate(Lam3Dash) + v1*ZH31*(complexconjugate(Lam3) + complexconjugate(Lam4))) + ZH21*(ZH33*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v2*ZH31*(complexconjugate(Lam3) + complexconjugate(Lam4)) + 4*v1*ZH32*(complexconjugate(Lam3) + complexconjugate(Lam4)))) - ZH21*(ZH23*(ZH32*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v3*ZH31*complexconjugate(Lam2Dash) + 2*ZH33*(Aa3*v2 + Aa4*v2 + v2*complexconjugate(Aa3) + v2*complexconjugate(Aa4) + 2*v1*complexconjugate(Lam2Dash))) + ZH22*(ZH33*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v2*ZH31*(complexconjugate(Lam3) + complexconjugate(Lam4)) + 4*v1*ZH32*(complexconjugate(Lam3) + complexconjugate(Lam4))) + 4*ZH21*(6*v1*ZH31*complexconjugate(Lam1) + v3*ZH33*complexconjugate(Lam2Dash) + v2*ZH32*(complexconjugate(Lam3) + complexconjugate(Lam4)))))', 
	 order = {'QED':1} ) 
 
GC_67 = Coupling(name = 'GC_67',
	 value = '1./4.*complex(0,1)*(-(ZH23*(ZH31*(ZH32*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v3*ZH31*complexconjugate(Lam2Dash) + 2*ZH33*(Aa3*v2 + Aa4*v2 + v2*complexconjugate(Aa3) + v2*complexconjugate(Aa4) + 2*v1*complexconjugate(Lam2Dash))) + 2*ZH33*(12*v3*ZH33*complexconjugate(Lam1Dash) + ZH31*(Aa3*v2 + Aa4*v2 + v2*complexconjugate(Aa3) + v2*complexconjugate(Aa4) + 2*v1*complexconjugate(Lam2Dash)) + ZH32*(Aa3*v1 + Aa4*v1 + v1*complexconjugate(Aa3) + v1*complexconjugate(Aa4) + 2*v2*complexconjugate(Lam3Dash))) + ZH32*(ZH31*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v3*ZH32*complexconjugate(Lam3Dash) + 2*ZH33*(Aa3*v1 + Aa4*v1 + v1*complexconjugate(Aa3) + v1*complexconjugate(Aa4) + 2*v2*complexconjugate(Lam3Dash))))) - ZH22*(ZH33*(ZH31*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v3*ZH32*complexconjugate(Lam3Dash) + 2*ZH33*(Aa3*v1 + Aa4*v1 + v1*complexconjugate(Aa3) + v1*complexconjugate(Aa4) + 2*v2*complexconjugate(Lam3Dash))) + 4*ZH32*(6*v2*ZH32*complexconjugate(Lam2) + v3*ZH33*complexconjugate(Lam3Dash) + v1*ZH31*(complexconjugate(Lam3) + complexconjugate(Lam4))) + ZH31*(ZH33*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v2*ZH31*(complexconjugate(Lam3) + complexconjugate(Lam4)) + 4*v1*ZH32*(complexconjugate(Lam3) + complexconjugate(Lam4)))) - ZH21*(ZH33*(ZH32*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v3*ZH31*complexconjugate(Lam2Dash) + 2*ZH33*(Aa3*v2 + Aa4*v2 + v2*complexconjugate(Aa3) + v2*complexconjugate(Aa4) + 2*v1*complexconjugate(Lam2Dash))) + ZH32*(ZH33*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v2*ZH31*(complexconjugate(Lam3) + complexconjugate(Lam4)) + 4*v1*ZH32*(complexconjugate(Lam3) + complexconjugate(Lam4))) + 4*ZH31*(6*v1*ZH31*complexconjugate(Lam1) + v3*ZH33*complexconjugate(Lam2Dash) + v2*ZH32*(complexconjugate(Lam3) + complexconjugate(Lam4)))))', 
	 order = {'QED':1} ) 
 
GC_68 = Coupling(name = 'GC_68',
	 value = '1./4.*complex(0,1)*(-(ZH33*(ZH31*(ZH32*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v3*ZH31*complexconjugate(Lam2Dash) + 2*ZH33*(Aa3*v2 + Aa4*v2 + v2*complexconjugate(Aa3) + v2*complexconjugate(Aa4) + 2*v1*complexconjugate(Lam2Dash))) + 2*ZH33*(12*v3*ZH33*complexconjugate(Lam1Dash) + ZH31*(Aa3*v2 + Aa4*v2 + v2*complexconjugate(Aa3) + v2*complexconjugate(Aa4) + 2*v1*complexconjugate(Lam2Dash)) + ZH32*(Aa3*v1 + Aa4*v1 + v1*complexconjugate(Aa3) + v1*complexconjugate(Aa4) + 2*v2*complexconjugate(Lam3Dash))) + ZH32*(ZH31*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v3*ZH32*complexconjugate(Lam3Dash) + 2*ZH33*(Aa3*v1 + Aa4*v1 + v1*complexconjugate(Aa3) + v1*complexconjugate(Aa4) + 2*v2*complexconjugate(Lam3Dash))))) - ZH32*(ZH33*(ZH31*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v3*ZH32*complexconjugate(Lam3Dash) + 2*ZH33*(Aa3*v1 + Aa4*v1 + v1*complexconjugate(Aa3) + v1*complexconjugate(Aa4) + 2*v2*complexconjugate(Lam3Dash))) + 4*ZH32*(6*v2*ZH32*complexconjugate(Lam2) + v3*ZH33*complexconjugate(Lam3Dash) + v1*ZH31*(complexconjugate(Lam3) + complexconjugate(Lam4))) + ZH31*(ZH33*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v2*ZH31*(complexconjugate(Lam3) + complexconjugate(Lam4)) + 4*v1*ZH32*(complexconjugate(Lam3) + complexconjugate(Lam4)))) - ZH31*(ZH33*(ZH32*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v3*ZH31*complexconjugate(Lam2Dash) + 2*ZH33*(Aa3*v2 + Aa4*v2 + v2*complexconjugate(Aa3) + v2*complexconjugate(Aa4) + 2*v1*complexconjugate(Lam2Dash))) + ZH32*(ZH33*(cmath.sqrt(2)*Aa1 + cmath.sqrt(2)*Aa2 + 2*Aa3*v3 + 2*Aa4*v3 + cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*complexconjugate(Aa3) + 2*v3*complexconjugate(Aa4)) + 4*v2*ZH31*(complexconjugate(Lam3) + complexconjugate(Lam4)) + 4*v1*ZH32*(complexconjugate(Lam3) + complexconjugate(Lam4))) + 4*ZH31*(6*v1*ZH31*complexconjugate(Lam1) + v3*ZH33*complexconjugate(Lam2Dash) + v2*ZH32*(complexconjugate(Lam3) + complexconjugate(Lam4)))))', 
	 order = {'QED':1} ) 
 
GC_69 = Coupling(name = 'GC_69',
	 value = '1./2.*complex(0,1)*(-(ZP11*(ZH13*(2*v3*complexconjugate(Lam2Dash)*complexconjugate(ZP11) + (cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*(complexconjugate(Aa3) + complexconjugate(Aa4)))*complexconjugate(ZP12)) + ZH12*(2*v2*complexconjugate(Lam3)*complexconjugate(ZP11) + v1*complexconjugate(Lam4)*complexconjugate(ZP12)) + ZH11*(4*v1*complexconjugate(Lam1)*complexconjugate(ZP11) + v2*complexconjugate(Lam4)*complexconjugate(ZP12)))) - ZP12*(ZH12*(v1*complexconjugate(Lam4)*complexconjugate(ZP11) + 4*v2*complexconjugate(Lam2)*complexconjugate(ZP12)) + ZH11*(v2*complexconjugate(Lam4)*complexconjugate(ZP11) + 2*v1*complexconjugate(Lam3)*complexconjugate(ZP12)) + ZH13*(cmath.sqrt(2)*Aa1*complexconjugate(ZP11) + cmath.sqrt(2)*Aa2*complexconjugate(ZP11) + 2*v3*(Aa3*complexconjugate(ZP11) + Aa4*complexconjugate(ZP11) + complexconjugate(Lam3Dash)*complexconjugate(ZP12)))))', 
	 order = {'QED':1} ) 
 
GC_70 = Coupling(name = 'GC_70',
	 value = '1./2.*complex(0,1)*(-(ZP11*(ZH13*(2*v3*complexconjugate(Lam2Dash)*complexconjugate(ZP21) + (cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*(complexconjugate(Aa3) + complexconjugate(Aa4)))*complexconjugate(ZP22)) + ZH12*(2*v2*complexconjugate(Lam3)*complexconjugate(ZP21) + v1*complexconjugate(Lam4)*complexconjugate(ZP22)) + ZH11*(4*v1*complexconjugate(Lam1)*complexconjugate(ZP21) + v2*complexconjugate(Lam4)*complexconjugate(ZP22)))) - ZP12*(ZH12*(v1*complexconjugate(Lam4)*complexconjugate(ZP21) + 4*v2*complexconjugate(Lam2)*complexconjugate(ZP22)) + ZH11*(v2*complexconjugate(Lam4)*complexconjugate(ZP21) + 2*v1*complexconjugate(Lam3)*complexconjugate(ZP22)) + ZH13*(cmath.sqrt(2)*Aa1*complexconjugate(ZP21) + cmath.sqrt(2)*Aa2*complexconjugate(ZP21) + 2*v3*(Aa3*complexconjugate(ZP21) + Aa4*complexconjugate(ZP21) + complexconjugate(Lam3Dash)*complexconjugate(ZP22)))))', 
	 order = {'QED':1} ) 
 
GC_71 = Coupling(name = 'GC_71',
	 value = '1./2.*complex(0,1)*(-(ZP21*(ZH13*(2*v3*complexconjugate(Lam2Dash)*complexconjugate(ZP11) + (cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*(complexconjugate(Aa3) + complexconjugate(Aa4)))*complexconjugate(ZP12)) + ZH12*(2*v2*complexconjugate(Lam3)*complexconjugate(ZP11) + v1*complexconjugate(Lam4)*complexconjugate(ZP12)) + ZH11*(4*v1*complexconjugate(Lam1)*complexconjugate(ZP11) + v2*complexconjugate(Lam4)*complexconjugate(ZP12)))) - ZP22*(ZH12*(v1*complexconjugate(Lam4)*complexconjugate(ZP11) + 4*v2*complexconjugate(Lam2)*complexconjugate(ZP12)) + ZH11*(v2*complexconjugate(Lam4)*complexconjugate(ZP11) + 2*v1*complexconjugate(Lam3)*complexconjugate(ZP12)) + ZH13*(cmath.sqrt(2)*Aa1*complexconjugate(ZP11) + cmath.sqrt(2)*Aa2*complexconjugate(ZP11) + 2*v3*(Aa3*complexconjugate(ZP11) + Aa4*complexconjugate(ZP11) + complexconjugate(Lam3Dash)*complexconjugate(ZP12)))))', 
	 order = {'QED':1} ) 
 
GC_72 = Coupling(name = 'GC_72',
	 value = '1./2.*complex(0,1)*(-(ZP21*(ZH13*(2*v3*complexconjugate(Lam2Dash)*complexconjugate(ZP21) + (cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*(complexconjugate(Aa3) + complexconjugate(Aa4)))*complexconjugate(ZP22)) + ZH12*(2*v2*complexconjugate(Lam3)*complexconjugate(ZP21) + v1*complexconjugate(Lam4)*complexconjugate(ZP22)) + ZH11*(4*v1*complexconjugate(Lam1)*complexconjugate(ZP21) + v2*complexconjugate(Lam4)*complexconjugate(ZP22)))) - ZP22*(ZH12*(v1*complexconjugate(Lam4)*complexconjugate(ZP21) + 4*v2*complexconjugate(Lam2)*complexconjugate(ZP22)) + ZH11*(v2*complexconjugate(Lam4)*complexconjugate(ZP21) + 2*v1*complexconjugate(Lam3)*complexconjugate(ZP22)) + ZH13*(cmath.sqrt(2)*Aa1*complexconjugate(ZP21) + cmath.sqrt(2)*Aa2*complexconjugate(ZP21) + 2*v3*(Aa3*complexconjugate(ZP21) + Aa4*complexconjugate(ZP21) + complexconjugate(Lam3Dash)*complexconjugate(ZP22)))))', 
	 order = {'QED':1} ) 
 
GC_73 = Coupling(name = 'GC_73',
	 value = '1./2.*complex(0,1)*(-(ZP11*(ZH23*(2*v3*complexconjugate(Lam2Dash)*complexconjugate(ZP11) + (cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*(complexconjugate(Aa3) + complexconjugate(Aa4)))*complexconjugate(ZP12)) + ZH22*(2*v2*complexconjugate(Lam3)*complexconjugate(ZP11) + v1*complexconjugate(Lam4)*complexconjugate(ZP12)) + ZH21*(4*v1*complexconjugate(Lam1)*complexconjugate(ZP11) + v2*complexconjugate(Lam4)*complexconjugate(ZP12)))) - ZP12*(ZH22*(v1*complexconjugate(Lam4)*complexconjugate(ZP11) + 4*v2*complexconjugate(Lam2)*complexconjugate(ZP12)) + ZH21*(v2*complexconjugate(Lam4)*complexconjugate(ZP11) + 2*v1*complexconjugate(Lam3)*complexconjugate(ZP12)) + ZH23*(cmath.sqrt(2)*Aa1*complexconjugate(ZP11) + cmath.sqrt(2)*Aa2*complexconjugate(ZP11) + 2*v3*(Aa3*complexconjugate(ZP11) + Aa4*complexconjugate(ZP11) + complexconjugate(Lam3Dash)*complexconjugate(ZP12)))))', 
	 order = {'QED':1} ) 
 
GC_74 = Coupling(name = 'GC_74',
	 value = '1./2.*complex(0,1)*(-(ZP11*(ZH23*(2*v3*complexconjugate(Lam2Dash)*complexconjugate(ZP21) + (cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*(complexconjugate(Aa3) + complexconjugate(Aa4)))*complexconjugate(ZP22)) + ZH22*(2*v2*complexconjugate(Lam3)*complexconjugate(ZP21) + v1*complexconjugate(Lam4)*complexconjugate(ZP22)) + ZH21*(4*v1*complexconjugate(Lam1)*complexconjugate(ZP21) + v2*complexconjugate(Lam4)*complexconjugate(ZP22)))) - ZP12*(ZH22*(v1*complexconjugate(Lam4)*complexconjugate(ZP21) + 4*v2*complexconjugate(Lam2)*complexconjugate(ZP22)) + ZH21*(v2*complexconjugate(Lam4)*complexconjugate(ZP21) + 2*v1*complexconjugate(Lam3)*complexconjugate(ZP22)) + ZH23*(cmath.sqrt(2)*Aa1*complexconjugate(ZP21) + cmath.sqrt(2)*Aa2*complexconjugate(ZP21) + 2*v3*(Aa3*complexconjugate(ZP21) + Aa4*complexconjugate(ZP21) + complexconjugate(Lam3Dash)*complexconjugate(ZP22)))))', 
	 order = {'QED':1} ) 
 
GC_75 = Coupling(name = 'GC_75',
	 value = '1./2.*complex(0,1)*(-(ZP21*(ZH23*(2*v3*complexconjugate(Lam2Dash)*complexconjugate(ZP11) + (cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*(complexconjugate(Aa3) + complexconjugate(Aa4)))*complexconjugate(ZP12)) + ZH22*(2*v2*complexconjugate(Lam3)*complexconjugate(ZP11) + v1*complexconjugate(Lam4)*complexconjugate(ZP12)) + ZH21*(4*v1*complexconjugate(Lam1)*complexconjugate(ZP11) + v2*complexconjugate(Lam4)*complexconjugate(ZP12)))) - ZP22*(ZH22*(v1*complexconjugate(Lam4)*complexconjugate(ZP11) + 4*v2*complexconjugate(Lam2)*complexconjugate(ZP12)) + ZH21*(v2*complexconjugate(Lam4)*complexconjugate(ZP11) + 2*v1*complexconjugate(Lam3)*complexconjugate(ZP12)) + ZH23*(cmath.sqrt(2)*Aa1*complexconjugate(ZP11) + cmath.sqrt(2)*Aa2*complexconjugate(ZP11) + 2*v3*(Aa3*complexconjugate(ZP11) + Aa4*complexconjugate(ZP11) + complexconjugate(Lam3Dash)*complexconjugate(ZP12)))))', 
	 order = {'QED':1} ) 
 
GC_76 = Coupling(name = 'GC_76',
	 value = '1./2.*complex(0,1)*(-(ZP21*(ZH23*(2*v3*complexconjugate(Lam2Dash)*complexconjugate(ZP21) + (cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*(complexconjugate(Aa3) + complexconjugate(Aa4)))*complexconjugate(ZP22)) + ZH22*(2*v2*complexconjugate(Lam3)*complexconjugate(ZP21) + v1*complexconjugate(Lam4)*complexconjugate(ZP22)) + ZH21*(4*v1*complexconjugate(Lam1)*complexconjugate(ZP21) + v2*complexconjugate(Lam4)*complexconjugate(ZP22)))) - ZP22*(ZH22*(v1*complexconjugate(Lam4)*complexconjugate(ZP21) + 4*v2*complexconjugate(Lam2)*complexconjugate(ZP22)) + ZH21*(v2*complexconjugate(Lam4)*complexconjugate(ZP21) + 2*v1*complexconjugate(Lam3)*complexconjugate(ZP22)) + ZH23*(cmath.sqrt(2)*Aa1*complexconjugate(ZP21) + cmath.sqrt(2)*Aa2*complexconjugate(ZP21) + 2*v3*(Aa3*complexconjugate(ZP21) + Aa4*complexconjugate(ZP21) + complexconjugate(Lam3Dash)*complexconjugate(ZP22)))))', 
	 order = {'QED':1} ) 
 
GC_77 = Coupling(name = 'GC_77',
	 value = '1./2.*complex(0,1)*(-(ZP11*(ZH33*(2*v3*complexconjugate(Lam2Dash)*complexconjugate(ZP11) + (cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*(complexconjugate(Aa3) + complexconjugate(Aa4)))*complexconjugate(ZP12)) + ZH32*(2*v2*complexconjugate(Lam3)*complexconjugate(ZP11) + v1*complexconjugate(Lam4)*complexconjugate(ZP12)) + ZH31*(4*v1*complexconjugate(Lam1)*complexconjugate(ZP11) + v2*complexconjugate(Lam4)*complexconjugate(ZP12)))) - ZP12*(ZH32*(v1*complexconjugate(Lam4)*complexconjugate(ZP11) + 4*v2*complexconjugate(Lam2)*complexconjugate(ZP12)) + ZH31*(v2*complexconjugate(Lam4)*complexconjugate(ZP11) + 2*v1*complexconjugate(Lam3)*complexconjugate(ZP12)) + ZH33*(cmath.sqrt(2)*Aa1*complexconjugate(ZP11) + cmath.sqrt(2)*Aa2*complexconjugate(ZP11) + 2*v3*(Aa3*complexconjugate(ZP11) + Aa4*complexconjugate(ZP11) + complexconjugate(Lam3Dash)*complexconjugate(ZP12)))))', 
	 order = {'QED':1} ) 
 
GC_78 = Coupling(name = 'GC_78',
	 value = '1./2.*complex(0,1)*(-(ZP11*(ZH33*(2*v3*complexconjugate(Lam2Dash)*complexconjugate(ZP21) + (cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*(complexconjugate(Aa3) + complexconjugate(Aa4)))*complexconjugate(ZP22)) + ZH32*(2*v2*complexconjugate(Lam3)*complexconjugate(ZP21) + v1*complexconjugate(Lam4)*complexconjugate(ZP22)) + ZH31*(4*v1*complexconjugate(Lam1)*complexconjugate(ZP21) + v2*complexconjugate(Lam4)*complexconjugate(ZP22)))) - ZP12*(ZH32*(v1*complexconjugate(Lam4)*complexconjugate(ZP21) + 4*v2*complexconjugate(Lam2)*complexconjugate(ZP22)) + ZH31*(v2*complexconjugate(Lam4)*complexconjugate(ZP21) + 2*v1*complexconjugate(Lam3)*complexconjugate(ZP22)) + ZH33*(cmath.sqrt(2)*Aa1*complexconjugate(ZP21) + cmath.sqrt(2)*Aa2*complexconjugate(ZP21) + 2*v3*(Aa3*complexconjugate(ZP21) + Aa4*complexconjugate(ZP21) + complexconjugate(Lam3Dash)*complexconjugate(ZP22)))))', 
	 order = {'QED':1} ) 
 
GC_79 = Coupling(name = 'GC_79',
	 value = '1./2.*complex(0,1)*(-(ZP21*(ZH33*(2*v3*complexconjugate(Lam2Dash)*complexconjugate(ZP11) + (cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*(complexconjugate(Aa3) + complexconjugate(Aa4)))*complexconjugate(ZP12)) + ZH32*(2*v2*complexconjugate(Lam3)*complexconjugate(ZP11) + v1*complexconjugate(Lam4)*complexconjugate(ZP12)) + ZH31*(4*v1*complexconjugate(Lam1)*complexconjugate(ZP11) + v2*complexconjugate(Lam4)*complexconjugate(ZP12)))) - ZP22*(ZH32*(v1*complexconjugate(Lam4)*complexconjugate(ZP11) + 4*v2*complexconjugate(Lam2)*complexconjugate(ZP12)) + ZH31*(v2*complexconjugate(Lam4)*complexconjugate(ZP11) + 2*v1*complexconjugate(Lam3)*complexconjugate(ZP12)) + ZH33*(cmath.sqrt(2)*Aa1*complexconjugate(ZP11) + cmath.sqrt(2)*Aa2*complexconjugate(ZP11) + 2*v3*(Aa3*complexconjugate(ZP11) + Aa4*complexconjugate(ZP11) + complexconjugate(Lam3Dash)*complexconjugate(ZP12)))))', 
	 order = {'QED':1} ) 
 
GC_80 = Coupling(name = 'GC_80',
	 value = '1./2.*complex(0,1)*(-(ZP21*(ZH33*(2*v3*complexconjugate(Lam2Dash)*complexconjugate(ZP21) + (cmath.sqrt(2)*complexconjugate(Aa1) + cmath.sqrt(2)*complexconjugate(Aa2) + 2*v3*(complexconjugate(Aa3) + complexconjugate(Aa4)))*complexconjugate(ZP22)) + ZH32*(2*v2*complexconjugate(Lam3)*complexconjugate(ZP21) + v1*complexconjugate(Lam4)*complexconjugate(ZP22)) + ZH31*(4*v1*complexconjugate(Lam1)*complexconjugate(ZP21) + v2*complexconjugate(Lam4)*complexconjugate(ZP22)))) - ZP22*(ZH32*(v1*complexconjugate(Lam4)*complexconjugate(ZP21) + 4*v2*complexconjugate(Lam2)*complexconjugate(ZP22)) + ZH31*(v2*complexconjugate(Lam4)*complexconjugate(ZP21) + 2*v1*complexconjugate(Lam3)*complexconjugate(ZP22)) + ZH33*(cmath.sqrt(2)*Aa1*complexconjugate(ZP21) + cmath.sqrt(2)*Aa2*complexconjugate(ZP21) + 2*v3*(Aa3*complexconjugate(ZP21) + Aa4*complexconjugate(ZP21) + complexconjugate(Lam3Dash)*complexconjugate(ZP22)))))', 
	 order = {'QED':1} ) 
 
GC_81 = Coupling(name = 'GC_81',
	 value = '1./2.*complex(0,1)*g1**2*ZA11**2*complexconjugate(ZZ11)**2 + 1./2.*complex(0,1)*g1**2*ZA12**2*complexconjugate(ZZ11)**2 - 1*complex(0,1)*g1*g2*ZA11**2*complexconjugate(ZZ11)*complexconjugate(ZZ21) - 1*complex(0,1)*g1*g2*ZA12**2*complexconjugate(ZZ11)*complexconjugate(ZZ21) + 1./2.*complex(0,1)*g2**2*ZA11**2*complexconjugate(ZZ21)**2 + 1./2.*complex(0,1)*g2**2*ZA12**2*complexconjugate(ZZ21)**2', 
	 order = {'QED':2} ) 
 
GC_82 = Coupling(name = 'GC_82',
	 value = '1./2.*complex(0,1)*g1**2*ZA11*ZA21*complexconjugate(ZZ11)**2 + 1./2.*complex(0,1)*g1**2*ZA12*ZA22*complexconjugate(ZZ11)**2 - 1*complex(0,1)*g1*g2*ZA11*ZA21*complexconjugate(ZZ11)*complexconjugate(ZZ21) - 1*complex(0,1)*g1*g2*ZA12*ZA22*complexconjugate(ZZ11)*complexconjugate(ZZ21) + 1./2.*complex(0,1)*g2**2*ZA11*ZA21*complexconjugate(ZZ21)**2 + 1./2.*complex(0,1)*g2**2*ZA12*ZA22*complexconjugate(ZZ21)**2', 
	 order = {'QED':2} ) 
 
GC_83 = Coupling(name = 'GC_83',
	 value = '1./2.*complex(0,1)*g1**2*ZA11*ZA31*complexconjugate(ZZ11)**2 + 1./2.*complex(0,1)*g1**2*ZA12*ZA32*complexconjugate(ZZ11)**2 - 1*complex(0,1)*g1*g2*ZA11*ZA31*complexconjugate(ZZ11)*complexconjugate(ZZ21) - 1*complex(0,1)*g1*g2*ZA12*ZA32*complexconjugate(ZZ11)*complexconjugate(ZZ21) + 1./2.*complex(0,1)*g2**2*ZA11*ZA31*complexconjugate(ZZ21)**2 + 1./2.*complex(0,1)*g2**2*ZA12*ZA32*complexconjugate(ZZ21)**2', 
	 order = {'QED':2} ) 
 
GC_84 = Coupling(name = 'GC_84',
	 value = '1./2.*complex(0,1)*g1**2*ZA21**2*complexconjugate(ZZ11)**2 + 1./2.*complex(0,1)*g1**2*ZA22**2*complexconjugate(ZZ11)**2 - 1*complex(0,1)*g1*g2*ZA21**2*complexconjugate(ZZ11)*complexconjugate(ZZ21) - 1*complex(0,1)*g1*g2*ZA22**2*complexconjugate(ZZ11)*complexconjugate(ZZ21) + 1./2.*complex(0,1)*g2**2*ZA21**2*complexconjugate(ZZ21)**2 + 1./2.*complex(0,1)*g2**2*ZA22**2*complexconjugate(ZZ21)**2', 
	 order = {'QED':2} ) 
 
GC_85 = Coupling(name = 'GC_85',
	 value = '1./2.*complex(0,1)*g1**2*ZA21*ZA31*complexconjugate(ZZ11)**2 + 1./2.*complex(0,1)*g1**2*ZA22*ZA32*complexconjugate(ZZ11)**2 - 1*complex(0,1)*g1*g2*ZA21*ZA31*complexconjugate(ZZ11)*complexconjugate(ZZ21) - 1*complex(0,1)*g1*g2*ZA22*ZA32*complexconjugate(ZZ11)*complexconjugate(ZZ21) + 1./2.*complex(0,1)*g2**2*ZA21*ZA31*complexconjugate(ZZ21)**2 + 1./2.*complex(0,1)*g2**2*ZA22*ZA32*complexconjugate(ZZ21)**2', 
	 order = {'QED':2} ) 
 
GC_86 = Coupling(name = 'GC_86',
	 value = '1./2.*complex(0,1)*g1**2*ZA31**2*complexconjugate(ZZ11)**2 + 1./2.*complex(0,1)*g1**2*ZA32**2*complexconjugate(ZZ11)**2 - 1*complex(0,1)*g1*g2*ZA31**2*complexconjugate(ZZ11)*complexconjugate(ZZ21) - 1*complex(0,1)*g1*g2*ZA32**2*complexconjugate(ZZ11)*complexconjugate(ZZ21) + 1./2.*complex(0,1)*g2**2*ZA31**2*complexconjugate(ZZ21)**2 + 1./2.*complex(0,1)*g2**2*ZA32**2*complexconjugate(ZZ21)**2', 
	 order = {'QED':2} ) 
 
GC_87 = Coupling(name = 'GC_87',
	 value = '1./2.*complex(0,1)*g1**2*ZA11**2*complexconjugate(ZZ11)*complexconjugate(ZZ12) + 1./2.*complex(0,1)*g1**2*ZA12**2*complexconjugate(ZZ11)*complexconjugate(ZZ12) - 1./2.*complex(0,1)*g1*g2*ZA11**2*complexconjugate(ZZ12)*complexconjugate(ZZ21) - 1./2.*complex(0,1)*g1*g2*ZA12**2*complexconjugate(ZZ12)*complexconjugate(ZZ21) - 1./2.*complex(0,1)*g1*g2*ZA11**2*complexconjugate(ZZ11)*complexconjugate(ZZ22) - 1./2.*complex(0,1)*g1*g2*ZA12**2*complexconjugate(ZZ11)*complexconjugate(ZZ22) + 1./2.*complex(0,1)*g2**2*ZA11**2*complexconjugate(ZZ21)*complexconjugate(ZZ22) + 1./2.*complex(0,1)*g2**2*ZA12**2*complexconjugate(ZZ21)*complexconjugate(ZZ22)', 
	 order = {'QED':2} ) 
 
GC_88 = Coupling(name = 'GC_88',
	 value = '1./2.*complex(0,1)*g1**2*ZA11*ZA21*complexconjugate(ZZ11)*complexconjugate(ZZ12) + 1./2.*complex(0,1)*g1**2*ZA12*ZA22*complexconjugate(ZZ11)*complexconjugate(ZZ12) - 1./2.*complex(0,1)*g1*g2*ZA11*ZA21*complexconjugate(ZZ12)*complexconjugate(ZZ21) - 1./2.*complex(0,1)*g1*g2*ZA12*ZA22*complexconjugate(ZZ12)*complexconjugate(ZZ21) - 1./2.*complex(0,1)*g1*g2*ZA11*ZA21*complexconjugate(ZZ11)*complexconjugate(ZZ22) - 1./2.*complex(0,1)*g1*g2*ZA12*ZA22*complexconjugate(ZZ11)*complexconjugate(ZZ22) + 1./2.*complex(0,1)*g2**2*ZA11*ZA21*complexconjugate(ZZ21)*complexconjugate(ZZ22) + 1./2.*complex(0,1)*g2**2*ZA12*ZA22*complexconjugate(ZZ21)*complexconjugate(ZZ22)', 
	 order = {'QED':2} ) 
 
GC_89 = Coupling(name = 'GC_89',
	 value = '1./2.*complex(0,1)*g1**2*ZA11*ZA31*complexconjugate(ZZ11)*complexconjugate(ZZ12) + 1./2.*complex(0,1)*g1**2*ZA12*ZA32*complexconjugate(ZZ11)*complexconjugate(ZZ12) - 1./2.*complex(0,1)*g1*g2*ZA11*ZA31*complexconjugate(ZZ12)*complexconjugate(ZZ21) - 1./2.*complex(0,1)*g1*g2*ZA12*ZA32*complexconjugate(ZZ12)*complexconjugate(ZZ21) - 1./2.*complex(0,1)*g1*g2*ZA11*ZA31*complexconjugate(ZZ11)*complexconjugate(ZZ22) - 1./2.*complex(0,1)*g1*g2*ZA12*ZA32*complexconjugate(ZZ11)*complexconjugate(ZZ22) + 1./2.*complex(0,1)*g2**2*ZA11*ZA31*complexconjugate(ZZ21)*complexconjugate(ZZ22) + 1./2.*complex(0,1)*g2**2*ZA12*ZA32*complexconjugate(ZZ21)*complexconjugate(ZZ22)', 
	 order = {'QED':2} ) 
 
GC_90 = Coupling(name = 'GC_90',
	 value = '1./2.*complex(0,1)*g1**2*ZA21**2*complexconjugate(ZZ11)*complexconjugate(ZZ12) + 1./2.*complex(0,1)*g1**2*ZA22**2*complexconjugate(ZZ11)*complexconjugate(ZZ12) - 1./2.*complex(0,1)*g1*g2*ZA21**2*complexconjugate(ZZ12)*complexconjugate(ZZ21) - 1./2.*complex(0,1)*g1*g2*ZA22**2*complexconjugate(ZZ12)*complexconjugate(ZZ21) - 1./2.*complex(0,1)*g1*g2*ZA21**2*complexconjugate(ZZ11)*complexconjugate(ZZ22) - 1./2.*complex(0,1)*g1*g2*ZA22**2*complexconjugate(ZZ11)*complexconjugate(ZZ22) + 1./2.*complex(0,1)*g2**2*ZA21**2*complexconjugate(ZZ21)*complexconjugate(ZZ22) + 1./2.*complex(0,1)*g2**2*ZA22**2*complexconjugate(ZZ21)*complexconjugate(ZZ22)', 
	 order = {'QED':2} ) 
 
GC_91 = Coupling(name = 'GC_91',
	 value = '1./2.*complex(0,1)*g1**2*ZA21*ZA31*complexconjugate(ZZ11)*complexconjugate(ZZ12) + 1./2.*complex(0,1)*g1**2*ZA22*ZA32*complexconjugate(ZZ11)*complexconjugate(ZZ12) - 1./2.*complex(0,1)*g1*g2*ZA21*ZA31*complexconjugate(ZZ12)*complexconjugate(ZZ21) - 1./2.*complex(0,1)*g1*g2*ZA22*ZA32*complexconjugate(ZZ12)*complexconjugate(ZZ21) - 1./2.*complex(0,1)*g1*g2*ZA21*ZA31*complexconjugate(ZZ11)*complexconjugate(ZZ22) - 1./2.*complex(0,1)*g1*g2*ZA22*ZA32*complexconjugate(ZZ11)*complexconjugate(ZZ22) + 1./2.*complex(0,1)*g2**2*ZA21*ZA31*complexconjugate(ZZ21)*complexconjugate(ZZ22) + 1./2.*complex(0,1)*g2**2*ZA22*ZA32*complexconjugate(ZZ21)*complexconjugate(ZZ22)', 
	 order = {'QED':2} ) 
 
GC_92 = Coupling(name = 'GC_92',
	 value = '1./2.*complex(0,1)*g1**2*ZA31**2*complexconjugate(ZZ11)*complexconjugate(ZZ12) + 1./2.*complex(0,1)*g1**2*ZA32**2*complexconjugate(ZZ11)*complexconjugate(ZZ12) - 1./2.*complex(0,1)*g1*g2*ZA31**2*complexconjugate(ZZ12)*complexconjugate(ZZ21) - 1./2.*complex(0,1)*g1*g2*ZA32**2*complexconjugate(ZZ12)*complexconjugate(ZZ21) - 1./2.*complex(0,1)*g1*g2*ZA31**2*complexconjugate(ZZ11)*complexconjugate(ZZ22) - 1./2.*complex(0,1)*g1*g2*ZA32**2*complexconjugate(ZZ11)*complexconjugate(ZZ22) + 1./2.*complex(0,1)*g2**2*ZA31**2*complexconjugate(ZZ21)*complexconjugate(ZZ22) + 1./2.*complex(0,1)*g2**2*ZA32**2*complexconjugate(ZZ21)*complexconjugate(ZZ22)', 
	 order = {'QED':2} ) 
 
GC_93 = Coupling(name = 'GC_93',
	 value = '1./2.*complex(0,1)*g2**2*ZA11**2 + 1./2.*complex(0,1)*g2**2*ZA12**2', 
	 order = {'QED':2} ) 
 
GC_94 = Coupling(name = 'GC_94',
	 value = '1./2.*complex(0,1)*g2**2*ZA11*ZA21 + 1./2.*complex(0,1)*g2**2*ZA12*ZA22', 
	 order = {'QED':2} ) 
 
GC_95 = Coupling(name = 'GC_95',
	 value = '1./2.*complex(0,1)*g2**2*ZA11*ZA31 + 1./2.*complex(0,1)*g2**2*ZA12*ZA32', 
	 order = {'QED':2} ) 
 
GC_96 = Coupling(name = 'GC_96',
	 value = '1./2.*complex(0,1)*g2**2*ZA21**2 + 1./2.*complex(0,1)*g2**2*ZA22**2', 
	 order = {'QED':2} ) 
 
GC_97 = Coupling(name = 'GC_97',
	 value = '1./2.*complex(0,1)*g2**2*ZA21*ZA31 + 1./2.*complex(0,1)*g2**2*ZA22*ZA32', 
	 order = {'QED':2} ) 
 
GC_98 = Coupling(name = 'GC_98',
	 value = '1./2.*complex(0,1)*g2**2*ZA31**2 + 1./2.*complex(0,1)*g2**2*ZA32**2', 
	 order = {'QED':2} ) 
 
GC_99 = Coupling(name = 'GC_99',
	 value = '1./2.*complex(0,1)*g1**2*ZA11**2*complexconjugate(ZZ12)**2 + 1./2.*complex(0,1)*g1**2*ZA12**2*complexconjugate(ZZ12)**2 - 1*complex(0,1)*g1*g2*ZA11**2*complexconjugate(ZZ12)*complexconjugate(ZZ22) - 1*complex(0,1)*g1*g2*ZA12**2*complexconjugate(ZZ12)*complexconjugate(ZZ22) + 1./2.*complex(0,1)*g2**2*ZA11**2*complexconjugate(ZZ22)**2 + 1./2.*complex(0,1)*g2**2*ZA12**2*complexconjugate(ZZ22)**2', 
	 order = {'QED':2} ) 
 
GC_100 = Coupling(name = 'GC_100',
	 value = '1./2.*complex(0,1)*g1**2*ZA11*ZA21*complexconjugate(ZZ12)**2 + 1./2.*complex(0,1)*g1**2*ZA12*ZA22*complexconjugate(ZZ12)**2 - 1*complex(0,1)*g1*g2*ZA11*ZA21*complexconjugate(ZZ12)*complexconjugate(ZZ22) - 1*complex(0,1)*g1*g2*ZA12*ZA22*complexconjugate(ZZ12)*complexconjugate(ZZ22) + 1./2.*complex(0,1)*g2**2*ZA11*ZA21*complexconjugate(ZZ22)**2 + 1./2.*complex(0,1)*g2**2*ZA12*ZA22*complexconjugate(ZZ22)**2', 
	 order = {'QED':2} ) 
 
GC_101 = Coupling(name = 'GC_101',
	 value = '1./2.*complex(0,1)*g1**2*ZA11*ZA31*complexconjugate(ZZ12)**2 + 1./2.*complex(0,1)*g1**2*ZA12*ZA32*complexconjugate(ZZ12)**2 - 1*complex(0,1)*g1*g2*ZA11*ZA31*complexconjugate(ZZ12)*complexconjugate(ZZ22) - 1*complex(0,1)*g1*g2*ZA12*ZA32*complexconjugate(ZZ12)*complexconjugate(ZZ22) + 1./2.*complex(0,1)*g2**2*ZA11*ZA31*complexconjugate(ZZ22)**2 + 1./2.*complex(0,1)*g2**2*ZA12*ZA32*complexconjugate(ZZ22)**2', 
	 order = {'QED':2} ) 
 
GC_102 = Coupling(name = 'GC_102',
	 value = '1./2.*complex(0,1)*g1**2*ZA21**2*complexconjugate(ZZ12)**2 + 1./2.*complex(0,1)*g1**2*ZA22**2*complexconjugate(ZZ12)**2 - 1*complex(0,1)*g1*g2*ZA21**2*complexconjugate(ZZ12)*complexconjugate(ZZ22) - 1*complex(0,1)*g1*g2*ZA22**2*complexconjugate(ZZ12)*complexconjugate(ZZ22) + 1./2.*complex(0,1)*g2**2*ZA21**2*complexconjugate(ZZ22)**2 + 1./2.*complex(0,1)*g2**2*ZA22**2*complexconjugate(ZZ22)**2', 
	 order = {'QED':2} ) 
 
GC_103 = Coupling(name = 'GC_103',
	 value = '1./2.*complex(0,1)*g1**2*ZA21*ZA31*complexconjugate(ZZ12)**2 + 1./2.*complex(0,1)*g1**2*ZA22*ZA32*complexconjugate(ZZ12)**2 - 1*complex(0,1)*g1*g2*ZA21*ZA31*complexconjugate(ZZ12)*complexconjugate(ZZ22) - 1*complex(0,1)*g1*g2*ZA22*ZA32*complexconjugate(ZZ12)*complexconjugate(ZZ22) + 1./2.*complex(0,1)*g2**2*ZA21*ZA31*complexconjugate(ZZ22)**2 + 1./2.*complex(0,1)*g2**2*ZA22*ZA32*complexconjugate(ZZ22)**2', 
	 order = {'QED':2} ) 
 
GC_104 = Coupling(name = 'GC_104',
	 value = '1./2.*complex(0,1)*g1**2*ZA31**2*complexconjugate(ZZ12)**2 + 1./2.*complex(0,1)*g1**2*ZA32**2*complexconjugate(ZZ12)**2 - 1*complex(0,1)*g1*g2*ZA31**2*complexconjugate(ZZ12)*complexconjugate(ZZ22) - 1*complex(0,1)*g1*g2*ZA32**2*complexconjugate(ZZ12)*complexconjugate(ZZ22) + 1./2.*complex(0,1)*g2**2*ZA31**2*complexconjugate(ZZ22)**2 + 1./2.*complex(0,1)*g2**2*ZA32**2*complexconjugate(ZZ22)**2', 
	 order = {'QED':2} ) 
 
GC_105 = Coupling(name = 'GC_105',
	 value = '-(g1*g2*ZA11*ZP11*complexconjugate(ZZ11))/2. - (g1*g2*ZA12*ZP12*complexconjugate(ZZ11))/2.', 
	 order = {'QED':2} ) 
 
GC_106 = Coupling(name = 'GC_106',
	 value = '-(g1*g2*ZA11*ZP21*complexconjugate(ZZ11))/2. - (g1*g2*ZA12*ZP22*complexconjugate(ZZ11))/2.', 
	 order = {'QED':2} ) 
 
GC_107 = Coupling(name = 'GC_107',
	 value = '-(g1*g2*ZA21*ZP11*complexconjugate(ZZ11))/2. - (g1*g2*ZA22*ZP12*complexconjugate(ZZ11))/2.', 
	 order = {'QED':2} ) 
 
GC_108 = Coupling(name = 'GC_108',
	 value = '-(g1*g2*ZA21*ZP21*complexconjugate(ZZ11))/2. - (g1*g2*ZA22*ZP22*complexconjugate(ZZ11))/2.', 
	 order = {'QED':2} ) 
 
GC_109 = Coupling(name = 'GC_109',
	 value = '-(g1*g2*ZA31*ZP11*complexconjugate(ZZ11))/2. - (g1*g2*ZA32*ZP12*complexconjugate(ZZ11))/2.', 
	 order = {'QED':2} ) 
 
GC_110 = Coupling(name = 'GC_110',
	 value = '-(g1*g2*ZA31*ZP21*complexconjugate(ZZ11))/2. - (g1*g2*ZA32*ZP22*complexconjugate(ZZ11))/2.', 
	 order = {'QED':2} ) 
 
GC_111 = Coupling(name = 'GC_111',
	 value = '-(g1*g2*ZA11*ZP11*complexconjugate(ZZ12))/2. - (g1*g2*ZA12*ZP12*complexconjugate(ZZ12))/2.', 
	 order = {'QED':2} ) 
 
GC_112 = Coupling(name = 'GC_112',
	 value = '-(g1*g2*ZA11*ZP21*complexconjugate(ZZ12))/2. - (g1*g2*ZA12*ZP22*complexconjugate(ZZ12))/2.', 
	 order = {'QED':2} ) 
 
GC_113 = Coupling(name = 'GC_113',
	 value = '-(g1*g2*ZA21*ZP11*complexconjugate(ZZ12))/2. - (g1*g2*ZA22*ZP12*complexconjugate(ZZ12))/2.', 
	 order = {'QED':2} ) 
 
GC_114 = Coupling(name = 'GC_114',
	 value = '-(g1*g2*ZA21*ZP21*complexconjugate(ZZ12))/2. - (g1*g2*ZA22*ZP22*complexconjugate(ZZ12))/2.', 
	 order = {'QED':2} ) 
 
GC_115 = Coupling(name = 'GC_115',
	 value = '-(g1*g2*ZA31*ZP11*complexconjugate(ZZ12))/2. - (g1*g2*ZA32*ZP12*complexconjugate(ZZ12))/2.', 
	 order = {'QED':2} ) 
 
GC_116 = Coupling(name = 'GC_116',
	 value = '-(g1*g2*ZA31*ZP21*complexconjugate(ZZ12))/2. - (g1*g2*ZA32*ZP22*complexconjugate(ZZ12))/2.', 
	 order = {'QED':2} ) 
 
GC_117 = Coupling(name = 'GC_117',
	 value = '(g1*g2*ZA11*complexconjugate(ZP11)*complexconjugate(ZZ11))/2. + (g1*g2*ZA12*complexconjugate(ZP12)*complexconjugate(ZZ11))/2.', 
	 order = {'QED':2} ) 
 
GC_118 = Coupling(name = 'GC_118',
	 value = '(g1*g2*ZA11*complexconjugate(ZP21)*complexconjugate(ZZ11))/2. + (g1*g2*ZA12*complexconjugate(ZP22)*complexconjugate(ZZ11))/2.', 
	 order = {'QED':2} ) 
 
GC_119 = Coupling(name = 'GC_119',
	 value = '(g1*g2*ZA21*complexconjugate(ZP11)*complexconjugate(ZZ11))/2. + (g1*g2*ZA22*complexconjugate(ZP12)*complexconjugate(ZZ11))/2.', 
	 order = {'QED':2} ) 
 
GC_120 = Coupling(name = 'GC_120',
	 value = '(g1*g2*ZA21*complexconjugate(ZP21)*complexconjugate(ZZ11))/2. + (g1*g2*ZA22*complexconjugate(ZP22)*complexconjugate(ZZ11))/2.', 
	 order = {'QED':2} ) 
 
GC_121 = Coupling(name = 'GC_121',
	 value = '(g1*g2*ZA31*complexconjugate(ZP11)*complexconjugate(ZZ11))/2. + (g1*g2*ZA32*complexconjugate(ZP12)*complexconjugate(ZZ11))/2.', 
	 order = {'QED':2} ) 
 
GC_122 = Coupling(name = 'GC_122',
	 value = '(g1*g2*ZA31*complexconjugate(ZP21)*complexconjugate(ZZ11))/2. + (g1*g2*ZA32*complexconjugate(ZP22)*complexconjugate(ZZ11))/2.', 
	 order = {'QED':2} ) 
 
GC_123 = Coupling(name = 'GC_123',
	 value = '(g1*g2*ZA11*complexconjugate(ZP11)*complexconjugate(ZZ12))/2. + (g1*g2*ZA12*complexconjugate(ZP12)*complexconjugate(ZZ12))/2.', 
	 order = {'QED':2} ) 
 
GC_124 = Coupling(name = 'GC_124',
	 value = '(g1*g2*ZA11*complexconjugate(ZP21)*complexconjugate(ZZ12))/2. + (g1*g2*ZA12*complexconjugate(ZP22)*complexconjugate(ZZ12))/2.', 
	 order = {'QED':2} ) 
 
GC_125 = Coupling(name = 'GC_125',
	 value = '(g1*g2*ZA21*complexconjugate(ZP11)*complexconjugate(ZZ12))/2. + (g1*g2*ZA22*complexconjugate(ZP12)*complexconjugate(ZZ12))/2.', 
	 order = {'QED':2} ) 
 
GC_126 = Coupling(name = 'GC_126',
	 value = '(g1*g2*ZA21*complexconjugate(ZP21)*complexconjugate(ZZ12))/2. + (g1*g2*ZA22*complexconjugate(ZP22)*complexconjugate(ZZ12))/2.', 
	 order = {'QED':2} ) 
 
GC_127 = Coupling(name = 'GC_127',
	 value = '(g1*g2*ZA31*complexconjugate(ZP11)*complexconjugate(ZZ12))/2. + (g1*g2*ZA32*complexconjugate(ZP12)*complexconjugate(ZZ12))/2.', 
	 order = {'QED':2} ) 
 
GC_128 = Coupling(name = 'GC_128',
	 value = '(g1*g2*ZA31*complexconjugate(ZP21)*complexconjugate(ZZ12))/2. + (g1*g2*ZA32*complexconjugate(ZP22)*complexconjugate(ZZ12))/2.', 
	 order = {'QED':2} ) 
 
GC_129 = Coupling(name = 'GC_129',
	 value = '1./2.*complex(0,1)*g1**2*ZH11**2*complexconjugate(ZZ11)**2 + 1./2.*complex(0,1)*g1**2*ZH12**2*complexconjugate(ZZ11)**2 - 1*complex(0,1)*g1*g2*ZH11**2*complexconjugate(ZZ11)*complexconjugate(ZZ21) - 1*complex(0,1)*g1*g2*ZH12**2*complexconjugate(ZZ11)*complexconjugate(ZZ21) + 1./2.*complex(0,1)*g2**2*ZH11**2*complexconjugate(ZZ21)**2 + 1./2.*complex(0,1)*g2**2*ZH12**2*complexconjugate(ZZ21)**2', 
	 order = {'QED':2} ) 
 
GC_130 = Coupling(name = 'GC_130',
	 value = '1./2.*complex(0,1)*g1**2*ZH11*ZH21*complexconjugate(ZZ11)**2 + 1./2.*complex(0,1)*g1**2*ZH12*ZH22*complexconjugate(ZZ11)**2 - 1*complex(0,1)*g1*g2*ZH11*ZH21*complexconjugate(ZZ11)*complexconjugate(ZZ21) - 1*complex(0,1)*g1*g2*ZH12*ZH22*complexconjugate(ZZ11)*complexconjugate(ZZ21) + 1./2.*complex(0,1)*g2**2*ZH11*ZH21*complexconjugate(ZZ21)**2 + 1./2.*complex(0,1)*g2**2*ZH12*ZH22*complexconjugate(ZZ21)**2', 
	 order = {'QED':2} ) 
 
GC_131 = Coupling(name = 'GC_131',
	 value = '1./2.*complex(0,1)*g1**2*ZH11*ZH31*complexconjugate(ZZ11)**2 + 1./2.*complex(0,1)*g1**2*ZH12*ZH32*complexconjugate(ZZ11)**2 - 1*complex(0,1)*g1*g2*ZH11*ZH31*complexconjugate(ZZ11)*complexconjugate(ZZ21) - 1*complex(0,1)*g1*g2*ZH12*ZH32*complexconjugate(ZZ11)*complexconjugate(ZZ21) + 1./2.*complex(0,1)*g2**2*ZH11*ZH31*complexconjugate(ZZ21)**2 + 1./2.*complex(0,1)*g2**2*ZH12*ZH32*complexconjugate(ZZ21)**2', 
	 order = {'QED':2} ) 
 
GC_132 = Coupling(name = 'GC_132',
	 value = '1./2.*complex(0,1)*g1**2*ZH21**2*complexconjugate(ZZ11)**2 + 1./2.*complex(0,1)*g1**2*ZH22**2*complexconjugate(ZZ11)**2 - 1*complex(0,1)*g1*g2*ZH21**2*complexconjugate(ZZ11)*complexconjugate(ZZ21) - 1*complex(0,1)*g1*g2*ZH22**2*complexconjugate(ZZ11)*complexconjugate(ZZ21) + 1./2.*complex(0,1)*g2**2*ZH21**2*complexconjugate(ZZ21)**2 + 1./2.*complex(0,1)*g2**2*ZH22**2*complexconjugate(ZZ21)**2', 
	 order = {'QED':2} ) 
 
GC_133 = Coupling(name = 'GC_133',
	 value = '1./2.*complex(0,1)*g1**2*ZH21*ZH31*complexconjugate(ZZ11)**2 + 1./2.*complex(0,1)*g1**2*ZH22*ZH32*complexconjugate(ZZ11)**2 - 1*complex(0,1)*g1*g2*ZH21*ZH31*complexconjugate(ZZ11)*complexconjugate(ZZ21) - 1*complex(0,1)*g1*g2*ZH22*ZH32*complexconjugate(ZZ11)*complexconjugate(ZZ21) + 1./2.*complex(0,1)*g2**2*ZH21*ZH31*complexconjugate(ZZ21)**2 + 1./2.*complex(0,1)*g2**2*ZH22*ZH32*complexconjugate(ZZ21)**2', 
	 order = {'QED':2} ) 
 
GC_134 = Coupling(name = 'GC_134',
	 value = '1./2.*complex(0,1)*g1**2*ZH31**2*complexconjugate(ZZ11)**2 + 1./2.*complex(0,1)*g1**2*ZH32**2*complexconjugate(ZZ11)**2 - 1*complex(0,1)*g1*g2*ZH31**2*complexconjugate(ZZ11)*complexconjugate(ZZ21) - 1*complex(0,1)*g1*g2*ZH32**2*complexconjugate(ZZ11)*complexconjugate(ZZ21) + 1./2.*complex(0,1)*g2**2*ZH31**2*complexconjugate(ZZ21)**2 + 1./2.*complex(0,1)*g2**2*ZH32**2*complexconjugate(ZZ21)**2', 
	 order = {'QED':2} ) 
 
GC_135 = Coupling(name = 'GC_135',
	 value = '1./2.*complex(0,1)*g1**2*ZH11**2*complexconjugate(ZZ11)*complexconjugate(ZZ12) + 1./2.*complex(0,1)*g1**2*ZH12**2*complexconjugate(ZZ11)*complexconjugate(ZZ12) - 1./2.*complex(0,1)*g1*g2*ZH11**2*complexconjugate(ZZ12)*complexconjugate(ZZ21) - 1./2.*complex(0,1)*g1*g2*ZH12**2*complexconjugate(ZZ12)*complexconjugate(ZZ21) - 1./2.*complex(0,1)*g1*g2*ZH11**2*complexconjugate(ZZ11)*complexconjugate(ZZ22) - 1./2.*complex(0,1)*g1*g2*ZH12**2*complexconjugate(ZZ11)*complexconjugate(ZZ22) + 1./2.*complex(0,1)*g2**2*ZH11**2*complexconjugate(ZZ21)*complexconjugate(ZZ22) + 1./2.*complex(0,1)*g2**2*ZH12**2*complexconjugate(ZZ21)*complexconjugate(ZZ22)', 
	 order = {'QED':2} ) 
 
GC_136 = Coupling(name = 'GC_136',
	 value = '1./2.*complex(0,1)*g1**2*ZH11*ZH21*complexconjugate(ZZ11)*complexconjugate(ZZ12) + 1./2.*complex(0,1)*g1**2*ZH12*ZH22*complexconjugate(ZZ11)*complexconjugate(ZZ12) - 1./2.*complex(0,1)*g1*g2*ZH11*ZH21*complexconjugate(ZZ12)*complexconjugate(ZZ21) - 1./2.*complex(0,1)*g1*g2*ZH12*ZH22*complexconjugate(ZZ12)*complexconjugate(ZZ21) - 1./2.*complex(0,1)*g1*g2*ZH11*ZH21*complexconjugate(ZZ11)*complexconjugate(ZZ22) - 1./2.*complex(0,1)*g1*g2*ZH12*ZH22*complexconjugate(ZZ11)*complexconjugate(ZZ22) + 1./2.*complex(0,1)*g2**2*ZH11*ZH21*complexconjugate(ZZ21)*complexconjugate(ZZ22) + 1./2.*complex(0,1)*g2**2*ZH12*ZH22*complexconjugate(ZZ21)*complexconjugate(ZZ22)', 
	 order = {'QED':2} ) 
 
GC_137 = Coupling(name = 'GC_137',
	 value = '1./2.*complex(0,1)*g1**2*ZH11*ZH31*complexconjugate(ZZ11)*complexconjugate(ZZ12) + 1./2.*complex(0,1)*g1**2*ZH12*ZH32*complexconjugate(ZZ11)*complexconjugate(ZZ12) - 1./2.*complex(0,1)*g1*g2*ZH11*ZH31*complexconjugate(ZZ12)*complexconjugate(ZZ21) - 1./2.*complex(0,1)*g1*g2*ZH12*ZH32*complexconjugate(ZZ12)*complexconjugate(ZZ21) - 1./2.*complex(0,1)*g1*g2*ZH11*ZH31*complexconjugate(ZZ11)*complexconjugate(ZZ22) - 1./2.*complex(0,1)*g1*g2*ZH12*ZH32*complexconjugate(ZZ11)*complexconjugate(ZZ22) + 1./2.*complex(0,1)*g2**2*ZH11*ZH31*complexconjugate(ZZ21)*complexconjugate(ZZ22) + 1./2.*complex(0,1)*g2**2*ZH12*ZH32*complexconjugate(ZZ21)*complexconjugate(ZZ22)', 
	 order = {'QED':2} ) 
 
GC_138 = Coupling(name = 'GC_138',
	 value = '1./2.*complex(0,1)*g1**2*ZH21**2*complexconjugate(ZZ11)*complexconjugate(ZZ12) + 1./2.*complex(0,1)*g1**2*ZH22**2*complexconjugate(ZZ11)*complexconjugate(ZZ12) - 1./2.*complex(0,1)*g1*g2*ZH21**2*complexconjugate(ZZ12)*complexconjugate(ZZ21) - 1./2.*complex(0,1)*g1*g2*ZH22**2*complexconjugate(ZZ12)*complexconjugate(ZZ21) - 1./2.*complex(0,1)*g1*g2*ZH21**2*complexconjugate(ZZ11)*complexconjugate(ZZ22) - 1./2.*complex(0,1)*g1*g2*ZH22**2*complexconjugate(ZZ11)*complexconjugate(ZZ22) + 1./2.*complex(0,1)*g2**2*ZH21**2*complexconjugate(ZZ21)*complexconjugate(ZZ22) + 1./2.*complex(0,1)*g2**2*ZH22**2*complexconjugate(ZZ21)*complexconjugate(ZZ22)', 
	 order = {'QED':2} ) 
 
GC_139 = Coupling(name = 'GC_139',
	 value = '1./2.*complex(0,1)*g1**2*ZH21*ZH31*complexconjugate(ZZ11)*complexconjugate(ZZ12) + 1./2.*complex(0,1)*g1**2*ZH22*ZH32*complexconjugate(ZZ11)*complexconjugate(ZZ12) - 1./2.*complex(0,1)*g1*g2*ZH21*ZH31*complexconjugate(ZZ12)*complexconjugate(ZZ21) - 1./2.*complex(0,1)*g1*g2*ZH22*ZH32*complexconjugate(ZZ12)*complexconjugate(ZZ21) - 1./2.*complex(0,1)*g1*g2*ZH21*ZH31*complexconjugate(ZZ11)*complexconjugate(ZZ22) - 1./2.*complex(0,1)*g1*g2*ZH22*ZH32*complexconjugate(ZZ11)*complexconjugate(ZZ22) + 1./2.*complex(0,1)*g2**2*ZH21*ZH31*complexconjugate(ZZ21)*complexconjugate(ZZ22) + 1./2.*complex(0,1)*g2**2*ZH22*ZH32*complexconjugate(ZZ21)*complexconjugate(ZZ22)', 
	 order = {'QED':2} ) 
 
GC_140 = Coupling(name = 'GC_140',
	 value = '1./2.*complex(0,1)*g1**2*ZH31**2*complexconjugate(ZZ11)*complexconjugate(ZZ12) + 1./2.*complex(0,1)*g1**2*ZH32**2*complexconjugate(ZZ11)*complexconjugate(ZZ12) - 1./2.*complex(0,1)*g1*g2*ZH31**2*complexconjugate(ZZ12)*complexconjugate(ZZ21) - 1./2.*complex(0,1)*g1*g2*ZH32**2*complexconjugate(ZZ12)*complexconjugate(ZZ21) - 1./2.*complex(0,1)*g1*g2*ZH31**2*complexconjugate(ZZ11)*complexconjugate(ZZ22) - 1./2.*complex(0,1)*g1*g2*ZH32**2*complexconjugate(ZZ11)*complexconjugate(ZZ22) + 1./2.*complex(0,1)*g2**2*ZH31**2*complexconjugate(ZZ21)*complexconjugate(ZZ22) + 1./2.*complex(0,1)*g2**2*ZH32**2*complexconjugate(ZZ21)*complexconjugate(ZZ22)', 
	 order = {'QED':2} ) 
 
GC_141 = Coupling(name = 'GC_141',
	 value = '1./2.*complex(0,1)*g2**2*ZH11**2 + 1./2.*complex(0,1)*g2**2*ZH12**2', 
	 order = {'QED':2} ) 
 
GC_142 = Coupling(name = 'GC_142',
	 value = '1./2.*complex(0,1)*g2**2*ZH11*ZH21 + 1./2.*complex(0,1)*g2**2*ZH12*ZH22', 
	 order = {'QED':2} ) 
 
GC_143 = Coupling(name = 'GC_143',
	 value = '1./2.*complex(0,1)*g2**2*ZH11*ZH31 + 1./2.*complex(0,1)*g2**2*ZH12*ZH32', 
	 order = {'QED':2} ) 
 
GC_144 = Coupling(name = 'GC_144',
	 value = '1./2.*complex(0,1)*g2**2*ZH21**2 + 1./2.*complex(0,1)*g2**2*ZH22**2', 
	 order = {'QED':2} ) 
 
GC_145 = Coupling(name = 'GC_145',
	 value = '1./2.*complex(0,1)*g2**2*ZH21*ZH31 + 1./2.*complex(0,1)*g2**2*ZH22*ZH32', 
	 order = {'QED':2} ) 
 
GC_146 = Coupling(name = 'GC_146',
	 value = '1./2.*complex(0,1)*g2**2*ZH31**2 + 1./2.*complex(0,1)*g2**2*ZH32**2', 
	 order = {'QED':2} ) 
 
GC_147 = Coupling(name = 'GC_147',
	 value = '1./2.*complex(0,1)*g1**2*ZH11**2*complexconjugate(ZZ12)**2 + 1./2.*complex(0,1)*g1**2*ZH12**2*complexconjugate(ZZ12)**2 - 1*complex(0,1)*g1*g2*ZH11**2*complexconjugate(ZZ12)*complexconjugate(ZZ22) - 1*complex(0,1)*g1*g2*ZH12**2*complexconjugate(ZZ12)*complexconjugate(ZZ22) + 1./2.*complex(0,1)*g2**2*ZH11**2*complexconjugate(ZZ22)**2 + 1./2.*complex(0,1)*g2**2*ZH12**2*complexconjugate(ZZ22)**2', 
	 order = {'QED':2} ) 
 
GC_148 = Coupling(name = 'GC_148',
	 value = '1./2.*complex(0,1)*g1**2*ZH11*ZH21*complexconjugate(ZZ12)**2 + 1./2.*complex(0,1)*g1**2*ZH12*ZH22*complexconjugate(ZZ12)**2 - 1*complex(0,1)*g1*g2*ZH11*ZH21*complexconjugate(ZZ12)*complexconjugate(ZZ22) - 1*complex(0,1)*g1*g2*ZH12*ZH22*complexconjugate(ZZ12)*complexconjugate(ZZ22) + 1./2.*complex(0,1)*g2**2*ZH11*ZH21*complexconjugate(ZZ22)**2 + 1./2.*complex(0,1)*g2**2*ZH12*ZH22*complexconjugate(ZZ22)**2', 
	 order = {'QED':2} ) 
 
GC_149 = Coupling(name = 'GC_149',
	 value = '1./2.*complex(0,1)*g1**2*ZH11*ZH31*complexconjugate(ZZ12)**2 + 1./2.*complex(0,1)*g1**2*ZH12*ZH32*complexconjugate(ZZ12)**2 - 1*complex(0,1)*g1*g2*ZH11*ZH31*complexconjugate(ZZ12)*complexconjugate(ZZ22) - 1*complex(0,1)*g1*g2*ZH12*ZH32*complexconjugate(ZZ12)*complexconjugate(ZZ22) + 1./2.*complex(0,1)*g2**2*ZH11*ZH31*complexconjugate(ZZ22)**2 + 1./2.*complex(0,1)*g2**2*ZH12*ZH32*complexconjugate(ZZ22)**2', 
	 order = {'QED':2} ) 
 
GC_150 = Coupling(name = 'GC_150',
	 value = '1./2.*complex(0,1)*g1**2*ZH21**2*complexconjugate(ZZ12)**2 + 1./2.*complex(0,1)*g1**2*ZH22**2*complexconjugate(ZZ12)**2 - 1*complex(0,1)*g1*g2*ZH21**2*complexconjugate(ZZ12)*complexconjugate(ZZ22) - 1*complex(0,1)*g1*g2*ZH22**2*complexconjugate(ZZ12)*complexconjugate(ZZ22) + 1./2.*complex(0,1)*g2**2*ZH21**2*complexconjugate(ZZ22)**2 + 1./2.*complex(0,1)*g2**2*ZH22**2*complexconjugate(ZZ22)**2', 
	 order = {'QED':2} ) 
 
GC_151 = Coupling(name = 'GC_151',
	 value = '1./2.*complex(0,1)*g1**2*ZH21*ZH31*complexconjugate(ZZ12)**2 + 1./2.*complex(0,1)*g1**2*ZH22*ZH32*complexconjugate(ZZ12)**2 - 1*complex(0,1)*g1*g2*ZH21*ZH31*complexconjugate(ZZ12)*complexconjugate(ZZ22) - 1*complex(0,1)*g1*g2*ZH22*ZH32*complexconjugate(ZZ12)*complexconjugate(ZZ22) + 1./2.*complex(0,1)*g2**2*ZH21*ZH31*complexconjugate(ZZ22)**2 + 1./2.*complex(0,1)*g2**2*ZH22*ZH32*complexconjugate(ZZ22)**2', 
	 order = {'QED':2} ) 
 
GC_152 = Coupling(name = 'GC_152',
	 value = '1./2.*complex(0,1)*g1**2*ZH31**2*complexconjugate(ZZ12)**2 + 1./2.*complex(0,1)*g1**2*ZH32**2*complexconjugate(ZZ12)**2 - 1*complex(0,1)*g1*g2*ZH31**2*complexconjugate(ZZ12)*complexconjugate(ZZ22) - 1*complex(0,1)*g1*g2*ZH32**2*complexconjugate(ZZ12)*complexconjugate(ZZ22) + 1./2.*complex(0,1)*g2**2*ZH31**2*complexconjugate(ZZ22)**2 + 1./2.*complex(0,1)*g2**2*ZH32**2*complexconjugate(ZZ22)**2', 
	 order = {'QED':2} ) 
 
GC_153 = Coupling(name = 'GC_153',
	 value = '1./2.*complex(0,1)*g1*g2*ZH11*ZP11*complexconjugate(ZZ11) + 1./2.*complex(0,1)*g1*g2*ZH12*ZP12*complexconjugate(ZZ11)', 
	 order = {'QED':2} ) 
 
GC_154 = Coupling(name = 'GC_154',
	 value = '1./2.*complex(0,1)*g1*g2*ZH11*ZP21*complexconjugate(ZZ11) + 1./2.*complex(0,1)*g1*g2*ZH12*ZP22*complexconjugate(ZZ11)', 
	 order = {'QED':2} ) 
 
GC_155 = Coupling(name = 'GC_155',
	 value = '1./2.*complex(0,1)*g1*g2*ZH21*ZP11*complexconjugate(ZZ11) + 1./2.*complex(0,1)*g1*g2*ZH22*ZP12*complexconjugate(ZZ11)', 
	 order = {'QED':2} ) 
 
GC_156 = Coupling(name = 'GC_156',
	 value = '1./2.*complex(0,1)*g1*g2*ZH21*ZP21*complexconjugate(ZZ11) + 1./2.*complex(0,1)*g1*g2*ZH22*ZP22*complexconjugate(ZZ11)', 
	 order = {'QED':2} ) 
 
GC_157 = Coupling(name = 'GC_157',
	 value = '1./2.*complex(0,1)*g1*g2*ZH31*ZP11*complexconjugate(ZZ11) + 1./2.*complex(0,1)*g1*g2*ZH32*ZP12*complexconjugate(ZZ11)', 
	 order = {'QED':2} ) 
 
GC_158 = Coupling(name = 'GC_158',
	 value = '1./2.*complex(0,1)*g1*g2*ZH31*ZP21*complexconjugate(ZZ11) + 1./2.*complex(0,1)*g1*g2*ZH32*ZP22*complexconjugate(ZZ11)', 
	 order = {'QED':2} ) 
 
GC_159 = Coupling(name = 'GC_159',
	 value = '1./2.*complex(0,1)*g1*g2*ZH11*ZP11*complexconjugate(ZZ12) + 1./2.*complex(0,1)*g1*g2*ZH12*ZP12*complexconjugate(ZZ12)', 
	 order = {'QED':2} ) 
 
GC_160 = Coupling(name = 'GC_160',
	 value = '1./2.*complex(0,1)*g1*g2*ZH11*ZP21*complexconjugate(ZZ12) + 1./2.*complex(0,1)*g1*g2*ZH12*ZP22*complexconjugate(ZZ12)', 
	 order = {'QED':2} ) 
 
GC_161 = Coupling(name = 'GC_161',
	 value = '1./2.*complex(0,1)*g1*g2*ZH21*ZP11*complexconjugate(ZZ12) + 1./2.*complex(0,1)*g1*g2*ZH22*ZP12*complexconjugate(ZZ12)', 
	 order = {'QED':2} ) 
 
GC_162 = Coupling(name = 'GC_162',
	 value = '1./2.*complex(0,1)*g1*g2*ZH21*ZP21*complexconjugate(ZZ12) + 1./2.*complex(0,1)*g1*g2*ZH22*ZP22*complexconjugate(ZZ12)', 
	 order = {'QED':2} ) 
 
GC_163 = Coupling(name = 'GC_163',
	 value = '1./2.*complex(0,1)*g1*g2*ZH31*ZP11*complexconjugate(ZZ12) + 1./2.*complex(0,1)*g1*g2*ZH32*ZP12*complexconjugate(ZZ12)', 
	 order = {'QED':2} ) 
 
GC_164 = Coupling(name = 'GC_164',
	 value = '1./2.*complex(0,1)*g1*g2*ZH31*ZP21*complexconjugate(ZZ12) + 1./2.*complex(0,1)*g1*g2*ZH32*ZP22*complexconjugate(ZZ12)', 
	 order = {'QED':2} ) 
 
GC_165 = Coupling(name = 'GC_165',
	 value = '1./2.*complex(0,1)*g1*g2*ZH11*complexconjugate(ZP11)*complexconjugate(ZZ11) + 1./2.*complex(0,1)*g1*g2*ZH12*complexconjugate(ZP12)*complexconjugate(ZZ11)', 
	 order = {'QED':2} ) 
 
GC_166 = Coupling(name = 'GC_166',
	 value = '1./2.*complex(0,1)*g1*g2*ZH11*complexconjugate(ZP21)*complexconjugate(ZZ11) + 1./2.*complex(0,1)*g1*g2*ZH12*complexconjugate(ZP22)*complexconjugate(ZZ11)', 
	 order = {'QED':2} ) 
 
GC_167 = Coupling(name = 'GC_167',
	 value = '1./2.*complex(0,1)*g1*g2*ZH21*complexconjugate(ZP11)*complexconjugate(ZZ11) + 1./2.*complex(0,1)*g1*g2*ZH22*complexconjugate(ZP12)*complexconjugate(ZZ11)', 
	 order = {'QED':2} ) 
 
GC_168 = Coupling(name = 'GC_168',
	 value = '1./2.*complex(0,1)*g1*g2*ZH21*complexconjugate(ZP21)*complexconjugate(ZZ11) + 1./2.*complex(0,1)*g1*g2*ZH22*complexconjugate(ZP22)*complexconjugate(ZZ11)', 
	 order = {'QED':2} ) 
 
GC_169 = Coupling(name = 'GC_169',
	 value = '1./2.*complex(0,1)*g1*g2*ZH31*complexconjugate(ZP11)*complexconjugate(ZZ11) + 1./2.*complex(0,1)*g1*g2*ZH32*complexconjugate(ZP12)*complexconjugate(ZZ11)', 
	 order = {'QED':2} ) 
 
GC_170 = Coupling(name = 'GC_170',
	 value = '1./2.*complex(0,1)*g1*g2*ZH31*complexconjugate(ZP21)*complexconjugate(ZZ11) + 1./2.*complex(0,1)*g1*g2*ZH32*complexconjugate(ZP22)*complexconjugate(ZZ11)', 
	 order = {'QED':2} ) 
 
GC_171 = Coupling(name = 'GC_171',
	 value = '1./2.*complex(0,1)*g1*g2*ZH11*complexconjugate(ZP11)*complexconjugate(ZZ12) + 1./2.*complex(0,1)*g1*g2*ZH12*complexconjugate(ZP12)*complexconjugate(ZZ12)', 
	 order = {'QED':2} ) 
 
GC_172 = Coupling(name = 'GC_172',
	 value = '1./2.*complex(0,1)*g1*g2*ZH11*complexconjugate(ZP21)*complexconjugate(ZZ12) + 1./2.*complex(0,1)*g1*g2*ZH12*complexconjugate(ZP22)*complexconjugate(ZZ12)', 
	 order = {'QED':2} ) 
 
GC_173 = Coupling(name = 'GC_173',
	 value = '1./2.*complex(0,1)*g1*g2*ZH21*complexconjugate(ZP11)*complexconjugate(ZZ12) + 1./2.*complex(0,1)*g1*g2*ZH22*complexconjugate(ZP12)*complexconjugate(ZZ12)', 
	 order = {'QED':2} ) 
 
GC_174 = Coupling(name = 'GC_174',
	 value = '1./2.*complex(0,1)*g1*g2*ZH21*complexconjugate(ZP21)*complexconjugate(ZZ12) + 1./2.*complex(0,1)*g1*g2*ZH22*complexconjugate(ZP22)*complexconjugate(ZZ12)', 
	 order = {'QED':2} ) 
 
GC_175 = Coupling(name = 'GC_175',
	 value = '1./2.*complex(0,1)*g1*g2*ZH31*complexconjugate(ZP11)*complexconjugate(ZZ12) + 1./2.*complex(0,1)*g1*g2*ZH32*complexconjugate(ZP12)*complexconjugate(ZZ12)', 
	 order = {'QED':2} ) 
 
GC_176 = Coupling(name = 'GC_176',
	 value = '1./2.*complex(0,1)*g1*g2*ZH31*complexconjugate(ZP21)*complexconjugate(ZZ12) + 1./2.*complex(0,1)*g1*g2*ZH32*complexconjugate(ZP22)*complexconjugate(ZZ12)', 
	 order = {'QED':2} ) 
 
GC_177 = Coupling(name = 'GC_177',
	 value = '1./2.*complex(0,1)*g1**2*ZP11*complexconjugate(ZP11)*complexconjugate(ZZ11)**2 + 1./2.*complex(0,1)*g1**2*ZP12*complexconjugate(ZP12)*complexconjugate(ZZ11)**2 + 1*complex(0,1)*g1*g2*ZP11*complexconjugate(ZP11)*complexconjugate(ZZ11)*complexconjugate(ZZ21) + 1*complex(0,1)*g1*g2*ZP12*complexconjugate(ZP12)*complexconjugate(ZZ11)*complexconjugate(ZZ21) + 1./2.*complex(0,1)*g2**2*ZP11*complexconjugate(ZP11)*complexconjugate(ZZ21)**2 + 1./2.*complex(0,1)*g2**2*ZP12*complexconjugate(ZP12)*complexconjugate(ZZ21)**2', 
	 order = {'QED':2} ) 
 
GC_178 = Coupling(name = 'GC_178',
	 value = '1./2.*complex(0,1)*g1**2*ZP11*complexconjugate(ZP21)*complexconjugate(ZZ11)**2 + 1./2.*complex(0,1)*g1**2*ZP12*complexconjugate(ZP22)*complexconjugate(ZZ11)**2 + 1*complex(0,1)*g1*g2*ZP11*complexconjugate(ZP21)*complexconjugate(ZZ11)*complexconjugate(ZZ21) + 1*complex(0,1)*g1*g2*ZP12*complexconjugate(ZP22)*complexconjugate(ZZ11)*complexconjugate(ZZ21) + 1./2.*complex(0,1)*g2**2*ZP11*complexconjugate(ZP21)*complexconjugate(ZZ21)**2 + 1./2.*complex(0,1)*g2**2*ZP12*complexconjugate(ZP22)*complexconjugate(ZZ21)**2', 
	 order = {'QED':2} ) 
 
GC_179 = Coupling(name = 'GC_179',
	 value = '1./2.*complex(0,1)*g1**2*ZP21*complexconjugate(ZP11)*complexconjugate(ZZ11)**2 + 1./2.*complex(0,1)*g1**2*ZP22*complexconjugate(ZP12)*complexconjugate(ZZ11)**2 + 1*complex(0,1)*g1*g2*ZP21*complexconjugate(ZP11)*complexconjugate(ZZ11)*complexconjugate(ZZ21) + 1*complex(0,1)*g1*g2*ZP22*complexconjugate(ZP12)*complexconjugate(ZZ11)*complexconjugate(ZZ21) + 1./2.*complex(0,1)*g2**2*ZP21*complexconjugate(ZP11)*complexconjugate(ZZ21)**2 + 1./2.*complex(0,1)*g2**2*ZP22*complexconjugate(ZP12)*complexconjugate(ZZ21)**2', 
	 order = {'QED':2} ) 
 
GC_180 = Coupling(name = 'GC_180',
	 value = '1./2.*complex(0,1)*g1**2*ZP21*complexconjugate(ZP21)*complexconjugate(ZZ11)**2 + 1./2.*complex(0,1)*g1**2*ZP22*complexconjugate(ZP22)*complexconjugate(ZZ11)**2 + 1*complex(0,1)*g1*g2*ZP21*complexconjugate(ZP21)*complexconjugate(ZZ11)*complexconjugate(ZZ21) + 1*complex(0,1)*g1*g2*ZP22*complexconjugate(ZP22)*complexconjugate(ZZ11)*complexconjugate(ZZ21) + 1./2.*complex(0,1)*g2**2*ZP21*complexconjugate(ZP21)*complexconjugate(ZZ21)**2 + 1./2.*complex(0,1)*g2**2*ZP22*complexconjugate(ZP22)*complexconjugate(ZZ21)**2', 
	 order = {'QED':2} ) 
 
GC_181 = Coupling(name = 'GC_181',
	 value = '1./2.*complex(0,1)*g1**2*ZP11*complexconjugate(ZP11)*complexconjugate(ZZ11)*complexconjugate(ZZ12) + 1./2.*complex(0,1)*g1**2*ZP12*complexconjugate(ZP12)*complexconjugate(ZZ11)*complexconjugate(ZZ12) + 1./2.*complex(0,1)*g1*g2*ZP11*complexconjugate(ZP11)*complexconjugate(ZZ12)*complexconjugate(ZZ21) + 1./2.*complex(0,1)*g1*g2*ZP12*complexconjugate(ZP12)*complexconjugate(ZZ12)*complexconjugate(ZZ21) + 1./2.*complex(0,1)*g1*g2*ZP11*complexconjugate(ZP11)*complexconjugate(ZZ11)*complexconjugate(ZZ22) + 1./2.*complex(0,1)*g1*g2*ZP12*complexconjugate(ZP12)*complexconjugate(ZZ11)*complexconjugate(ZZ22) + 1./2.*complex(0,1)*g2**2*ZP11*complexconjugate(ZP11)*complexconjugate(ZZ21)*complexconjugate(ZZ22) + 1./2.*complex(0,1)*g2**2*ZP12*complexconjugate(ZP12)*complexconjugate(ZZ21)*complexconjugate(ZZ22)', 
	 order = {'QED':2} ) 
 
GC_182 = Coupling(name = 'GC_182',
	 value = '1./2.*complex(0,1)*g1**2*ZP11*complexconjugate(ZP21)*complexconjugate(ZZ11)*complexconjugate(ZZ12) + 1./2.*complex(0,1)*g1**2*ZP12*complexconjugate(ZP22)*complexconjugate(ZZ11)*complexconjugate(ZZ12) + 1./2.*complex(0,1)*g1*g2*ZP11*complexconjugate(ZP21)*complexconjugate(ZZ12)*complexconjugate(ZZ21) + 1./2.*complex(0,1)*g1*g2*ZP12*complexconjugate(ZP22)*complexconjugate(ZZ12)*complexconjugate(ZZ21) + 1./2.*complex(0,1)*g1*g2*ZP11*complexconjugate(ZP21)*complexconjugate(ZZ11)*complexconjugate(ZZ22) + 1./2.*complex(0,1)*g1*g2*ZP12*complexconjugate(ZP22)*complexconjugate(ZZ11)*complexconjugate(ZZ22) + 1./2.*complex(0,1)*g2**2*ZP11*complexconjugate(ZP21)*complexconjugate(ZZ21)*complexconjugate(ZZ22) + 1./2.*complex(0,1)*g2**2*ZP12*complexconjugate(ZP22)*complexconjugate(ZZ21)*complexconjugate(ZZ22)', 
	 order = {'QED':2} ) 
 
GC_183 = Coupling(name = 'GC_183',
	 value = '1./2.*complex(0,1)*g1**2*ZP21*complexconjugate(ZP11)*complexconjugate(ZZ11)*complexconjugate(ZZ12) + 1./2.*complex(0,1)*g1**2*ZP22*complexconjugate(ZP12)*complexconjugate(ZZ11)*complexconjugate(ZZ12) + 1./2.*complex(0,1)*g1*g2*ZP21*complexconjugate(ZP11)*complexconjugate(ZZ12)*complexconjugate(ZZ21) + 1./2.*complex(0,1)*g1*g2*ZP22*complexconjugate(ZP12)*complexconjugate(ZZ12)*complexconjugate(ZZ21) + 1./2.*complex(0,1)*g1*g2*ZP21*complexconjugate(ZP11)*complexconjugate(ZZ11)*complexconjugate(ZZ22) + 1./2.*complex(0,1)*g1*g2*ZP22*complexconjugate(ZP12)*complexconjugate(ZZ11)*complexconjugate(ZZ22) + 1./2.*complex(0,1)*g2**2*ZP21*complexconjugate(ZP11)*complexconjugate(ZZ21)*complexconjugate(ZZ22) + 1./2.*complex(0,1)*g2**2*ZP22*complexconjugate(ZP12)*complexconjugate(ZZ21)*complexconjugate(ZZ22)', 
	 order = {'QED':2} ) 
 
GC_184 = Coupling(name = 'GC_184',
	 value = '1./2.*complex(0,1)*g1**2*ZP21*complexconjugate(ZP21)*complexconjugate(ZZ11)*complexconjugate(ZZ12) + 1./2.*complex(0,1)*g1**2*ZP22*complexconjugate(ZP22)*complexconjugate(ZZ11)*complexconjugate(ZZ12) + 1./2.*complex(0,1)*g1*g2*ZP21*complexconjugate(ZP21)*complexconjugate(ZZ12)*complexconjugate(ZZ21) + 1./2.*complex(0,1)*g1*g2*ZP22*complexconjugate(ZP22)*complexconjugate(ZZ12)*complexconjugate(ZZ21) + 1./2.*complex(0,1)*g1*g2*ZP21*complexconjugate(ZP21)*complexconjugate(ZZ11)*complexconjugate(ZZ22) + 1./2.*complex(0,1)*g1*g2*ZP22*complexconjugate(ZP22)*complexconjugate(ZZ11)*complexconjugate(ZZ22) + 1./2.*complex(0,1)*g2**2*ZP21*complexconjugate(ZP21)*complexconjugate(ZZ21)*complexconjugate(ZZ22) + 1./2.*complex(0,1)*g2**2*ZP22*complexconjugate(ZP22)*complexconjugate(ZZ21)*complexconjugate(ZZ22)', 
	 order = {'QED':2} ) 
 
GC_185 = Coupling(name = 'GC_185',
	 value = '1./2.*complex(0,1)*g2**2*ZP11*complexconjugate(ZP11) + 1./2.*complex(0,1)*g2**2*ZP12*complexconjugate(ZP12)', 
	 order = {'QED':2} ) 
 
GC_186 = Coupling(name = 'GC_186',
	 value = '1./2.*complex(0,1)*g2**2*ZP11*complexconjugate(ZP21) + 1./2.*complex(0,1)*g2**2*ZP12*complexconjugate(ZP22)', 
	 order = {'QED':2} ) 
 
GC_187 = Coupling(name = 'GC_187',
	 value = '1./2.*complex(0,1)*g2**2*ZP21*complexconjugate(ZP11) + 1./2.*complex(0,1)*g2**2*ZP22*complexconjugate(ZP12)', 
	 order = {'QED':2} ) 
 
GC_188 = Coupling(name = 'GC_188',
	 value = '1./2.*complex(0,1)*g2**2*ZP21*complexconjugate(ZP21) + 1./2.*complex(0,1)*g2**2*ZP22*complexconjugate(ZP22)', 
	 order = {'QED':2} ) 
 
GC_189 = Coupling(name = 'GC_189',
	 value = '1./2.*complex(0,1)*g1**2*ZP11*complexconjugate(ZP11)*complexconjugate(ZZ12)**2 + 1./2.*complex(0,1)*g1**2*ZP12*complexconjugate(ZP12)*complexconjugate(ZZ12)**2 + 1*complex(0,1)*g1*g2*ZP11*complexconjugate(ZP11)*complexconjugate(ZZ12)*complexconjugate(ZZ22) + 1*complex(0,1)*g1*g2*ZP12*complexconjugate(ZP12)*complexconjugate(ZZ12)*complexconjugate(ZZ22) + 1./2.*complex(0,1)*g2**2*ZP11*complexconjugate(ZP11)*complexconjugate(ZZ22)**2 + 1./2.*complex(0,1)*g2**2*ZP12*complexconjugate(ZP12)*complexconjugate(ZZ22)**2', 
	 order = {'QED':2} ) 
 
GC_190 = Coupling(name = 'GC_190',
	 value = '1./2.*complex(0,1)*g1**2*ZP11*complexconjugate(ZP21)*complexconjugate(ZZ12)**2 + 1./2.*complex(0,1)*g1**2*ZP12*complexconjugate(ZP22)*complexconjugate(ZZ12)**2 + 1*complex(0,1)*g1*g2*ZP11*complexconjugate(ZP21)*complexconjugate(ZZ12)*complexconjugate(ZZ22) + 1*complex(0,1)*g1*g2*ZP12*complexconjugate(ZP22)*complexconjugate(ZZ12)*complexconjugate(ZZ22) + 1./2.*complex(0,1)*g2**2*ZP11*complexconjugate(ZP21)*complexconjugate(ZZ22)**2 + 1./2.*complex(0,1)*g2**2*ZP12*complexconjugate(ZP22)*complexconjugate(ZZ22)**2', 
	 order = {'QED':2} ) 
 
GC_191 = Coupling(name = 'GC_191',
	 value = '1./2.*complex(0,1)*g1**2*ZP21*complexconjugate(ZP11)*complexconjugate(ZZ12)**2 + 1./2.*complex(0,1)*g1**2*ZP22*complexconjugate(ZP12)*complexconjugate(ZZ12)**2 + 1*complex(0,1)*g1*g2*ZP21*complexconjugate(ZP11)*complexconjugate(ZZ12)*complexconjugate(ZZ22) + 1*complex(0,1)*g1*g2*ZP22*complexconjugate(ZP12)*complexconjugate(ZZ12)*complexconjugate(ZZ22) + 1./2.*complex(0,1)*g2**2*ZP21*complexconjugate(ZP11)*complexconjugate(ZZ22)**2 + 1./2.*complex(0,1)*g2**2*ZP22*complexconjugate(ZP12)*complexconjugate(ZZ22)**2', 
	 order = {'QED':2} ) 
 
GC_192 = Coupling(name = 'GC_192',
	 value = '1./2.*complex(0,1)*g1**2*ZP21*complexconjugate(ZP21)*complexconjugate(ZZ12)**2 + 1./2.*complex(0,1)*g1**2*ZP22*complexconjugate(ZP22)*complexconjugate(ZZ12)**2 + 1*complex(0,1)*g1*g2*ZP21*complexconjugate(ZP21)*complexconjugate(ZZ12)*complexconjugate(ZZ22) + 1*complex(0,1)*g1*g2*ZP22*complexconjugate(ZP22)*complexconjugate(ZZ12)*complexconjugate(ZZ22) + 1./2.*complex(0,1)*g2**2*ZP21*complexconjugate(ZP21)*complexconjugate(ZZ22)**2 + 1./2.*complex(0,1)*g2**2*ZP22*complexconjugate(ZP22)*complexconjugate(ZZ22)**2', 
	 order = {'QED':2} ) 
 
GC_193 = Coupling(name = 'GC_193',
	 value = '-((ZA11*ZH11 + ZA12*ZH12)*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21)))/2.', 
	 order = {'QED':1} ) 
 
GC_194 = Coupling(name = 'GC_194',
	 value = '-((ZA11*ZH21 + ZA12*ZH22)*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21)))/2.', 
	 order = {'QED':1} ) 
 
GC_195 = Coupling(name = 'GC_195',
	 value = '-((ZA11*ZH31 + ZA12*ZH32)*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21)))/2.', 
	 order = {'QED':1} ) 
 
GC_196 = Coupling(name = 'GC_196',
	 value = '-((ZA21*ZH11 + ZA22*ZH12)*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21)))/2.', 
	 order = {'QED':1} ) 
 
GC_197 = Coupling(name = 'GC_197',
	 value = '-((ZA21*ZH21 + ZA22*ZH22)*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21)))/2.', 
	 order = {'QED':1} ) 
 
GC_198 = Coupling(name = 'GC_198',
	 value = '-((ZA21*ZH31 + ZA22*ZH32)*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21)))/2.', 
	 order = {'QED':1} ) 
 
GC_199 = Coupling(name = 'GC_199',
	 value = '-((ZA31*ZH11 + ZA32*ZH12)*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21)))/2.', 
	 order = {'QED':1} ) 
 
GC_200 = Coupling(name = 'GC_200',
	 value = '-((ZA31*ZH21 + ZA32*ZH22)*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21)))/2.', 
	 order = {'QED':1} ) 
 
GC_201 = Coupling(name = 'GC_201',
	 value = '-((ZA31*ZH31 + ZA32*ZH32)*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21)))/2.', 
	 order = {'QED':1} ) 
 
GC_202 = Coupling(name = 'GC_202',
	 value = '-((ZA11*ZH11 + ZA12*ZH12)*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22)))/2.', 
	 order = {'QED':1} ) 
 
GC_203 = Coupling(name = 'GC_203',
	 value = '-((ZA11*ZH21 + ZA12*ZH22)*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22)))/2.', 
	 order = {'QED':1} ) 
 
GC_204 = Coupling(name = 'GC_204',
	 value = '-((ZA11*ZH31 + ZA12*ZH32)*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22)))/2.', 
	 order = {'QED':1} ) 
 
GC_205 = Coupling(name = 'GC_205',
	 value = '-((ZA21*ZH11 + ZA22*ZH12)*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22)))/2.', 
	 order = {'QED':1} ) 
 
GC_206 = Coupling(name = 'GC_206',
	 value = '-((ZA21*ZH21 + ZA22*ZH22)*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22)))/2.', 
	 order = {'QED':1} ) 
 
GC_207 = Coupling(name = 'GC_207',
	 value = '-((ZA21*ZH31 + ZA22*ZH32)*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22)))/2.', 
	 order = {'QED':1} ) 
 
GC_208 = Coupling(name = 'GC_208',
	 value = '-((ZA31*ZH11 + ZA32*ZH12)*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22)))/2.', 
	 order = {'QED':1} ) 
 
GC_209 = Coupling(name = 'GC_209',
	 value = '-((ZA31*ZH21 + ZA32*ZH22)*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22)))/2.', 
	 order = {'QED':1} ) 
 
GC_210 = Coupling(name = 'GC_210',
	 value = '-((ZA31*ZH31 + ZA32*ZH32)*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22)))/2.', 
	 order = {'QED':1} ) 
 
GC_211 = Coupling(name = 'GC_211',
	 value = '-(g2*(ZA11*ZP11 + ZA12*ZP12))/2.', 
	 order = {'QED':1} ) 
 
GC_212 = Coupling(name = 'GC_212',
	 value = '-(g2*(ZA11*ZP21 + ZA12*ZP22))/2.', 
	 order = {'QED':1} ) 
 
GC_213 = Coupling(name = 'GC_213',
	 value = '-(g2*(ZA21*ZP11 + ZA22*ZP12))/2.', 
	 order = {'QED':1} ) 
 
GC_214 = Coupling(name = 'GC_214',
	 value = '-(g2*(ZA21*ZP21 + ZA22*ZP22))/2.', 
	 order = {'QED':1} ) 
 
GC_215 = Coupling(name = 'GC_215',
	 value = '-(g2*(ZA31*ZP11 + ZA32*ZP12))/2.', 
	 order = {'QED':1} ) 
 
GC_216 = Coupling(name = 'GC_216',
	 value = '-(g2*(ZA31*ZP21 + ZA32*ZP22))/2.', 
	 order = {'QED':1} ) 
 
GC_217 = Coupling(name = 'GC_217',
	 value = '-(g2*(ZA11*complexconjugate(ZP11) + ZA12*complexconjugate(ZP12)))/2.', 
	 order = {'QED':1} ) 
 
GC_218 = Coupling(name = 'GC_218',
	 value = '-(g2*(ZA11*complexconjugate(ZP21) + ZA12*complexconjugate(ZP22)))/2.', 
	 order = {'QED':1} ) 
 
GC_219 = Coupling(name = 'GC_219',
	 value = '-(g2*(ZA21*complexconjugate(ZP11) + ZA22*complexconjugate(ZP12)))/2.', 
	 order = {'QED':1} ) 
 
GC_220 = Coupling(name = 'GC_220',
	 value = '-(g2*(ZA21*complexconjugate(ZP21) + ZA22*complexconjugate(ZP22)))/2.', 
	 order = {'QED':1} ) 
 
GC_221 = Coupling(name = 'GC_221',
	 value = '-(g2*(ZA31*complexconjugate(ZP11) + ZA32*complexconjugate(ZP12)))/2.', 
	 order = {'QED':1} ) 
 
GC_222 = Coupling(name = 'GC_222',
	 value = '-(g2*(ZA31*complexconjugate(ZP21) + ZA32*complexconjugate(ZP22)))/2.', 
	 order = {'QED':1} ) 
 
GC_223 = Coupling(name = 'GC_223',
	 value = '1./2.*complex(0,1)*g2*(ZH11*ZP11 + ZH12*ZP12)', 
	 order = {'QED':1} ) 
 
GC_224 = Coupling(name = 'GC_224',
	 value = '1./2.*complex(0,1)*g2*(ZH11*ZP21 + ZH12*ZP22)', 
	 order = {'QED':1} ) 
 
GC_225 = Coupling(name = 'GC_225',
	 value = '1./2.*complex(0,1)*g2*(ZH21*ZP11 + ZH22*ZP12)', 
	 order = {'QED':1} ) 
 
GC_226 = Coupling(name = 'GC_226',
	 value = '1./2.*complex(0,1)*g2*(ZH21*ZP21 + ZH22*ZP22)', 
	 order = {'QED':1} ) 
 
GC_227 = Coupling(name = 'GC_227',
	 value = '1./2.*complex(0,1)*g2*(ZH31*ZP11 + ZH32*ZP12)', 
	 order = {'QED':1} ) 
 
GC_228 = Coupling(name = 'GC_228',
	 value = '1./2.*complex(0,1)*g2*(ZH31*ZP21 + ZH32*ZP22)', 
	 order = {'QED':1} ) 
 
GC_229 = Coupling(name = 'GC_229',
	 value = '-1./2.*complex(0,1)*g2*(ZH11*complexconjugate(ZP11) + ZH12*complexconjugate(ZP12))', 
	 order = {'QED':1} ) 
 
GC_230 = Coupling(name = 'GC_230',
	 value = '-1./2.*complex(0,1)*g2*(ZH11*complexconjugate(ZP21) + ZH12*complexconjugate(ZP22))', 
	 order = {'QED':1} ) 
 
GC_231 = Coupling(name = 'GC_231',
	 value = '-1./2.*complex(0,1)*g2*(ZH21*complexconjugate(ZP11) + ZH22*complexconjugate(ZP12))', 
	 order = {'QED':1} ) 
 
GC_232 = Coupling(name = 'GC_232',
	 value = '-1./2.*complex(0,1)*g2*(ZH21*complexconjugate(ZP21) + ZH22*complexconjugate(ZP22))', 
	 order = {'QED':1} ) 
 
GC_233 = Coupling(name = 'GC_233',
	 value = '-1./2.*complex(0,1)*g2*(ZH31*complexconjugate(ZP11) + ZH32*complexconjugate(ZP12))', 
	 order = {'QED':1} ) 
 
GC_234 = Coupling(name = 'GC_234',
	 value = '-1./2.*complex(0,1)*g2*(ZH31*complexconjugate(ZP21) + ZH32*complexconjugate(ZP22))', 
	 order = {'QED':1} ) 
 
GC_235 = Coupling(name = 'GC_235',
	 value = '-1./2.*complex(0,1)*(g1*complexconjugate(ZZ11) + g2*complexconjugate(ZZ21))', 
	 order = {'QED':1} ) 
 
GC_236 = Coupling(name = 'GC_236',
	 value = '-1./2.*complex(0,1)*(g1*complexconjugate(ZZ11) + g2*complexconjugate(ZZ21))', 
	 order = {'QED':1} ) 
 
GC_237 = Coupling(name = 'GC_237',
	 value = '-1./2.*complex(0,1)*(g1*complexconjugate(ZZ12) + g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_238 = Coupling(name = 'GC_238',
	 value = '-1./2.*complex(0,1)*(g1*complexconjugate(ZZ12) + g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_239 = Coupling(name = 'GC_239',
	 value = '1./2.*complex(0,1)*(v1*ZH11 + v2*ZH12)*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21))*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_240 = Coupling(name = 'GC_240',
	 value = '1./2.*complex(0,1)*(v1*ZH21 + v2*ZH22)*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21))*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_241 = Coupling(name = 'GC_241',
	 value = '1./2.*complex(0,1)*(v1*ZH31 + v2*ZH32)*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21))*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_242 = Coupling(name = 'GC_242',
	 value = '1./2.*complex(0,1)*g2**2*(v1*ZH11 + v2*ZH12)', 
	 order = {'QED':1} ) 
 
GC_243 = Coupling(name = 'GC_243',
	 value = '1./2.*complex(0,1)*g2**2*(v1*ZH21 + v2*ZH22)', 
	 order = {'QED':1} ) 
 
GC_244 = Coupling(name = 'GC_244',
	 value = '1./2.*complex(0,1)*g2**2*(v1*ZH31 + v2*ZH32)', 
	 order = {'QED':1} ) 
 
GC_245 = Coupling(name = 'GC_245',
	 value = '1./2.*complex(0,1)*(v1*ZH11 + v2*ZH12)*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22))**2', 
	 order = {'QED':1} ) 
 
GC_246 = Coupling(name = 'GC_246',
	 value = '1./2.*complex(0,1)*(v1*ZH21 + v2*ZH22)*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22))**2', 
	 order = {'QED':1} ) 
 
GC_247 = Coupling(name = 'GC_247',
	 value = '1./2.*complex(0,1)*(v1*ZH31 + v2*ZH32)*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22))**2', 
	 order = {'QED':1} ) 
 
GC_248 = Coupling(name = 'GC_248',
	 value = '1./2.*complex(0,1)*g1*g2*(v1*ZP11 + v2*ZP12)*complexconjugate(ZZ11)', 
	 order = {'QED':1} ) 
 
GC_249 = Coupling(name = 'GC_249',
	 value = '1./2.*complex(0,1)*g1*g2*(v1*ZP21 + v2*ZP22)*complexconjugate(ZZ11)', 
	 order = {'QED':1} ) 
 
GC_250 = Coupling(name = 'GC_250',
	 value = '1./2.*complex(0,1)*g1*g2*(v1*ZP11 + v2*ZP12)*complexconjugate(ZZ12)', 
	 order = {'QED':1} ) 
 
GC_251 = Coupling(name = 'GC_251',
	 value = '1./2.*complex(0,1)*g1*g2*(v1*ZP21 + v2*ZP22)*complexconjugate(ZZ12)', 
	 order = {'QED':1} ) 
 
GC_252 = Coupling(name = 'GC_252',
	 value = '1./2.*complex(0,1)*g1*g2*(v1*complexconjugate(ZP11) + v2*complexconjugate(ZP12))*complexconjugate(ZZ11)', 
	 order = {'QED':1} ) 
 
GC_253 = Coupling(name = 'GC_253',
	 value = '1./2.*complex(0,1)*g1*g2*(v1*complexconjugate(ZP21) + v2*complexconjugate(ZP22))*complexconjugate(ZZ11)', 
	 order = {'QED':1} ) 
 
GC_254 = Coupling(name = 'GC_254',
	 value = '1./2.*complex(0,1)*g1*g2*(v1*complexconjugate(ZP11) + v2*complexconjugate(ZP12))*complexconjugate(ZZ12)', 
	 order = {'QED':1} ) 
 
GC_255 = Coupling(name = 'GC_255',
	 value = '1./2.*complex(0,1)*g1*g2*(v1*complexconjugate(ZP21) + v2*complexconjugate(ZP22))*complexconjugate(ZZ12)', 
	 order = {'QED':1} ) 
 
GC_256 = Coupling(name = 'GC_256',
	 value = '-((ZDR11*(ZA11*ZDL11*complexconjugate(Y1d11) + ZA11*ZDL12*complexconjugate(Y1d21) + ZA12*ZDL13*complexconjugate(Y2d31)) + ZDR12*(ZA11*ZDL11*complexconjugate(Y1d12) + ZA11*ZDL12*complexconjugate(Y1d22) + ZA12*ZDL13*complexconjugate(Y2d32)) + ZDR13*(ZA11*ZDL11*complexconjugate(Y1d13) + ZA11*ZDL12*complexconjugate(Y1d23) + ZA12*ZDL13*complexconjugate(Y2d33)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_257 = Coupling(name = 'GC_257',
	 value = '(Y1d11*ZA11*complexconjugate(ZDL11)*complexconjugate(ZDR11) + Y1d21*ZA11*complexconjugate(ZDL12)*complexconjugate(ZDR11) + Y2d31*ZA12*complexconjugate(ZDL13)*complexconjugate(ZDR11) + Y1d12*ZA11*complexconjugate(ZDL11)*complexconjugate(ZDR12) + Y1d22*ZA11*complexconjugate(ZDL12)*complexconjugate(ZDR12) + Y2d32*ZA12*complexconjugate(ZDL13)*complexconjugate(ZDR12) + Y1d13*ZA11*complexconjugate(ZDL11)*complexconjugate(ZDR13) + Y1d23*ZA11*complexconjugate(ZDL12)*complexconjugate(ZDR13) + Y2d33*ZA12*complexconjugate(ZDL13)*complexconjugate(ZDR13))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_258 = Coupling(name = 'GC_258',
	 value = '-((ZDR11*(ZA21*ZDL11*complexconjugate(Y1d11) + ZA21*ZDL12*complexconjugate(Y1d21) + ZA22*ZDL13*complexconjugate(Y2d31)) + ZDR12*(ZA21*ZDL11*complexconjugate(Y1d12) + ZA21*ZDL12*complexconjugate(Y1d22) + ZA22*ZDL13*complexconjugate(Y2d32)) + ZDR13*(ZA21*ZDL11*complexconjugate(Y1d13) + ZA21*ZDL12*complexconjugate(Y1d23) + ZA22*ZDL13*complexconjugate(Y2d33)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_259 = Coupling(name = 'GC_259',
	 value = '(Y1d11*ZA21*complexconjugate(ZDL11)*complexconjugate(ZDR11) + Y1d21*ZA21*complexconjugate(ZDL12)*complexconjugate(ZDR11) + Y2d31*ZA22*complexconjugate(ZDL13)*complexconjugate(ZDR11) + Y1d12*ZA21*complexconjugate(ZDL11)*complexconjugate(ZDR12) + Y1d22*ZA21*complexconjugate(ZDL12)*complexconjugate(ZDR12) + Y2d32*ZA22*complexconjugate(ZDL13)*complexconjugate(ZDR12) + Y1d13*ZA21*complexconjugate(ZDL11)*complexconjugate(ZDR13) + Y1d23*ZA21*complexconjugate(ZDL12)*complexconjugate(ZDR13) + Y2d33*ZA22*complexconjugate(ZDL13)*complexconjugate(ZDR13))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_260 = Coupling(name = 'GC_260',
	 value = '-((ZDR11*(ZA31*ZDL11*complexconjugate(Y1d11) + ZA31*ZDL12*complexconjugate(Y1d21) + ZA32*ZDL13*complexconjugate(Y2d31)) + ZDR12*(ZA31*ZDL11*complexconjugate(Y1d12) + ZA31*ZDL12*complexconjugate(Y1d22) + ZA32*ZDL13*complexconjugate(Y2d32)) + ZDR13*(ZA31*ZDL11*complexconjugate(Y1d13) + ZA31*ZDL12*complexconjugate(Y1d23) + ZA32*ZDL13*complexconjugate(Y2d33)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_261 = Coupling(name = 'GC_261',
	 value = '(Y1d11*ZA31*complexconjugate(ZDL11)*complexconjugate(ZDR11) + Y1d21*ZA31*complexconjugate(ZDL12)*complexconjugate(ZDR11) + Y2d31*ZA32*complexconjugate(ZDL13)*complexconjugate(ZDR11) + Y1d12*ZA31*complexconjugate(ZDL11)*complexconjugate(ZDR12) + Y1d22*ZA31*complexconjugate(ZDL12)*complexconjugate(ZDR12) + Y2d32*ZA32*complexconjugate(ZDL13)*complexconjugate(ZDR12) + Y1d13*ZA31*complexconjugate(ZDL11)*complexconjugate(ZDR13) + Y1d23*ZA31*complexconjugate(ZDL12)*complexconjugate(ZDR13) + Y2d33*ZA32*complexconjugate(ZDL13)*complexconjugate(ZDR13))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_262 = Coupling(name = 'GC_262',
	 value = '-((ZDR11*(ZA11*ZDL21*complexconjugate(Y1d11) + ZA11*ZDL22*complexconjugate(Y1d21) + ZA12*ZDL23*complexconjugate(Y2d31)) + ZDR12*(ZA11*ZDL21*complexconjugate(Y1d12) + ZA11*ZDL22*complexconjugate(Y1d22) + ZA12*ZDL23*complexconjugate(Y2d32)) + ZDR13*(ZA11*ZDL21*complexconjugate(Y1d13) + ZA11*ZDL22*complexconjugate(Y1d23) + ZA12*ZDL23*complexconjugate(Y2d33)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_263 = Coupling(name = 'GC_263',
	 value = '(Y1d11*ZA11*complexconjugate(ZDL11)*complexconjugate(ZDR21) + Y1d21*ZA11*complexconjugate(ZDL12)*complexconjugate(ZDR21) + Y2d31*ZA12*complexconjugate(ZDL13)*complexconjugate(ZDR21) + Y1d12*ZA11*complexconjugate(ZDL11)*complexconjugate(ZDR22) + Y1d22*ZA11*complexconjugate(ZDL12)*complexconjugate(ZDR22) + Y2d32*ZA12*complexconjugate(ZDL13)*complexconjugate(ZDR22) + Y1d13*ZA11*complexconjugate(ZDL11)*complexconjugate(ZDR23) + Y1d23*ZA11*complexconjugate(ZDL12)*complexconjugate(ZDR23) + Y2d33*ZA12*complexconjugate(ZDL13)*complexconjugate(ZDR23))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_264 = Coupling(name = 'GC_264',
	 value = '-((ZDR11*(ZA21*ZDL21*complexconjugate(Y1d11) + ZA21*ZDL22*complexconjugate(Y1d21) + ZA22*ZDL23*complexconjugate(Y2d31)) + ZDR12*(ZA21*ZDL21*complexconjugate(Y1d12) + ZA21*ZDL22*complexconjugate(Y1d22) + ZA22*ZDL23*complexconjugate(Y2d32)) + ZDR13*(ZA21*ZDL21*complexconjugate(Y1d13) + ZA21*ZDL22*complexconjugate(Y1d23) + ZA22*ZDL23*complexconjugate(Y2d33)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_265 = Coupling(name = 'GC_265',
	 value = '(Y1d11*ZA21*complexconjugate(ZDL11)*complexconjugate(ZDR21) + Y1d21*ZA21*complexconjugate(ZDL12)*complexconjugate(ZDR21) + Y2d31*ZA22*complexconjugate(ZDL13)*complexconjugate(ZDR21) + Y1d12*ZA21*complexconjugate(ZDL11)*complexconjugate(ZDR22) + Y1d22*ZA21*complexconjugate(ZDL12)*complexconjugate(ZDR22) + Y2d32*ZA22*complexconjugate(ZDL13)*complexconjugate(ZDR22) + Y1d13*ZA21*complexconjugate(ZDL11)*complexconjugate(ZDR23) + Y1d23*ZA21*complexconjugate(ZDL12)*complexconjugate(ZDR23) + Y2d33*ZA22*complexconjugate(ZDL13)*complexconjugate(ZDR23))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_266 = Coupling(name = 'GC_266',
	 value = '-((ZDR11*(ZA31*ZDL21*complexconjugate(Y1d11) + ZA31*ZDL22*complexconjugate(Y1d21) + ZA32*ZDL23*complexconjugate(Y2d31)) + ZDR12*(ZA31*ZDL21*complexconjugate(Y1d12) + ZA31*ZDL22*complexconjugate(Y1d22) + ZA32*ZDL23*complexconjugate(Y2d32)) + ZDR13*(ZA31*ZDL21*complexconjugate(Y1d13) + ZA31*ZDL22*complexconjugate(Y1d23) + ZA32*ZDL23*complexconjugate(Y2d33)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_267 = Coupling(name = 'GC_267',
	 value = '(Y1d11*ZA31*complexconjugate(ZDL11)*complexconjugate(ZDR21) + Y1d21*ZA31*complexconjugate(ZDL12)*complexconjugate(ZDR21) + Y2d31*ZA32*complexconjugate(ZDL13)*complexconjugate(ZDR21) + Y1d12*ZA31*complexconjugate(ZDL11)*complexconjugate(ZDR22) + Y1d22*ZA31*complexconjugate(ZDL12)*complexconjugate(ZDR22) + Y2d32*ZA32*complexconjugate(ZDL13)*complexconjugate(ZDR22) + Y1d13*ZA31*complexconjugate(ZDL11)*complexconjugate(ZDR23) + Y1d23*ZA31*complexconjugate(ZDL12)*complexconjugate(ZDR23) + Y2d33*ZA32*complexconjugate(ZDL13)*complexconjugate(ZDR23))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_268 = Coupling(name = 'GC_268',
	 value = '-((ZDR11*(ZA11*ZDL31*complexconjugate(Y1d11) + ZA11*ZDL32*complexconjugate(Y1d21) + ZA12*ZDL33*complexconjugate(Y2d31)) + ZDR12*(ZA11*ZDL31*complexconjugate(Y1d12) + ZA11*ZDL32*complexconjugate(Y1d22) + ZA12*ZDL33*complexconjugate(Y2d32)) + ZDR13*(ZA11*ZDL31*complexconjugate(Y1d13) + ZA11*ZDL32*complexconjugate(Y1d23) + ZA12*ZDL33*complexconjugate(Y2d33)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_269 = Coupling(name = 'GC_269',
	 value = '(Y1d11*ZA11*complexconjugate(ZDL11)*complexconjugate(ZDR31) + Y1d21*ZA11*complexconjugate(ZDL12)*complexconjugate(ZDR31) + Y2d31*ZA12*complexconjugate(ZDL13)*complexconjugate(ZDR31) + Y1d12*ZA11*complexconjugate(ZDL11)*complexconjugate(ZDR32) + Y1d22*ZA11*complexconjugate(ZDL12)*complexconjugate(ZDR32) + Y2d32*ZA12*complexconjugate(ZDL13)*complexconjugate(ZDR32) + Y1d13*ZA11*complexconjugate(ZDL11)*complexconjugate(ZDR33) + Y1d23*ZA11*complexconjugate(ZDL12)*complexconjugate(ZDR33) + Y2d33*ZA12*complexconjugate(ZDL13)*complexconjugate(ZDR33))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_270 = Coupling(name = 'GC_270',
	 value = '-((ZDR11*(ZA21*ZDL31*complexconjugate(Y1d11) + ZA21*ZDL32*complexconjugate(Y1d21) + ZA22*ZDL33*complexconjugate(Y2d31)) + ZDR12*(ZA21*ZDL31*complexconjugate(Y1d12) + ZA21*ZDL32*complexconjugate(Y1d22) + ZA22*ZDL33*complexconjugate(Y2d32)) + ZDR13*(ZA21*ZDL31*complexconjugate(Y1d13) + ZA21*ZDL32*complexconjugate(Y1d23) + ZA22*ZDL33*complexconjugate(Y2d33)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_271 = Coupling(name = 'GC_271',
	 value = '(Y1d11*ZA21*complexconjugate(ZDL11)*complexconjugate(ZDR31) + Y1d21*ZA21*complexconjugate(ZDL12)*complexconjugate(ZDR31) + Y2d31*ZA22*complexconjugate(ZDL13)*complexconjugate(ZDR31) + Y1d12*ZA21*complexconjugate(ZDL11)*complexconjugate(ZDR32) + Y1d22*ZA21*complexconjugate(ZDL12)*complexconjugate(ZDR32) + Y2d32*ZA22*complexconjugate(ZDL13)*complexconjugate(ZDR32) + Y1d13*ZA21*complexconjugate(ZDL11)*complexconjugate(ZDR33) + Y1d23*ZA21*complexconjugate(ZDL12)*complexconjugate(ZDR33) + Y2d33*ZA22*complexconjugate(ZDL13)*complexconjugate(ZDR33))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_272 = Coupling(name = 'GC_272',
	 value = '-((ZDR11*(ZA31*ZDL31*complexconjugate(Y1d11) + ZA31*ZDL32*complexconjugate(Y1d21) + ZA32*ZDL33*complexconjugate(Y2d31)) + ZDR12*(ZA31*ZDL31*complexconjugate(Y1d12) + ZA31*ZDL32*complexconjugate(Y1d22) + ZA32*ZDL33*complexconjugate(Y2d32)) + ZDR13*(ZA31*ZDL31*complexconjugate(Y1d13) + ZA31*ZDL32*complexconjugate(Y1d23) + ZA32*ZDL33*complexconjugate(Y2d33)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_273 = Coupling(name = 'GC_273',
	 value = '(Y1d11*ZA31*complexconjugate(ZDL11)*complexconjugate(ZDR31) + Y1d21*ZA31*complexconjugate(ZDL12)*complexconjugate(ZDR31) + Y2d31*ZA32*complexconjugate(ZDL13)*complexconjugate(ZDR31) + Y1d12*ZA31*complexconjugate(ZDL11)*complexconjugate(ZDR32) + Y1d22*ZA31*complexconjugate(ZDL12)*complexconjugate(ZDR32) + Y2d32*ZA32*complexconjugate(ZDL13)*complexconjugate(ZDR32) + Y1d13*ZA31*complexconjugate(ZDL11)*complexconjugate(ZDR33) + Y1d23*ZA31*complexconjugate(ZDL12)*complexconjugate(ZDR33) + Y2d33*ZA32*complexconjugate(ZDL13)*complexconjugate(ZDR33))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_274 = Coupling(name = 'GC_274',
	 value = '-((ZDR21*(ZA11*ZDL11*complexconjugate(Y1d11) + ZA11*ZDL12*complexconjugate(Y1d21) + ZA12*ZDL13*complexconjugate(Y2d31)) + ZDR22*(ZA11*ZDL11*complexconjugate(Y1d12) + ZA11*ZDL12*complexconjugate(Y1d22) + ZA12*ZDL13*complexconjugate(Y2d32)) + ZDR23*(ZA11*ZDL11*complexconjugate(Y1d13) + ZA11*ZDL12*complexconjugate(Y1d23) + ZA12*ZDL13*complexconjugate(Y2d33)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_275 = Coupling(name = 'GC_275',
	 value = '(Y1d11*ZA11*complexconjugate(ZDL21)*complexconjugate(ZDR11) + Y1d21*ZA11*complexconjugate(ZDL22)*complexconjugate(ZDR11) + Y2d31*ZA12*complexconjugate(ZDL23)*complexconjugate(ZDR11) + Y1d12*ZA11*complexconjugate(ZDL21)*complexconjugate(ZDR12) + Y1d22*ZA11*complexconjugate(ZDL22)*complexconjugate(ZDR12) + Y2d32*ZA12*complexconjugate(ZDL23)*complexconjugate(ZDR12) + Y1d13*ZA11*complexconjugate(ZDL21)*complexconjugate(ZDR13) + Y1d23*ZA11*complexconjugate(ZDL22)*complexconjugate(ZDR13) + Y2d33*ZA12*complexconjugate(ZDL23)*complexconjugate(ZDR13))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_276 = Coupling(name = 'GC_276',
	 value = '-((ZDR21*(ZA21*ZDL11*complexconjugate(Y1d11) + ZA21*ZDL12*complexconjugate(Y1d21) + ZA22*ZDL13*complexconjugate(Y2d31)) + ZDR22*(ZA21*ZDL11*complexconjugate(Y1d12) + ZA21*ZDL12*complexconjugate(Y1d22) + ZA22*ZDL13*complexconjugate(Y2d32)) + ZDR23*(ZA21*ZDL11*complexconjugate(Y1d13) + ZA21*ZDL12*complexconjugate(Y1d23) + ZA22*ZDL13*complexconjugate(Y2d33)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_277 = Coupling(name = 'GC_277',
	 value = '(Y1d11*ZA21*complexconjugate(ZDL21)*complexconjugate(ZDR11) + Y1d21*ZA21*complexconjugate(ZDL22)*complexconjugate(ZDR11) + Y2d31*ZA22*complexconjugate(ZDL23)*complexconjugate(ZDR11) + Y1d12*ZA21*complexconjugate(ZDL21)*complexconjugate(ZDR12) + Y1d22*ZA21*complexconjugate(ZDL22)*complexconjugate(ZDR12) + Y2d32*ZA22*complexconjugate(ZDL23)*complexconjugate(ZDR12) + Y1d13*ZA21*complexconjugate(ZDL21)*complexconjugate(ZDR13) + Y1d23*ZA21*complexconjugate(ZDL22)*complexconjugate(ZDR13) + Y2d33*ZA22*complexconjugate(ZDL23)*complexconjugate(ZDR13))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_278 = Coupling(name = 'GC_278',
	 value = '-((ZDR21*(ZA31*ZDL11*complexconjugate(Y1d11) + ZA31*ZDL12*complexconjugate(Y1d21) + ZA32*ZDL13*complexconjugate(Y2d31)) + ZDR22*(ZA31*ZDL11*complexconjugate(Y1d12) + ZA31*ZDL12*complexconjugate(Y1d22) + ZA32*ZDL13*complexconjugate(Y2d32)) + ZDR23*(ZA31*ZDL11*complexconjugate(Y1d13) + ZA31*ZDL12*complexconjugate(Y1d23) + ZA32*ZDL13*complexconjugate(Y2d33)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_279 = Coupling(name = 'GC_279',
	 value = '(Y1d11*ZA31*complexconjugate(ZDL21)*complexconjugate(ZDR11) + Y1d21*ZA31*complexconjugate(ZDL22)*complexconjugate(ZDR11) + Y2d31*ZA32*complexconjugate(ZDL23)*complexconjugate(ZDR11) + Y1d12*ZA31*complexconjugate(ZDL21)*complexconjugate(ZDR12) + Y1d22*ZA31*complexconjugate(ZDL22)*complexconjugate(ZDR12) + Y2d32*ZA32*complexconjugate(ZDL23)*complexconjugate(ZDR12) + Y1d13*ZA31*complexconjugate(ZDL21)*complexconjugate(ZDR13) + Y1d23*ZA31*complexconjugate(ZDL22)*complexconjugate(ZDR13) + Y2d33*ZA32*complexconjugate(ZDL23)*complexconjugate(ZDR13))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_280 = Coupling(name = 'GC_280',
	 value = '-((ZDR21*(ZA11*ZDL21*complexconjugate(Y1d11) + ZA11*ZDL22*complexconjugate(Y1d21) + ZA12*ZDL23*complexconjugate(Y2d31)) + ZDR22*(ZA11*ZDL21*complexconjugate(Y1d12) + ZA11*ZDL22*complexconjugate(Y1d22) + ZA12*ZDL23*complexconjugate(Y2d32)) + ZDR23*(ZA11*ZDL21*complexconjugate(Y1d13) + ZA11*ZDL22*complexconjugate(Y1d23) + ZA12*ZDL23*complexconjugate(Y2d33)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_281 = Coupling(name = 'GC_281',
	 value = '(Y1d11*ZA11*complexconjugate(ZDL21)*complexconjugate(ZDR21) + Y1d21*ZA11*complexconjugate(ZDL22)*complexconjugate(ZDR21) + Y2d31*ZA12*complexconjugate(ZDL23)*complexconjugate(ZDR21) + Y1d12*ZA11*complexconjugate(ZDL21)*complexconjugate(ZDR22) + Y1d22*ZA11*complexconjugate(ZDL22)*complexconjugate(ZDR22) + Y2d32*ZA12*complexconjugate(ZDL23)*complexconjugate(ZDR22) + Y1d13*ZA11*complexconjugate(ZDL21)*complexconjugate(ZDR23) + Y1d23*ZA11*complexconjugate(ZDL22)*complexconjugate(ZDR23) + Y2d33*ZA12*complexconjugate(ZDL23)*complexconjugate(ZDR23))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_282 = Coupling(name = 'GC_282',
	 value = '-((ZDR21*(ZA21*ZDL21*complexconjugate(Y1d11) + ZA21*ZDL22*complexconjugate(Y1d21) + ZA22*ZDL23*complexconjugate(Y2d31)) + ZDR22*(ZA21*ZDL21*complexconjugate(Y1d12) + ZA21*ZDL22*complexconjugate(Y1d22) + ZA22*ZDL23*complexconjugate(Y2d32)) + ZDR23*(ZA21*ZDL21*complexconjugate(Y1d13) + ZA21*ZDL22*complexconjugate(Y1d23) + ZA22*ZDL23*complexconjugate(Y2d33)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_283 = Coupling(name = 'GC_283',
	 value = '(Y1d11*ZA21*complexconjugate(ZDL21)*complexconjugate(ZDR21) + Y1d21*ZA21*complexconjugate(ZDL22)*complexconjugate(ZDR21) + Y2d31*ZA22*complexconjugate(ZDL23)*complexconjugate(ZDR21) + Y1d12*ZA21*complexconjugate(ZDL21)*complexconjugate(ZDR22) + Y1d22*ZA21*complexconjugate(ZDL22)*complexconjugate(ZDR22) + Y2d32*ZA22*complexconjugate(ZDL23)*complexconjugate(ZDR22) + Y1d13*ZA21*complexconjugate(ZDL21)*complexconjugate(ZDR23) + Y1d23*ZA21*complexconjugate(ZDL22)*complexconjugate(ZDR23) + Y2d33*ZA22*complexconjugate(ZDL23)*complexconjugate(ZDR23))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_284 = Coupling(name = 'GC_284',
	 value = '-((ZDR21*(ZA31*ZDL21*complexconjugate(Y1d11) + ZA31*ZDL22*complexconjugate(Y1d21) + ZA32*ZDL23*complexconjugate(Y2d31)) + ZDR22*(ZA31*ZDL21*complexconjugate(Y1d12) + ZA31*ZDL22*complexconjugate(Y1d22) + ZA32*ZDL23*complexconjugate(Y2d32)) + ZDR23*(ZA31*ZDL21*complexconjugate(Y1d13) + ZA31*ZDL22*complexconjugate(Y1d23) + ZA32*ZDL23*complexconjugate(Y2d33)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_285 = Coupling(name = 'GC_285',
	 value = '(Y1d11*ZA31*complexconjugate(ZDL21)*complexconjugate(ZDR21) + Y1d21*ZA31*complexconjugate(ZDL22)*complexconjugate(ZDR21) + Y2d31*ZA32*complexconjugate(ZDL23)*complexconjugate(ZDR21) + Y1d12*ZA31*complexconjugate(ZDL21)*complexconjugate(ZDR22) + Y1d22*ZA31*complexconjugate(ZDL22)*complexconjugate(ZDR22) + Y2d32*ZA32*complexconjugate(ZDL23)*complexconjugate(ZDR22) + Y1d13*ZA31*complexconjugate(ZDL21)*complexconjugate(ZDR23) + Y1d23*ZA31*complexconjugate(ZDL22)*complexconjugate(ZDR23) + Y2d33*ZA32*complexconjugate(ZDL23)*complexconjugate(ZDR23))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_286 = Coupling(name = 'GC_286',
	 value = '-((ZDR21*(ZA11*ZDL31*complexconjugate(Y1d11) + ZA11*ZDL32*complexconjugate(Y1d21) + ZA12*ZDL33*complexconjugate(Y2d31)) + ZDR22*(ZA11*ZDL31*complexconjugate(Y1d12) + ZA11*ZDL32*complexconjugate(Y1d22) + ZA12*ZDL33*complexconjugate(Y2d32)) + ZDR23*(ZA11*ZDL31*complexconjugate(Y1d13) + ZA11*ZDL32*complexconjugate(Y1d23) + ZA12*ZDL33*complexconjugate(Y2d33)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_287 = Coupling(name = 'GC_287',
	 value = '(Y1d11*ZA11*complexconjugate(ZDL21)*complexconjugate(ZDR31) + Y1d21*ZA11*complexconjugate(ZDL22)*complexconjugate(ZDR31) + Y2d31*ZA12*complexconjugate(ZDL23)*complexconjugate(ZDR31) + Y1d12*ZA11*complexconjugate(ZDL21)*complexconjugate(ZDR32) + Y1d22*ZA11*complexconjugate(ZDL22)*complexconjugate(ZDR32) + Y2d32*ZA12*complexconjugate(ZDL23)*complexconjugate(ZDR32) + Y1d13*ZA11*complexconjugate(ZDL21)*complexconjugate(ZDR33) + Y1d23*ZA11*complexconjugate(ZDL22)*complexconjugate(ZDR33) + Y2d33*ZA12*complexconjugate(ZDL23)*complexconjugate(ZDR33))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_288 = Coupling(name = 'GC_288',
	 value = '-((ZDR21*(ZA21*ZDL31*complexconjugate(Y1d11) + ZA21*ZDL32*complexconjugate(Y1d21) + ZA22*ZDL33*complexconjugate(Y2d31)) + ZDR22*(ZA21*ZDL31*complexconjugate(Y1d12) + ZA21*ZDL32*complexconjugate(Y1d22) + ZA22*ZDL33*complexconjugate(Y2d32)) + ZDR23*(ZA21*ZDL31*complexconjugate(Y1d13) + ZA21*ZDL32*complexconjugate(Y1d23) + ZA22*ZDL33*complexconjugate(Y2d33)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_289 = Coupling(name = 'GC_289',
	 value = '(Y1d11*ZA21*complexconjugate(ZDL21)*complexconjugate(ZDR31) + Y1d21*ZA21*complexconjugate(ZDL22)*complexconjugate(ZDR31) + Y2d31*ZA22*complexconjugate(ZDL23)*complexconjugate(ZDR31) + Y1d12*ZA21*complexconjugate(ZDL21)*complexconjugate(ZDR32) + Y1d22*ZA21*complexconjugate(ZDL22)*complexconjugate(ZDR32) + Y2d32*ZA22*complexconjugate(ZDL23)*complexconjugate(ZDR32) + Y1d13*ZA21*complexconjugate(ZDL21)*complexconjugate(ZDR33) + Y1d23*ZA21*complexconjugate(ZDL22)*complexconjugate(ZDR33) + Y2d33*ZA22*complexconjugate(ZDL23)*complexconjugate(ZDR33))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_290 = Coupling(name = 'GC_290',
	 value = '-((ZDR21*(ZA31*ZDL31*complexconjugate(Y1d11) + ZA31*ZDL32*complexconjugate(Y1d21) + ZA32*ZDL33*complexconjugate(Y2d31)) + ZDR22*(ZA31*ZDL31*complexconjugate(Y1d12) + ZA31*ZDL32*complexconjugate(Y1d22) + ZA32*ZDL33*complexconjugate(Y2d32)) + ZDR23*(ZA31*ZDL31*complexconjugate(Y1d13) + ZA31*ZDL32*complexconjugate(Y1d23) + ZA32*ZDL33*complexconjugate(Y2d33)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_291 = Coupling(name = 'GC_291',
	 value = '(Y1d11*ZA31*complexconjugate(ZDL21)*complexconjugate(ZDR31) + Y1d21*ZA31*complexconjugate(ZDL22)*complexconjugate(ZDR31) + Y2d31*ZA32*complexconjugate(ZDL23)*complexconjugate(ZDR31) + Y1d12*ZA31*complexconjugate(ZDL21)*complexconjugate(ZDR32) + Y1d22*ZA31*complexconjugate(ZDL22)*complexconjugate(ZDR32) + Y2d32*ZA32*complexconjugate(ZDL23)*complexconjugate(ZDR32) + Y1d13*ZA31*complexconjugate(ZDL21)*complexconjugate(ZDR33) + Y1d23*ZA31*complexconjugate(ZDL22)*complexconjugate(ZDR33) + Y2d33*ZA32*complexconjugate(ZDL23)*complexconjugate(ZDR33))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_292 = Coupling(name = 'GC_292',
	 value = '-((ZDR31*(ZA11*ZDL11*complexconjugate(Y1d11) + ZA11*ZDL12*complexconjugate(Y1d21) + ZA12*ZDL13*complexconjugate(Y2d31)) + ZDR32*(ZA11*ZDL11*complexconjugate(Y1d12) + ZA11*ZDL12*complexconjugate(Y1d22) + ZA12*ZDL13*complexconjugate(Y2d32)) + ZDR33*(ZA11*ZDL11*complexconjugate(Y1d13) + ZA11*ZDL12*complexconjugate(Y1d23) + ZA12*ZDL13*complexconjugate(Y2d33)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_293 = Coupling(name = 'GC_293',
	 value = '(Y1d11*ZA11*complexconjugate(ZDL31)*complexconjugate(ZDR11) + Y1d21*ZA11*complexconjugate(ZDL32)*complexconjugate(ZDR11) + Y2d31*ZA12*complexconjugate(ZDL33)*complexconjugate(ZDR11) + Y1d12*ZA11*complexconjugate(ZDL31)*complexconjugate(ZDR12) + Y1d22*ZA11*complexconjugate(ZDL32)*complexconjugate(ZDR12) + Y2d32*ZA12*complexconjugate(ZDL33)*complexconjugate(ZDR12) + Y1d13*ZA11*complexconjugate(ZDL31)*complexconjugate(ZDR13) + Y1d23*ZA11*complexconjugate(ZDL32)*complexconjugate(ZDR13) + Y2d33*ZA12*complexconjugate(ZDL33)*complexconjugate(ZDR13))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_294 = Coupling(name = 'GC_294',
	 value = '-((ZDR31*(ZA21*ZDL11*complexconjugate(Y1d11) + ZA21*ZDL12*complexconjugate(Y1d21) + ZA22*ZDL13*complexconjugate(Y2d31)) + ZDR32*(ZA21*ZDL11*complexconjugate(Y1d12) + ZA21*ZDL12*complexconjugate(Y1d22) + ZA22*ZDL13*complexconjugate(Y2d32)) + ZDR33*(ZA21*ZDL11*complexconjugate(Y1d13) + ZA21*ZDL12*complexconjugate(Y1d23) + ZA22*ZDL13*complexconjugate(Y2d33)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_295 = Coupling(name = 'GC_295',
	 value = '(Y1d11*ZA21*complexconjugate(ZDL31)*complexconjugate(ZDR11) + Y1d21*ZA21*complexconjugate(ZDL32)*complexconjugate(ZDR11) + Y2d31*ZA22*complexconjugate(ZDL33)*complexconjugate(ZDR11) + Y1d12*ZA21*complexconjugate(ZDL31)*complexconjugate(ZDR12) + Y1d22*ZA21*complexconjugate(ZDL32)*complexconjugate(ZDR12) + Y2d32*ZA22*complexconjugate(ZDL33)*complexconjugate(ZDR12) + Y1d13*ZA21*complexconjugate(ZDL31)*complexconjugate(ZDR13) + Y1d23*ZA21*complexconjugate(ZDL32)*complexconjugate(ZDR13) + Y2d33*ZA22*complexconjugate(ZDL33)*complexconjugate(ZDR13))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_296 = Coupling(name = 'GC_296',
	 value = '-((ZDR31*(ZA31*ZDL11*complexconjugate(Y1d11) + ZA31*ZDL12*complexconjugate(Y1d21) + ZA32*ZDL13*complexconjugate(Y2d31)) + ZDR32*(ZA31*ZDL11*complexconjugate(Y1d12) + ZA31*ZDL12*complexconjugate(Y1d22) + ZA32*ZDL13*complexconjugate(Y2d32)) + ZDR33*(ZA31*ZDL11*complexconjugate(Y1d13) + ZA31*ZDL12*complexconjugate(Y1d23) + ZA32*ZDL13*complexconjugate(Y2d33)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_297 = Coupling(name = 'GC_297',
	 value = '(Y1d11*ZA31*complexconjugate(ZDL31)*complexconjugate(ZDR11) + Y1d21*ZA31*complexconjugate(ZDL32)*complexconjugate(ZDR11) + Y2d31*ZA32*complexconjugate(ZDL33)*complexconjugate(ZDR11) + Y1d12*ZA31*complexconjugate(ZDL31)*complexconjugate(ZDR12) + Y1d22*ZA31*complexconjugate(ZDL32)*complexconjugate(ZDR12) + Y2d32*ZA32*complexconjugate(ZDL33)*complexconjugate(ZDR12) + Y1d13*ZA31*complexconjugate(ZDL31)*complexconjugate(ZDR13) + Y1d23*ZA31*complexconjugate(ZDL32)*complexconjugate(ZDR13) + Y2d33*ZA32*complexconjugate(ZDL33)*complexconjugate(ZDR13))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_298 = Coupling(name = 'GC_298',
	 value = '-((ZDR31*(ZA11*ZDL21*complexconjugate(Y1d11) + ZA11*ZDL22*complexconjugate(Y1d21) + ZA12*ZDL23*complexconjugate(Y2d31)) + ZDR32*(ZA11*ZDL21*complexconjugate(Y1d12) + ZA11*ZDL22*complexconjugate(Y1d22) + ZA12*ZDL23*complexconjugate(Y2d32)) + ZDR33*(ZA11*ZDL21*complexconjugate(Y1d13) + ZA11*ZDL22*complexconjugate(Y1d23) + ZA12*ZDL23*complexconjugate(Y2d33)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_299 = Coupling(name = 'GC_299',
	 value = '(Y1d11*ZA11*complexconjugate(ZDL31)*complexconjugate(ZDR21) + Y1d21*ZA11*complexconjugate(ZDL32)*complexconjugate(ZDR21) + Y2d31*ZA12*complexconjugate(ZDL33)*complexconjugate(ZDR21) + Y1d12*ZA11*complexconjugate(ZDL31)*complexconjugate(ZDR22) + Y1d22*ZA11*complexconjugate(ZDL32)*complexconjugate(ZDR22) + Y2d32*ZA12*complexconjugate(ZDL33)*complexconjugate(ZDR22) + Y1d13*ZA11*complexconjugate(ZDL31)*complexconjugate(ZDR23) + Y1d23*ZA11*complexconjugate(ZDL32)*complexconjugate(ZDR23) + Y2d33*ZA12*complexconjugate(ZDL33)*complexconjugate(ZDR23))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_300 = Coupling(name = 'GC_300',
	 value = '-((ZDR31*(ZA21*ZDL21*complexconjugate(Y1d11) + ZA21*ZDL22*complexconjugate(Y1d21) + ZA22*ZDL23*complexconjugate(Y2d31)) + ZDR32*(ZA21*ZDL21*complexconjugate(Y1d12) + ZA21*ZDL22*complexconjugate(Y1d22) + ZA22*ZDL23*complexconjugate(Y2d32)) + ZDR33*(ZA21*ZDL21*complexconjugate(Y1d13) + ZA21*ZDL22*complexconjugate(Y1d23) + ZA22*ZDL23*complexconjugate(Y2d33)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_301 = Coupling(name = 'GC_301',
	 value = '(Y1d11*ZA21*complexconjugate(ZDL31)*complexconjugate(ZDR21) + Y1d21*ZA21*complexconjugate(ZDL32)*complexconjugate(ZDR21) + Y2d31*ZA22*complexconjugate(ZDL33)*complexconjugate(ZDR21) + Y1d12*ZA21*complexconjugate(ZDL31)*complexconjugate(ZDR22) + Y1d22*ZA21*complexconjugate(ZDL32)*complexconjugate(ZDR22) + Y2d32*ZA22*complexconjugate(ZDL33)*complexconjugate(ZDR22) + Y1d13*ZA21*complexconjugate(ZDL31)*complexconjugate(ZDR23) + Y1d23*ZA21*complexconjugate(ZDL32)*complexconjugate(ZDR23) + Y2d33*ZA22*complexconjugate(ZDL33)*complexconjugate(ZDR23))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_302 = Coupling(name = 'GC_302',
	 value = '-((ZDR31*(ZA31*ZDL21*complexconjugate(Y1d11) + ZA31*ZDL22*complexconjugate(Y1d21) + ZA32*ZDL23*complexconjugate(Y2d31)) + ZDR32*(ZA31*ZDL21*complexconjugate(Y1d12) + ZA31*ZDL22*complexconjugate(Y1d22) + ZA32*ZDL23*complexconjugate(Y2d32)) + ZDR33*(ZA31*ZDL21*complexconjugate(Y1d13) + ZA31*ZDL22*complexconjugate(Y1d23) + ZA32*ZDL23*complexconjugate(Y2d33)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_303 = Coupling(name = 'GC_303',
	 value = '(Y1d11*ZA31*complexconjugate(ZDL31)*complexconjugate(ZDR21) + Y1d21*ZA31*complexconjugate(ZDL32)*complexconjugate(ZDR21) + Y2d31*ZA32*complexconjugate(ZDL33)*complexconjugate(ZDR21) + Y1d12*ZA31*complexconjugate(ZDL31)*complexconjugate(ZDR22) + Y1d22*ZA31*complexconjugate(ZDL32)*complexconjugate(ZDR22) + Y2d32*ZA32*complexconjugate(ZDL33)*complexconjugate(ZDR22) + Y1d13*ZA31*complexconjugate(ZDL31)*complexconjugate(ZDR23) + Y1d23*ZA31*complexconjugate(ZDL32)*complexconjugate(ZDR23) + Y2d33*ZA32*complexconjugate(ZDL33)*complexconjugate(ZDR23))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_304 = Coupling(name = 'GC_304',
	 value = '-((ZDR31*(ZA11*ZDL31*complexconjugate(Y1d11) + ZA11*ZDL32*complexconjugate(Y1d21) + ZA12*ZDL33*complexconjugate(Y2d31)) + ZDR32*(ZA11*ZDL31*complexconjugate(Y1d12) + ZA11*ZDL32*complexconjugate(Y1d22) + ZA12*ZDL33*complexconjugate(Y2d32)) + ZDR33*(ZA11*ZDL31*complexconjugate(Y1d13) + ZA11*ZDL32*complexconjugate(Y1d23) + ZA12*ZDL33*complexconjugate(Y2d33)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_305 = Coupling(name = 'GC_305',
	 value = '(Y1d11*ZA11*complexconjugate(ZDL31)*complexconjugate(ZDR31) + Y1d21*ZA11*complexconjugate(ZDL32)*complexconjugate(ZDR31) + Y2d31*ZA12*complexconjugate(ZDL33)*complexconjugate(ZDR31) + Y1d12*ZA11*complexconjugate(ZDL31)*complexconjugate(ZDR32) + Y1d22*ZA11*complexconjugate(ZDL32)*complexconjugate(ZDR32) + Y2d32*ZA12*complexconjugate(ZDL33)*complexconjugate(ZDR32) + Y1d13*ZA11*complexconjugate(ZDL31)*complexconjugate(ZDR33) + Y1d23*ZA11*complexconjugate(ZDL32)*complexconjugate(ZDR33) + Y2d33*ZA12*complexconjugate(ZDL33)*complexconjugate(ZDR33))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_306 = Coupling(name = 'GC_306',
	 value = '-((ZDR31*(ZA21*ZDL31*complexconjugate(Y1d11) + ZA21*ZDL32*complexconjugate(Y1d21) + ZA22*ZDL33*complexconjugate(Y2d31)) + ZDR32*(ZA21*ZDL31*complexconjugate(Y1d12) + ZA21*ZDL32*complexconjugate(Y1d22) + ZA22*ZDL33*complexconjugate(Y2d32)) + ZDR33*(ZA21*ZDL31*complexconjugate(Y1d13) + ZA21*ZDL32*complexconjugate(Y1d23) + ZA22*ZDL33*complexconjugate(Y2d33)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_307 = Coupling(name = 'GC_307',
	 value = '(Y1d11*ZA21*complexconjugate(ZDL31)*complexconjugate(ZDR31) + Y1d21*ZA21*complexconjugate(ZDL32)*complexconjugate(ZDR31) + Y2d31*ZA22*complexconjugate(ZDL33)*complexconjugate(ZDR31) + Y1d12*ZA21*complexconjugate(ZDL31)*complexconjugate(ZDR32) + Y1d22*ZA21*complexconjugate(ZDL32)*complexconjugate(ZDR32) + Y2d32*ZA22*complexconjugate(ZDL33)*complexconjugate(ZDR32) + Y1d13*ZA21*complexconjugate(ZDL31)*complexconjugate(ZDR33) + Y1d23*ZA21*complexconjugate(ZDL32)*complexconjugate(ZDR33) + Y2d33*ZA22*complexconjugate(ZDL33)*complexconjugate(ZDR33))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_308 = Coupling(name = 'GC_308',
	 value = '-((ZDR31*(ZA31*ZDL31*complexconjugate(Y1d11) + ZA31*ZDL32*complexconjugate(Y1d21) + ZA32*ZDL33*complexconjugate(Y2d31)) + ZDR32*(ZA31*ZDL31*complexconjugate(Y1d12) + ZA31*ZDL32*complexconjugate(Y1d22) + ZA32*ZDL33*complexconjugate(Y2d32)) + ZDR33*(ZA31*ZDL31*complexconjugate(Y1d13) + ZA31*ZDL32*complexconjugate(Y1d23) + ZA32*ZDL33*complexconjugate(Y2d33)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_309 = Coupling(name = 'GC_309',
	 value = '(Y1d11*ZA31*complexconjugate(ZDL31)*complexconjugate(ZDR31) + Y1d21*ZA31*complexconjugate(ZDL32)*complexconjugate(ZDR31) + Y2d31*ZA32*complexconjugate(ZDL33)*complexconjugate(ZDR31) + Y1d12*ZA31*complexconjugate(ZDL31)*complexconjugate(ZDR32) + Y1d22*ZA31*complexconjugate(ZDL32)*complexconjugate(ZDR32) + Y2d32*ZA32*complexconjugate(ZDL33)*complexconjugate(ZDR32) + Y1d13*ZA31*complexconjugate(ZDL31)*complexconjugate(ZDR33) + Y1d23*ZA31*complexconjugate(ZDL32)*complexconjugate(ZDR33) + Y2d33*ZA32*complexconjugate(ZDL33)*complexconjugate(ZDR33))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_310 = Coupling(name = 'GC_310',
	 value = '-((ZA11*ZER11*(ZEL11*complexconjugate(Y1e11) + ZEL12*complexconjugate(Y1e21)) + ZA11*ZER12*(ZEL11*complexconjugate(Y1e12) + ZEL12*complexconjugate(Y1e22)) + ZA12*ZEL13*ZER13*complexconjugate(Y2e33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_311 = Coupling(name = 'GC_311',
	 value = '(Y1e11*ZA11*complexconjugate(ZEL11)*complexconjugate(ZER11) + Y1e21*ZA11*complexconjugate(ZEL12)*complexconjugate(ZER11) + Y1e12*ZA11*complexconjugate(ZEL11)*complexconjugate(ZER12) + Y1e22*ZA11*complexconjugate(ZEL12)*complexconjugate(ZER12) + Y2e33*ZA12*complexconjugate(ZEL13)*complexconjugate(ZER13))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_312 = Coupling(name = 'GC_312',
	 value = '-((ZA21*ZER11*(ZEL11*complexconjugate(Y1e11) + ZEL12*complexconjugate(Y1e21)) + ZA21*ZER12*(ZEL11*complexconjugate(Y1e12) + ZEL12*complexconjugate(Y1e22)) + ZA22*ZEL13*ZER13*complexconjugate(Y2e33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_313 = Coupling(name = 'GC_313',
	 value = '(Y1e11*ZA21*complexconjugate(ZEL11)*complexconjugate(ZER11) + Y1e21*ZA21*complexconjugate(ZEL12)*complexconjugate(ZER11) + Y1e12*ZA21*complexconjugate(ZEL11)*complexconjugate(ZER12) + Y1e22*ZA21*complexconjugate(ZEL12)*complexconjugate(ZER12) + Y2e33*ZA22*complexconjugate(ZEL13)*complexconjugate(ZER13))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_314 = Coupling(name = 'GC_314',
	 value = '-((ZA31*ZER11*(ZEL11*complexconjugate(Y1e11) + ZEL12*complexconjugate(Y1e21)) + ZA31*ZER12*(ZEL11*complexconjugate(Y1e12) + ZEL12*complexconjugate(Y1e22)) + ZA32*ZEL13*ZER13*complexconjugate(Y2e33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_315 = Coupling(name = 'GC_315',
	 value = '(Y1e11*ZA31*complexconjugate(ZEL11)*complexconjugate(ZER11) + Y1e21*ZA31*complexconjugate(ZEL12)*complexconjugate(ZER11) + Y1e12*ZA31*complexconjugate(ZEL11)*complexconjugate(ZER12) + Y1e22*ZA31*complexconjugate(ZEL12)*complexconjugate(ZER12) + Y2e33*ZA32*complexconjugate(ZEL13)*complexconjugate(ZER13))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_316 = Coupling(name = 'GC_316',
	 value = '-((ZA11*ZER11*(ZEL21*complexconjugate(Y1e11) + ZEL22*complexconjugate(Y1e21)) + ZA11*ZER12*(ZEL21*complexconjugate(Y1e12) + ZEL22*complexconjugate(Y1e22)) + ZA12*ZEL23*ZER13*complexconjugate(Y2e33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_317 = Coupling(name = 'GC_317',
	 value = '(Y1e11*ZA11*complexconjugate(ZEL11)*complexconjugate(ZER21) + Y1e21*ZA11*complexconjugate(ZEL12)*complexconjugate(ZER21) + Y1e12*ZA11*complexconjugate(ZEL11)*complexconjugate(ZER22) + Y1e22*ZA11*complexconjugate(ZEL12)*complexconjugate(ZER22) + Y2e33*ZA12*complexconjugate(ZEL13)*complexconjugate(ZER23))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_318 = Coupling(name = 'GC_318',
	 value = '-((ZA21*ZER11*(ZEL21*complexconjugate(Y1e11) + ZEL22*complexconjugate(Y1e21)) + ZA21*ZER12*(ZEL21*complexconjugate(Y1e12) + ZEL22*complexconjugate(Y1e22)) + ZA22*ZEL23*ZER13*complexconjugate(Y2e33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_319 = Coupling(name = 'GC_319',
	 value = '(Y1e11*ZA21*complexconjugate(ZEL11)*complexconjugate(ZER21) + Y1e21*ZA21*complexconjugate(ZEL12)*complexconjugate(ZER21) + Y1e12*ZA21*complexconjugate(ZEL11)*complexconjugate(ZER22) + Y1e22*ZA21*complexconjugate(ZEL12)*complexconjugate(ZER22) + Y2e33*ZA22*complexconjugate(ZEL13)*complexconjugate(ZER23))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_320 = Coupling(name = 'GC_320',
	 value = '-((ZA31*ZER11*(ZEL21*complexconjugate(Y1e11) + ZEL22*complexconjugate(Y1e21)) + ZA31*ZER12*(ZEL21*complexconjugate(Y1e12) + ZEL22*complexconjugate(Y1e22)) + ZA32*ZEL23*ZER13*complexconjugate(Y2e33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_321 = Coupling(name = 'GC_321',
	 value = '(Y1e11*ZA31*complexconjugate(ZEL11)*complexconjugate(ZER21) + Y1e21*ZA31*complexconjugate(ZEL12)*complexconjugate(ZER21) + Y1e12*ZA31*complexconjugate(ZEL11)*complexconjugate(ZER22) + Y1e22*ZA31*complexconjugate(ZEL12)*complexconjugate(ZER22) + Y2e33*ZA32*complexconjugate(ZEL13)*complexconjugate(ZER23))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_322 = Coupling(name = 'GC_322',
	 value = '-((ZA11*ZER11*(ZEL31*complexconjugate(Y1e11) + ZEL32*complexconjugate(Y1e21)) + ZA11*ZER12*(ZEL31*complexconjugate(Y1e12) + ZEL32*complexconjugate(Y1e22)) + ZA12*ZEL33*ZER13*complexconjugate(Y2e33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_323 = Coupling(name = 'GC_323',
	 value = '(Y1e11*ZA11*complexconjugate(ZEL11)*complexconjugate(ZER31) + Y1e21*ZA11*complexconjugate(ZEL12)*complexconjugate(ZER31) + Y1e12*ZA11*complexconjugate(ZEL11)*complexconjugate(ZER32) + Y1e22*ZA11*complexconjugate(ZEL12)*complexconjugate(ZER32) + Y2e33*ZA12*complexconjugate(ZEL13)*complexconjugate(ZER33))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_324 = Coupling(name = 'GC_324',
	 value = '-((ZA21*ZER11*(ZEL31*complexconjugate(Y1e11) + ZEL32*complexconjugate(Y1e21)) + ZA21*ZER12*(ZEL31*complexconjugate(Y1e12) + ZEL32*complexconjugate(Y1e22)) + ZA22*ZEL33*ZER13*complexconjugate(Y2e33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_325 = Coupling(name = 'GC_325',
	 value = '(Y1e11*ZA21*complexconjugate(ZEL11)*complexconjugate(ZER31) + Y1e21*ZA21*complexconjugate(ZEL12)*complexconjugate(ZER31) + Y1e12*ZA21*complexconjugate(ZEL11)*complexconjugate(ZER32) + Y1e22*ZA21*complexconjugate(ZEL12)*complexconjugate(ZER32) + Y2e33*ZA22*complexconjugate(ZEL13)*complexconjugate(ZER33))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_326 = Coupling(name = 'GC_326',
	 value = '-((ZA31*ZER11*(ZEL31*complexconjugate(Y1e11) + ZEL32*complexconjugate(Y1e21)) + ZA31*ZER12*(ZEL31*complexconjugate(Y1e12) + ZEL32*complexconjugate(Y1e22)) + ZA32*ZEL33*ZER13*complexconjugate(Y2e33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_327 = Coupling(name = 'GC_327',
	 value = '(Y1e11*ZA31*complexconjugate(ZEL11)*complexconjugate(ZER31) + Y1e21*ZA31*complexconjugate(ZEL12)*complexconjugate(ZER31) + Y1e12*ZA31*complexconjugate(ZEL11)*complexconjugate(ZER32) + Y1e22*ZA31*complexconjugate(ZEL12)*complexconjugate(ZER32) + Y2e33*ZA32*complexconjugate(ZEL13)*complexconjugate(ZER33))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_328 = Coupling(name = 'GC_328',
	 value = '-((ZA11*ZER21*(ZEL11*complexconjugate(Y1e11) + ZEL12*complexconjugate(Y1e21)) + ZA11*ZER22*(ZEL11*complexconjugate(Y1e12) + ZEL12*complexconjugate(Y1e22)) + ZA12*ZEL13*ZER23*complexconjugate(Y2e33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_329 = Coupling(name = 'GC_329',
	 value = '(Y1e11*ZA11*complexconjugate(ZEL21)*complexconjugate(ZER11) + Y1e21*ZA11*complexconjugate(ZEL22)*complexconjugate(ZER11) + Y1e12*ZA11*complexconjugate(ZEL21)*complexconjugate(ZER12) + Y1e22*ZA11*complexconjugate(ZEL22)*complexconjugate(ZER12) + Y2e33*ZA12*complexconjugate(ZEL23)*complexconjugate(ZER13))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_330 = Coupling(name = 'GC_330',
	 value = '-((ZA21*ZER21*(ZEL11*complexconjugate(Y1e11) + ZEL12*complexconjugate(Y1e21)) + ZA21*ZER22*(ZEL11*complexconjugate(Y1e12) + ZEL12*complexconjugate(Y1e22)) + ZA22*ZEL13*ZER23*complexconjugate(Y2e33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_331 = Coupling(name = 'GC_331',
	 value = '(Y1e11*ZA21*complexconjugate(ZEL21)*complexconjugate(ZER11) + Y1e21*ZA21*complexconjugate(ZEL22)*complexconjugate(ZER11) + Y1e12*ZA21*complexconjugate(ZEL21)*complexconjugate(ZER12) + Y1e22*ZA21*complexconjugate(ZEL22)*complexconjugate(ZER12) + Y2e33*ZA22*complexconjugate(ZEL23)*complexconjugate(ZER13))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_332 = Coupling(name = 'GC_332',
	 value = '-((ZA31*ZER21*(ZEL11*complexconjugate(Y1e11) + ZEL12*complexconjugate(Y1e21)) + ZA31*ZER22*(ZEL11*complexconjugate(Y1e12) + ZEL12*complexconjugate(Y1e22)) + ZA32*ZEL13*ZER23*complexconjugate(Y2e33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_333 = Coupling(name = 'GC_333',
	 value = '(Y1e11*ZA31*complexconjugate(ZEL21)*complexconjugate(ZER11) + Y1e21*ZA31*complexconjugate(ZEL22)*complexconjugate(ZER11) + Y1e12*ZA31*complexconjugate(ZEL21)*complexconjugate(ZER12) + Y1e22*ZA31*complexconjugate(ZEL22)*complexconjugate(ZER12) + Y2e33*ZA32*complexconjugate(ZEL23)*complexconjugate(ZER13))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_334 = Coupling(name = 'GC_334',
	 value = '-((ZA11*ZER21*(ZEL21*complexconjugate(Y1e11) + ZEL22*complexconjugate(Y1e21)) + ZA11*ZER22*(ZEL21*complexconjugate(Y1e12) + ZEL22*complexconjugate(Y1e22)) + ZA12*ZEL23*ZER23*complexconjugate(Y2e33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_335 = Coupling(name = 'GC_335',
	 value = '(Y1e11*ZA11*complexconjugate(ZEL21)*complexconjugate(ZER21) + Y1e21*ZA11*complexconjugate(ZEL22)*complexconjugate(ZER21) + Y1e12*ZA11*complexconjugate(ZEL21)*complexconjugate(ZER22) + Y1e22*ZA11*complexconjugate(ZEL22)*complexconjugate(ZER22) + Y2e33*ZA12*complexconjugate(ZEL23)*complexconjugate(ZER23))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_336 = Coupling(name = 'GC_336',
	 value = '-((ZA21*ZER21*(ZEL21*complexconjugate(Y1e11) + ZEL22*complexconjugate(Y1e21)) + ZA21*ZER22*(ZEL21*complexconjugate(Y1e12) + ZEL22*complexconjugate(Y1e22)) + ZA22*ZEL23*ZER23*complexconjugate(Y2e33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_337 = Coupling(name = 'GC_337',
	 value = '(Y1e11*ZA21*complexconjugate(ZEL21)*complexconjugate(ZER21) + Y1e21*ZA21*complexconjugate(ZEL22)*complexconjugate(ZER21) + Y1e12*ZA21*complexconjugate(ZEL21)*complexconjugate(ZER22) + Y1e22*ZA21*complexconjugate(ZEL22)*complexconjugate(ZER22) + Y2e33*ZA22*complexconjugate(ZEL23)*complexconjugate(ZER23))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_338 = Coupling(name = 'GC_338',
	 value = '-((ZA31*ZER21*(ZEL21*complexconjugate(Y1e11) + ZEL22*complexconjugate(Y1e21)) + ZA31*ZER22*(ZEL21*complexconjugate(Y1e12) + ZEL22*complexconjugate(Y1e22)) + ZA32*ZEL23*ZER23*complexconjugate(Y2e33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_339 = Coupling(name = 'GC_339',
	 value = '(Y1e11*ZA31*complexconjugate(ZEL21)*complexconjugate(ZER21) + Y1e21*ZA31*complexconjugate(ZEL22)*complexconjugate(ZER21) + Y1e12*ZA31*complexconjugate(ZEL21)*complexconjugate(ZER22) + Y1e22*ZA31*complexconjugate(ZEL22)*complexconjugate(ZER22) + Y2e33*ZA32*complexconjugate(ZEL23)*complexconjugate(ZER23))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_340 = Coupling(name = 'GC_340',
	 value = '-((ZA11*ZER21*(ZEL31*complexconjugate(Y1e11) + ZEL32*complexconjugate(Y1e21)) + ZA11*ZER22*(ZEL31*complexconjugate(Y1e12) + ZEL32*complexconjugate(Y1e22)) + ZA12*ZEL33*ZER23*complexconjugate(Y2e33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_341 = Coupling(name = 'GC_341',
	 value = '(Y1e11*ZA11*complexconjugate(ZEL21)*complexconjugate(ZER31) + Y1e21*ZA11*complexconjugate(ZEL22)*complexconjugate(ZER31) + Y1e12*ZA11*complexconjugate(ZEL21)*complexconjugate(ZER32) + Y1e22*ZA11*complexconjugate(ZEL22)*complexconjugate(ZER32) + Y2e33*ZA12*complexconjugate(ZEL23)*complexconjugate(ZER33))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_342 = Coupling(name = 'GC_342',
	 value = '-((ZA21*ZER21*(ZEL31*complexconjugate(Y1e11) + ZEL32*complexconjugate(Y1e21)) + ZA21*ZER22*(ZEL31*complexconjugate(Y1e12) + ZEL32*complexconjugate(Y1e22)) + ZA22*ZEL33*ZER23*complexconjugate(Y2e33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_343 = Coupling(name = 'GC_343',
	 value = '(Y1e11*ZA21*complexconjugate(ZEL21)*complexconjugate(ZER31) + Y1e21*ZA21*complexconjugate(ZEL22)*complexconjugate(ZER31) + Y1e12*ZA21*complexconjugate(ZEL21)*complexconjugate(ZER32) + Y1e22*ZA21*complexconjugate(ZEL22)*complexconjugate(ZER32) + Y2e33*ZA22*complexconjugate(ZEL23)*complexconjugate(ZER33))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_344 = Coupling(name = 'GC_344',
	 value = '-((ZA31*ZER21*(ZEL31*complexconjugate(Y1e11) + ZEL32*complexconjugate(Y1e21)) + ZA31*ZER22*(ZEL31*complexconjugate(Y1e12) + ZEL32*complexconjugate(Y1e22)) + ZA32*ZEL33*ZER23*complexconjugate(Y2e33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_345 = Coupling(name = 'GC_345',
	 value = '(Y1e11*ZA31*complexconjugate(ZEL21)*complexconjugate(ZER31) + Y1e21*ZA31*complexconjugate(ZEL22)*complexconjugate(ZER31) + Y1e12*ZA31*complexconjugate(ZEL21)*complexconjugate(ZER32) + Y1e22*ZA31*complexconjugate(ZEL22)*complexconjugate(ZER32) + Y2e33*ZA32*complexconjugate(ZEL23)*complexconjugate(ZER33))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_346 = Coupling(name = 'GC_346',
	 value = '-((ZA11*ZER31*(ZEL11*complexconjugate(Y1e11) + ZEL12*complexconjugate(Y1e21)) + ZA11*ZER32*(ZEL11*complexconjugate(Y1e12) + ZEL12*complexconjugate(Y1e22)) + ZA12*ZEL13*ZER33*complexconjugate(Y2e33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_347 = Coupling(name = 'GC_347',
	 value = '(Y1e11*ZA11*complexconjugate(ZEL31)*complexconjugate(ZER11) + Y1e21*ZA11*complexconjugate(ZEL32)*complexconjugate(ZER11) + Y1e12*ZA11*complexconjugate(ZEL31)*complexconjugate(ZER12) + Y1e22*ZA11*complexconjugate(ZEL32)*complexconjugate(ZER12) + Y2e33*ZA12*complexconjugate(ZEL33)*complexconjugate(ZER13))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_348 = Coupling(name = 'GC_348',
	 value = '-((ZA21*ZER31*(ZEL11*complexconjugate(Y1e11) + ZEL12*complexconjugate(Y1e21)) + ZA21*ZER32*(ZEL11*complexconjugate(Y1e12) + ZEL12*complexconjugate(Y1e22)) + ZA22*ZEL13*ZER33*complexconjugate(Y2e33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_349 = Coupling(name = 'GC_349',
	 value = '(Y1e11*ZA21*complexconjugate(ZEL31)*complexconjugate(ZER11) + Y1e21*ZA21*complexconjugate(ZEL32)*complexconjugate(ZER11) + Y1e12*ZA21*complexconjugate(ZEL31)*complexconjugate(ZER12) + Y1e22*ZA21*complexconjugate(ZEL32)*complexconjugate(ZER12) + Y2e33*ZA22*complexconjugate(ZEL33)*complexconjugate(ZER13))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_350 = Coupling(name = 'GC_350',
	 value = '-((ZA31*ZER31*(ZEL11*complexconjugate(Y1e11) + ZEL12*complexconjugate(Y1e21)) + ZA31*ZER32*(ZEL11*complexconjugate(Y1e12) + ZEL12*complexconjugate(Y1e22)) + ZA32*ZEL13*ZER33*complexconjugate(Y2e33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_351 = Coupling(name = 'GC_351',
	 value = '(Y1e11*ZA31*complexconjugate(ZEL31)*complexconjugate(ZER11) + Y1e21*ZA31*complexconjugate(ZEL32)*complexconjugate(ZER11) + Y1e12*ZA31*complexconjugate(ZEL31)*complexconjugate(ZER12) + Y1e22*ZA31*complexconjugate(ZEL32)*complexconjugate(ZER12) + Y2e33*ZA32*complexconjugate(ZEL33)*complexconjugate(ZER13))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_352 = Coupling(name = 'GC_352',
	 value = '-((ZA11*ZER31*(ZEL21*complexconjugate(Y1e11) + ZEL22*complexconjugate(Y1e21)) + ZA11*ZER32*(ZEL21*complexconjugate(Y1e12) + ZEL22*complexconjugate(Y1e22)) + ZA12*ZEL23*ZER33*complexconjugate(Y2e33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_353 = Coupling(name = 'GC_353',
	 value = '(Y1e11*ZA11*complexconjugate(ZEL31)*complexconjugate(ZER21) + Y1e21*ZA11*complexconjugate(ZEL32)*complexconjugate(ZER21) + Y1e12*ZA11*complexconjugate(ZEL31)*complexconjugate(ZER22) + Y1e22*ZA11*complexconjugate(ZEL32)*complexconjugate(ZER22) + Y2e33*ZA12*complexconjugate(ZEL33)*complexconjugate(ZER23))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_354 = Coupling(name = 'GC_354',
	 value = '-((ZA21*ZER31*(ZEL21*complexconjugate(Y1e11) + ZEL22*complexconjugate(Y1e21)) + ZA21*ZER32*(ZEL21*complexconjugate(Y1e12) + ZEL22*complexconjugate(Y1e22)) + ZA22*ZEL23*ZER33*complexconjugate(Y2e33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_355 = Coupling(name = 'GC_355',
	 value = '(Y1e11*ZA21*complexconjugate(ZEL31)*complexconjugate(ZER21) + Y1e21*ZA21*complexconjugate(ZEL32)*complexconjugate(ZER21) + Y1e12*ZA21*complexconjugate(ZEL31)*complexconjugate(ZER22) + Y1e22*ZA21*complexconjugate(ZEL32)*complexconjugate(ZER22) + Y2e33*ZA22*complexconjugate(ZEL33)*complexconjugate(ZER23))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_356 = Coupling(name = 'GC_356',
	 value = '-((ZA31*ZER31*(ZEL21*complexconjugate(Y1e11) + ZEL22*complexconjugate(Y1e21)) + ZA31*ZER32*(ZEL21*complexconjugate(Y1e12) + ZEL22*complexconjugate(Y1e22)) + ZA32*ZEL23*ZER33*complexconjugate(Y2e33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_357 = Coupling(name = 'GC_357',
	 value = '(Y1e11*ZA31*complexconjugate(ZEL31)*complexconjugate(ZER21) + Y1e21*ZA31*complexconjugate(ZEL32)*complexconjugate(ZER21) + Y1e12*ZA31*complexconjugate(ZEL31)*complexconjugate(ZER22) + Y1e22*ZA31*complexconjugate(ZEL32)*complexconjugate(ZER22) + Y2e33*ZA32*complexconjugate(ZEL33)*complexconjugate(ZER23))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_358 = Coupling(name = 'GC_358',
	 value = '-((ZA11*ZER31*(ZEL31*complexconjugate(Y1e11) + ZEL32*complexconjugate(Y1e21)) + ZA11*ZER32*(ZEL31*complexconjugate(Y1e12) + ZEL32*complexconjugate(Y1e22)) + ZA12*ZEL33*ZER33*complexconjugate(Y2e33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_359 = Coupling(name = 'GC_359',
	 value = '(Y1e11*ZA11*complexconjugate(ZEL31)*complexconjugate(ZER31) + Y1e21*ZA11*complexconjugate(ZEL32)*complexconjugate(ZER31) + Y1e12*ZA11*complexconjugate(ZEL31)*complexconjugate(ZER32) + Y1e22*ZA11*complexconjugate(ZEL32)*complexconjugate(ZER32) + Y2e33*ZA12*complexconjugate(ZEL33)*complexconjugate(ZER33))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_360 = Coupling(name = 'GC_360',
	 value = '-((ZA21*ZER31*(ZEL31*complexconjugate(Y1e11) + ZEL32*complexconjugate(Y1e21)) + ZA21*ZER32*(ZEL31*complexconjugate(Y1e12) + ZEL32*complexconjugate(Y1e22)) + ZA22*ZEL33*ZER33*complexconjugate(Y2e33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_361 = Coupling(name = 'GC_361',
	 value = '(Y1e11*ZA21*complexconjugate(ZEL31)*complexconjugate(ZER31) + Y1e21*ZA21*complexconjugate(ZEL32)*complexconjugate(ZER31) + Y1e12*ZA21*complexconjugate(ZEL31)*complexconjugate(ZER32) + Y1e22*ZA21*complexconjugate(ZEL32)*complexconjugate(ZER32) + Y2e33*ZA22*complexconjugate(ZEL33)*complexconjugate(ZER33))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_362 = Coupling(name = 'GC_362',
	 value = '-((ZA31*ZER31*(ZEL31*complexconjugate(Y1e11) + ZEL32*complexconjugate(Y1e21)) + ZA31*ZER32*(ZEL31*complexconjugate(Y1e12) + ZEL32*complexconjugate(Y1e22)) + ZA32*ZEL33*ZER33*complexconjugate(Y2e33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_363 = Coupling(name = 'GC_363',
	 value = '(Y1e11*ZA31*complexconjugate(ZEL31)*complexconjugate(ZER31) + Y1e21*ZA31*complexconjugate(ZEL32)*complexconjugate(ZER31) + Y1e12*ZA31*complexconjugate(ZEL31)*complexconjugate(ZER32) + Y1e22*ZA31*complexconjugate(ZEL32)*complexconjugate(ZER32) + Y2e33*ZA32*complexconjugate(ZEL33)*complexconjugate(ZER33))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_364 = Coupling(name = 'GC_364',
	 value = '-((ZA11*ZUR11*(ZUL11*complexconjugate(Y1u11) + ZUL12*complexconjugate(Y1u21)) + ZA11*ZUR12*(ZUL11*complexconjugate(Y1u12) + ZUL12*complexconjugate(Y1u22)) + ZA12*ZUL13*ZUR13*complexconjugate(Y2u33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_365 = Coupling(name = 'GC_365',
	 value = '(Y1u11*ZA11*complexconjugate(ZUL11)*complexconjugate(ZUR11) + Y1u21*ZA11*complexconjugate(ZUL12)*complexconjugate(ZUR11) + Y1u12*ZA11*complexconjugate(ZUL11)*complexconjugate(ZUR12) + Y1u22*ZA11*complexconjugate(ZUL12)*complexconjugate(ZUR12) + Y2u33*ZA12*complexconjugate(ZUL13)*complexconjugate(ZUR13))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_366 = Coupling(name = 'GC_366',
	 value = '-((ZA21*ZUR11*(ZUL11*complexconjugate(Y1u11) + ZUL12*complexconjugate(Y1u21)) + ZA21*ZUR12*(ZUL11*complexconjugate(Y1u12) + ZUL12*complexconjugate(Y1u22)) + ZA22*ZUL13*ZUR13*complexconjugate(Y2u33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_367 = Coupling(name = 'GC_367',
	 value = '(Y1u11*ZA21*complexconjugate(ZUL11)*complexconjugate(ZUR11) + Y1u21*ZA21*complexconjugate(ZUL12)*complexconjugate(ZUR11) + Y1u12*ZA21*complexconjugate(ZUL11)*complexconjugate(ZUR12) + Y1u22*ZA21*complexconjugate(ZUL12)*complexconjugate(ZUR12) + Y2u33*ZA22*complexconjugate(ZUL13)*complexconjugate(ZUR13))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_368 = Coupling(name = 'GC_368',
	 value = '-((ZA31*ZUR11*(ZUL11*complexconjugate(Y1u11) + ZUL12*complexconjugate(Y1u21)) + ZA31*ZUR12*(ZUL11*complexconjugate(Y1u12) + ZUL12*complexconjugate(Y1u22)) + ZA32*ZUL13*ZUR13*complexconjugate(Y2u33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_369 = Coupling(name = 'GC_369',
	 value = '(Y1u11*ZA31*complexconjugate(ZUL11)*complexconjugate(ZUR11) + Y1u21*ZA31*complexconjugate(ZUL12)*complexconjugate(ZUR11) + Y1u12*ZA31*complexconjugate(ZUL11)*complexconjugate(ZUR12) + Y1u22*ZA31*complexconjugate(ZUL12)*complexconjugate(ZUR12) + Y2u33*ZA32*complexconjugate(ZUL13)*complexconjugate(ZUR13))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_370 = Coupling(name = 'GC_370',
	 value = '-((ZA11*ZUR11*(ZUL21*complexconjugate(Y1u11) + ZUL22*complexconjugate(Y1u21)) + ZA11*ZUR12*(ZUL21*complexconjugate(Y1u12) + ZUL22*complexconjugate(Y1u22)) + ZA12*ZUL23*ZUR13*complexconjugate(Y2u33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_371 = Coupling(name = 'GC_371',
	 value = '(Y1u11*ZA11*complexconjugate(ZUL11)*complexconjugate(ZUR21) + Y1u21*ZA11*complexconjugate(ZUL12)*complexconjugate(ZUR21) + Y1u12*ZA11*complexconjugate(ZUL11)*complexconjugate(ZUR22) + Y1u22*ZA11*complexconjugate(ZUL12)*complexconjugate(ZUR22) + Y2u33*ZA12*complexconjugate(ZUL13)*complexconjugate(ZUR23))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_372 = Coupling(name = 'GC_372',
	 value = '-((ZA21*ZUR11*(ZUL21*complexconjugate(Y1u11) + ZUL22*complexconjugate(Y1u21)) + ZA21*ZUR12*(ZUL21*complexconjugate(Y1u12) + ZUL22*complexconjugate(Y1u22)) + ZA22*ZUL23*ZUR13*complexconjugate(Y2u33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_373 = Coupling(name = 'GC_373',
	 value = '(Y1u11*ZA21*complexconjugate(ZUL11)*complexconjugate(ZUR21) + Y1u21*ZA21*complexconjugate(ZUL12)*complexconjugate(ZUR21) + Y1u12*ZA21*complexconjugate(ZUL11)*complexconjugate(ZUR22) + Y1u22*ZA21*complexconjugate(ZUL12)*complexconjugate(ZUR22) + Y2u33*ZA22*complexconjugate(ZUL13)*complexconjugate(ZUR23))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_374 = Coupling(name = 'GC_374',
	 value = '-((ZA31*ZUR11*(ZUL21*complexconjugate(Y1u11) + ZUL22*complexconjugate(Y1u21)) + ZA31*ZUR12*(ZUL21*complexconjugate(Y1u12) + ZUL22*complexconjugate(Y1u22)) + ZA32*ZUL23*ZUR13*complexconjugate(Y2u33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_375 = Coupling(name = 'GC_375',
	 value = '(Y1u11*ZA31*complexconjugate(ZUL11)*complexconjugate(ZUR21) + Y1u21*ZA31*complexconjugate(ZUL12)*complexconjugate(ZUR21) + Y1u12*ZA31*complexconjugate(ZUL11)*complexconjugate(ZUR22) + Y1u22*ZA31*complexconjugate(ZUL12)*complexconjugate(ZUR22) + Y2u33*ZA32*complexconjugate(ZUL13)*complexconjugate(ZUR23))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_376 = Coupling(name = 'GC_376',
	 value = '-((ZA11*ZUR11*(ZUL31*complexconjugate(Y1u11) + ZUL32*complexconjugate(Y1u21)) + ZA11*ZUR12*(ZUL31*complexconjugate(Y1u12) + ZUL32*complexconjugate(Y1u22)) + ZA12*ZUL33*ZUR13*complexconjugate(Y2u33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_377 = Coupling(name = 'GC_377',
	 value = '(Y1u11*ZA11*complexconjugate(ZUL11)*complexconjugate(ZUR31) + Y1u21*ZA11*complexconjugate(ZUL12)*complexconjugate(ZUR31) + Y1u12*ZA11*complexconjugate(ZUL11)*complexconjugate(ZUR32) + Y1u22*ZA11*complexconjugate(ZUL12)*complexconjugate(ZUR32) + Y2u33*ZA12*complexconjugate(ZUL13)*complexconjugate(ZUR33))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_378 = Coupling(name = 'GC_378',
	 value = '-((ZA21*ZUR11*(ZUL31*complexconjugate(Y1u11) + ZUL32*complexconjugate(Y1u21)) + ZA21*ZUR12*(ZUL31*complexconjugate(Y1u12) + ZUL32*complexconjugate(Y1u22)) + ZA22*ZUL33*ZUR13*complexconjugate(Y2u33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_379 = Coupling(name = 'GC_379',
	 value = '(Y1u11*ZA21*complexconjugate(ZUL11)*complexconjugate(ZUR31) + Y1u21*ZA21*complexconjugate(ZUL12)*complexconjugate(ZUR31) + Y1u12*ZA21*complexconjugate(ZUL11)*complexconjugate(ZUR32) + Y1u22*ZA21*complexconjugate(ZUL12)*complexconjugate(ZUR32) + Y2u33*ZA22*complexconjugate(ZUL13)*complexconjugate(ZUR33))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_380 = Coupling(name = 'GC_380',
	 value = '-((ZA31*ZUR11*(ZUL31*complexconjugate(Y1u11) + ZUL32*complexconjugate(Y1u21)) + ZA31*ZUR12*(ZUL31*complexconjugate(Y1u12) + ZUL32*complexconjugate(Y1u22)) + ZA32*ZUL33*ZUR13*complexconjugate(Y2u33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_381 = Coupling(name = 'GC_381',
	 value = '(Y1u11*ZA31*complexconjugate(ZUL11)*complexconjugate(ZUR31) + Y1u21*ZA31*complexconjugate(ZUL12)*complexconjugate(ZUR31) + Y1u12*ZA31*complexconjugate(ZUL11)*complexconjugate(ZUR32) + Y1u22*ZA31*complexconjugate(ZUL12)*complexconjugate(ZUR32) + Y2u33*ZA32*complexconjugate(ZUL13)*complexconjugate(ZUR33))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_382 = Coupling(name = 'GC_382',
	 value = '-((ZA11*ZUR21*(ZUL11*complexconjugate(Y1u11) + ZUL12*complexconjugate(Y1u21)) + ZA11*ZUR22*(ZUL11*complexconjugate(Y1u12) + ZUL12*complexconjugate(Y1u22)) + ZA12*ZUL13*ZUR23*complexconjugate(Y2u33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_383 = Coupling(name = 'GC_383',
	 value = '(Y1u11*ZA11*complexconjugate(ZUL21)*complexconjugate(ZUR11) + Y1u21*ZA11*complexconjugate(ZUL22)*complexconjugate(ZUR11) + Y1u12*ZA11*complexconjugate(ZUL21)*complexconjugate(ZUR12) + Y1u22*ZA11*complexconjugate(ZUL22)*complexconjugate(ZUR12) + Y2u33*ZA12*complexconjugate(ZUL23)*complexconjugate(ZUR13))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_384 = Coupling(name = 'GC_384',
	 value = '-((ZA21*ZUR21*(ZUL11*complexconjugate(Y1u11) + ZUL12*complexconjugate(Y1u21)) + ZA21*ZUR22*(ZUL11*complexconjugate(Y1u12) + ZUL12*complexconjugate(Y1u22)) + ZA22*ZUL13*ZUR23*complexconjugate(Y2u33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_385 = Coupling(name = 'GC_385',
	 value = '(Y1u11*ZA21*complexconjugate(ZUL21)*complexconjugate(ZUR11) + Y1u21*ZA21*complexconjugate(ZUL22)*complexconjugate(ZUR11) + Y1u12*ZA21*complexconjugate(ZUL21)*complexconjugate(ZUR12) + Y1u22*ZA21*complexconjugate(ZUL22)*complexconjugate(ZUR12) + Y2u33*ZA22*complexconjugate(ZUL23)*complexconjugate(ZUR13))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_386 = Coupling(name = 'GC_386',
	 value = '-((ZA31*ZUR21*(ZUL11*complexconjugate(Y1u11) + ZUL12*complexconjugate(Y1u21)) + ZA31*ZUR22*(ZUL11*complexconjugate(Y1u12) + ZUL12*complexconjugate(Y1u22)) + ZA32*ZUL13*ZUR23*complexconjugate(Y2u33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_387 = Coupling(name = 'GC_387',
	 value = '(Y1u11*ZA31*complexconjugate(ZUL21)*complexconjugate(ZUR11) + Y1u21*ZA31*complexconjugate(ZUL22)*complexconjugate(ZUR11) + Y1u12*ZA31*complexconjugate(ZUL21)*complexconjugate(ZUR12) + Y1u22*ZA31*complexconjugate(ZUL22)*complexconjugate(ZUR12) + Y2u33*ZA32*complexconjugate(ZUL23)*complexconjugate(ZUR13))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_388 = Coupling(name = 'GC_388',
	 value = '-((ZA11*ZUR21*(ZUL21*complexconjugate(Y1u11) + ZUL22*complexconjugate(Y1u21)) + ZA11*ZUR22*(ZUL21*complexconjugate(Y1u12) + ZUL22*complexconjugate(Y1u22)) + ZA12*ZUL23*ZUR23*complexconjugate(Y2u33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_389 = Coupling(name = 'GC_389',
	 value = '(Y1u11*ZA11*complexconjugate(ZUL21)*complexconjugate(ZUR21) + Y1u21*ZA11*complexconjugate(ZUL22)*complexconjugate(ZUR21) + Y1u12*ZA11*complexconjugate(ZUL21)*complexconjugate(ZUR22) + Y1u22*ZA11*complexconjugate(ZUL22)*complexconjugate(ZUR22) + Y2u33*ZA12*complexconjugate(ZUL23)*complexconjugate(ZUR23))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_390 = Coupling(name = 'GC_390',
	 value = '-((ZA21*ZUR21*(ZUL21*complexconjugate(Y1u11) + ZUL22*complexconjugate(Y1u21)) + ZA21*ZUR22*(ZUL21*complexconjugate(Y1u12) + ZUL22*complexconjugate(Y1u22)) + ZA22*ZUL23*ZUR23*complexconjugate(Y2u33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_391 = Coupling(name = 'GC_391',
	 value = '(Y1u11*ZA21*complexconjugate(ZUL21)*complexconjugate(ZUR21) + Y1u21*ZA21*complexconjugate(ZUL22)*complexconjugate(ZUR21) + Y1u12*ZA21*complexconjugate(ZUL21)*complexconjugate(ZUR22) + Y1u22*ZA21*complexconjugate(ZUL22)*complexconjugate(ZUR22) + Y2u33*ZA22*complexconjugate(ZUL23)*complexconjugate(ZUR23))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_392 = Coupling(name = 'GC_392',
	 value = '-((ZA31*ZUR21*(ZUL21*complexconjugate(Y1u11) + ZUL22*complexconjugate(Y1u21)) + ZA31*ZUR22*(ZUL21*complexconjugate(Y1u12) + ZUL22*complexconjugate(Y1u22)) + ZA32*ZUL23*ZUR23*complexconjugate(Y2u33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_393 = Coupling(name = 'GC_393',
	 value = '(Y1u11*ZA31*complexconjugate(ZUL21)*complexconjugate(ZUR21) + Y1u21*ZA31*complexconjugate(ZUL22)*complexconjugate(ZUR21) + Y1u12*ZA31*complexconjugate(ZUL21)*complexconjugate(ZUR22) + Y1u22*ZA31*complexconjugate(ZUL22)*complexconjugate(ZUR22) + Y2u33*ZA32*complexconjugate(ZUL23)*complexconjugate(ZUR23))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_394 = Coupling(name = 'GC_394',
	 value = '-((ZA11*ZUR21*(ZUL31*complexconjugate(Y1u11) + ZUL32*complexconjugate(Y1u21)) + ZA11*ZUR22*(ZUL31*complexconjugate(Y1u12) + ZUL32*complexconjugate(Y1u22)) + ZA12*ZUL33*ZUR23*complexconjugate(Y2u33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_395 = Coupling(name = 'GC_395',
	 value = '(Y1u11*ZA11*complexconjugate(ZUL21)*complexconjugate(ZUR31) + Y1u21*ZA11*complexconjugate(ZUL22)*complexconjugate(ZUR31) + Y1u12*ZA11*complexconjugate(ZUL21)*complexconjugate(ZUR32) + Y1u22*ZA11*complexconjugate(ZUL22)*complexconjugate(ZUR32) + Y2u33*ZA12*complexconjugate(ZUL23)*complexconjugate(ZUR33))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_396 = Coupling(name = 'GC_396',
	 value = '-((ZA21*ZUR21*(ZUL31*complexconjugate(Y1u11) + ZUL32*complexconjugate(Y1u21)) + ZA21*ZUR22*(ZUL31*complexconjugate(Y1u12) + ZUL32*complexconjugate(Y1u22)) + ZA22*ZUL33*ZUR23*complexconjugate(Y2u33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_397 = Coupling(name = 'GC_397',
	 value = '(Y1u11*ZA21*complexconjugate(ZUL21)*complexconjugate(ZUR31) + Y1u21*ZA21*complexconjugate(ZUL22)*complexconjugate(ZUR31) + Y1u12*ZA21*complexconjugate(ZUL21)*complexconjugate(ZUR32) + Y1u22*ZA21*complexconjugate(ZUL22)*complexconjugate(ZUR32) + Y2u33*ZA22*complexconjugate(ZUL23)*complexconjugate(ZUR33))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_398 = Coupling(name = 'GC_398',
	 value = '-((ZA31*ZUR21*(ZUL31*complexconjugate(Y1u11) + ZUL32*complexconjugate(Y1u21)) + ZA31*ZUR22*(ZUL31*complexconjugate(Y1u12) + ZUL32*complexconjugate(Y1u22)) + ZA32*ZUL33*ZUR23*complexconjugate(Y2u33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_399 = Coupling(name = 'GC_399',
	 value = '(Y1u11*ZA31*complexconjugate(ZUL21)*complexconjugate(ZUR31) + Y1u21*ZA31*complexconjugate(ZUL22)*complexconjugate(ZUR31) + Y1u12*ZA31*complexconjugate(ZUL21)*complexconjugate(ZUR32) + Y1u22*ZA31*complexconjugate(ZUL22)*complexconjugate(ZUR32) + Y2u33*ZA32*complexconjugate(ZUL23)*complexconjugate(ZUR33))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_400 = Coupling(name = 'GC_400',
	 value = '-((ZA11*ZUR31*(ZUL11*complexconjugate(Y1u11) + ZUL12*complexconjugate(Y1u21)) + ZA11*ZUR32*(ZUL11*complexconjugate(Y1u12) + ZUL12*complexconjugate(Y1u22)) + ZA12*ZUL13*ZUR33*complexconjugate(Y2u33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_401 = Coupling(name = 'GC_401',
	 value = '(Y1u11*ZA11*complexconjugate(ZUL31)*complexconjugate(ZUR11) + Y1u21*ZA11*complexconjugate(ZUL32)*complexconjugate(ZUR11) + Y1u12*ZA11*complexconjugate(ZUL31)*complexconjugate(ZUR12) + Y1u22*ZA11*complexconjugate(ZUL32)*complexconjugate(ZUR12) + Y2u33*ZA12*complexconjugate(ZUL33)*complexconjugate(ZUR13))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_402 = Coupling(name = 'GC_402',
	 value = '-((ZA21*ZUR31*(ZUL11*complexconjugate(Y1u11) + ZUL12*complexconjugate(Y1u21)) + ZA21*ZUR32*(ZUL11*complexconjugate(Y1u12) + ZUL12*complexconjugate(Y1u22)) + ZA22*ZUL13*ZUR33*complexconjugate(Y2u33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_403 = Coupling(name = 'GC_403',
	 value = '(Y1u11*ZA21*complexconjugate(ZUL31)*complexconjugate(ZUR11) + Y1u21*ZA21*complexconjugate(ZUL32)*complexconjugate(ZUR11) + Y1u12*ZA21*complexconjugate(ZUL31)*complexconjugate(ZUR12) + Y1u22*ZA21*complexconjugate(ZUL32)*complexconjugate(ZUR12) + Y2u33*ZA22*complexconjugate(ZUL33)*complexconjugate(ZUR13))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_404 = Coupling(name = 'GC_404',
	 value = '-((ZA31*ZUR31*(ZUL11*complexconjugate(Y1u11) + ZUL12*complexconjugate(Y1u21)) + ZA31*ZUR32*(ZUL11*complexconjugate(Y1u12) + ZUL12*complexconjugate(Y1u22)) + ZA32*ZUL13*ZUR33*complexconjugate(Y2u33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_405 = Coupling(name = 'GC_405',
	 value = '(Y1u11*ZA31*complexconjugate(ZUL31)*complexconjugate(ZUR11) + Y1u21*ZA31*complexconjugate(ZUL32)*complexconjugate(ZUR11) + Y1u12*ZA31*complexconjugate(ZUL31)*complexconjugate(ZUR12) + Y1u22*ZA31*complexconjugate(ZUL32)*complexconjugate(ZUR12) + Y2u33*ZA32*complexconjugate(ZUL33)*complexconjugate(ZUR13))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_406 = Coupling(name = 'GC_406',
	 value = '-((ZA11*ZUR31*(ZUL21*complexconjugate(Y1u11) + ZUL22*complexconjugate(Y1u21)) + ZA11*ZUR32*(ZUL21*complexconjugate(Y1u12) + ZUL22*complexconjugate(Y1u22)) + ZA12*ZUL23*ZUR33*complexconjugate(Y2u33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_407 = Coupling(name = 'GC_407',
	 value = '(Y1u11*ZA11*complexconjugate(ZUL31)*complexconjugate(ZUR21) + Y1u21*ZA11*complexconjugate(ZUL32)*complexconjugate(ZUR21) + Y1u12*ZA11*complexconjugate(ZUL31)*complexconjugate(ZUR22) + Y1u22*ZA11*complexconjugate(ZUL32)*complexconjugate(ZUR22) + Y2u33*ZA12*complexconjugate(ZUL33)*complexconjugate(ZUR23))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_408 = Coupling(name = 'GC_408',
	 value = '-((ZA21*ZUR31*(ZUL21*complexconjugate(Y1u11) + ZUL22*complexconjugate(Y1u21)) + ZA21*ZUR32*(ZUL21*complexconjugate(Y1u12) + ZUL22*complexconjugate(Y1u22)) + ZA22*ZUL23*ZUR33*complexconjugate(Y2u33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_409 = Coupling(name = 'GC_409',
	 value = '(Y1u11*ZA21*complexconjugate(ZUL31)*complexconjugate(ZUR21) + Y1u21*ZA21*complexconjugate(ZUL32)*complexconjugate(ZUR21) + Y1u12*ZA21*complexconjugate(ZUL31)*complexconjugate(ZUR22) + Y1u22*ZA21*complexconjugate(ZUL32)*complexconjugate(ZUR22) + Y2u33*ZA22*complexconjugate(ZUL33)*complexconjugate(ZUR23))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_410 = Coupling(name = 'GC_410',
	 value = '-((ZA31*ZUR31*(ZUL21*complexconjugate(Y1u11) + ZUL22*complexconjugate(Y1u21)) + ZA31*ZUR32*(ZUL21*complexconjugate(Y1u12) + ZUL22*complexconjugate(Y1u22)) + ZA32*ZUL23*ZUR33*complexconjugate(Y2u33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_411 = Coupling(name = 'GC_411',
	 value = '(Y1u11*ZA31*complexconjugate(ZUL31)*complexconjugate(ZUR21) + Y1u21*ZA31*complexconjugate(ZUL32)*complexconjugate(ZUR21) + Y1u12*ZA31*complexconjugate(ZUL31)*complexconjugate(ZUR22) + Y1u22*ZA31*complexconjugate(ZUL32)*complexconjugate(ZUR22) + Y2u33*ZA32*complexconjugate(ZUL33)*complexconjugate(ZUR23))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_412 = Coupling(name = 'GC_412',
	 value = '-((ZA11*ZUR31*(ZUL31*complexconjugate(Y1u11) + ZUL32*complexconjugate(Y1u21)) + ZA11*ZUR32*(ZUL31*complexconjugate(Y1u12) + ZUL32*complexconjugate(Y1u22)) + ZA12*ZUL33*ZUR33*complexconjugate(Y2u33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_413 = Coupling(name = 'GC_413',
	 value = '(Y1u11*ZA11*complexconjugate(ZUL31)*complexconjugate(ZUR31) + Y1u21*ZA11*complexconjugate(ZUL32)*complexconjugate(ZUR31) + Y1u12*ZA11*complexconjugate(ZUL31)*complexconjugate(ZUR32) + Y1u22*ZA11*complexconjugate(ZUL32)*complexconjugate(ZUR32) + Y2u33*ZA12*complexconjugate(ZUL33)*complexconjugate(ZUR33))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_414 = Coupling(name = 'GC_414',
	 value = '-((ZA21*ZUR31*(ZUL31*complexconjugate(Y1u11) + ZUL32*complexconjugate(Y1u21)) + ZA21*ZUR32*(ZUL31*complexconjugate(Y1u12) + ZUL32*complexconjugate(Y1u22)) + ZA22*ZUL33*ZUR33*complexconjugate(Y2u33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_415 = Coupling(name = 'GC_415',
	 value = '(Y1u11*ZA21*complexconjugate(ZUL31)*complexconjugate(ZUR31) + Y1u21*ZA21*complexconjugate(ZUL32)*complexconjugate(ZUR31) + Y1u12*ZA21*complexconjugate(ZUL31)*complexconjugate(ZUR32) + Y1u22*ZA21*complexconjugate(ZUL32)*complexconjugate(ZUR32) + Y2u33*ZA22*complexconjugate(ZUL33)*complexconjugate(ZUR33))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_416 = Coupling(name = 'GC_416',
	 value = '-((ZA31*ZUR31*(ZUL31*complexconjugate(Y1u11) + ZUL32*complexconjugate(Y1u21)) + ZA31*ZUR32*(ZUL31*complexconjugate(Y1u12) + ZUL32*complexconjugate(Y1u22)) + ZA32*ZUL33*ZUR33*complexconjugate(Y2u33))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_417 = Coupling(name = 'GC_417',
	 value = '(Y1u11*ZA31*complexconjugate(ZUL31)*complexconjugate(ZUR31) + Y1u21*ZA31*complexconjugate(ZUL32)*complexconjugate(ZUR31) + Y1u12*ZA31*complexconjugate(ZUL31)*complexconjugate(ZUR32) + Y1u22*ZA31*complexconjugate(ZUL32)*complexconjugate(ZUR32) + Y2u33*ZA32*complexconjugate(ZUL33)*complexconjugate(ZUR33))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_418 = Coupling(name = 'GC_418',
	 value = '-(Vv14*Vv16*ZA13*complexconjugate(C13) + Vv15*Vv16*ZA13*complexconjugate(C23) + Vv14*Vv16*ZA13*complexconjugate(C31) + Vv15*Vv16*ZA13*complexconjugate(C32) + 2*Vv11*Vv14*ZA11*complexconjugate(Y1n11) + 2*Vv11*Vv15*ZA11*complexconjugate(Y1n12) + 2*Vv12*Vv14*ZA11*complexconjugate(Y1n21) + Vv14*(ZA13*(2*Vv14*complexconjugate(BB11) - Vv15*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv16*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv11*ZA11*complexconjugate(Y1n11) + 2*Vv12*ZA11*complexconjugate(Y1n21)) + 2*Vv12*Vv15*ZA11*complexconjugate(Y1n22) + Vv15*(ZA13*(-(Vv14*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv15*complexconjugate(BB22) + Vv16*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv11*ZA11*complexconjugate(Y1n12) + 2*Vv12*ZA11*complexconjugate(Y1n22)) + 4*Vv13*Vv16*ZA12*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_419 = Coupling(name = 'GC_419',
	 value = '(4*Y1n11*ZA11*complexconjugate(Vv11)*complexconjugate(Vv14) + 4*Y1n21*ZA11*complexconjugate(Vv12)*complexconjugate(Vv14) + 2*BB11*ZA13*complexconjugate(Vv14)**2 + 4*Y1n12*ZA11*complexconjugate(Vv11)*complexconjugate(Vv15) + 4*Y1n22*ZA11*complexconjugate(Vv12)*complexconjugate(Vv15) - 2*BB12*ZA13*complexconjugate(Vv14)*complexconjugate(Vv15) - 2*BB21*ZA13*complexconjugate(Vv14)*complexconjugate(Vv15) - 2*BB22*ZA13*complexconjugate(Vv15)**2 + 4*Y2n33*ZA12*complexconjugate(Vv13)*complexconjugate(Vv16) + 2*C13*ZA13*complexconjugate(Vv14)*complexconjugate(Vv16) + 2*C31*ZA13*complexconjugate(Vv14)*complexconjugate(Vv16) + 2*C23*ZA13*complexconjugate(Vv15)*complexconjugate(Vv16) + 2*C32*ZA13*complexconjugate(Vv15)*complexconjugate(Vv16))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_420 = Coupling(name = 'GC_420',
	 value = '-(Vv14*Vv16*ZA23*complexconjugate(C13) + Vv15*Vv16*ZA23*complexconjugate(C23) + Vv14*Vv16*ZA23*complexconjugate(C31) + Vv15*Vv16*ZA23*complexconjugate(C32) + 2*Vv11*Vv14*ZA21*complexconjugate(Y1n11) + 2*Vv11*Vv15*ZA21*complexconjugate(Y1n12) + 2*Vv12*Vv14*ZA21*complexconjugate(Y1n21) + Vv14*(ZA23*(2*Vv14*complexconjugate(BB11) - Vv15*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv16*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv11*ZA21*complexconjugate(Y1n11) + 2*Vv12*ZA21*complexconjugate(Y1n21)) + 2*Vv12*Vv15*ZA21*complexconjugate(Y1n22) + Vv15*(ZA23*(-(Vv14*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv15*complexconjugate(BB22) + Vv16*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv11*ZA21*complexconjugate(Y1n12) + 2*Vv12*ZA21*complexconjugate(Y1n22)) + 4*Vv13*Vv16*ZA22*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_421 = Coupling(name = 'GC_421',
	 value = '(4*Y1n11*ZA21*complexconjugate(Vv11)*complexconjugate(Vv14) + 4*Y1n21*ZA21*complexconjugate(Vv12)*complexconjugate(Vv14) + 2*BB11*ZA23*complexconjugate(Vv14)**2 + 4*Y1n12*ZA21*complexconjugate(Vv11)*complexconjugate(Vv15) + 4*Y1n22*ZA21*complexconjugate(Vv12)*complexconjugate(Vv15) - 2*BB12*ZA23*complexconjugate(Vv14)*complexconjugate(Vv15) - 2*BB21*ZA23*complexconjugate(Vv14)*complexconjugate(Vv15) - 2*BB22*ZA23*complexconjugate(Vv15)**2 + 4*Y2n33*ZA22*complexconjugate(Vv13)*complexconjugate(Vv16) + 2*C13*ZA23*complexconjugate(Vv14)*complexconjugate(Vv16) + 2*C31*ZA23*complexconjugate(Vv14)*complexconjugate(Vv16) + 2*C23*ZA23*complexconjugate(Vv15)*complexconjugate(Vv16) + 2*C32*ZA23*complexconjugate(Vv15)*complexconjugate(Vv16))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_422 = Coupling(name = 'GC_422',
	 value = '-(Vv14*Vv16*ZA33*complexconjugate(C13) + Vv15*Vv16*ZA33*complexconjugate(C23) + Vv14*Vv16*ZA33*complexconjugate(C31) + Vv15*Vv16*ZA33*complexconjugate(C32) + 2*Vv11*Vv14*ZA31*complexconjugate(Y1n11) + 2*Vv11*Vv15*ZA31*complexconjugate(Y1n12) + 2*Vv12*Vv14*ZA31*complexconjugate(Y1n21) + Vv14*(ZA33*(2*Vv14*complexconjugate(BB11) - Vv15*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv16*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv11*ZA31*complexconjugate(Y1n11) + 2*Vv12*ZA31*complexconjugate(Y1n21)) + 2*Vv12*Vv15*ZA31*complexconjugate(Y1n22) + Vv15*(ZA33*(-(Vv14*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv15*complexconjugate(BB22) + Vv16*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv11*ZA31*complexconjugate(Y1n12) + 2*Vv12*ZA31*complexconjugate(Y1n22)) + 4*Vv13*Vv16*ZA32*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_423 = Coupling(name = 'GC_423',
	 value = '(4*Y1n11*ZA31*complexconjugate(Vv11)*complexconjugate(Vv14) + 4*Y1n21*ZA31*complexconjugate(Vv12)*complexconjugate(Vv14) + 2*BB11*ZA33*complexconjugate(Vv14)**2 + 4*Y1n12*ZA31*complexconjugate(Vv11)*complexconjugate(Vv15) + 4*Y1n22*ZA31*complexconjugate(Vv12)*complexconjugate(Vv15) - 2*BB12*ZA33*complexconjugate(Vv14)*complexconjugate(Vv15) - 2*BB21*ZA33*complexconjugate(Vv14)*complexconjugate(Vv15) - 2*BB22*ZA33*complexconjugate(Vv15)**2 + 4*Y2n33*ZA32*complexconjugate(Vv13)*complexconjugate(Vv16) + 2*C13*ZA33*complexconjugate(Vv14)*complexconjugate(Vv16) + 2*C31*ZA33*complexconjugate(Vv14)*complexconjugate(Vv16) + 2*C23*ZA33*complexconjugate(Vv15)*complexconjugate(Vv16) + 2*C32*ZA33*complexconjugate(Vv15)*complexconjugate(Vv16))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_424 = Coupling(name = 'GC_424',
	 value = '-(Vv16*Vv24*ZA13*complexconjugate(C13) + Vv16*Vv25*ZA13*complexconjugate(C23) + Vv16*Vv24*ZA13*complexconjugate(C31) + Vv16*Vv25*ZA13*complexconjugate(C32) + 2*Vv11*Vv24*ZA11*complexconjugate(Y1n11) + 2*Vv11*Vv25*ZA11*complexconjugate(Y1n12) + 2*Vv12*Vv24*ZA11*complexconjugate(Y1n21) + Vv14*(ZA13*(2*Vv24*complexconjugate(BB11) - Vv25*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv26*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv21*ZA11*complexconjugate(Y1n11) + 2*Vv22*ZA11*complexconjugate(Y1n21)) + 2*Vv12*Vv25*ZA11*complexconjugate(Y1n22) + Vv15*(ZA13*(-(Vv24*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv25*complexconjugate(BB22) + Vv26*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv21*ZA11*complexconjugate(Y1n12) + 2*Vv22*ZA11*complexconjugate(Y1n22)) + 2*Vv16*Vv23*ZA12*complexconjugate(Y2n33) + 2*Vv13*Vv26*ZA12*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_425 = Coupling(name = 'GC_425',
	 value = '(2*Y1n21*ZA11*complexconjugate(Vv14)*complexconjugate(Vv22) + 2*Y1n22*ZA11*complexconjugate(Vv15)*complexconjugate(Vv22) + 2*Y2n33*ZA12*complexconjugate(Vv16)*complexconjugate(Vv23) + 2*Y1n21*ZA11*complexconjugate(Vv12)*complexconjugate(Vv24) + 2*BB11*ZA13*complexconjugate(Vv14)*complexconjugate(Vv24) - BB12*ZA13*complexconjugate(Vv15)*complexconjugate(Vv24) - BB21*ZA13*complexconjugate(Vv15)*complexconjugate(Vv24) + C13*ZA13*complexconjugate(Vv16)*complexconjugate(Vv24) + C31*ZA13*complexconjugate(Vv16)*complexconjugate(Vv24) + 2*Y1n11*ZA11*(complexconjugate(Vv14)*complexconjugate(Vv21) + complexconjugate(Vv11)*complexconjugate(Vv24)) + 2*Y1n22*ZA11*complexconjugate(Vv12)*complexconjugate(Vv25) - BB12*ZA13*complexconjugate(Vv14)*complexconjugate(Vv25) - BB21*ZA13*complexconjugate(Vv14)*complexconjugate(Vv25) - 2*BB22*ZA13*complexconjugate(Vv15)*complexconjugate(Vv25) + C23*ZA13*complexconjugate(Vv16)*complexconjugate(Vv25) + C32*ZA13*complexconjugate(Vv16)*complexconjugate(Vv25) + 2*Y1n12*ZA11*(complexconjugate(Vv15)*complexconjugate(Vv21) + complexconjugate(Vv11)*complexconjugate(Vv25)) + 2*Y2n33*ZA12*complexconjugate(Vv13)*complexconjugate(Vv26) + C13*ZA13*complexconjugate(Vv14)*complexconjugate(Vv26) + C31*ZA13*complexconjugate(Vv14)*complexconjugate(Vv26) + C23*ZA13*complexconjugate(Vv15)*complexconjugate(Vv26) + C32*ZA13*complexconjugate(Vv15)*complexconjugate(Vv26))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_426 = Coupling(name = 'GC_426',
	 value = '-(Vv16*Vv24*ZA23*complexconjugate(C13) + Vv16*Vv25*ZA23*complexconjugate(C23) + Vv16*Vv24*ZA23*complexconjugate(C31) + Vv16*Vv25*ZA23*complexconjugate(C32) + 2*Vv11*Vv24*ZA21*complexconjugate(Y1n11) + 2*Vv11*Vv25*ZA21*complexconjugate(Y1n12) + 2*Vv12*Vv24*ZA21*complexconjugate(Y1n21) + Vv14*(ZA23*(2*Vv24*complexconjugate(BB11) - Vv25*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv26*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv21*ZA21*complexconjugate(Y1n11) + 2*Vv22*ZA21*complexconjugate(Y1n21)) + 2*Vv12*Vv25*ZA21*complexconjugate(Y1n22) + Vv15*(ZA23*(-(Vv24*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv25*complexconjugate(BB22) + Vv26*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv21*ZA21*complexconjugate(Y1n12) + 2*Vv22*ZA21*complexconjugate(Y1n22)) + 2*Vv16*Vv23*ZA22*complexconjugate(Y2n33) + 2*Vv13*Vv26*ZA22*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_427 = Coupling(name = 'GC_427',
	 value = '(2*Y1n21*ZA21*complexconjugate(Vv14)*complexconjugate(Vv22) + 2*Y1n22*ZA21*complexconjugate(Vv15)*complexconjugate(Vv22) + 2*Y2n33*ZA22*complexconjugate(Vv16)*complexconjugate(Vv23) + 2*Y1n21*ZA21*complexconjugate(Vv12)*complexconjugate(Vv24) + 2*BB11*ZA23*complexconjugate(Vv14)*complexconjugate(Vv24) - BB12*ZA23*complexconjugate(Vv15)*complexconjugate(Vv24) - BB21*ZA23*complexconjugate(Vv15)*complexconjugate(Vv24) + C13*ZA23*complexconjugate(Vv16)*complexconjugate(Vv24) + C31*ZA23*complexconjugate(Vv16)*complexconjugate(Vv24) + 2*Y1n11*ZA21*(complexconjugate(Vv14)*complexconjugate(Vv21) + complexconjugate(Vv11)*complexconjugate(Vv24)) + 2*Y1n22*ZA21*complexconjugate(Vv12)*complexconjugate(Vv25) - BB12*ZA23*complexconjugate(Vv14)*complexconjugate(Vv25) - BB21*ZA23*complexconjugate(Vv14)*complexconjugate(Vv25) - 2*BB22*ZA23*complexconjugate(Vv15)*complexconjugate(Vv25) + C23*ZA23*complexconjugate(Vv16)*complexconjugate(Vv25) + C32*ZA23*complexconjugate(Vv16)*complexconjugate(Vv25) + 2*Y1n12*ZA21*(complexconjugate(Vv15)*complexconjugate(Vv21) + complexconjugate(Vv11)*complexconjugate(Vv25)) + 2*Y2n33*ZA22*complexconjugate(Vv13)*complexconjugate(Vv26) + C13*ZA23*complexconjugate(Vv14)*complexconjugate(Vv26) + C31*ZA23*complexconjugate(Vv14)*complexconjugate(Vv26) + C23*ZA23*complexconjugate(Vv15)*complexconjugate(Vv26) + C32*ZA23*complexconjugate(Vv15)*complexconjugate(Vv26))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_428 = Coupling(name = 'GC_428',
	 value = '-(Vv16*Vv24*ZA33*complexconjugate(C13) + Vv16*Vv25*ZA33*complexconjugate(C23) + Vv16*Vv24*ZA33*complexconjugate(C31) + Vv16*Vv25*ZA33*complexconjugate(C32) + 2*Vv11*Vv24*ZA31*complexconjugate(Y1n11) + 2*Vv11*Vv25*ZA31*complexconjugate(Y1n12) + 2*Vv12*Vv24*ZA31*complexconjugate(Y1n21) + Vv14*(ZA33*(2*Vv24*complexconjugate(BB11) - Vv25*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv26*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv21*ZA31*complexconjugate(Y1n11) + 2*Vv22*ZA31*complexconjugate(Y1n21)) + 2*Vv12*Vv25*ZA31*complexconjugate(Y1n22) + Vv15*(ZA33*(-(Vv24*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv25*complexconjugate(BB22) + Vv26*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv21*ZA31*complexconjugate(Y1n12) + 2*Vv22*ZA31*complexconjugate(Y1n22)) + 2*Vv16*Vv23*ZA32*complexconjugate(Y2n33) + 2*Vv13*Vv26*ZA32*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_429 = Coupling(name = 'GC_429',
	 value = '(2*Y1n21*ZA31*complexconjugate(Vv14)*complexconjugate(Vv22) + 2*Y1n22*ZA31*complexconjugate(Vv15)*complexconjugate(Vv22) + 2*Y2n33*ZA32*complexconjugate(Vv16)*complexconjugate(Vv23) + 2*Y1n21*ZA31*complexconjugate(Vv12)*complexconjugate(Vv24) + 2*BB11*ZA33*complexconjugate(Vv14)*complexconjugate(Vv24) - BB12*ZA33*complexconjugate(Vv15)*complexconjugate(Vv24) - BB21*ZA33*complexconjugate(Vv15)*complexconjugate(Vv24) + C13*ZA33*complexconjugate(Vv16)*complexconjugate(Vv24) + C31*ZA33*complexconjugate(Vv16)*complexconjugate(Vv24) + 2*Y1n11*ZA31*(complexconjugate(Vv14)*complexconjugate(Vv21) + complexconjugate(Vv11)*complexconjugate(Vv24)) + 2*Y1n22*ZA31*complexconjugate(Vv12)*complexconjugate(Vv25) - BB12*ZA33*complexconjugate(Vv14)*complexconjugate(Vv25) - BB21*ZA33*complexconjugate(Vv14)*complexconjugate(Vv25) - 2*BB22*ZA33*complexconjugate(Vv15)*complexconjugate(Vv25) + C23*ZA33*complexconjugate(Vv16)*complexconjugate(Vv25) + C32*ZA33*complexconjugate(Vv16)*complexconjugate(Vv25) + 2*Y1n12*ZA31*(complexconjugate(Vv15)*complexconjugate(Vv21) + complexconjugate(Vv11)*complexconjugate(Vv25)) + 2*Y2n33*ZA32*complexconjugate(Vv13)*complexconjugate(Vv26) + C13*ZA33*complexconjugate(Vv14)*complexconjugate(Vv26) + C31*ZA33*complexconjugate(Vv14)*complexconjugate(Vv26) + C23*ZA33*complexconjugate(Vv15)*complexconjugate(Vv26) + C32*ZA33*complexconjugate(Vv15)*complexconjugate(Vv26))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_430 = Coupling(name = 'GC_430',
	 value = '-(Vv16*Vv34*ZA13*complexconjugate(C13) + Vv16*Vv35*ZA13*complexconjugate(C23) + Vv16*Vv34*ZA13*complexconjugate(C31) + Vv16*Vv35*ZA13*complexconjugate(C32) + 2*Vv11*Vv34*ZA11*complexconjugate(Y1n11) + 2*Vv11*Vv35*ZA11*complexconjugate(Y1n12) + 2*Vv12*Vv34*ZA11*complexconjugate(Y1n21) + Vv14*(ZA13*(2*Vv34*complexconjugate(BB11) - Vv35*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv36*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv31*ZA11*complexconjugate(Y1n11) + 2*Vv32*ZA11*complexconjugate(Y1n21)) + 2*Vv12*Vv35*ZA11*complexconjugate(Y1n22) + Vv15*(ZA13*(-(Vv34*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv35*complexconjugate(BB22) + Vv36*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv31*ZA11*complexconjugate(Y1n12) + 2*Vv32*ZA11*complexconjugate(Y1n22)) + 2*Vv16*Vv33*ZA12*complexconjugate(Y2n33) + 2*Vv13*Vv36*ZA12*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_431 = Coupling(name = 'GC_431',
	 value = '(2*Y1n21*ZA11*complexconjugate(Vv14)*complexconjugate(Vv32) + 2*Y1n22*ZA11*complexconjugate(Vv15)*complexconjugate(Vv32) + 2*Y2n33*ZA12*complexconjugate(Vv16)*complexconjugate(Vv33) + 2*Y1n21*ZA11*complexconjugate(Vv12)*complexconjugate(Vv34) + 2*BB11*ZA13*complexconjugate(Vv14)*complexconjugate(Vv34) - BB12*ZA13*complexconjugate(Vv15)*complexconjugate(Vv34) - BB21*ZA13*complexconjugate(Vv15)*complexconjugate(Vv34) + C13*ZA13*complexconjugate(Vv16)*complexconjugate(Vv34) + C31*ZA13*complexconjugate(Vv16)*complexconjugate(Vv34) + 2*Y1n11*ZA11*(complexconjugate(Vv14)*complexconjugate(Vv31) + complexconjugate(Vv11)*complexconjugate(Vv34)) + 2*Y1n22*ZA11*complexconjugate(Vv12)*complexconjugate(Vv35) - BB12*ZA13*complexconjugate(Vv14)*complexconjugate(Vv35) - BB21*ZA13*complexconjugate(Vv14)*complexconjugate(Vv35) - 2*BB22*ZA13*complexconjugate(Vv15)*complexconjugate(Vv35) + C23*ZA13*complexconjugate(Vv16)*complexconjugate(Vv35) + C32*ZA13*complexconjugate(Vv16)*complexconjugate(Vv35) + 2*Y1n12*ZA11*(complexconjugate(Vv15)*complexconjugate(Vv31) + complexconjugate(Vv11)*complexconjugate(Vv35)) + 2*Y2n33*ZA12*complexconjugate(Vv13)*complexconjugate(Vv36) + C13*ZA13*complexconjugate(Vv14)*complexconjugate(Vv36) + C31*ZA13*complexconjugate(Vv14)*complexconjugate(Vv36) + C23*ZA13*complexconjugate(Vv15)*complexconjugate(Vv36) + C32*ZA13*complexconjugate(Vv15)*complexconjugate(Vv36))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_432 = Coupling(name = 'GC_432',
	 value = '-(Vv16*Vv34*ZA23*complexconjugate(C13) + Vv16*Vv35*ZA23*complexconjugate(C23) + Vv16*Vv34*ZA23*complexconjugate(C31) + Vv16*Vv35*ZA23*complexconjugate(C32) + 2*Vv11*Vv34*ZA21*complexconjugate(Y1n11) + 2*Vv11*Vv35*ZA21*complexconjugate(Y1n12) + 2*Vv12*Vv34*ZA21*complexconjugate(Y1n21) + Vv14*(ZA23*(2*Vv34*complexconjugate(BB11) - Vv35*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv36*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv31*ZA21*complexconjugate(Y1n11) + 2*Vv32*ZA21*complexconjugate(Y1n21)) + 2*Vv12*Vv35*ZA21*complexconjugate(Y1n22) + Vv15*(ZA23*(-(Vv34*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv35*complexconjugate(BB22) + Vv36*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv31*ZA21*complexconjugate(Y1n12) + 2*Vv32*ZA21*complexconjugate(Y1n22)) + 2*Vv16*Vv33*ZA22*complexconjugate(Y2n33) + 2*Vv13*Vv36*ZA22*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_433 = Coupling(name = 'GC_433',
	 value = '(2*Y1n21*ZA21*complexconjugate(Vv14)*complexconjugate(Vv32) + 2*Y1n22*ZA21*complexconjugate(Vv15)*complexconjugate(Vv32) + 2*Y2n33*ZA22*complexconjugate(Vv16)*complexconjugate(Vv33) + 2*Y1n21*ZA21*complexconjugate(Vv12)*complexconjugate(Vv34) + 2*BB11*ZA23*complexconjugate(Vv14)*complexconjugate(Vv34) - BB12*ZA23*complexconjugate(Vv15)*complexconjugate(Vv34) - BB21*ZA23*complexconjugate(Vv15)*complexconjugate(Vv34) + C13*ZA23*complexconjugate(Vv16)*complexconjugate(Vv34) + C31*ZA23*complexconjugate(Vv16)*complexconjugate(Vv34) + 2*Y1n11*ZA21*(complexconjugate(Vv14)*complexconjugate(Vv31) + complexconjugate(Vv11)*complexconjugate(Vv34)) + 2*Y1n22*ZA21*complexconjugate(Vv12)*complexconjugate(Vv35) - BB12*ZA23*complexconjugate(Vv14)*complexconjugate(Vv35) - BB21*ZA23*complexconjugate(Vv14)*complexconjugate(Vv35) - 2*BB22*ZA23*complexconjugate(Vv15)*complexconjugate(Vv35) + C23*ZA23*complexconjugate(Vv16)*complexconjugate(Vv35) + C32*ZA23*complexconjugate(Vv16)*complexconjugate(Vv35) + 2*Y1n12*ZA21*(complexconjugate(Vv15)*complexconjugate(Vv31) + complexconjugate(Vv11)*complexconjugate(Vv35)) + 2*Y2n33*ZA22*complexconjugate(Vv13)*complexconjugate(Vv36) + C13*ZA23*complexconjugate(Vv14)*complexconjugate(Vv36) + C31*ZA23*complexconjugate(Vv14)*complexconjugate(Vv36) + C23*ZA23*complexconjugate(Vv15)*complexconjugate(Vv36) + C32*ZA23*complexconjugate(Vv15)*complexconjugate(Vv36))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_434 = Coupling(name = 'GC_434',
	 value = '-(Vv16*Vv34*ZA33*complexconjugate(C13) + Vv16*Vv35*ZA33*complexconjugate(C23) + Vv16*Vv34*ZA33*complexconjugate(C31) + Vv16*Vv35*ZA33*complexconjugate(C32) + 2*Vv11*Vv34*ZA31*complexconjugate(Y1n11) + 2*Vv11*Vv35*ZA31*complexconjugate(Y1n12) + 2*Vv12*Vv34*ZA31*complexconjugate(Y1n21) + Vv14*(ZA33*(2*Vv34*complexconjugate(BB11) - Vv35*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv36*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv31*ZA31*complexconjugate(Y1n11) + 2*Vv32*ZA31*complexconjugate(Y1n21)) + 2*Vv12*Vv35*ZA31*complexconjugate(Y1n22) + Vv15*(ZA33*(-(Vv34*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv35*complexconjugate(BB22) + Vv36*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv31*ZA31*complexconjugate(Y1n12) + 2*Vv32*ZA31*complexconjugate(Y1n22)) + 2*Vv16*Vv33*ZA32*complexconjugate(Y2n33) + 2*Vv13*Vv36*ZA32*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_435 = Coupling(name = 'GC_435',
	 value = '(2*Y1n21*ZA31*complexconjugate(Vv14)*complexconjugate(Vv32) + 2*Y1n22*ZA31*complexconjugate(Vv15)*complexconjugate(Vv32) + 2*Y2n33*ZA32*complexconjugate(Vv16)*complexconjugate(Vv33) + 2*Y1n21*ZA31*complexconjugate(Vv12)*complexconjugate(Vv34) + 2*BB11*ZA33*complexconjugate(Vv14)*complexconjugate(Vv34) - BB12*ZA33*complexconjugate(Vv15)*complexconjugate(Vv34) - BB21*ZA33*complexconjugate(Vv15)*complexconjugate(Vv34) + C13*ZA33*complexconjugate(Vv16)*complexconjugate(Vv34) + C31*ZA33*complexconjugate(Vv16)*complexconjugate(Vv34) + 2*Y1n11*ZA31*(complexconjugate(Vv14)*complexconjugate(Vv31) + complexconjugate(Vv11)*complexconjugate(Vv34)) + 2*Y1n22*ZA31*complexconjugate(Vv12)*complexconjugate(Vv35) - BB12*ZA33*complexconjugate(Vv14)*complexconjugate(Vv35) - BB21*ZA33*complexconjugate(Vv14)*complexconjugate(Vv35) - 2*BB22*ZA33*complexconjugate(Vv15)*complexconjugate(Vv35) + C23*ZA33*complexconjugate(Vv16)*complexconjugate(Vv35) + C32*ZA33*complexconjugate(Vv16)*complexconjugate(Vv35) + 2*Y1n12*ZA31*(complexconjugate(Vv15)*complexconjugate(Vv31) + complexconjugate(Vv11)*complexconjugate(Vv35)) + 2*Y2n33*ZA32*complexconjugate(Vv13)*complexconjugate(Vv36) + C13*ZA33*complexconjugate(Vv14)*complexconjugate(Vv36) + C31*ZA33*complexconjugate(Vv14)*complexconjugate(Vv36) + C23*ZA33*complexconjugate(Vv15)*complexconjugate(Vv36) + C32*ZA33*complexconjugate(Vv15)*complexconjugate(Vv36))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_436 = Coupling(name = 'GC_436',
	 value = '-(Vv16*Vv44*ZA13*complexconjugate(C13) + Vv16*Vv45*ZA13*complexconjugate(C23) + Vv16*Vv44*ZA13*complexconjugate(C31) + Vv16*Vv45*ZA13*complexconjugate(C32) + 2*Vv11*Vv44*ZA11*complexconjugate(Y1n11) + 2*Vv11*Vv45*ZA11*complexconjugate(Y1n12) + 2*Vv12*Vv44*ZA11*complexconjugate(Y1n21) + Vv14*(ZA13*(2*Vv44*complexconjugate(BB11) - Vv45*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv46*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv41*ZA11*complexconjugate(Y1n11) + 2*Vv42*ZA11*complexconjugate(Y1n21)) + 2*Vv12*Vv45*ZA11*complexconjugate(Y1n22) + Vv15*(ZA13*(-(Vv44*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv45*complexconjugate(BB22) + Vv46*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv41*ZA11*complexconjugate(Y1n12) + 2*Vv42*ZA11*complexconjugate(Y1n22)) + 2*Vv16*Vv43*ZA12*complexconjugate(Y2n33) + 2*Vv13*Vv46*ZA12*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_437 = Coupling(name = 'GC_437',
	 value = '(2*Y1n21*ZA11*complexconjugate(Vv14)*complexconjugate(Vv42) + 2*Y1n22*ZA11*complexconjugate(Vv15)*complexconjugate(Vv42) + 2*Y2n33*ZA12*complexconjugate(Vv16)*complexconjugate(Vv43) + 2*Y1n21*ZA11*complexconjugate(Vv12)*complexconjugate(Vv44) + 2*BB11*ZA13*complexconjugate(Vv14)*complexconjugate(Vv44) - BB12*ZA13*complexconjugate(Vv15)*complexconjugate(Vv44) - BB21*ZA13*complexconjugate(Vv15)*complexconjugate(Vv44) + C13*ZA13*complexconjugate(Vv16)*complexconjugate(Vv44) + C31*ZA13*complexconjugate(Vv16)*complexconjugate(Vv44) + 2*Y1n11*ZA11*(complexconjugate(Vv14)*complexconjugate(Vv41) + complexconjugate(Vv11)*complexconjugate(Vv44)) + 2*Y1n22*ZA11*complexconjugate(Vv12)*complexconjugate(Vv45) - BB12*ZA13*complexconjugate(Vv14)*complexconjugate(Vv45) - BB21*ZA13*complexconjugate(Vv14)*complexconjugate(Vv45) - 2*BB22*ZA13*complexconjugate(Vv15)*complexconjugate(Vv45) + C23*ZA13*complexconjugate(Vv16)*complexconjugate(Vv45) + C32*ZA13*complexconjugate(Vv16)*complexconjugate(Vv45) + 2*Y1n12*ZA11*(complexconjugate(Vv15)*complexconjugate(Vv41) + complexconjugate(Vv11)*complexconjugate(Vv45)) + 2*Y2n33*ZA12*complexconjugate(Vv13)*complexconjugate(Vv46) + C13*ZA13*complexconjugate(Vv14)*complexconjugate(Vv46) + C31*ZA13*complexconjugate(Vv14)*complexconjugate(Vv46) + C23*ZA13*complexconjugate(Vv15)*complexconjugate(Vv46) + C32*ZA13*complexconjugate(Vv15)*complexconjugate(Vv46))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_438 = Coupling(name = 'GC_438',
	 value = '-(Vv16*Vv44*ZA23*complexconjugate(C13) + Vv16*Vv45*ZA23*complexconjugate(C23) + Vv16*Vv44*ZA23*complexconjugate(C31) + Vv16*Vv45*ZA23*complexconjugate(C32) + 2*Vv11*Vv44*ZA21*complexconjugate(Y1n11) + 2*Vv11*Vv45*ZA21*complexconjugate(Y1n12) + 2*Vv12*Vv44*ZA21*complexconjugate(Y1n21) + Vv14*(ZA23*(2*Vv44*complexconjugate(BB11) - Vv45*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv46*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv41*ZA21*complexconjugate(Y1n11) + 2*Vv42*ZA21*complexconjugate(Y1n21)) + 2*Vv12*Vv45*ZA21*complexconjugate(Y1n22) + Vv15*(ZA23*(-(Vv44*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv45*complexconjugate(BB22) + Vv46*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv41*ZA21*complexconjugate(Y1n12) + 2*Vv42*ZA21*complexconjugate(Y1n22)) + 2*Vv16*Vv43*ZA22*complexconjugate(Y2n33) + 2*Vv13*Vv46*ZA22*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_439 = Coupling(name = 'GC_439',
	 value = '(2*Y1n21*ZA21*complexconjugate(Vv14)*complexconjugate(Vv42) + 2*Y1n22*ZA21*complexconjugate(Vv15)*complexconjugate(Vv42) + 2*Y2n33*ZA22*complexconjugate(Vv16)*complexconjugate(Vv43) + 2*Y1n21*ZA21*complexconjugate(Vv12)*complexconjugate(Vv44) + 2*BB11*ZA23*complexconjugate(Vv14)*complexconjugate(Vv44) - BB12*ZA23*complexconjugate(Vv15)*complexconjugate(Vv44) - BB21*ZA23*complexconjugate(Vv15)*complexconjugate(Vv44) + C13*ZA23*complexconjugate(Vv16)*complexconjugate(Vv44) + C31*ZA23*complexconjugate(Vv16)*complexconjugate(Vv44) + 2*Y1n11*ZA21*(complexconjugate(Vv14)*complexconjugate(Vv41) + complexconjugate(Vv11)*complexconjugate(Vv44)) + 2*Y1n22*ZA21*complexconjugate(Vv12)*complexconjugate(Vv45) - BB12*ZA23*complexconjugate(Vv14)*complexconjugate(Vv45) - BB21*ZA23*complexconjugate(Vv14)*complexconjugate(Vv45) - 2*BB22*ZA23*complexconjugate(Vv15)*complexconjugate(Vv45) + C23*ZA23*complexconjugate(Vv16)*complexconjugate(Vv45) + C32*ZA23*complexconjugate(Vv16)*complexconjugate(Vv45) + 2*Y1n12*ZA21*(complexconjugate(Vv15)*complexconjugate(Vv41) + complexconjugate(Vv11)*complexconjugate(Vv45)) + 2*Y2n33*ZA22*complexconjugate(Vv13)*complexconjugate(Vv46) + C13*ZA23*complexconjugate(Vv14)*complexconjugate(Vv46) + C31*ZA23*complexconjugate(Vv14)*complexconjugate(Vv46) + C23*ZA23*complexconjugate(Vv15)*complexconjugate(Vv46) + C32*ZA23*complexconjugate(Vv15)*complexconjugate(Vv46))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_440 = Coupling(name = 'GC_440',
	 value = '-(Vv16*Vv44*ZA33*complexconjugate(C13) + Vv16*Vv45*ZA33*complexconjugate(C23) + Vv16*Vv44*ZA33*complexconjugate(C31) + Vv16*Vv45*ZA33*complexconjugate(C32) + 2*Vv11*Vv44*ZA31*complexconjugate(Y1n11) + 2*Vv11*Vv45*ZA31*complexconjugate(Y1n12) + 2*Vv12*Vv44*ZA31*complexconjugate(Y1n21) + Vv14*(ZA33*(2*Vv44*complexconjugate(BB11) - Vv45*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv46*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv41*ZA31*complexconjugate(Y1n11) + 2*Vv42*ZA31*complexconjugate(Y1n21)) + 2*Vv12*Vv45*ZA31*complexconjugate(Y1n22) + Vv15*(ZA33*(-(Vv44*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv45*complexconjugate(BB22) + Vv46*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv41*ZA31*complexconjugate(Y1n12) + 2*Vv42*ZA31*complexconjugate(Y1n22)) + 2*Vv16*Vv43*ZA32*complexconjugate(Y2n33) + 2*Vv13*Vv46*ZA32*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_441 = Coupling(name = 'GC_441',
	 value = '(2*Y1n21*ZA31*complexconjugate(Vv14)*complexconjugate(Vv42) + 2*Y1n22*ZA31*complexconjugate(Vv15)*complexconjugate(Vv42) + 2*Y2n33*ZA32*complexconjugate(Vv16)*complexconjugate(Vv43) + 2*Y1n21*ZA31*complexconjugate(Vv12)*complexconjugate(Vv44) + 2*BB11*ZA33*complexconjugate(Vv14)*complexconjugate(Vv44) - BB12*ZA33*complexconjugate(Vv15)*complexconjugate(Vv44) - BB21*ZA33*complexconjugate(Vv15)*complexconjugate(Vv44) + C13*ZA33*complexconjugate(Vv16)*complexconjugate(Vv44) + C31*ZA33*complexconjugate(Vv16)*complexconjugate(Vv44) + 2*Y1n11*ZA31*(complexconjugate(Vv14)*complexconjugate(Vv41) + complexconjugate(Vv11)*complexconjugate(Vv44)) + 2*Y1n22*ZA31*complexconjugate(Vv12)*complexconjugate(Vv45) - BB12*ZA33*complexconjugate(Vv14)*complexconjugate(Vv45) - BB21*ZA33*complexconjugate(Vv14)*complexconjugate(Vv45) - 2*BB22*ZA33*complexconjugate(Vv15)*complexconjugate(Vv45) + C23*ZA33*complexconjugate(Vv16)*complexconjugate(Vv45) + C32*ZA33*complexconjugate(Vv16)*complexconjugate(Vv45) + 2*Y1n12*ZA31*(complexconjugate(Vv15)*complexconjugate(Vv41) + complexconjugate(Vv11)*complexconjugate(Vv45)) + 2*Y2n33*ZA32*complexconjugate(Vv13)*complexconjugate(Vv46) + C13*ZA33*complexconjugate(Vv14)*complexconjugate(Vv46) + C31*ZA33*complexconjugate(Vv14)*complexconjugate(Vv46) + C23*ZA33*complexconjugate(Vv15)*complexconjugate(Vv46) + C32*ZA33*complexconjugate(Vv15)*complexconjugate(Vv46))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_442 = Coupling(name = 'GC_442',
	 value = '-(Vv16*Vv54*ZA13*complexconjugate(C13) + Vv16*Vv55*ZA13*complexconjugate(C23) + Vv16*Vv54*ZA13*complexconjugate(C31) + Vv16*Vv55*ZA13*complexconjugate(C32) + 2*Vv11*Vv54*ZA11*complexconjugate(Y1n11) + 2*Vv11*Vv55*ZA11*complexconjugate(Y1n12) + 2*Vv12*Vv54*ZA11*complexconjugate(Y1n21) + Vv14*(ZA13*(2*Vv54*complexconjugate(BB11) - Vv55*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv56*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv51*ZA11*complexconjugate(Y1n11) + 2*Vv52*ZA11*complexconjugate(Y1n21)) + 2*Vv12*Vv55*ZA11*complexconjugate(Y1n22) + Vv15*(ZA13*(-(Vv54*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv55*complexconjugate(BB22) + Vv56*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv51*ZA11*complexconjugate(Y1n12) + 2*Vv52*ZA11*complexconjugate(Y1n22)) + 2*Vv16*Vv53*ZA12*complexconjugate(Y2n33) + 2*Vv13*Vv56*ZA12*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_443 = Coupling(name = 'GC_443',
	 value = '(2*Y1n21*ZA11*complexconjugate(Vv14)*complexconjugate(Vv52) + 2*Y1n22*ZA11*complexconjugate(Vv15)*complexconjugate(Vv52) + 2*Y2n33*ZA12*complexconjugate(Vv16)*complexconjugate(Vv53) + 2*Y1n21*ZA11*complexconjugate(Vv12)*complexconjugate(Vv54) + 2*BB11*ZA13*complexconjugate(Vv14)*complexconjugate(Vv54) - BB12*ZA13*complexconjugate(Vv15)*complexconjugate(Vv54) - BB21*ZA13*complexconjugate(Vv15)*complexconjugate(Vv54) + C13*ZA13*complexconjugate(Vv16)*complexconjugate(Vv54) + C31*ZA13*complexconjugate(Vv16)*complexconjugate(Vv54) + 2*Y1n11*ZA11*(complexconjugate(Vv14)*complexconjugate(Vv51) + complexconjugate(Vv11)*complexconjugate(Vv54)) + 2*Y1n22*ZA11*complexconjugate(Vv12)*complexconjugate(Vv55) - BB12*ZA13*complexconjugate(Vv14)*complexconjugate(Vv55) - BB21*ZA13*complexconjugate(Vv14)*complexconjugate(Vv55) - 2*BB22*ZA13*complexconjugate(Vv15)*complexconjugate(Vv55) + C23*ZA13*complexconjugate(Vv16)*complexconjugate(Vv55) + C32*ZA13*complexconjugate(Vv16)*complexconjugate(Vv55) + 2*Y1n12*ZA11*(complexconjugate(Vv15)*complexconjugate(Vv51) + complexconjugate(Vv11)*complexconjugate(Vv55)) + 2*Y2n33*ZA12*complexconjugate(Vv13)*complexconjugate(Vv56) + C13*ZA13*complexconjugate(Vv14)*complexconjugate(Vv56) + C31*ZA13*complexconjugate(Vv14)*complexconjugate(Vv56) + C23*ZA13*complexconjugate(Vv15)*complexconjugate(Vv56) + C32*ZA13*complexconjugate(Vv15)*complexconjugate(Vv56))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_444 = Coupling(name = 'GC_444',
	 value = '-(Vv16*Vv54*ZA23*complexconjugate(C13) + Vv16*Vv55*ZA23*complexconjugate(C23) + Vv16*Vv54*ZA23*complexconjugate(C31) + Vv16*Vv55*ZA23*complexconjugate(C32) + 2*Vv11*Vv54*ZA21*complexconjugate(Y1n11) + 2*Vv11*Vv55*ZA21*complexconjugate(Y1n12) + 2*Vv12*Vv54*ZA21*complexconjugate(Y1n21) + Vv14*(ZA23*(2*Vv54*complexconjugate(BB11) - Vv55*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv56*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv51*ZA21*complexconjugate(Y1n11) + 2*Vv52*ZA21*complexconjugate(Y1n21)) + 2*Vv12*Vv55*ZA21*complexconjugate(Y1n22) + Vv15*(ZA23*(-(Vv54*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv55*complexconjugate(BB22) + Vv56*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv51*ZA21*complexconjugate(Y1n12) + 2*Vv52*ZA21*complexconjugate(Y1n22)) + 2*Vv16*Vv53*ZA22*complexconjugate(Y2n33) + 2*Vv13*Vv56*ZA22*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_445 = Coupling(name = 'GC_445',
	 value = '(2*Y1n21*ZA21*complexconjugate(Vv14)*complexconjugate(Vv52) + 2*Y1n22*ZA21*complexconjugate(Vv15)*complexconjugate(Vv52) + 2*Y2n33*ZA22*complexconjugate(Vv16)*complexconjugate(Vv53) + 2*Y1n21*ZA21*complexconjugate(Vv12)*complexconjugate(Vv54) + 2*BB11*ZA23*complexconjugate(Vv14)*complexconjugate(Vv54) - BB12*ZA23*complexconjugate(Vv15)*complexconjugate(Vv54) - BB21*ZA23*complexconjugate(Vv15)*complexconjugate(Vv54) + C13*ZA23*complexconjugate(Vv16)*complexconjugate(Vv54) + C31*ZA23*complexconjugate(Vv16)*complexconjugate(Vv54) + 2*Y1n11*ZA21*(complexconjugate(Vv14)*complexconjugate(Vv51) + complexconjugate(Vv11)*complexconjugate(Vv54)) + 2*Y1n22*ZA21*complexconjugate(Vv12)*complexconjugate(Vv55) - BB12*ZA23*complexconjugate(Vv14)*complexconjugate(Vv55) - BB21*ZA23*complexconjugate(Vv14)*complexconjugate(Vv55) - 2*BB22*ZA23*complexconjugate(Vv15)*complexconjugate(Vv55) + C23*ZA23*complexconjugate(Vv16)*complexconjugate(Vv55) + C32*ZA23*complexconjugate(Vv16)*complexconjugate(Vv55) + 2*Y1n12*ZA21*(complexconjugate(Vv15)*complexconjugate(Vv51) + complexconjugate(Vv11)*complexconjugate(Vv55)) + 2*Y2n33*ZA22*complexconjugate(Vv13)*complexconjugate(Vv56) + C13*ZA23*complexconjugate(Vv14)*complexconjugate(Vv56) + C31*ZA23*complexconjugate(Vv14)*complexconjugate(Vv56) + C23*ZA23*complexconjugate(Vv15)*complexconjugate(Vv56) + C32*ZA23*complexconjugate(Vv15)*complexconjugate(Vv56))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_446 = Coupling(name = 'GC_446',
	 value = '-(Vv16*Vv54*ZA33*complexconjugate(C13) + Vv16*Vv55*ZA33*complexconjugate(C23) + Vv16*Vv54*ZA33*complexconjugate(C31) + Vv16*Vv55*ZA33*complexconjugate(C32) + 2*Vv11*Vv54*ZA31*complexconjugate(Y1n11) + 2*Vv11*Vv55*ZA31*complexconjugate(Y1n12) + 2*Vv12*Vv54*ZA31*complexconjugate(Y1n21) + Vv14*(ZA33*(2*Vv54*complexconjugate(BB11) - Vv55*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv56*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv51*ZA31*complexconjugate(Y1n11) + 2*Vv52*ZA31*complexconjugate(Y1n21)) + 2*Vv12*Vv55*ZA31*complexconjugate(Y1n22) + Vv15*(ZA33*(-(Vv54*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv55*complexconjugate(BB22) + Vv56*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv51*ZA31*complexconjugate(Y1n12) + 2*Vv52*ZA31*complexconjugate(Y1n22)) + 2*Vv16*Vv53*ZA32*complexconjugate(Y2n33) + 2*Vv13*Vv56*ZA32*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_447 = Coupling(name = 'GC_447',
	 value = '(2*Y1n21*ZA31*complexconjugate(Vv14)*complexconjugate(Vv52) + 2*Y1n22*ZA31*complexconjugate(Vv15)*complexconjugate(Vv52) + 2*Y2n33*ZA32*complexconjugate(Vv16)*complexconjugate(Vv53) + 2*Y1n21*ZA31*complexconjugate(Vv12)*complexconjugate(Vv54) + 2*BB11*ZA33*complexconjugate(Vv14)*complexconjugate(Vv54) - BB12*ZA33*complexconjugate(Vv15)*complexconjugate(Vv54) - BB21*ZA33*complexconjugate(Vv15)*complexconjugate(Vv54) + C13*ZA33*complexconjugate(Vv16)*complexconjugate(Vv54) + C31*ZA33*complexconjugate(Vv16)*complexconjugate(Vv54) + 2*Y1n11*ZA31*(complexconjugate(Vv14)*complexconjugate(Vv51) + complexconjugate(Vv11)*complexconjugate(Vv54)) + 2*Y1n22*ZA31*complexconjugate(Vv12)*complexconjugate(Vv55) - BB12*ZA33*complexconjugate(Vv14)*complexconjugate(Vv55) - BB21*ZA33*complexconjugate(Vv14)*complexconjugate(Vv55) - 2*BB22*ZA33*complexconjugate(Vv15)*complexconjugate(Vv55) + C23*ZA33*complexconjugate(Vv16)*complexconjugate(Vv55) + C32*ZA33*complexconjugate(Vv16)*complexconjugate(Vv55) + 2*Y1n12*ZA31*(complexconjugate(Vv15)*complexconjugate(Vv51) + complexconjugate(Vv11)*complexconjugate(Vv55)) + 2*Y2n33*ZA32*complexconjugate(Vv13)*complexconjugate(Vv56) + C13*ZA33*complexconjugate(Vv14)*complexconjugate(Vv56) + C31*ZA33*complexconjugate(Vv14)*complexconjugate(Vv56) + C23*ZA33*complexconjugate(Vv15)*complexconjugate(Vv56) + C32*ZA33*complexconjugate(Vv15)*complexconjugate(Vv56))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_448 = Coupling(name = 'GC_448',
	 value = '-(Vv16*Vv64*ZA13*complexconjugate(C13) + Vv16*Vv65*ZA13*complexconjugate(C23) + Vv16*Vv64*ZA13*complexconjugate(C31) + Vv16*Vv65*ZA13*complexconjugate(C32) + 2*Vv11*Vv64*ZA11*complexconjugate(Y1n11) + 2*Vv11*Vv65*ZA11*complexconjugate(Y1n12) + 2*Vv12*Vv64*ZA11*complexconjugate(Y1n21) + Vv14*(ZA13*(2*Vv64*complexconjugate(BB11) - Vv65*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv66*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv61*ZA11*complexconjugate(Y1n11) + 2*Vv62*ZA11*complexconjugate(Y1n21)) + 2*Vv12*Vv65*ZA11*complexconjugate(Y1n22) + Vv15*(ZA13*(-(Vv64*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv65*complexconjugate(BB22) + Vv66*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv61*ZA11*complexconjugate(Y1n12) + 2*Vv62*ZA11*complexconjugate(Y1n22)) + 2*Vv16*Vv63*ZA12*complexconjugate(Y2n33) + 2*Vv13*Vv66*ZA12*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_449 = Coupling(name = 'GC_449',
	 value = '(2*Y1n21*ZA11*complexconjugate(Vv14)*complexconjugate(Vv62) + 2*Y1n22*ZA11*complexconjugate(Vv15)*complexconjugate(Vv62) + 2*Y2n33*ZA12*complexconjugate(Vv16)*complexconjugate(Vv63) + 2*Y1n21*ZA11*complexconjugate(Vv12)*complexconjugate(Vv64) + 2*BB11*ZA13*complexconjugate(Vv14)*complexconjugate(Vv64) - BB12*ZA13*complexconjugate(Vv15)*complexconjugate(Vv64) - BB21*ZA13*complexconjugate(Vv15)*complexconjugate(Vv64) + C13*ZA13*complexconjugate(Vv16)*complexconjugate(Vv64) + C31*ZA13*complexconjugate(Vv16)*complexconjugate(Vv64) + 2*Y1n11*ZA11*(complexconjugate(Vv14)*complexconjugate(Vv61) + complexconjugate(Vv11)*complexconjugate(Vv64)) + 2*Y1n22*ZA11*complexconjugate(Vv12)*complexconjugate(Vv65) - BB12*ZA13*complexconjugate(Vv14)*complexconjugate(Vv65) - BB21*ZA13*complexconjugate(Vv14)*complexconjugate(Vv65) - 2*BB22*ZA13*complexconjugate(Vv15)*complexconjugate(Vv65) + C23*ZA13*complexconjugate(Vv16)*complexconjugate(Vv65) + C32*ZA13*complexconjugate(Vv16)*complexconjugate(Vv65) + 2*Y1n12*ZA11*(complexconjugate(Vv15)*complexconjugate(Vv61) + complexconjugate(Vv11)*complexconjugate(Vv65)) + 2*Y2n33*ZA12*complexconjugate(Vv13)*complexconjugate(Vv66) + C13*ZA13*complexconjugate(Vv14)*complexconjugate(Vv66) + C31*ZA13*complexconjugate(Vv14)*complexconjugate(Vv66) + C23*ZA13*complexconjugate(Vv15)*complexconjugate(Vv66) + C32*ZA13*complexconjugate(Vv15)*complexconjugate(Vv66))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_450 = Coupling(name = 'GC_450',
	 value = '-(Vv16*Vv64*ZA23*complexconjugate(C13) + Vv16*Vv65*ZA23*complexconjugate(C23) + Vv16*Vv64*ZA23*complexconjugate(C31) + Vv16*Vv65*ZA23*complexconjugate(C32) + 2*Vv11*Vv64*ZA21*complexconjugate(Y1n11) + 2*Vv11*Vv65*ZA21*complexconjugate(Y1n12) + 2*Vv12*Vv64*ZA21*complexconjugate(Y1n21) + Vv14*(ZA23*(2*Vv64*complexconjugate(BB11) - Vv65*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv66*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv61*ZA21*complexconjugate(Y1n11) + 2*Vv62*ZA21*complexconjugate(Y1n21)) + 2*Vv12*Vv65*ZA21*complexconjugate(Y1n22) + Vv15*(ZA23*(-(Vv64*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv65*complexconjugate(BB22) + Vv66*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv61*ZA21*complexconjugate(Y1n12) + 2*Vv62*ZA21*complexconjugate(Y1n22)) + 2*Vv16*Vv63*ZA22*complexconjugate(Y2n33) + 2*Vv13*Vv66*ZA22*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_451 = Coupling(name = 'GC_451',
	 value = '(2*Y1n21*ZA21*complexconjugate(Vv14)*complexconjugate(Vv62) + 2*Y1n22*ZA21*complexconjugate(Vv15)*complexconjugate(Vv62) + 2*Y2n33*ZA22*complexconjugate(Vv16)*complexconjugate(Vv63) + 2*Y1n21*ZA21*complexconjugate(Vv12)*complexconjugate(Vv64) + 2*BB11*ZA23*complexconjugate(Vv14)*complexconjugate(Vv64) - BB12*ZA23*complexconjugate(Vv15)*complexconjugate(Vv64) - BB21*ZA23*complexconjugate(Vv15)*complexconjugate(Vv64) + C13*ZA23*complexconjugate(Vv16)*complexconjugate(Vv64) + C31*ZA23*complexconjugate(Vv16)*complexconjugate(Vv64) + 2*Y1n11*ZA21*(complexconjugate(Vv14)*complexconjugate(Vv61) + complexconjugate(Vv11)*complexconjugate(Vv64)) + 2*Y1n22*ZA21*complexconjugate(Vv12)*complexconjugate(Vv65) - BB12*ZA23*complexconjugate(Vv14)*complexconjugate(Vv65) - BB21*ZA23*complexconjugate(Vv14)*complexconjugate(Vv65) - 2*BB22*ZA23*complexconjugate(Vv15)*complexconjugate(Vv65) + C23*ZA23*complexconjugate(Vv16)*complexconjugate(Vv65) + C32*ZA23*complexconjugate(Vv16)*complexconjugate(Vv65) + 2*Y1n12*ZA21*(complexconjugate(Vv15)*complexconjugate(Vv61) + complexconjugate(Vv11)*complexconjugate(Vv65)) + 2*Y2n33*ZA22*complexconjugate(Vv13)*complexconjugate(Vv66) + C13*ZA23*complexconjugate(Vv14)*complexconjugate(Vv66) + C31*ZA23*complexconjugate(Vv14)*complexconjugate(Vv66) + C23*ZA23*complexconjugate(Vv15)*complexconjugate(Vv66) + C32*ZA23*complexconjugate(Vv15)*complexconjugate(Vv66))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_452 = Coupling(name = 'GC_452',
	 value = '-(Vv16*Vv64*ZA33*complexconjugate(C13) + Vv16*Vv65*ZA33*complexconjugate(C23) + Vv16*Vv64*ZA33*complexconjugate(C31) + Vv16*Vv65*ZA33*complexconjugate(C32) + 2*Vv11*Vv64*ZA31*complexconjugate(Y1n11) + 2*Vv11*Vv65*ZA31*complexconjugate(Y1n12) + 2*Vv12*Vv64*ZA31*complexconjugate(Y1n21) + Vv14*(ZA33*(2*Vv64*complexconjugate(BB11) - Vv65*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv66*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv61*ZA31*complexconjugate(Y1n11) + 2*Vv62*ZA31*complexconjugate(Y1n21)) + 2*Vv12*Vv65*ZA31*complexconjugate(Y1n22) + Vv15*(ZA33*(-(Vv64*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv65*complexconjugate(BB22) + Vv66*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv61*ZA31*complexconjugate(Y1n12) + 2*Vv62*ZA31*complexconjugate(Y1n22)) + 2*Vv16*Vv63*ZA32*complexconjugate(Y2n33) + 2*Vv13*Vv66*ZA32*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_453 = Coupling(name = 'GC_453',
	 value = '(2*Y1n21*ZA31*complexconjugate(Vv14)*complexconjugate(Vv62) + 2*Y1n22*ZA31*complexconjugate(Vv15)*complexconjugate(Vv62) + 2*Y2n33*ZA32*complexconjugate(Vv16)*complexconjugate(Vv63) + 2*Y1n21*ZA31*complexconjugate(Vv12)*complexconjugate(Vv64) + 2*BB11*ZA33*complexconjugate(Vv14)*complexconjugate(Vv64) - BB12*ZA33*complexconjugate(Vv15)*complexconjugate(Vv64) - BB21*ZA33*complexconjugate(Vv15)*complexconjugate(Vv64) + C13*ZA33*complexconjugate(Vv16)*complexconjugate(Vv64) + C31*ZA33*complexconjugate(Vv16)*complexconjugate(Vv64) + 2*Y1n11*ZA31*(complexconjugate(Vv14)*complexconjugate(Vv61) + complexconjugate(Vv11)*complexconjugate(Vv64)) + 2*Y1n22*ZA31*complexconjugate(Vv12)*complexconjugate(Vv65) - BB12*ZA33*complexconjugate(Vv14)*complexconjugate(Vv65) - BB21*ZA33*complexconjugate(Vv14)*complexconjugate(Vv65) - 2*BB22*ZA33*complexconjugate(Vv15)*complexconjugate(Vv65) + C23*ZA33*complexconjugate(Vv16)*complexconjugate(Vv65) + C32*ZA33*complexconjugate(Vv16)*complexconjugate(Vv65) + 2*Y1n12*ZA31*(complexconjugate(Vv15)*complexconjugate(Vv61) + complexconjugate(Vv11)*complexconjugate(Vv65)) + 2*Y2n33*ZA32*complexconjugate(Vv13)*complexconjugate(Vv66) + C13*ZA33*complexconjugate(Vv14)*complexconjugate(Vv66) + C31*ZA33*complexconjugate(Vv14)*complexconjugate(Vv66) + C23*ZA33*complexconjugate(Vv15)*complexconjugate(Vv66) + C32*ZA33*complexconjugate(Vv15)*complexconjugate(Vv66))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_454 = Coupling(name = 'GC_454',
	 value = '-(Vv24*Vv26*ZA13*complexconjugate(C13) + Vv25*Vv26*ZA13*complexconjugate(C23) + Vv24*Vv26*ZA13*complexconjugate(C31) + Vv25*Vv26*ZA13*complexconjugate(C32) + 2*Vv21*Vv24*ZA11*complexconjugate(Y1n11) + 2*Vv21*Vv25*ZA11*complexconjugate(Y1n12) + 2*Vv22*Vv24*ZA11*complexconjugate(Y1n21) + Vv24*(ZA13*(2*Vv24*complexconjugate(BB11) - Vv25*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv26*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv21*ZA11*complexconjugate(Y1n11) + 2*Vv22*ZA11*complexconjugate(Y1n21)) + 2*Vv22*Vv25*ZA11*complexconjugate(Y1n22) + Vv25*(ZA13*(-(Vv24*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv25*complexconjugate(BB22) + Vv26*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv21*ZA11*complexconjugate(Y1n12) + 2*Vv22*ZA11*complexconjugate(Y1n22)) + 4*Vv23*Vv26*ZA12*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_455 = Coupling(name = 'GC_455',
	 value = '(4*Y1n11*ZA11*complexconjugate(Vv21)*complexconjugate(Vv24) + 4*Y1n21*ZA11*complexconjugate(Vv22)*complexconjugate(Vv24) + 2*BB11*ZA13*complexconjugate(Vv24)**2 + 4*Y1n12*ZA11*complexconjugate(Vv21)*complexconjugate(Vv25) + 4*Y1n22*ZA11*complexconjugate(Vv22)*complexconjugate(Vv25) - 2*BB12*ZA13*complexconjugate(Vv24)*complexconjugate(Vv25) - 2*BB21*ZA13*complexconjugate(Vv24)*complexconjugate(Vv25) - 2*BB22*ZA13*complexconjugate(Vv25)**2 + 4*Y2n33*ZA12*complexconjugate(Vv23)*complexconjugate(Vv26) + 2*C13*ZA13*complexconjugate(Vv24)*complexconjugate(Vv26) + 2*C31*ZA13*complexconjugate(Vv24)*complexconjugate(Vv26) + 2*C23*ZA13*complexconjugate(Vv25)*complexconjugate(Vv26) + 2*C32*ZA13*complexconjugate(Vv25)*complexconjugate(Vv26))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_456 = Coupling(name = 'GC_456',
	 value = '-(Vv24*Vv26*ZA23*complexconjugate(C13) + Vv25*Vv26*ZA23*complexconjugate(C23) + Vv24*Vv26*ZA23*complexconjugate(C31) + Vv25*Vv26*ZA23*complexconjugate(C32) + 2*Vv21*Vv24*ZA21*complexconjugate(Y1n11) + 2*Vv21*Vv25*ZA21*complexconjugate(Y1n12) + 2*Vv22*Vv24*ZA21*complexconjugate(Y1n21) + Vv24*(ZA23*(2*Vv24*complexconjugate(BB11) - Vv25*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv26*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv21*ZA21*complexconjugate(Y1n11) + 2*Vv22*ZA21*complexconjugate(Y1n21)) + 2*Vv22*Vv25*ZA21*complexconjugate(Y1n22) + Vv25*(ZA23*(-(Vv24*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv25*complexconjugate(BB22) + Vv26*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv21*ZA21*complexconjugate(Y1n12) + 2*Vv22*ZA21*complexconjugate(Y1n22)) + 4*Vv23*Vv26*ZA22*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_457 = Coupling(name = 'GC_457',
	 value = '(4*Y1n11*ZA21*complexconjugate(Vv21)*complexconjugate(Vv24) + 4*Y1n21*ZA21*complexconjugate(Vv22)*complexconjugate(Vv24) + 2*BB11*ZA23*complexconjugate(Vv24)**2 + 4*Y1n12*ZA21*complexconjugate(Vv21)*complexconjugate(Vv25) + 4*Y1n22*ZA21*complexconjugate(Vv22)*complexconjugate(Vv25) - 2*BB12*ZA23*complexconjugate(Vv24)*complexconjugate(Vv25) - 2*BB21*ZA23*complexconjugate(Vv24)*complexconjugate(Vv25) - 2*BB22*ZA23*complexconjugate(Vv25)**2 + 4*Y2n33*ZA22*complexconjugate(Vv23)*complexconjugate(Vv26) + 2*C13*ZA23*complexconjugate(Vv24)*complexconjugate(Vv26) + 2*C31*ZA23*complexconjugate(Vv24)*complexconjugate(Vv26) + 2*C23*ZA23*complexconjugate(Vv25)*complexconjugate(Vv26) + 2*C32*ZA23*complexconjugate(Vv25)*complexconjugate(Vv26))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_458 = Coupling(name = 'GC_458',
	 value = '-(Vv24*Vv26*ZA33*complexconjugate(C13) + Vv25*Vv26*ZA33*complexconjugate(C23) + Vv24*Vv26*ZA33*complexconjugate(C31) + Vv25*Vv26*ZA33*complexconjugate(C32) + 2*Vv21*Vv24*ZA31*complexconjugate(Y1n11) + 2*Vv21*Vv25*ZA31*complexconjugate(Y1n12) + 2*Vv22*Vv24*ZA31*complexconjugate(Y1n21) + Vv24*(ZA33*(2*Vv24*complexconjugate(BB11) - Vv25*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv26*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv21*ZA31*complexconjugate(Y1n11) + 2*Vv22*ZA31*complexconjugate(Y1n21)) + 2*Vv22*Vv25*ZA31*complexconjugate(Y1n22) + Vv25*(ZA33*(-(Vv24*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv25*complexconjugate(BB22) + Vv26*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv21*ZA31*complexconjugate(Y1n12) + 2*Vv22*ZA31*complexconjugate(Y1n22)) + 4*Vv23*Vv26*ZA32*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_459 = Coupling(name = 'GC_459',
	 value = '(4*Y1n11*ZA31*complexconjugate(Vv21)*complexconjugate(Vv24) + 4*Y1n21*ZA31*complexconjugate(Vv22)*complexconjugate(Vv24) + 2*BB11*ZA33*complexconjugate(Vv24)**2 + 4*Y1n12*ZA31*complexconjugate(Vv21)*complexconjugate(Vv25) + 4*Y1n22*ZA31*complexconjugate(Vv22)*complexconjugate(Vv25) - 2*BB12*ZA33*complexconjugate(Vv24)*complexconjugate(Vv25) - 2*BB21*ZA33*complexconjugate(Vv24)*complexconjugate(Vv25) - 2*BB22*ZA33*complexconjugate(Vv25)**2 + 4*Y2n33*ZA32*complexconjugate(Vv23)*complexconjugate(Vv26) + 2*C13*ZA33*complexconjugate(Vv24)*complexconjugate(Vv26) + 2*C31*ZA33*complexconjugate(Vv24)*complexconjugate(Vv26) + 2*C23*ZA33*complexconjugate(Vv25)*complexconjugate(Vv26) + 2*C32*ZA33*complexconjugate(Vv25)*complexconjugate(Vv26))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_460 = Coupling(name = 'GC_460',
	 value = '-(Vv26*Vv34*ZA13*complexconjugate(C13) + Vv26*Vv35*ZA13*complexconjugate(C23) + Vv26*Vv34*ZA13*complexconjugate(C31) + Vv26*Vv35*ZA13*complexconjugate(C32) + 2*Vv21*Vv34*ZA11*complexconjugate(Y1n11) + 2*Vv21*Vv35*ZA11*complexconjugate(Y1n12) + 2*Vv22*Vv34*ZA11*complexconjugate(Y1n21) + Vv24*(ZA13*(2*Vv34*complexconjugate(BB11) - Vv35*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv36*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv31*ZA11*complexconjugate(Y1n11) + 2*Vv32*ZA11*complexconjugate(Y1n21)) + 2*Vv22*Vv35*ZA11*complexconjugate(Y1n22) + Vv25*(ZA13*(-(Vv34*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv35*complexconjugate(BB22) + Vv36*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv31*ZA11*complexconjugate(Y1n12) + 2*Vv32*ZA11*complexconjugate(Y1n22)) + 2*Vv26*Vv33*ZA12*complexconjugate(Y2n33) + 2*Vv23*Vv36*ZA12*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_461 = Coupling(name = 'GC_461',
	 value = '(2*Y1n21*ZA11*complexconjugate(Vv24)*complexconjugate(Vv32) + 2*Y1n22*ZA11*complexconjugate(Vv25)*complexconjugate(Vv32) + 2*Y2n33*ZA12*complexconjugate(Vv26)*complexconjugate(Vv33) + 2*Y1n21*ZA11*complexconjugate(Vv22)*complexconjugate(Vv34) + 2*BB11*ZA13*complexconjugate(Vv24)*complexconjugate(Vv34) - BB12*ZA13*complexconjugate(Vv25)*complexconjugate(Vv34) - BB21*ZA13*complexconjugate(Vv25)*complexconjugate(Vv34) + C13*ZA13*complexconjugate(Vv26)*complexconjugate(Vv34) + C31*ZA13*complexconjugate(Vv26)*complexconjugate(Vv34) + 2*Y1n11*ZA11*(complexconjugate(Vv24)*complexconjugate(Vv31) + complexconjugate(Vv21)*complexconjugate(Vv34)) + 2*Y1n22*ZA11*complexconjugate(Vv22)*complexconjugate(Vv35) - BB12*ZA13*complexconjugate(Vv24)*complexconjugate(Vv35) - BB21*ZA13*complexconjugate(Vv24)*complexconjugate(Vv35) - 2*BB22*ZA13*complexconjugate(Vv25)*complexconjugate(Vv35) + C23*ZA13*complexconjugate(Vv26)*complexconjugate(Vv35) + C32*ZA13*complexconjugate(Vv26)*complexconjugate(Vv35) + 2*Y1n12*ZA11*(complexconjugate(Vv25)*complexconjugate(Vv31) + complexconjugate(Vv21)*complexconjugate(Vv35)) + 2*Y2n33*ZA12*complexconjugate(Vv23)*complexconjugate(Vv36) + C13*ZA13*complexconjugate(Vv24)*complexconjugate(Vv36) + C31*ZA13*complexconjugate(Vv24)*complexconjugate(Vv36) + C23*ZA13*complexconjugate(Vv25)*complexconjugate(Vv36) + C32*ZA13*complexconjugate(Vv25)*complexconjugate(Vv36))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_462 = Coupling(name = 'GC_462',
	 value = '-(Vv26*Vv34*ZA23*complexconjugate(C13) + Vv26*Vv35*ZA23*complexconjugate(C23) + Vv26*Vv34*ZA23*complexconjugate(C31) + Vv26*Vv35*ZA23*complexconjugate(C32) + 2*Vv21*Vv34*ZA21*complexconjugate(Y1n11) + 2*Vv21*Vv35*ZA21*complexconjugate(Y1n12) + 2*Vv22*Vv34*ZA21*complexconjugate(Y1n21) + Vv24*(ZA23*(2*Vv34*complexconjugate(BB11) - Vv35*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv36*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv31*ZA21*complexconjugate(Y1n11) + 2*Vv32*ZA21*complexconjugate(Y1n21)) + 2*Vv22*Vv35*ZA21*complexconjugate(Y1n22) + Vv25*(ZA23*(-(Vv34*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv35*complexconjugate(BB22) + Vv36*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv31*ZA21*complexconjugate(Y1n12) + 2*Vv32*ZA21*complexconjugate(Y1n22)) + 2*Vv26*Vv33*ZA22*complexconjugate(Y2n33) + 2*Vv23*Vv36*ZA22*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_463 = Coupling(name = 'GC_463',
	 value = '(2*Y1n21*ZA21*complexconjugate(Vv24)*complexconjugate(Vv32) + 2*Y1n22*ZA21*complexconjugate(Vv25)*complexconjugate(Vv32) + 2*Y2n33*ZA22*complexconjugate(Vv26)*complexconjugate(Vv33) + 2*Y1n21*ZA21*complexconjugate(Vv22)*complexconjugate(Vv34) + 2*BB11*ZA23*complexconjugate(Vv24)*complexconjugate(Vv34) - BB12*ZA23*complexconjugate(Vv25)*complexconjugate(Vv34) - BB21*ZA23*complexconjugate(Vv25)*complexconjugate(Vv34) + C13*ZA23*complexconjugate(Vv26)*complexconjugate(Vv34) + C31*ZA23*complexconjugate(Vv26)*complexconjugate(Vv34) + 2*Y1n11*ZA21*(complexconjugate(Vv24)*complexconjugate(Vv31) + complexconjugate(Vv21)*complexconjugate(Vv34)) + 2*Y1n22*ZA21*complexconjugate(Vv22)*complexconjugate(Vv35) - BB12*ZA23*complexconjugate(Vv24)*complexconjugate(Vv35) - BB21*ZA23*complexconjugate(Vv24)*complexconjugate(Vv35) - 2*BB22*ZA23*complexconjugate(Vv25)*complexconjugate(Vv35) + C23*ZA23*complexconjugate(Vv26)*complexconjugate(Vv35) + C32*ZA23*complexconjugate(Vv26)*complexconjugate(Vv35) + 2*Y1n12*ZA21*(complexconjugate(Vv25)*complexconjugate(Vv31) + complexconjugate(Vv21)*complexconjugate(Vv35)) + 2*Y2n33*ZA22*complexconjugate(Vv23)*complexconjugate(Vv36) + C13*ZA23*complexconjugate(Vv24)*complexconjugate(Vv36) + C31*ZA23*complexconjugate(Vv24)*complexconjugate(Vv36) + C23*ZA23*complexconjugate(Vv25)*complexconjugate(Vv36) + C32*ZA23*complexconjugate(Vv25)*complexconjugate(Vv36))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_464 = Coupling(name = 'GC_464',
	 value = '-(Vv26*Vv34*ZA33*complexconjugate(C13) + Vv26*Vv35*ZA33*complexconjugate(C23) + Vv26*Vv34*ZA33*complexconjugate(C31) + Vv26*Vv35*ZA33*complexconjugate(C32) + 2*Vv21*Vv34*ZA31*complexconjugate(Y1n11) + 2*Vv21*Vv35*ZA31*complexconjugate(Y1n12) + 2*Vv22*Vv34*ZA31*complexconjugate(Y1n21) + Vv24*(ZA33*(2*Vv34*complexconjugate(BB11) - Vv35*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv36*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv31*ZA31*complexconjugate(Y1n11) + 2*Vv32*ZA31*complexconjugate(Y1n21)) + 2*Vv22*Vv35*ZA31*complexconjugate(Y1n22) + Vv25*(ZA33*(-(Vv34*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv35*complexconjugate(BB22) + Vv36*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv31*ZA31*complexconjugate(Y1n12) + 2*Vv32*ZA31*complexconjugate(Y1n22)) + 2*Vv26*Vv33*ZA32*complexconjugate(Y2n33) + 2*Vv23*Vv36*ZA32*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_465 = Coupling(name = 'GC_465',
	 value = '(2*Y1n21*ZA31*complexconjugate(Vv24)*complexconjugate(Vv32) + 2*Y1n22*ZA31*complexconjugate(Vv25)*complexconjugate(Vv32) + 2*Y2n33*ZA32*complexconjugate(Vv26)*complexconjugate(Vv33) + 2*Y1n21*ZA31*complexconjugate(Vv22)*complexconjugate(Vv34) + 2*BB11*ZA33*complexconjugate(Vv24)*complexconjugate(Vv34) - BB12*ZA33*complexconjugate(Vv25)*complexconjugate(Vv34) - BB21*ZA33*complexconjugate(Vv25)*complexconjugate(Vv34) + C13*ZA33*complexconjugate(Vv26)*complexconjugate(Vv34) + C31*ZA33*complexconjugate(Vv26)*complexconjugate(Vv34) + 2*Y1n11*ZA31*(complexconjugate(Vv24)*complexconjugate(Vv31) + complexconjugate(Vv21)*complexconjugate(Vv34)) + 2*Y1n22*ZA31*complexconjugate(Vv22)*complexconjugate(Vv35) - BB12*ZA33*complexconjugate(Vv24)*complexconjugate(Vv35) - BB21*ZA33*complexconjugate(Vv24)*complexconjugate(Vv35) - 2*BB22*ZA33*complexconjugate(Vv25)*complexconjugate(Vv35) + C23*ZA33*complexconjugate(Vv26)*complexconjugate(Vv35) + C32*ZA33*complexconjugate(Vv26)*complexconjugate(Vv35) + 2*Y1n12*ZA31*(complexconjugate(Vv25)*complexconjugate(Vv31) + complexconjugate(Vv21)*complexconjugate(Vv35)) + 2*Y2n33*ZA32*complexconjugate(Vv23)*complexconjugate(Vv36) + C13*ZA33*complexconjugate(Vv24)*complexconjugate(Vv36) + C31*ZA33*complexconjugate(Vv24)*complexconjugate(Vv36) + C23*ZA33*complexconjugate(Vv25)*complexconjugate(Vv36) + C32*ZA33*complexconjugate(Vv25)*complexconjugate(Vv36))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_466 = Coupling(name = 'GC_466',
	 value = '-(Vv26*Vv44*ZA13*complexconjugate(C13) + Vv26*Vv45*ZA13*complexconjugate(C23) + Vv26*Vv44*ZA13*complexconjugate(C31) + Vv26*Vv45*ZA13*complexconjugate(C32) + 2*Vv21*Vv44*ZA11*complexconjugate(Y1n11) + 2*Vv21*Vv45*ZA11*complexconjugate(Y1n12) + 2*Vv22*Vv44*ZA11*complexconjugate(Y1n21) + Vv24*(ZA13*(2*Vv44*complexconjugate(BB11) - Vv45*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv46*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv41*ZA11*complexconjugate(Y1n11) + 2*Vv42*ZA11*complexconjugate(Y1n21)) + 2*Vv22*Vv45*ZA11*complexconjugate(Y1n22) + Vv25*(ZA13*(-(Vv44*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv45*complexconjugate(BB22) + Vv46*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv41*ZA11*complexconjugate(Y1n12) + 2*Vv42*ZA11*complexconjugate(Y1n22)) + 2*Vv26*Vv43*ZA12*complexconjugate(Y2n33) + 2*Vv23*Vv46*ZA12*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_467 = Coupling(name = 'GC_467',
	 value = '(2*Y1n21*ZA11*complexconjugate(Vv24)*complexconjugate(Vv42) + 2*Y1n22*ZA11*complexconjugate(Vv25)*complexconjugate(Vv42) + 2*Y2n33*ZA12*complexconjugate(Vv26)*complexconjugate(Vv43) + 2*Y1n21*ZA11*complexconjugate(Vv22)*complexconjugate(Vv44) + 2*BB11*ZA13*complexconjugate(Vv24)*complexconjugate(Vv44) - BB12*ZA13*complexconjugate(Vv25)*complexconjugate(Vv44) - BB21*ZA13*complexconjugate(Vv25)*complexconjugate(Vv44) + C13*ZA13*complexconjugate(Vv26)*complexconjugate(Vv44) + C31*ZA13*complexconjugate(Vv26)*complexconjugate(Vv44) + 2*Y1n11*ZA11*(complexconjugate(Vv24)*complexconjugate(Vv41) + complexconjugate(Vv21)*complexconjugate(Vv44)) + 2*Y1n22*ZA11*complexconjugate(Vv22)*complexconjugate(Vv45) - BB12*ZA13*complexconjugate(Vv24)*complexconjugate(Vv45) - BB21*ZA13*complexconjugate(Vv24)*complexconjugate(Vv45) - 2*BB22*ZA13*complexconjugate(Vv25)*complexconjugate(Vv45) + C23*ZA13*complexconjugate(Vv26)*complexconjugate(Vv45) + C32*ZA13*complexconjugate(Vv26)*complexconjugate(Vv45) + 2*Y1n12*ZA11*(complexconjugate(Vv25)*complexconjugate(Vv41) + complexconjugate(Vv21)*complexconjugate(Vv45)) + 2*Y2n33*ZA12*complexconjugate(Vv23)*complexconjugate(Vv46) + C13*ZA13*complexconjugate(Vv24)*complexconjugate(Vv46) + C31*ZA13*complexconjugate(Vv24)*complexconjugate(Vv46) + C23*ZA13*complexconjugate(Vv25)*complexconjugate(Vv46) + C32*ZA13*complexconjugate(Vv25)*complexconjugate(Vv46))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_468 = Coupling(name = 'GC_468',
	 value = '-(Vv26*Vv44*ZA23*complexconjugate(C13) + Vv26*Vv45*ZA23*complexconjugate(C23) + Vv26*Vv44*ZA23*complexconjugate(C31) + Vv26*Vv45*ZA23*complexconjugate(C32) + 2*Vv21*Vv44*ZA21*complexconjugate(Y1n11) + 2*Vv21*Vv45*ZA21*complexconjugate(Y1n12) + 2*Vv22*Vv44*ZA21*complexconjugate(Y1n21) + Vv24*(ZA23*(2*Vv44*complexconjugate(BB11) - Vv45*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv46*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv41*ZA21*complexconjugate(Y1n11) + 2*Vv42*ZA21*complexconjugate(Y1n21)) + 2*Vv22*Vv45*ZA21*complexconjugate(Y1n22) + Vv25*(ZA23*(-(Vv44*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv45*complexconjugate(BB22) + Vv46*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv41*ZA21*complexconjugate(Y1n12) + 2*Vv42*ZA21*complexconjugate(Y1n22)) + 2*Vv26*Vv43*ZA22*complexconjugate(Y2n33) + 2*Vv23*Vv46*ZA22*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_469 = Coupling(name = 'GC_469',
	 value = '(2*Y1n21*ZA21*complexconjugate(Vv24)*complexconjugate(Vv42) + 2*Y1n22*ZA21*complexconjugate(Vv25)*complexconjugate(Vv42) + 2*Y2n33*ZA22*complexconjugate(Vv26)*complexconjugate(Vv43) + 2*Y1n21*ZA21*complexconjugate(Vv22)*complexconjugate(Vv44) + 2*BB11*ZA23*complexconjugate(Vv24)*complexconjugate(Vv44) - BB12*ZA23*complexconjugate(Vv25)*complexconjugate(Vv44) - BB21*ZA23*complexconjugate(Vv25)*complexconjugate(Vv44) + C13*ZA23*complexconjugate(Vv26)*complexconjugate(Vv44) + C31*ZA23*complexconjugate(Vv26)*complexconjugate(Vv44) + 2*Y1n11*ZA21*(complexconjugate(Vv24)*complexconjugate(Vv41) + complexconjugate(Vv21)*complexconjugate(Vv44)) + 2*Y1n22*ZA21*complexconjugate(Vv22)*complexconjugate(Vv45) - BB12*ZA23*complexconjugate(Vv24)*complexconjugate(Vv45) - BB21*ZA23*complexconjugate(Vv24)*complexconjugate(Vv45) - 2*BB22*ZA23*complexconjugate(Vv25)*complexconjugate(Vv45) + C23*ZA23*complexconjugate(Vv26)*complexconjugate(Vv45) + C32*ZA23*complexconjugate(Vv26)*complexconjugate(Vv45) + 2*Y1n12*ZA21*(complexconjugate(Vv25)*complexconjugate(Vv41) + complexconjugate(Vv21)*complexconjugate(Vv45)) + 2*Y2n33*ZA22*complexconjugate(Vv23)*complexconjugate(Vv46) + C13*ZA23*complexconjugate(Vv24)*complexconjugate(Vv46) + C31*ZA23*complexconjugate(Vv24)*complexconjugate(Vv46) + C23*ZA23*complexconjugate(Vv25)*complexconjugate(Vv46) + C32*ZA23*complexconjugate(Vv25)*complexconjugate(Vv46))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_470 = Coupling(name = 'GC_470',
	 value = '-(Vv26*Vv44*ZA33*complexconjugate(C13) + Vv26*Vv45*ZA33*complexconjugate(C23) + Vv26*Vv44*ZA33*complexconjugate(C31) + Vv26*Vv45*ZA33*complexconjugate(C32) + 2*Vv21*Vv44*ZA31*complexconjugate(Y1n11) + 2*Vv21*Vv45*ZA31*complexconjugate(Y1n12) + 2*Vv22*Vv44*ZA31*complexconjugate(Y1n21) + Vv24*(ZA33*(2*Vv44*complexconjugate(BB11) - Vv45*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv46*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv41*ZA31*complexconjugate(Y1n11) + 2*Vv42*ZA31*complexconjugate(Y1n21)) + 2*Vv22*Vv45*ZA31*complexconjugate(Y1n22) + Vv25*(ZA33*(-(Vv44*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv45*complexconjugate(BB22) + Vv46*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv41*ZA31*complexconjugate(Y1n12) + 2*Vv42*ZA31*complexconjugate(Y1n22)) + 2*Vv26*Vv43*ZA32*complexconjugate(Y2n33) + 2*Vv23*Vv46*ZA32*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_471 = Coupling(name = 'GC_471',
	 value = '(2*Y1n21*ZA31*complexconjugate(Vv24)*complexconjugate(Vv42) + 2*Y1n22*ZA31*complexconjugate(Vv25)*complexconjugate(Vv42) + 2*Y2n33*ZA32*complexconjugate(Vv26)*complexconjugate(Vv43) + 2*Y1n21*ZA31*complexconjugate(Vv22)*complexconjugate(Vv44) + 2*BB11*ZA33*complexconjugate(Vv24)*complexconjugate(Vv44) - BB12*ZA33*complexconjugate(Vv25)*complexconjugate(Vv44) - BB21*ZA33*complexconjugate(Vv25)*complexconjugate(Vv44) + C13*ZA33*complexconjugate(Vv26)*complexconjugate(Vv44) + C31*ZA33*complexconjugate(Vv26)*complexconjugate(Vv44) + 2*Y1n11*ZA31*(complexconjugate(Vv24)*complexconjugate(Vv41) + complexconjugate(Vv21)*complexconjugate(Vv44)) + 2*Y1n22*ZA31*complexconjugate(Vv22)*complexconjugate(Vv45) - BB12*ZA33*complexconjugate(Vv24)*complexconjugate(Vv45) - BB21*ZA33*complexconjugate(Vv24)*complexconjugate(Vv45) - 2*BB22*ZA33*complexconjugate(Vv25)*complexconjugate(Vv45) + C23*ZA33*complexconjugate(Vv26)*complexconjugate(Vv45) + C32*ZA33*complexconjugate(Vv26)*complexconjugate(Vv45) + 2*Y1n12*ZA31*(complexconjugate(Vv25)*complexconjugate(Vv41) + complexconjugate(Vv21)*complexconjugate(Vv45)) + 2*Y2n33*ZA32*complexconjugate(Vv23)*complexconjugate(Vv46) + C13*ZA33*complexconjugate(Vv24)*complexconjugate(Vv46) + C31*ZA33*complexconjugate(Vv24)*complexconjugate(Vv46) + C23*ZA33*complexconjugate(Vv25)*complexconjugate(Vv46) + C32*ZA33*complexconjugate(Vv25)*complexconjugate(Vv46))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_472 = Coupling(name = 'GC_472',
	 value = '-(Vv26*Vv54*ZA13*complexconjugate(C13) + Vv26*Vv55*ZA13*complexconjugate(C23) + Vv26*Vv54*ZA13*complexconjugate(C31) + Vv26*Vv55*ZA13*complexconjugate(C32) + 2*Vv21*Vv54*ZA11*complexconjugate(Y1n11) + 2*Vv21*Vv55*ZA11*complexconjugate(Y1n12) + 2*Vv22*Vv54*ZA11*complexconjugate(Y1n21) + Vv24*(ZA13*(2*Vv54*complexconjugate(BB11) - Vv55*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv56*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv51*ZA11*complexconjugate(Y1n11) + 2*Vv52*ZA11*complexconjugate(Y1n21)) + 2*Vv22*Vv55*ZA11*complexconjugate(Y1n22) + Vv25*(ZA13*(-(Vv54*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv55*complexconjugate(BB22) + Vv56*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv51*ZA11*complexconjugate(Y1n12) + 2*Vv52*ZA11*complexconjugate(Y1n22)) + 2*Vv26*Vv53*ZA12*complexconjugate(Y2n33) + 2*Vv23*Vv56*ZA12*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_473 = Coupling(name = 'GC_473',
	 value = '(2*Y1n21*ZA11*complexconjugate(Vv24)*complexconjugate(Vv52) + 2*Y1n22*ZA11*complexconjugate(Vv25)*complexconjugate(Vv52) + 2*Y2n33*ZA12*complexconjugate(Vv26)*complexconjugate(Vv53) + 2*Y1n21*ZA11*complexconjugate(Vv22)*complexconjugate(Vv54) + 2*BB11*ZA13*complexconjugate(Vv24)*complexconjugate(Vv54) - BB12*ZA13*complexconjugate(Vv25)*complexconjugate(Vv54) - BB21*ZA13*complexconjugate(Vv25)*complexconjugate(Vv54) + C13*ZA13*complexconjugate(Vv26)*complexconjugate(Vv54) + C31*ZA13*complexconjugate(Vv26)*complexconjugate(Vv54) + 2*Y1n11*ZA11*(complexconjugate(Vv24)*complexconjugate(Vv51) + complexconjugate(Vv21)*complexconjugate(Vv54)) + 2*Y1n22*ZA11*complexconjugate(Vv22)*complexconjugate(Vv55) - BB12*ZA13*complexconjugate(Vv24)*complexconjugate(Vv55) - BB21*ZA13*complexconjugate(Vv24)*complexconjugate(Vv55) - 2*BB22*ZA13*complexconjugate(Vv25)*complexconjugate(Vv55) + C23*ZA13*complexconjugate(Vv26)*complexconjugate(Vv55) + C32*ZA13*complexconjugate(Vv26)*complexconjugate(Vv55) + 2*Y1n12*ZA11*(complexconjugate(Vv25)*complexconjugate(Vv51) + complexconjugate(Vv21)*complexconjugate(Vv55)) + 2*Y2n33*ZA12*complexconjugate(Vv23)*complexconjugate(Vv56) + C13*ZA13*complexconjugate(Vv24)*complexconjugate(Vv56) + C31*ZA13*complexconjugate(Vv24)*complexconjugate(Vv56) + C23*ZA13*complexconjugate(Vv25)*complexconjugate(Vv56) + C32*ZA13*complexconjugate(Vv25)*complexconjugate(Vv56))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_474 = Coupling(name = 'GC_474',
	 value = '-(Vv26*Vv54*ZA23*complexconjugate(C13) + Vv26*Vv55*ZA23*complexconjugate(C23) + Vv26*Vv54*ZA23*complexconjugate(C31) + Vv26*Vv55*ZA23*complexconjugate(C32) + 2*Vv21*Vv54*ZA21*complexconjugate(Y1n11) + 2*Vv21*Vv55*ZA21*complexconjugate(Y1n12) + 2*Vv22*Vv54*ZA21*complexconjugate(Y1n21) + Vv24*(ZA23*(2*Vv54*complexconjugate(BB11) - Vv55*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv56*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv51*ZA21*complexconjugate(Y1n11) + 2*Vv52*ZA21*complexconjugate(Y1n21)) + 2*Vv22*Vv55*ZA21*complexconjugate(Y1n22) + Vv25*(ZA23*(-(Vv54*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv55*complexconjugate(BB22) + Vv56*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv51*ZA21*complexconjugate(Y1n12) + 2*Vv52*ZA21*complexconjugate(Y1n22)) + 2*Vv26*Vv53*ZA22*complexconjugate(Y2n33) + 2*Vv23*Vv56*ZA22*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_475 = Coupling(name = 'GC_475',
	 value = '(2*Y1n21*ZA21*complexconjugate(Vv24)*complexconjugate(Vv52) + 2*Y1n22*ZA21*complexconjugate(Vv25)*complexconjugate(Vv52) + 2*Y2n33*ZA22*complexconjugate(Vv26)*complexconjugate(Vv53) + 2*Y1n21*ZA21*complexconjugate(Vv22)*complexconjugate(Vv54) + 2*BB11*ZA23*complexconjugate(Vv24)*complexconjugate(Vv54) - BB12*ZA23*complexconjugate(Vv25)*complexconjugate(Vv54) - BB21*ZA23*complexconjugate(Vv25)*complexconjugate(Vv54) + C13*ZA23*complexconjugate(Vv26)*complexconjugate(Vv54) + C31*ZA23*complexconjugate(Vv26)*complexconjugate(Vv54) + 2*Y1n11*ZA21*(complexconjugate(Vv24)*complexconjugate(Vv51) + complexconjugate(Vv21)*complexconjugate(Vv54)) + 2*Y1n22*ZA21*complexconjugate(Vv22)*complexconjugate(Vv55) - BB12*ZA23*complexconjugate(Vv24)*complexconjugate(Vv55) - BB21*ZA23*complexconjugate(Vv24)*complexconjugate(Vv55) - 2*BB22*ZA23*complexconjugate(Vv25)*complexconjugate(Vv55) + C23*ZA23*complexconjugate(Vv26)*complexconjugate(Vv55) + C32*ZA23*complexconjugate(Vv26)*complexconjugate(Vv55) + 2*Y1n12*ZA21*(complexconjugate(Vv25)*complexconjugate(Vv51) + complexconjugate(Vv21)*complexconjugate(Vv55)) + 2*Y2n33*ZA22*complexconjugate(Vv23)*complexconjugate(Vv56) + C13*ZA23*complexconjugate(Vv24)*complexconjugate(Vv56) + C31*ZA23*complexconjugate(Vv24)*complexconjugate(Vv56) + C23*ZA23*complexconjugate(Vv25)*complexconjugate(Vv56) + C32*ZA23*complexconjugate(Vv25)*complexconjugate(Vv56))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_476 = Coupling(name = 'GC_476',
	 value = '-(Vv26*Vv54*ZA33*complexconjugate(C13) + Vv26*Vv55*ZA33*complexconjugate(C23) + Vv26*Vv54*ZA33*complexconjugate(C31) + Vv26*Vv55*ZA33*complexconjugate(C32) + 2*Vv21*Vv54*ZA31*complexconjugate(Y1n11) + 2*Vv21*Vv55*ZA31*complexconjugate(Y1n12) + 2*Vv22*Vv54*ZA31*complexconjugate(Y1n21) + Vv24*(ZA33*(2*Vv54*complexconjugate(BB11) - Vv55*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv56*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv51*ZA31*complexconjugate(Y1n11) + 2*Vv52*ZA31*complexconjugate(Y1n21)) + 2*Vv22*Vv55*ZA31*complexconjugate(Y1n22) + Vv25*(ZA33*(-(Vv54*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv55*complexconjugate(BB22) + Vv56*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv51*ZA31*complexconjugate(Y1n12) + 2*Vv52*ZA31*complexconjugate(Y1n22)) + 2*Vv26*Vv53*ZA32*complexconjugate(Y2n33) + 2*Vv23*Vv56*ZA32*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_477 = Coupling(name = 'GC_477',
	 value = '(2*Y1n21*ZA31*complexconjugate(Vv24)*complexconjugate(Vv52) + 2*Y1n22*ZA31*complexconjugate(Vv25)*complexconjugate(Vv52) + 2*Y2n33*ZA32*complexconjugate(Vv26)*complexconjugate(Vv53) + 2*Y1n21*ZA31*complexconjugate(Vv22)*complexconjugate(Vv54) + 2*BB11*ZA33*complexconjugate(Vv24)*complexconjugate(Vv54) - BB12*ZA33*complexconjugate(Vv25)*complexconjugate(Vv54) - BB21*ZA33*complexconjugate(Vv25)*complexconjugate(Vv54) + C13*ZA33*complexconjugate(Vv26)*complexconjugate(Vv54) + C31*ZA33*complexconjugate(Vv26)*complexconjugate(Vv54) + 2*Y1n11*ZA31*(complexconjugate(Vv24)*complexconjugate(Vv51) + complexconjugate(Vv21)*complexconjugate(Vv54)) + 2*Y1n22*ZA31*complexconjugate(Vv22)*complexconjugate(Vv55) - BB12*ZA33*complexconjugate(Vv24)*complexconjugate(Vv55) - BB21*ZA33*complexconjugate(Vv24)*complexconjugate(Vv55) - 2*BB22*ZA33*complexconjugate(Vv25)*complexconjugate(Vv55) + C23*ZA33*complexconjugate(Vv26)*complexconjugate(Vv55) + C32*ZA33*complexconjugate(Vv26)*complexconjugate(Vv55) + 2*Y1n12*ZA31*(complexconjugate(Vv25)*complexconjugate(Vv51) + complexconjugate(Vv21)*complexconjugate(Vv55)) + 2*Y2n33*ZA32*complexconjugate(Vv23)*complexconjugate(Vv56) + C13*ZA33*complexconjugate(Vv24)*complexconjugate(Vv56) + C31*ZA33*complexconjugate(Vv24)*complexconjugate(Vv56) + C23*ZA33*complexconjugate(Vv25)*complexconjugate(Vv56) + C32*ZA33*complexconjugate(Vv25)*complexconjugate(Vv56))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_478 = Coupling(name = 'GC_478',
	 value = '-(Vv26*Vv64*ZA13*complexconjugate(C13) + Vv26*Vv65*ZA13*complexconjugate(C23) + Vv26*Vv64*ZA13*complexconjugate(C31) + Vv26*Vv65*ZA13*complexconjugate(C32) + 2*Vv21*Vv64*ZA11*complexconjugate(Y1n11) + 2*Vv21*Vv65*ZA11*complexconjugate(Y1n12) + 2*Vv22*Vv64*ZA11*complexconjugate(Y1n21) + Vv24*(ZA13*(2*Vv64*complexconjugate(BB11) - Vv65*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv66*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv61*ZA11*complexconjugate(Y1n11) + 2*Vv62*ZA11*complexconjugate(Y1n21)) + 2*Vv22*Vv65*ZA11*complexconjugate(Y1n22) + Vv25*(ZA13*(-(Vv64*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv65*complexconjugate(BB22) + Vv66*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv61*ZA11*complexconjugate(Y1n12) + 2*Vv62*ZA11*complexconjugate(Y1n22)) + 2*Vv26*Vv63*ZA12*complexconjugate(Y2n33) + 2*Vv23*Vv66*ZA12*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_479 = Coupling(name = 'GC_479',
	 value = '(2*Y1n21*ZA11*complexconjugate(Vv24)*complexconjugate(Vv62) + 2*Y1n22*ZA11*complexconjugate(Vv25)*complexconjugate(Vv62) + 2*Y2n33*ZA12*complexconjugate(Vv26)*complexconjugate(Vv63) + 2*Y1n21*ZA11*complexconjugate(Vv22)*complexconjugate(Vv64) + 2*BB11*ZA13*complexconjugate(Vv24)*complexconjugate(Vv64) - BB12*ZA13*complexconjugate(Vv25)*complexconjugate(Vv64) - BB21*ZA13*complexconjugate(Vv25)*complexconjugate(Vv64) + C13*ZA13*complexconjugate(Vv26)*complexconjugate(Vv64) + C31*ZA13*complexconjugate(Vv26)*complexconjugate(Vv64) + 2*Y1n11*ZA11*(complexconjugate(Vv24)*complexconjugate(Vv61) + complexconjugate(Vv21)*complexconjugate(Vv64)) + 2*Y1n22*ZA11*complexconjugate(Vv22)*complexconjugate(Vv65) - BB12*ZA13*complexconjugate(Vv24)*complexconjugate(Vv65) - BB21*ZA13*complexconjugate(Vv24)*complexconjugate(Vv65) - 2*BB22*ZA13*complexconjugate(Vv25)*complexconjugate(Vv65) + C23*ZA13*complexconjugate(Vv26)*complexconjugate(Vv65) + C32*ZA13*complexconjugate(Vv26)*complexconjugate(Vv65) + 2*Y1n12*ZA11*(complexconjugate(Vv25)*complexconjugate(Vv61) + complexconjugate(Vv21)*complexconjugate(Vv65)) + 2*Y2n33*ZA12*complexconjugate(Vv23)*complexconjugate(Vv66) + C13*ZA13*complexconjugate(Vv24)*complexconjugate(Vv66) + C31*ZA13*complexconjugate(Vv24)*complexconjugate(Vv66) + C23*ZA13*complexconjugate(Vv25)*complexconjugate(Vv66) + C32*ZA13*complexconjugate(Vv25)*complexconjugate(Vv66))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_480 = Coupling(name = 'GC_480',
	 value = '-(Vv26*Vv64*ZA23*complexconjugate(C13) + Vv26*Vv65*ZA23*complexconjugate(C23) + Vv26*Vv64*ZA23*complexconjugate(C31) + Vv26*Vv65*ZA23*complexconjugate(C32) + 2*Vv21*Vv64*ZA21*complexconjugate(Y1n11) + 2*Vv21*Vv65*ZA21*complexconjugate(Y1n12) + 2*Vv22*Vv64*ZA21*complexconjugate(Y1n21) + Vv24*(ZA23*(2*Vv64*complexconjugate(BB11) - Vv65*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv66*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv61*ZA21*complexconjugate(Y1n11) + 2*Vv62*ZA21*complexconjugate(Y1n21)) + 2*Vv22*Vv65*ZA21*complexconjugate(Y1n22) + Vv25*(ZA23*(-(Vv64*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv65*complexconjugate(BB22) + Vv66*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv61*ZA21*complexconjugate(Y1n12) + 2*Vv62*ZA21*complexconjugate(Y1n22)) + 2*Vv26*Vv63*ZA22*complexconjugate(Y2n33) + 2*Vv23*Vv66*ZA22*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_481 = Coupling(name = 'GC_481',
	 value = '(2*Y1n21*ZA21*complexconjugate(Vv24)*complexconjugate(Vv62) + 2*Y1n22*ZA21*complexconjugate(Vv25)*complexconjugate(Vv62) + 2*Y2n33*ZA22*complexconjugate(Vv26)*complexconjugate(Vv63) + 2*Y1n21*ZA21*complexconjugate(Vv22)*complexconjugate(Vv64) + 2*BB11*ZA23*complexconjugate(Vv24)*complexconjugate(Vv64) - BB12*ZA23*complexconjugate(Vv25)*complexconjugate(Vv64) - BB21*ZA23*complexconjugate(Vv25)*complexconjugate(Vv64) + C13*ZA23*complexconjugate(Vv26)*complexconjugate(Vv64) + C31*ZA23*complexconjugate(Vv26)*complexconjugate(Vv64) + 2*Y1n11*ZA21*(complexconjugate(Vv24)*complexconjugate(Vv61) + complexconjugate(Vv21)*complexconjugate(Vv64)) + 2*Y1n22*ZA21*complexconjugate(Vv22)*complexconjugate(Vv65) - BB12*ZA23*complexconjugate(Vv24)*complexconjugate(Vv65) - BB21*ZA23*complexconjugate(Vv24)*complexconjugate(Vv65) - 2*BB22*ZA23*complexconjugate(Vv25)*complexconjugate(Vv65) + C23*ZA23*complexconjugate(Vv26)*complexconjugate(Vv65) + C32*ZA23*complexconjugate(Vv26)*complexconjugate(Vv65) + 2*Y1n12*ZA21*(complexconjugate(Vv25)*complexconjugate(Vv61) + complexconjugate(Vv21)*complexconjugate(Vv65)) + 2*Y2n33*ZA22*complexconjugate(Vv23)*complexconjugate(Vv66) + C13*ZA23*complexconjugate(Vv24)*complexconjugate(Vv66) + C31*ZA23*complexconjugate(Vv24)*complexconjugate(Vv66) + C23*ZA23*complexconjugate(Vv25)*complexconjugate(Vv66) + C32*ZA23*complexconjugate(Vv25)*complexconjugate(Vv66))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_482 = Coupling(name = 'GC_482',
	 value = '-(Vv26*Vv64*ZA33*complexconjugate(C13) + Vv26*Vv65*ZA33*complexconjugate(C23) + Vv26*Vv64*ZA33*complexconjugate(C31) + Vv26*Vv65*ZA33*complexconjugate(C32) + 2*Vv21*Vv64*ZA31*complexconjugate(Y1n11) + 2*Vv21*Vv65*ZA31*complexconjugate(Y1n12) + 2*Vv22*Vv64*ZA31*complexconjugate(Y1n21) + Vv24*(ZA33*(2*Vv64*complexconjugate(BB11) - Vv65*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv66*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv61*ZA31*complexconjugate(Y1n11) + 2*Vv62*ZA31*complexconjugate(Y1n21)) + 2*Vv22*Vv65*ZA31*complexconjugate(Y1n22) + Vv25*(ZA33*(-(Vv64*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv65*complexconjugate(BB22) + Vv66*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv61*ZA31*complexconjugate(Y1n12) + 2*Vv62*ZA31*complexconjugate(Y1n22)) + 2*Vv26*Vv63*ZA32*complexconjugate(Y2n33) + 2*Vv23*Vv66*ZA32*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_483 = Coupling(name = 'GC_483',
	 value = '(2*Y1n21*ZA31*complexconjugate(Vv24)*complexconjugate(Vv62) + 2*Y1n22*ZA31*complexconjugate(Vv25)*complexconjugate(Vv62) + 2*Y2n33*ZA32*complexconjugate(Vv26)*complexconjugate(Vv63) + 2*Y1n21*ZA31*complexconjugate(Vv22)*complexconjugate(Vv64) + 2*BB11*ZA33*complexconjugate(Vv24)*complexconjugate(Vv64) - BB12*ZA33*complexconjugate(Vv25)*complexconjugate(Vv64) - BB21*ZA33*complexconjugate(Vv25)*complexconjugate(Vv64) + C13*ZA33*complexconjugate(Vv26)*complexconjugate(Vv64) + C31*ZA33*complexconjugate(Vv26)*complexconjugate(Vv64) + 2*Y1n11*ZA31*(complexconjugate(Vv24)*complexconjugate(Vv61) + complexconjugate(Vv21)*complexconjugate(Vv64)) + 2*Y1n22*ZA31*complexconjugate(Vv22)*complexconjugate(Vv65) - BB12*ZA33*complexconjugate(Vv24)*complexconjugate(Vv65) - BB21*ZA33*complexconjugate(Vv24)*complexconjugate(Vv65) - 2*BB22*ZA33*complexconjugate(Vv25)*complexconjugate(Vv65) + C23*ZA33*complexconjugate(Vv26)*complexconjugate(Vv65) + C32*ZA33*complexconjugate(Vv26)*complexconjugate(Vv65) + 2*Y1n12*ZA31*(complexconjugate(Vv25)*complexconjugate(Vv61) + complexconjugate(Vv21)*complexconjugate(Vv65)) + 2*Y2n33*ZA32*complexconjugate(Vv23)*complexconjugate(Vv66) + C13*ZA33*complexconjugate(Vv24)*complexconjugate(Vv66) + C31*ZA33*complexconjugate(Vv24)*complexconjugate(Vv66) + C23*ZA33*complexconjugate(Vv25)*complexconjugate(Vv66) + C32*ZA33*complexconjugate(Vv25)*complexconjugate(Vv66))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_484 = Coupling(name = 'GC_484',
	 value = '-(Vv34*Vv36*ZA13*complexconjugate(C13) + Vv35*Vv36*ZA13*complexconjugate(C23) + Vv34*Vv36*ZA13*complexconjugate(C31) + Vv35*Vv36*ZA13*complexconjugate(C32) + 2*Vv31*Vv34*ZA11*complexconjugate(Y1n11) + 2*Vv31*Vv35*ZA11*complexconjugate(Y1n12) + 2*Vv32*Vv34*ZA11*complexconjugate(Y1n21) + Vv34*(ZA13*(2*Vv34*complexconjugate(BB11) - Vv35*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv36*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv31*ZA11*complexconjugate(Y1n11) + 2*Vv32*ZA11*complexconjugate(Y1n21)) + 2*Vv32*Vv35*ZA11*complexconjugate(Y1n22) + Vv35*(ZA13*(-(Vv34*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv35*complexconjugate(BB22) + Vv36*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv31*ZA11*complexconjugate(Y1n12) + 2*Vv32*ZA11*complexconjugate(Y1n22)) + 4*Vv33*Vv36*ZA12*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_485 = Coupling(name = 'GC_485',
	 value = '(4*Y1n11*ZA11*complexconjugate(Vv31)*complexconjugate(Vv34) + 4*Y1n21*ZA11*complexconjugate(Vv32)*complexconjugate(Vv34) + 2*BB11*ZA13*complexconjugate(Vv34)**2 + 4*Y1n12*ZA11*complexconjugate(Vv31)*complexconjugate(Vv35) + 4*Y1n22*ZA11*complexconjugate(Vv32)*complexconjugate(Vv35) - 2*BB12*ZA13*complexconjugate(Vv34)*complexconjugate(Vv35) - 2*BB21*ZA13*complexconjugate(Vv34)*complexconjugate(Vv35) - 2*BB22*ZA13*complexconjugate(Vv35)**2 + 4*Y2n33*ZA12*complexconjugate(Vv33)*complexconjugate(Vv36) + 2*C13*ZA13*complexconjugate(Vv34)*complexconjugate(Vv36) + 2*C31*ZA13*complexconjugate(Vv34)*complexconjugate(Vv36) + 2*C23*ZA13*complexconjugate(Vv35)*complexconjugate(Vv36) + 2*C32*ZA13*complexconjugate(Vv35)*complexconjugate(Vv36))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_486 = Coupling(name = 'GC_486',
	 value = '-(Vv34*Vv36*ZA23*complexconjugate(C13) + Vv35*Vv36*ZA23*complexconjugate(C23) + Vv34*Vv36*ZA23*complexconjugate(C31) + Vv35*Vv36*ZA23*complexconjugate(C32) + 2*Vv31*Vv34*ZA21*complexconjugate(Y1n11) + 2*Vv31*Vv35*ZA21*complexconjugate(Y1n12) + 2*Vv32*Vv34*ZA21*complexconjugate(Y1n21) + Vv34*(ZA23*(2*Vv34*complexconjugate(BB11) - Vv35*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv36*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv31*ZA21*complexconjugate(Y1n11) + 2*Vv32*ZA21*complexconjugate(Y1n21)) + 2*Vv32*Vv35*ZA21*complexconjugate(Y1n22) + Vv35*(ZA23*(-(Vv34*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv35*complexconjugate(BB22) + Vv36*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv31*ZA21*complexconjugate(Y1n12) + 2*Vv32*ZA21*complexconjugate(Y1n22)) + 4*Vv33*Vv36*ZA22*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_487 = Coupling(name = 'GC_487',
	 value = '(4*Y1n11*ZA21*complexconjugate(Vv31)*complexconjugate(Vv34) + 4*Y1n21*ZA21*complexconjugate(Vv32)*complexconjugate(Vv34) + 2*BB11*ZA23*complexconjugate(Vv34)**2 + 4*Y1n12*ZA21*complexconjugate(Vv31)*complexconjugate(Vv35) + 4*Y1n22*ZA21*complexconjugate(Vv32)*complexconjugate(Vv35) - 2*BB12*ZA23*complexconjugate(Vv34)*complexconjugate(Vv35) - 2*BB21*ZA23*complexconjugate(Vv34)*complexconjugate(Vv35) - 2*BB22*ZA23*complexconjugate(Vv35)**2 + 4*Y2n33*ZA22*complexconjugate(Vv33)*complexconjugate(Vv36) + 2*C13*ZA23*complexconjugate(Vv34)*complexconjugate(Vv36) + 2*C31*ZA23*complexconjugate(Vv34)*complexconjugate(Vv36) + 2*C23*ZA23*complexconjugate(Vv35)*complexconjugate(Vv36) + 2*C32*ZA23*complexconjugate(Vv35)*complexconjugate(Vv36))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_488 = Coupling(name = 'GC_488',
	 value = '-(Vv34*Vv36*ZA33*complexconjugate(C13) + Vv35*Vv36*ZA33*complexconjugate(C23) + Vv34*Vv36*ZA33*complexconjugate(C31) + Vv35*Vv36*ZA33*complexconjugate(C32) + 2*Vv31*Vv34*ZA31*complexconjugate(Y1n11) + 2*Vv31*Vv35*ZA31*complexconjugate(Y1n12) + 2*Vv32*Vv34*ZA31*complexconjugate(Y1n21) + Vv34*(ZA33*(2*Vv34*complexconjugate(BB11) - Vv35*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv36*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv31*ZA31*complexconjugate(Y1n11) + 2*Vv32*ZA31*complexconjugate(Y1n21)) + 2*Vv32*Vv35*ZA31*complexconjugate(Y1n22) + Vv35*(ZA33*(-(Vv34*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv35*complexconjugate(BB22) + Vv36*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv31*ZA31*complexconjugate(Y1n12) + 2*Vv32*ZA31*complexconjugate(Y1n22)) + 4*Vv33*Vv36*ZA32*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_489 = Coupling(name = 'GC_489',
	 value = '(4*Y1n11*ZA31*complexconjugate(Vv31)*complexconjugate(Vv34) + 4*Y1n21*ZA31*complexconjugate(Vv32)*complexconjugate(Vv34) + 2*BB11*ZA33*complexconjugate(Vv34)**2 + 4*Y1n12*ZA31*complexconjugate(Vv31)*complexconjugate(Vv35) + 4*Y1n22*ZA31*complexconjugate(Vv32)*complexconjugate(Vv35) - 2*BB12*ZA33*complexconjugate(Vv34)*complexconjugate(Vv35) - 2*BB21*ZA33*complexconjugate(Vv34)*complexconjugate(Vv35) - 2*BB22*ZA33*complexconjugate(Vv35)**2 + 4*Y2n33*ZA32*complexconjugate(Vv33)*complexconjugate(Vv36) + 2*C13*ZA33*complexconjugate(Vv34)*complexconjugate(Vv36) + 2*C31*ZA33*complexconjugate(Vv34)*complexconjugate(Vv36) + 2*C23*ZA33*complexconjugate(Vv35)*complexconjugate(Vv36) + 2*C32*ZA33*complexconjugate(Vv35)*complexconjugate(Vv36))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_490 = Coupling(name = 'GC_490',
	 value = '-(Vv36*Vv44*ZA13*complexconjugate(C13) + Vv36*Vv45*ZA13*complexconjugate(C23) + Vv36*Vv44*ZA13*complexconjugate(C31) + Vv36*Vv45*ZA13*complexconjugate(C32) + 2*Vv31*Vv44*ZA11*complexconjugate(Y1n11) + 2*Vv31*Vv45*ZA11*complexconjugate(Y1n12) + 2*Vv32*Vv44*ZA11*complexconjugate(Y1n21) + Vv34*(ZA13*(2*Vv44*complexconjugate(BB11) - Vv45*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv46*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv41*ZA11*complexconjugate(Y1n11) + 2*Vv42*ZA11*complexconjugate(Y1n21)) + 2*Vv32*Vv45*ZA11*complexconjugate(Y1n22) + Vv35*(ZA13*(-(Vv44*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv45*complexconjugate(BB22) + Vv46*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv41*ZA11*complexconjugate(Y1n12) + 2*Vv42*ZA11*complexconjugate(Y1n22)) + 2*Vv36*Vv43*ZA12*complexconjugate(Y2n33) + 2*Vv33*Vv46*ZA12*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_491 = Coupling(name = 'GC_491',
	 value = '(2*Y1n21*ZA11*complexconjugate(Vv34)*complexconjugate(Vv42) + 2*Y1n22*ZA11*complexconjugate(Vv35)*complexconjugate(Vv42) + 2*Y2n33*ZA12*complexconjugate(Vv36)*complexconjugate(Vv43) + 2*Y1n21*ZA11*complexconjugate(Vv32)*complexconjugate(Vv44) + 2*BB11*ZA13*complexconjugate(Vv34)*complexconjugate(Vv44) - BB12*ZA13*complexconjugate(Vv35)*complexconjugate(Vv44) - BB21*ZA13*complexconjugate(Vv35)*complexconjugate(Vv44) + C13*ZA13*complexconjugate(Vv36)*complexconjugate(Vv44) + C31*ZA13*complexconjugate(Vv36)*complexconjugate(Vv44) + 2*Y1n11*ZA11*(complexconjugate(Vv34)*complexconjugate(Vv41) + complexconjugate(Vv31)*complexconjugate(Vv44)) + 2*Y1n22*ZA11*complexconjugate(Vv32)*complexconjugate(Vv45) - BB12*ZA13*complexconjugate(Vv34)*complexconjugate(Vv45) - BB21*ZA13*complexconjugate(Vv34)*complexconjugate(Vv45) - 2*BB22*ZA13*complexconjugate(Vv35)*complexconjugate(Vv45) + C23*ZA13*complexconjugate(Vv36)*complexconjugate(Vv45) + C32*ZA13*complexconjugate(Vv36)*complexconjugate(Vv45) + 2*Y1n12*ZA11*(complexconjugate(Vv35)*complexconjugate(Vv41) + complexconjugate(Vv31)*complexconjugate(Vv45)) + 2*Y2n33*ZA12*complexconjugate(Vv33)*complexconjugate(Vv46) + C13*ZA13*complexconjugate(Vv34)*complexconjugate(Vv46) + C31*ZA13*complexconjugate(Vv34)*complexconjugate(Vv46) + C23*ZA13*complexconjugate(Vv35)*complexconjugate(Vv46) + C32*ZA13*complexconjugate(Vv35)*complexconjugate(Vv46))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_492 = Coupling(name = 'GC_492',
	 value = '-(Vv36*Vv44*ZA23*complexconjugate(C13) + Vv36*Vv45*ZA23*complexconjugate(C23) + Vv36*Vv44*ZA23*complexconjugate(C31) + Vv36*Vv45*ZA23*complexconjugate(C32) + 2*Vv31*Vv44*ZA21*complexconjugate(Y1n11) + 2*Vv31*Vv45*ZA21*complexconjugate(Y1n12) + 2*Vv32*Vv44*ZA21*complexconjugate(Y1n21) + Vv34*(ZA23*(2*Vv44*complexconjugate(BB11) - Vv45*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv46*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv41*ZA21*complexconjugate(Y1n11) + 2*Vv42*ZA21*complexconjugate(Y1n21)) + 2*Vv32*Vv45*ZA21*complexconjugate(Y1n22) + Vv35*(ZA23*(-(Vv44*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv45*complexconjugate(BB22) + Vv46*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv41*ZA21*complexconjugate(Y1n12) + 2*Vv42*ZA21*complexconjugate(Y1n22)) + 2*Vv36*Vv43*ZA22*complexconjugate(Y2n33) + 2*Vv33*Vv46*ZA22*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_493 = Coupling(name = 'GC_493',
	 value = '(2*Y1n21*ZA21*complexconjugate(Vv34)*complexconjugate(Vv42) + 2*Y1n22*ZA21*complexconjugate(Vv35)*complexconjugate(Vv42) + 2*Y2n33*ZA22*complexconjugate(Vv36)*complexconjugate(Vv43) + 2*Y1n21*ZA21*complexconjugate(Vv32)*complexconjugate(Vv44) + 2*BB11*ZA23*complexconjugate(Vv34)*complexconjugate(Vv44) - BB12*ZA23*complexconjugate(Vv35)*complexconjugate(Vv44) - BB21*ZA23*complexconjugate(Vv35)*complexconjugate(Vv44) + C13*ZA23*complexconjugate(Vv36)*complexconjugate(Vv44) + C31*ZA23*complexconjugate(Vv36)*complexconjugate(Vv44) + 2*Y1n11*ZA21*(complexconjugate(Vv34)*complexconjugate(Vv41) + complexconjugate(Vv31)*complexconjugate(Vv44)) + 2*Y1n22*ZA21*complexconjugate(Vv32)*complexconjugate(Vv45) - BB12*ZA23*complexconjugate(Vv34)*complexconjugate(Vv45) - BB21*ZA23*complexconjugate(Vv34)*complexconjugate(Vv45) - 2*BB22*ZA23*complexconjugate(Vv35)*complexconjugate(Vv45) + C23*ZA23*complexconjugate(Vv36)*complexconjugate(Vv45) + C32*ZA23*complexconjugate(Vv36)*complexconjugate(Vv45) + 2*Y1n12*ZA21*(complexconjugate(Vv35)*complexconjugate(Vv41) + complexconjugate(Vv31)*complexconjugate(Vv45)) + 2*Y2n33*ZA22*complexconjugate(Vv33)*complexconjugate(Vv46) + C13*ZA23*complexconjugate(Vv34)*complexconjugate(Vv46) + C31*ZA23*complexconjugate(Vv34)*complexconjugate(Vv46) + C23*ZA23*complexconjugate(Vv35)*complexconjugate(Vv46) + C32*ZA23*complexconjugate(Vv35)*complexconjugate(Vv46))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_494 = Coupling(name = 'GC_494',
	 value = '-(Vv36*Vv44*ZA33*complexconjugate(C13) + Vv36*Vv45*ZA33*complexconjugate(C23) + Vv36*Vv44*ZA33*complexconjugate(C31) + Vv36*Vv45*ZA33*complexconjugate(C32) + 2*Vv31*Vv44*ZA31*complexconjugate(Y1n11) + 2*Vv31*Vv45*ZA31*complexconjugate(Y1n12) + 2*Vv32*Vv44*ZA31*complexconjugate(Y1n21) + Vv34*(ZA33*(2*Vv44*complexconjugate(BB11) - Vv45*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv46*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv41*ZA31*complexconjugate(Y1n11) + 2*Vv42*ZA31*complexconjugate(Y1n21)) + 2*Vv32*Vv45*ZA31*complexconjugate(Y1n22) + Vv35*(ZA33*(-(Vv44*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv45*complexconjugate(BB22) + Vv46*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv41*ZA31*complexconjugate(Y1n12) + 2*Vv42*ZA31*complexconjugate(Y1n22)) + 2*Vv36*Vv43*ZA32*complexconjugate(Y2n33) + 2*Vv33*Vv46*ZA32*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_495 = Coupling(name = 'GC_495',
	 value = '(2*Y1n21*ZA31*complexconjugate(Vv34)*complexconjugate(Vv42) + 2*Y1n22*ZA31*complexconjugate(Vv35)*complexconjugate(Vv42) + 2*Y2n33*ZA32*complexconjugate(Vv36)*complexconjugate(Vv43) + 2*Y1n21*ZA31*complexconjugate(Vv32)*complexconjugate(Vv44) + 2*BB11*ZA33*complexconjugate(Vv34)*complexconjugate(Vv44) - BB12*ZA33*complexconjugate(Vv35)*complexconjugate(Vv44) - BB21*ZA33*complexconjugate(Vv35)*complexconjugate(Vv44) + C13*ZA33*complexconjugate(Vv36)*complexconjugate(Vv44) + C31*ZA33*complexconjugate(Vv36)*complexconjugate(Vv44) + 2*Y1n11*ZA31*(complexconjugate(Vv34)*complexconjugate(Vv41) + complexconjugate(Vv31)*complexconjugate(Vv44)) + 2*Y1n22*ZA31*complexconjugate(Vv32)*complexconjugate(Vv45) - BB12*ZA33*complexconjugate(Vv34)*complexconjugate(Vv45) - BB21*ZA33*complexconjugate(Vv34)*complexconjugate(Vv45) - 2*BB22*ZA33*complexconjugate(Vv35)*complexconjugate(Vv45) + C23*ZA33*complexconjugate(Vv36)*complexconjugate(Vv45) + C32*ZA33*complexconjugate(Vv36)*complexconjugate(Vv45) + 2*Y1n12*ZA31*(complexconjugate(Vv35)*complexconjugate(Vv41) + complexconjugate(Vv31)*complexconjugate(Vv45)) + 2*Y2n33*ZA32*complexconjugate(Vv33)*complexconjugate(Vv46) + C13*ZA33*complexconjugate(Vv34)*complexconjugate(Vv46) + C31*ZA33*complexconjugate(Vv34)*complexconjugate(Vv46) + C23*ZA33*complexconjugate(Vv35)*complexconjugate(Vv46) + C32*ZA33*complexconjugate(Vv35)*complexconjugate(Vv46))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_496 = Coupling(name = 'GC_496',
	 value = '-(Vv36*Vv54*ZA13*complexconjugate(C13) + Vv36*Vv55*ZA13*complexconjugate(C23) + Vv36*Vv54*ZA13*complexconjugate(C31) + Vv36*Vv55*ZA13*complexconjugate(C32) + 2*Vv31*Vv54*ZA11*complexconjugate(Y1n11) + 2*Vv31*Vv55*ZA11*complexconjugate(Y1n12) + 2*Vv32*Vv54*ZA11*complexconjugate(Y1n21) + Vv34*(ZA13*(2*Vv54*complexconjugate(BB11) - Vv55*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv56*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv51*ZA11*complexconjugate(Y1n11) + 2*Vv52*ZA11*complexconjugate(Y1n21)) + 2*Vv32*Vv55*ZA11*complexconjugate(Y1n22) + Vv35*(ZA13*(-(Vv54*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv55*complexconjugate(BB22) + Vv56*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv51*ZA11*complexconjugate(Y1n12) + 2*Vv52*ZA11*complexconjugate(Y1n22)) + 2*Vv36*Vv53*ZA12*complexconjugate(Y2n33) + 2*Vv33*Vv56*ZA12*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_497 = Coupling(name = 'GC_497',
	 value = '(2*Y1n21*ZA11*complexconjugate(Vv34)*complexconjugate(Vv52) + 2*Y1n22*ZA11*complexconjugate(Vv35)*complexconjugate(Vv52) + 2*Y2n33*ZA12*complexconjugate(Vv36)*complexconjugate(Vv53) + 2*Y1n21*ZA11*complexconjugate(Vv32)*complexconjugate(Vv54) + 2*BB11*ZA13*complexconjugate(Vv34)*complexconjugate(Vv54) - BB12*ZA13*complexconjugate(Vv35)*complexconjugate(Vv54) - BB21*ZA13*complexconjugate(Vv35)*complexconjugate(Vv54) + C13*ZA13*complexconjugate(Vv36)*complexconjugate(Vv54) + C31*ZA13*complexconjugate(Vv36)*complexconjugate(Vv54) + 2*Y1n11*ZA11*(complexconjugate(Vv34)*complexconjugate(Vv51) + complexconjugate(Vv31)*complexconjugate(Vv54)) + 2*Y1n22*ZA11*complexconjugate(Vv32)*complexconjugate(Vv55) - BB12*ZA13*complexconjugate(Vv34)*complexconjugate(Vv55) - BB21*ZA13*complexconjugate(Vv34)*complexconjugate(Vv55) - 2*BB22*ZA13*complexconjugate(Vv35)*complexconjugate(Vv55) + C23*ZA13*complexconjugate(Vv36)*complexconjugate(Vv55) + C32*ZA13*complexconjugate(Vv36)*complexconjugate(Vv55) + 2*Y1n12*ZA11*(complexconjugate(Vv35)*complexconjugate(Vv51) + complexconjugate(Vv31)*complexconjugate(Vv55)) + 2*Y2n33*ZA12*complexconjugate(Vv33)*complexconjugate(Vv56) + C13*ZA13*complexconjugate(Vv34)*complexconjugate(Vv56) + C31*ZA13*complexconjugate(Vv34)*complexconjugate(Vv56) + C23*ZA13*complexconjugate(Vv35)*complexconjugate(Vv56) + C32*ZA13*complexconjugate(Vv35)*complexconjugate(Vv56))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_498 = Coupling(name = 'GC_498',
	 value = '-(Vv36*Vv54*ZA23*complexconjugate(C13) + Vv36*Vv55*ZA23*complexconjugate(C23) + Vv36*Vv54*ZA23*complexconjugate(C31) + Vv36*Vv55*ZA23*complexconjugate(C32) + 2*Vv31*Vv54*ZA21*complexconjugate(Y1n11) + 2*Vv31*Vv55*ZA21*complexconjugate(Y1n12) + 2*Vv32*Vv54*ZA21*complexconjugate(Y1n21) + Vv34*(ZA23*(2*Vv54*complexconjugate(BB11) - Vv55*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv56*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv51*ZA21*complexconjugate(Y1n11) + 2*Vv52*ZA21*complexconjugate(Y1n21)) + 2*Vv32*Vv55*ZA21*complexconjugate(Y1n22) + Vv35*(ZA23*(-(Vv54*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv55*complexconjugate(BB22) + Vv56*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv51*ZA21*complexconjugate(Y1n12) + 2*Vv52*ZA21*complexconjugate(Y1n22)) + 2*Vv36*Vv53*ZA22*complexconjugate(Y2n33) + 2*Vv33*Vv56*ZA22*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_499 = Coupling(name = 'GC_499',
	 value = '(2*Y1n21*ZA21*complexconjugate(Vv34)*complexconjugate(Vv52) + 2*Y1n22*ZA21*complexconjugate(Vv35)*complexconjugate(Vv52) + 2*Y2n33*ZA22*complexconjugate(Vv36)*complexconjugate(Vv53) + 2*Y1n21*ZA21*complexconjugate(Vv32)*complexconjugate(Vv54) + 2*BB11*ZA23*complexconjugate(Vv34)*complexconjugate(Vv54) - BB12*ZA23*complexconjugate(Vv35)*complexconjugate(Vv54) - BB21*ZA23*complexconjugate(Vv35)*complexconjugate(Vv54) + C13*ZA23*complexconjugate(Vv36)*complexconjugate(Vv54) + C31*ZA23*complexconjugate(Vv36)*complexconjugate(Vv54) + 2*Y1n11*ZA21*(complexconjugate(Vv34)*complexconjugate(Vv51) + complexconjugate(Vv31)*complexconjugate(Vv54)) + 2*Y1n22*ZA21*complexconjugate(Vv32)*complexconjugate(Vv55) - BB12*ZA23*complexconjugate(Vv34)*complexconjugate(Vv55) - BB21*ZA23*complexconjugate(Vv34)*complexconjugate(Vv55) - 2*BB22*ZA23*complexconjugate(Vv35)*complexconjugate(Vv55) + C23*ZA23*complexconjugate(Vv36)*complexconjugate(Vv55) + C32*ZA23*complexconjugate(Vv36)*complexconjugate(Vv55) + 2*Y1n12*ZA21*(complexconjugate(Vv35)*complexconjugate(Vv51) + complexconjugate(Vv31)*complexconjugate(Vv55)) + 2*Y2n33*ZA22*complexconjugate(Vv33)*complexconjugate(Vv56) + C13*ZA23*complexconjugate(Vv34)*complexconjugate(Vv56) + C31*ZA23*complexconjugate(Vv34)*complexconjugate(Vv56) + C23*ZA23*complexconjugate(Vv35)*complexconjugate(Vv56) + C32*ZA23*complexconjugate(Vv35)*complexconjugate(Vv56))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_500 = Coupling(name = 'GC_500',
	 value = '-(Vv36*Vv54*ZA33*complexconjugate(C13) + Vv36*Vv55*ZA33*complexconjugate(C23) + Vv36*Vv54*ZA33*complexconjugate(C31) + Vv36*Vv55*ZA33*complexconjugate(C32) + 2*Vv31*Vv54*ZA31*complexconjugate(Y1n11) + 2*Vv31*Vv55*ZA31*complexconjugate(Y1n12) + 2*Vv32*Vv54*ZA31*complexconjugate(Y1n21) + Vv34*(ZA33*(2*Vv54*complexconjugate(BB11) - Vv55*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv56*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv51*ZA31*complexconjugate(Y1n11) + 2*Vv52*ZA31*complexconjugate(Y1n21)) + 2*Vv32*Vv55*ZA31*complexconjugate(Y1n22) + Vv35*(ZA33*(-(Vv54*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv55*complexconjugate(BB22) + Vv56*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv51*ZA31*complexconjugate(Y1n12) + 2*Vv52*ZA31*complexconjugate(Y1n22)) + 2*Vv36*Vv53*ZA32*complexconjugate(Y2n33) + 2*Vv33*Vv56*ZA32*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_501 = Coupling(name = 'GC_501',
	 value = '(2*Y1n21*ZA31*complexconjugate(Vv34)*complexconjugate(Vv52) + 2*Y1n22*ZA31*complexconjugate(Vv35)*complexconjugate(Vv52) + 2*Y2n33*ZA32*complexconjugate(Vv36)*complexconjugate(Vv53) + 2*Y1n21*ZA31*complexconjugate(Vv32)*complexconjugate(Vv54) + 2*BB11*ZA33*complexconjugate(Vv34)*complexconjugate(Vv54) - BB12*ZA33*complexconjugate(Vv35)*complexconjugate(Vv54) - BB21*ZA33*complexconjugate(Vv35)*complexconjugate(Vv54) + C13*ZA33*complexconjugate(Vv36)*complexconjugate(Vv54) + C31*ZA33*complexconjugate(Vv36)*complexconjugate(Vv54) + 2*Y1n11*ZA31*(complexconjugate(Vv34)*complexconjugate(Vv51) + complexconjugate(Vv31)*complexconjugate(Vv54)) + 2*Y1n22*ZA31*complexconjugate(Vv32)*complexconjugate(Vv55) - BB12*ZA33*complexconjugate(Vv34)*complexconjugate(Vv55) - BB21*ZA33*complexconjugate(Vv34)*complexconjugate(Vv55) - 2*BB22*ZA33*complexconjugate(Vv35)*complexconjugate(Vv55) + C23*ZA33*complexconjugate(Vv36)*complexconjugate(Vv55) + C32*ZA33*complexconjugate(Vv36)*complexconjugate(Vv55) + 2*Y1n12*ZA31*(complexconjugate(Vv35)*complexconjugate(Vv51) + complexconjugate(Vv31)*complexconjugate(Vv55)) + 2*Y2n33*ZA32*complexconjugate(Vv33)*complexconjugate(Vv56) + C13*ZA33*complexconjugate(Vv34)*complexconjugate(Vv56) + C31*ZA33*complexconjugate(Vv34)*complexconjugate(Vv56) + C23*ZA33*complexconjugate(Vv35)*complexconjugate(Vv56) + C32*ZA33*complexconjugate(Vv35)*complexconjugate(Vv56))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_502 = Coupling(name = 'GC_502',
	 value = '-(Vv36*Vv64*ZA13*complexconjugate(C13) + Vv36*Vv65*ZA13*complexconjugate(C23) + Vv36*Vv64*ZA13*complexconjugate(C31) + Vv36*Vv65*ZA13*complexconjugate(C32) + 2*Vv31*Vv64*ZA11*complexconjugate(Y1n11) + 2*Vv31*Vv65*ZA11*complexconjugate(Y1n12) + 2*Vv32*Vv64*ZA11*complexconjugate(Y1n21) + Vv34*(ZA13*(2*Vv64*complexconjugate(BB11) - Vv65*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv66*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv61*ZA11*complexconjugate(Y1n11) + 2*Vv62*ZA11*complexconjugate(Y1n21)) + 2*Vv32*Vv65*ZA11*complexconjugate(Y1n22) + Vv35*(ZA13*(-(Vv64*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv65*complexconjugate(BB22) + Vv66*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv61*ZA11*complexconjugate(Y1n12) + 2*Vv62*ZA11*complexconjugate(Y1n22)) + 2*Vv36*Vv63*ZA12*complexconjugate(Y2n33) + 2*Vv33*Vv66*ZA12*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_503 = Coupling(name = 'GC_503',
	 value = '(2*Y1n21*ZA11*complexconjugate(Vv34)*complexconjugate(Vv62) + 2*Y1n22*ZA11*complexconjugate(Vv35)*complexconjugate(Vv62) + 2*Y2n33*ZA12*complexconjugate(Vv36)*complexconjugate(Vv63) + 2*Y1n21*ZA11*complexconjugate(Vv32)*complexconjugate(Vv64) + 2*BB11*ZA13*complexconjugate(Vv34)*complexconjugate(Vv64) - BB12*ZA13*complexconjugate(Vv35)*complexconjugate(Vv64) - BB21*ZA13*complexconjugate(Vv35)*complexconjugate(Vv64) + C13*ZA13*complexconjugate(Vv36)*complexconjugate(Vv64) + C31*ZA13*complexconjugate(Vv36)*complexconjugate(Vv64) + 2*Y1n11*ZA11*(complexconjugate(Vv34)*complexconjugate(Vv61) + complexconjugate(Vv31)*complexconjugate(Vv64)) + 2*Y1n22*ZA11*complexconjugate(Vv32)*complexconjugate(Vv65) - BB12*ZA13*complexconjugate(Vv34)*complexconjugate(Vv65) - BB21*ZA13*complexconjugate(Vv34)*complexconjugate(Vv65) - 2*BB22*ZA13*complexconjugate(Vv35)*complexconjugate(Vv65) + C23*ZA13*complexconjugate(Vv36)*complexconjugate(Vv65) + C32*ZA13*complexconjugate(Vv36)*complexconjugate(Vv65) + 2*Y1n12*ZA11*(complexconjugate(Vv35)*complexconjugate(Vv61) + complexconjugate(Vv31)*complexconjugate(Vv65)) + 2*Y2n33*ZA12*complexconjugate(Vv33)*complexconjugate(Vv66) + C13*ZA13*complexconjugate(Vv34)*complexconjugate(Vv66) + C31*ZA13*complexconjugate(Vv34)*complexconjugate(Vv66) + C23*ZA13*complexconjugate(Vv35)*complexconjugate(Vv66) + C32*ZA13*complexconjugate(Vv35)*complexconjugate(Vv66))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_504 = Coupling(name = 'GC_504',
	 value = '-(Vv36*Vv64*ZA23*complexconjugate(C13) + Vv36*Vv65*ZA23*complexconjugate(C23) + Vv36*Vv64*ZA23*complexconjugate(C31) + Vv36*Vv65*ZA23*complexconjugate(C32) + 2*Vv31*Vv64*ZA21*complexconjugate(Y1n11) + 2*Vv31*Vv65*ZA21*complexconjugate(Y1n12) + 2*Vv32*Vv64*ZA21*complexconjugate(Y1n21) + Vv34*(ZA23*(2*Vv64*complexconjugate(BB11) - Vv65*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv66*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv61*ZA21*complexconjugate(Y1n11) + 2*Vv62*ZA21*complexconjugate(Y1n21)) + 2*Vv32*Vv65*ZA21*complexconjugate(Y1n22) + Vv35*(ZA23*(-(Vv64*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv65*complexconjugate(BB22) + Vv66*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv61*ZA21*complexconjugate(Y1n12) + 2*Vv62*ZA21*complexconjugate(Y1n22)) + 2*Vv36*Vv63*ZA22*complexconjugate(Y2n33) + 2*Vv33*Vv66*ZA22*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_505 = Coupling(name = 'GC_505',
	 value = '(2*Y1n21*ZA21*complexconjugate(Vv34)*complexconjugate(Vv62) + 2*Y1n22*ZA21*complexconjugate(Vv35)*complexconjugate(Vv62) + 2*Y2n33*ZA22*complexconjugate(Vv36)*complexconjugate(Vv63) + 2*Y1n21*ZA21*complexconjugate(Vv32)*complexconjugate(Vv64) + 2*BB11*ZA23*complexconjugate(Vv34)*complexconjugate(Vv64) - BB12*ZA23*complexconjugate(Vv35)*complexconjugate(Vv64) - BB21*ZA23*complexconjugate(Vv35)*complexconjugate(Vv64) + C13*ZA23*complexconjugate(Vv36)*complexconjugate(Vv64) + C31*ZA23*complexconjugate(Vv36)*complexconjugate(Vv64) + 2*Y1n11*ZA21*(complexconjugate(Vv34)*complexconjugate(Vv61) + complexconjugate(Vv31)*complexconjugate(Vv64)) + 2*Y1n22*ZA21*complexconjugate(Vv32)*complexconjugate(Vv65) - BB12*ZA23*complexconjugate(Vv34)*complexconjugate(Vv65) - BB21*ZA23*complexconjugate(Vv34)*complexconjugate(Vv65) - 2*BB22*ZA23*complexconjugate(Vv35)*complexconjugate(Vv65) + C23*ZA23*complexconjugate(Vv36)*complexconjugate(Vv65) + C32*ZA23*complexconjugate(Vv36)*complexconjugate(Vv65) + 2*Y1n12*ZA21*(complexconjugate(Vv35)*complexconjugate(Vv61) + complexconjugate(Vv31)*complexconjugate(Vv65)) + 2*Y2n33*ZA22*complexconjugate(Vv33)*complexconjugate(Vv66) + C13*ZA23*complexconjugate(Vv34)*complexconjugate(Vv66) + C31*ZA23*complexconjugate(Vv34)*complexconjugate(Vv66) + C23*ZA23*complexconjugate(Vv35)*complexconjugate(Vv66) + C32*ZA23*complexconjugate(Vv35)*complexconjugate(Vv66))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_506 = Coupling(name = 'GC_506',
	 value = '-(Vv36*Vv64*ZA33*complexconjugate(C13) + Vv36*Vv65*ZA33*complexconjugate(C23) + Vv36*Vv64*ZA33*complexconjugate(C31) + Vv36*Vv65*ZA33*complexconjugate(C32) + 2*Vv31*Vv64*ZA31*complexconjugate(Y1n11) + 2*Vv31*Vv65*ZA31*complexconjugate(Y1n12) + 2*Vv32*Vv64*ZA31*complexconjugate(Y1n21) + Vv34*(ZA33*(2*Vv64*complexconjugate(BB11) - Vv65*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv66*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv61*ZA31*complexconjugate(Y1n11) + 2*Vv62*ZA31*complexconjugate(Y1n21)) + 2*Vv32*Vv65*ZA31*complexconjugate(Y1n22) + Vv35*(ZA33*(-(Vv64*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv65*complexconjugate(BB22) + Vv66*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv61*ZA31*complexconjugate(Y1n12) + 2*Vv62*ZA31*complexconjugate(Y1n22)) + 2*Vv36*Vv63*ZA32*complexconjugate(Y2n33) + 2*Vv33*Vv66*ZA32*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_507 = Coupling(name = 'GC_507',
	 value = '(2*Y1n21*ZA31*complexconjugate(Vv34)*complexconjugate(Vv62) + 2*Y1n22*ZA31*complexconjugate(Vv35)*complexconjugate(Vv62) + 2*Y2n33*ZA32*complexconjugate(Vv36)*complexconjugate(Vv63) + 2*Y1n21*ZA31*complexconjugate(Vv32)*complexconjugate(Vv64) + 2*BB11*ZA33*complexconjugate(Vv34)*complexconjugate(Vv64) - BB12*ZA33*complexconjugate(Vv35)*complexconjugate(Vv64) - BB21*ZA33*complexconjugate(Vv35)*complexconjugate(Vv64) + C13*ZA33*complexconjugate(Vv36)*complexconjugate(Vv64) + C31*ZA33*complexconjugate(Vv36)*complexconjugate(Vv64) + 2*Y1n11*ZA31*(complexconjugate(Vv34)*complexconjugate(Vv61) + complexconjugate(Vv31)*complexconjugate(Vv64)) + 2*Y1n22*ZA31*complexconjugate(Vv32)*complexconjugate(Vv65) - BB12*ZA33*complexconjugate(Vv34)*complexconjugate(Vv65) - BB21*ZA33*complexconjugate(Vv34)*complexconjugate(Vv65) - 2*BB22*ZA33*complexconjugate(Vv35)*complexconjugate(Vv65) + C23*ZA33*complexconjugate(Vv36)*complexconjugate(Vv65) + C32*ZA33*complexconjugate(Vv36)*complexconjugate(Vv65) + 2*Y1n12*ZA31*(complexconjugate(Vv35)*complexconjugate(Vv61) + complexconjugate(Vv31)*complexconjugate(Vv65)) + 2*Y2n33*ZA32*complexconjugate(Vv33)*complexconjugate(Vv66) + C13*ZA33*complexconjugate(Vv34)*complexconjugate(Vv66) + C31*ZA33*complexconjugate(Vv34)*complexconjugate(Vv66) + C23*ZA33*complexconjugate(Vv35)*complexconjugate(Vv66) + C32*ZA33*complexconjugate(Vv35)*complexconjugate(Vv66))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_508 = Coupling(name = 'GC_508',
	 value = '-(Vv44*Vv46*ZA13*complexconjugate(C13) + Vv45*Vv46*ZA13*complexconjugate(C23) + Vv44*Vv46*ZA13*complexconjugate(C31) + Vv45*Vv46*ZA13*complexconjugate(C32) + 2*Vv41*Vv44*ZA11*complexconjugate(Y1n11) + 2*Vv41*Vv45*ZA11*complexconjugate(Y1n12) + 2*Vv42*Vv44*ZA11*complexconjugate(Y1n21) + Vv44*(ZA13*(2*Vv44*complexconjugate(BB11) - Vv45*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv46*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv41*ZA11*complexconjugate(Y1n11) + 2*Vv42*ZA11*complexconjugate(Y1n21)) + 2*Vv42*Vv45*ZA11*complexconjugate(Y1n22) + Vv45*(ZA13*(-(Vv44*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv45*complexconjugate(BB22) + Vv46*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv41*ZA11*complexconjugate(Y1n12) + 2*Vv42*ZA11*complexconjugate(Y1n22)) + 4*Vv43*Vv46*ZA12*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_509 = Coupling(name = 'GC_509',
	 value = '(4*Y1n11*ZA11*complexconjugate(Vv41)*complexconjugate(Vv44) + 4*Y1n21*ZA11*complexconjugate(Vv42)*complexconjugate(Vv44) + 2*BB11*ZA13*complexconjugate(Vv44)**2 + 4*Y1n12*ZA11*complexconjugate(Vv41)*complexconjugate(Vv45) + 4*Y1n22*ZA11*complexconjugate(Vv42)*complexconjugate(Vv45) - 2*BB12*ZA13*complexconjugate(Vv44)*complexconjugate(Vv45) - 2*BB21*ZA13*complexconjugate(Vv44)*complexconjugate(Vv45) - 2*BB22*ZA13*complexconjugate(Vv45)**2 + 4*Y2n33*ZA12*complexconjugate(Vv43)*complexconjugate(Vv46) + 2*C13*ZA13*complexconjugate(Vv44)*complexconjugate(Vv46) + 2*C31*ZA13*complexconjugate(Vv44)*complexconjugate(Vv46) + 2*C23*ZA13*complexconjugate(Vv45)*complexconjugate(Vv46) + 2*C32*ZA13*complexconjugate(Vv45)*complexconjugate(Vv46))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_510 = Coupling(name = 'GC_510',
	 value = '-(Vv44*Vv46*ZA23*complexconjugate(C13) + Vv45*Vv46*ZA23*complexconjugate(C23) + Vv44*Vv46*ZA23*complexconjugate(C31) + Vv45*Vv46*ZA23*complexconjugate(C32) + 2*Vv41*Vv44*ZA21*complexconjugate(Y1n11) + 2*Vv41*Vv45*ZA21*complexconjugate(Y1n12) + 2*Vv42*Vv44*ZA21*complexconjugate(Y1n21) + Vv44*(ZA23*(2*Vv44*complexconjugate(BB11) - Vv45*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv46*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv41*ZA21*complexconjugate(Y1n11) + 2*Vv42*ZA21*complexconjugate(Y1n21)) + 2*Vv42*Vv45*ZA21*complexconjugate(Y1n22) + Vv45*(ZA23*(-(Vv44*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv45*complexconjugate(BB22) + Vv46*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv41*ZA21*complexconjugate(Y1n12) + 2*Vv42*ZA21*complexconjugate(Y1n22)) + 4*Vv43*Vv46*ZA22*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_511 = Coupling(name = 'GC_511',
	 value = '(4*Y1n11*ZA21*complexconjugate(Vv41)*complexconjugate(Vv44) + 4*Y1n21*ZA21*complexconjugate(Vv42)*complexconjugate(Vv44) + 2*BB11*ZA23*complexconjugate(Vv44)**2 + 4*Y1n12*ZA21*complexconjugate(Vv41)*complexconjugate(Vv45) + 4*Y1n22*ZA21*complexconjugate(Vv42)*complexconjugate(Vv45) - 2*BB12*ZA23*complexconjugate(Vv44)*complexconjugate(Vv45) - 2*BB21*ZA23*complexconjugate(Vv44)*complexconjugate(Vv45) - 2*BB22*ZA23*complexconjugate(Vv45)**2 + 4*Y2n33*ZA22*complexconjugate(Vv43)*complexconjugate(Vv46) + 2*C13*ZA23*complexconjugate(Vv44)*complexconjugate(Vv46) + 2*C31*ZA23*complexconjugate(Vv44)*complexconjugate(Vv46) + 2*C23*ZA23*complexconjugate(Vv45)*complexconjugate(Vv46) + 2*C32*ZA23*complexconjugate(Vv45)*complexconjugate(Vv46))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_512 = Coupling(name = 'GC_512',
	 value = '-(Vv44*Vv46*ZA33*complexconjugate(C13) + Vv45*Vv46*ZA33*complexconjugate(C23) + Vv44*Vv46*ZA33*complexconjugate(C31) + Vv45*Vv46*ZA33*complexconjugate(C32) + 2*Vv41*Vv44*ZA31*complexconjugate(Y1n11) + 2*Vv41*Vv45*ZA31*complexconjugate(Y1n12) + 2*Vv42*Vv44*ZA31*complexconjugate(Y1n21) + Vv44*(ZA33*(2*Vv44*complexconjugate(BB11) - Vv45*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv46*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv41*ZA31*complexconjugate(Y1n11) + 2*Vv42*ZA31*complexconjugate(Y1n21)) + 2*Vv42*Vv45*ZA31*complexconjugate(Y1n22) + Vv45*(ZA33*(-(Vv44*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv45*complexconjugate(BB22) + Vv46*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv41*ZA31*complexconjugate(Y1n12) + 2*Vv42*ZA31*complexconjugate(Y1n22)) + 4*Vv43*Vv46*ZA32*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_513 = Coupling(name = 'GC_513',
	 value = '(4*Y1n11*ZA31*complexconjugate(Vv41)*complexconjugate(Vv44) + 4*Y1n21*ZA31*complexconjugate(Vv42)*complexconjugate(Vv44) + 2*BB11*ZA33*complexconjugate(Vv44)**2 + 4*Y1n12*ZA31*complexconjugate(Vv41)*complexconjugate(Vv45) + 4*Y1n22*ZA31*complexconjugate(Vv42)*complexconjugate(Vv45) - 2*BB12*ZA33*complexconjugate(Vv44)*complexconjugate(Vv45) - 2*BB21*ZA33*complexconjugate(Vv44)*complexconjugate(Vv45) - 2*BB22*ZA33*complexconjugate(Vv45)**2 + 4*Y2n33*ZA32*complexconjugate(Vv43)*complexconjugate(Vv46) + 2*C13*ZA33*complexconjugate(Vv44)*complexconjugate(Vv46) + 2*C31*ZA33*complexconjugate(Vv44)*complexconjugate(Vv46) + 2*C23*ZA33*complexconjugate(Vv45)*complexconjugate(Vv46) + 2*C32*ZA33*complexconjugate(Vv45)*complexconjugate(Vv46))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_514 = Coupling(name = 'GC_514',
	 value = '-(Vv46*Vv54*ZA13*complexconjugate(C13) + Vv46*Vv55*ZA13*complexconjugate(C23) + Vv46*Vv54*ZA13*complexconjugate(C31) + Vv46*Vv55*ZA13*complexconjugate(C32) + 2*Vv41*Vv54*ZA11*complexconjugate(Y1n11) + 2*Vv41*Vv55*ZA11*complexconjugate(Y1n12) + 2*Vv42*Vv54*ZA11*complexconjugate(Y1n21) + Vv44*(ZA13*(2*Vv54*complexconjugate(BB11) - Vv55*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv56*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv51*ZA11*complexconjugate(Y1n11) + 2*Vv52*ZA11*complexconjugate(Y1n21)) + 2*Vv42*Vv55*ZA11*complexconjugate(Y1n22) + Vv45*(ZA13*(-(Vv54*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv55*complexconjugate(BB22) + Vv56*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv51*ZA11*complexconjugate(Y1n12) + 2*Vv52*ZA11*complexconjugate(Y1n22)) + 2*Vv46*Vv53*ZA12*complexconjugate(Y2n33) + 2*Vv43*Vv56*ZA12*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_515 = Coupling(name = 'GC_515',
	 value = '(2*Y1n21*ZA11*complexconjugate(Vv44)*complexconjugate(Vv52) + 2*Y1n22*ZA11*complexconjugate(Vv45)*complexconjugate(Vv52) + 2*Y2n33*ZA12*complexconjugate(Vv46)*complexconjugate(Vv53) + 2*Y1n21*ZA11*complexconjugate(Vv42)*complexconjugate(Vv54) + 2*BB11*ZA13*complexconjugate(Vv44)*complexconjugate(Vv54) - BB12*ZA13*complexconjugate(Vv45)*complexconjugate(Vv54) - BB21*ZA13*complexconjugate(Vv45)*complexconjugate(Vv54) + C13*ZA13*complexconjugate(Vv46)*complexconjugate(Vv54) + C31*ZA13*complexconjugate(Vv46)*complexconjugate(Vv54) + 2*Y1n11*ZA11*(complexconjugate(Vv44)*complexconjugate(Vv51) + complexconjugate(Vv41)*complexconjugate(Vv54)) + 2*Y1n22*ZA11*complexconjugate(Vv42)*complexconjugate(Vv55) - BB12*ZA13*complexconjugate(Vv44)*complexconjugate(Vv55) - BB21*ZA13*complexconjugate(Vv44)*complexconjugate(Vv55) - 2*BB22*ZA13*complexconjugate(Vv45)*complexconjugate(Vv55) + C23*ZA13*complexconjugate(Vv46)*complexconjugate(Vv55) + C32*ZA13*complexconjugate(Vv46)*complexconjugate(Vv55) + 2*Y1n12*ZA11*(complexconjugate(Vv45)*complexconjugate(Vv51) + complexconjugate(Vv41)*complexconjugate(Vv55)) + 2*Y2n33*ZA12*complexconjugate(Vv43)*complexconjugate(Vv56) + C13*ZA13*complexconjugate(Vv44)*complexconjugate(Vv56) + C31*ZA13*complexconjugate(Vv44)*complexconjugate(Vv56) + C23*ZA13*complexconjugate(Vv45)*complexconjugate(Vv56) + C32*ZA13*complexconjugate(Vv45)*complexconjugate(Vv56))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_516 = Coupling(name = 'GC_516',
	 value = '-(Vv46*Vv54*ZA23*complexconjugate(C13) + Vv46*Vv55*ZA23*complexconjugate(C23) + Vv46*Vv54*ZA23*complexconjugate(C31) + Vv46*Vv55*ZA23*complexconjugate(C32) + 2*Vv41*Vv54*ZA21*complexconjugate(Y1n11) + 2*Vv41*Vv55*ZA21*complexconjugate(Y1n12) + 2*Vv42*Vv54*ZA21*complexconjugate(Y1n21) + Vv44*(ZA23*(2*Vv54*complexconjugate(BB11) - Vv55*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv56*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv51*ZA21*complexconjugate(Y1n11) + 2*Vv52*ZA21*complexconjugate(Y1n21)) + 2*Vv42*Vv55*ZA21*complexconjugate(Y1n22) + Vv45*(ZA23*(-(Vv54*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv55*complexconjugate(BB22) + Vv56*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv51*ZA21*complexconjugate(Y1n12) + 2*Vv52*ZA21*complexconjugate(Y1n22)) + 2*Vv46*Vv53*ZA22*complexconjugate(Y2n33) + 2*Vv43*Vv56*ZA22*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_517 = Coupling(name = 'GC_517',
	 value = '(2*Y1n21*ZA21*complexconjugate(Vv44)*complexconjugate(Vv52) + 2*Y1n22*ZA21*complexconjugate(Vv45)*complexconjugate(Vv52) + 2*Y2n33*ZA22*complexconjugate(Vv46)*complexconjugate(Vv53) + 2*Y1n21*ZA21*complexconjugate(Vv42)*complexconjugate(Vv54) + 2*BB11*ZA23*complexconjugate(Vv44)*complexconjugate(Vv54) - BB12*ZA23*complexconjugate(Vv45)*complexconjugate(Vv54) - BB21*ZA23*complexconjugate(Vv45)*complexconjugate(Vv54) + C13*ZA23*complexconjugate(Vv46)*complexconjugate(Vv54) + C31*ZA23*complexconjugate(Vv46)*complexconjugate(Vv54) + 2*Y1n11*ZA21*(complexconjugate(Vv44)*complexconjugate(Vv51) + complexconjugate(Vv41)*complexconjugate(Vv54)) + 2*Y1n22*ZA21*complexconjugate(Vv42)*complexconjugate(Vv55) - BB12*ZA23*complexconjugate(Vv44)*complexconjugate(Vv55) - BB21*ZA23*complexconjugate(Vv44)*complexconjugate(Vv55) - 2*BB22*ZA23*complexconjugate(Vv45)*complexconjugate(Vv55) + C23*ZA23*complexconjugate(Vv46)*complexconjugate(Vv55) + C32*ZA23*complexconjugate(Vv46)*complexconjugate(Vv55) + 2*Y1n12*ZA21*(complexconjugate(Vv45)*complexconjugate(Vv51) + complexconjugate(Vv41)*complexconjugate(Vv55)) + 2*Y2n33*ZA22*complexconjugate(Vv43)*complexconjugate(Vv56) + C13*ZA23*complexconjugate(Vv44)*complexconjugate(Vv56) + C31*ZA23*complexconjugate(Vv44)*complexconjugate(Vv56) + C23*ZA23*complexconjugate(Vv45)*complexconjugate(Vv56) + C32*ZA23*complexconjugate(Vv45)*complexconjugate(Vv56))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_518 = Coupling(name = 'GC_518',
	 value = '-(Vv46*Vv54*ZA33*complexconjugate(C13) + Vv46*Vv55*ZA33*complexconjugate(C23) + Vv46*Vv54*ZA33*complexconjugate(C31) + Vv46*Vv55*ZA33*complexconjugate(C32) + 2*Vv41*Vv54*ZA31*complexconjugate(Y1n11) + 2*Vv41*Vv55*ZA31*complexconjugate(Y1n12) + 2*Vv42*Vv54*ZA31*complexconjugate(Y1n21) + Vv44*(ZA33*(2*Vv54*complexconjugate(BB11) - Vv55*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv56*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv51*ZA31*complexconjugate(Y1n11) + 2*Vv52*ZA31*complexconjugate(Y1n21)) + 2*Vv42*Vv55*ZA31*complexconjugate(Y1n22) + Vv45*(ZA33*(-(Vv54*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv55*complexconjugate(BB22) + Vv56*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv51*ZA31*complexconjugate(Y1n12) + 2*Vv52*ZA31*complexconjugate(Y1n22)) + 2*Vv46*Vv53*ZA32*complexconjugate(Y2n33) + 2*Vv43*Vv56*ZA32*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_519 = Coupling(name = 'GC_519',
	 value = '(2*Y1n21*ZA31*complexconjugate(Vv44)*complexconjugate(Vv52) + 2*Y1n22*ZA31*complexconjugate(Vv45)*complexconjugate(Vv52) + 2*Y2n33*ZA32*complexconjugate(Vv46)*complexconjugate(Vv53) + 2*Y1n21*ZA31*complexconjugate(Vv42)*complexconjugate(Vv54) + 2*BB11*ZA33*complexconjugate(Vv44)*complexconjugate(Vv54) - BB12*ZA33*complexconjugate(Vv45)*complexconjugate(Vv54) - BB21*ZA33*complexconjugate(Vv45)*complexconjugate(Vv54) + C13*ZA33*complexconjugate(Vv46)*complexconjugate(Vv54) + C31*ZA33*complexconjugate(Vv46)*complexconjugate(Vv54) + 2*Y1n11*ZA31*(complexconjugate(Vv44)*complexconjugate(Vv51) + complexconjugate(Vv41)*complexconjugate(Vv54)) + 2*Y1n22*ZA31*complexconjugate(Vv42)*complexconjugate(Vv55) - BB12*ZA33*complexconjugate(Vv44)*complexconjugate(Vv55) - BB21*ZA33*complexconjugate(Vv44)*complexconjugate(Vv55) - 2*BB22*ZA33*complexconjugate(Vv45)*complexconjugate(Vv55) + C23*ZA33*complexconjugate(Vv46)*complexconjugate(Vv55) + C32*ZA33*complexconjugate(Vv46)*complexconjugate(Vv55) + 2*Y1n12*ZA31*(complexconjugate(Vv45)*complexconjugate(Vv51) + complexconjugate(Vv41)*complexconjugate(Vv55)) + 2*Y2n33*ZA32*complexconjugate(Vv43)*complexconjugate(Vv56) + C13*ZA33*complexconjugate(Vv44)*complexconjugate(Vv56) + C31*ZA33*complexconjugate(Vv44)*complexconjugate(Vv56) + C23*ZA33*complexconjugate(Vv45)*complexconjugate(Vv56) + C32*ZA33*complexconjugate(Vv45)*complexconjugate(Vv56))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_520 = Coupling(name = 'GC_520',
	 value = '-(Vv46*Vv64*ZA13*complexconjugate(C13) + Vv46*Vv65*ZA13*complexconjugate(C23) + Vv46*Vv64*ZA13*complexconjugate(C31) + Vv46*Vv65*ZA13*complexconjugate(C32) + 2*Vv41*Vv64*ZA11*complexconjugate(Y1n11) + 2*Vv41*Vv65*ZA11*complexconjugate(Y1n12) + 2*Vv42*Vv64*ZA11*complexconjugate(Y1n21) + Vv44*(ZA13*(2*Vv64*complexconjugate(BB11) - Vv65*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv66*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv61*ZA11*complexconjugate(Y1n11) + 2*Vv62*ZA11*complexconjugate(Y1n21)) + 2*Vv42*Vv65*ZA11*complexconjugate(Y1n22) + Vv45*(ZA13*(-(Vv64*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv65*complexconjugate(BB22) + Vv66*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv61*ZA11*complexconjugate(Y1n12) + 2*Vv62*ZA11*complexconjugate(Y1n22)) + 2*Vv46*Vv63*ZA12*complexconjugate(Y2n33) + 2*Vv43*Vv66*ZA12*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_521 = Coupling(name = 'GC_521',
	 value = '(2*Y1n21*ZA11*complexconjugate(Vv44)*complexconjugate(Vv62) + 2*Y1n22*ZA11*complexconjugate(Vv45)*complexconjugate(Vv62) + 2*Y2n33*ZA12*complexconjugate(Vv46)*complexconjugate(Vv63) + 2*Y1n21*ZA11*complexconjugate(Vv42)*complexconjugate(Vv64) + 2*BB11*ZA13*complexconjugate(Vv44)*complexconjugate(Vv64) - BB12*ZA13*complexconjugate(Vv45)*complexconjugate(Vv64) - BB21*ZA13*complexconjugate(Vv45)*complexconjugate(Vv64) + C13*ZA13*complexconjugate(Vv46)*complexconjugate(Vv64) + C31*ZA13*complexconjugate(Vv46)*complexconjugate(Vv64) + 2*Y1n11*ZA11*(complexconjugate(Vv44)*complexconjugate(Vv61) + complexconjugate(Vv41)*complexconjugate(Vv64)) + 2*Y1n22*ZA11*complexconjugate(Vv42)*complexconjugate(Vv65) - BB12*ZA13*complexconjugate(Vv44)*complexconjugate(Vv65) - BB21*ZA13*complexconjugate(Vv44)*complexconjugate(Vv65) - 2*BB22*ZA13*complexconjugate(Vv45)*complexconjugate(Vv65) + C23*ZA13*complexconjugate(Vv46)*complexconjugate(Vv65) + C32*ZA13*complexconjugate(Vv46)*complexconjugate(Vv65) + 2*Y1n12*ZA11*(complexconjugate(Vv45)*complexconjugate(Vv61) + complexconjugate(Vv41)*complexconjugate(Vv65)) + 2*Y2n33*ZA12*complexconjugate(Vv43)*complexconjugate(Vv66) + C13*ZA13*complexconjugate(Vv44)*complexconjugate(Vv66) + C31*ZA13*complexconjugate(Vv44)*complexconjugate(Vv66) + C23*ZA13*complexconjugate(Vv45)*complexconjugate(Vv66) + C32*ZA13*complexconjugate(Vv45)*complexconjugate(Vv66))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_522 = Coupling(name = 'GC_522',
	 value = '-(Vv46*Vv64*ZA23*complexconjugate(C13) + Vv46*Vv65*ZA23*complexconjugate(C23) + Vv46*Vv64*ZA23*complexconjugate(C31) + Vv46*Vv65*ZA23*complexconjugate(C32) + 2*Vv41*Vv64*ZA21*complexconjugate(Y1n11) + 2*Vv41*Vv65*ZA21*complexconjugate(Y1n12) + 2*Vv42*Vv64*ZA21*complexconjugate(Y1n21) + Vv44*(ZA23*(2*Vv64*complexconjugate(BB11) - Vv65*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv66*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv61*ZA21*complexconjugate(Y1n11) + 2*Vv62*ZA21*complexconjugate(Y1n21)) + 2*Vv42*Vv65*ZA21*complexconjugate(Y1n22) + Vv45*(ZA23*(-(Vv64*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv65*complexconjugate(BB22) + Vv66*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv61*ZA21*complexconjugate(Y1n12) + 2*Vv62*ZA21*complexconjugate(Y1n22)) + 2*Vv46*Vv63*ZA22*complexconjugate(Y2n33) + 2*Vv43*Vv66*ZA22*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_523 = Coupling(name = 'GC_523',
	 value = '(2*Y1n21*ZA21*complexconjugate(Vv44)*complexconjugate(Vv62) + 2*Y1n22*ZA21*complexconjugate(Vv45)*complexconjugate(Vv62) + 2*Y2n33*ZA22*complexconjugate(Vv46)*complexconjugate(Vv63) + 2*Y1n21*ZA21*complexconjugate(Vv42)*complexconjugate(Vv64) + 2*BB11*ZA23*complexconjugate(Vv44)*complexconjugate(Vv64) - BB12*ZA23*complexconjugate(Vv45)*complexconjugate(Vv64) - BB21*ZA23*complexconjugate(Vv45)*complexconjugate(Vv64) + C13*ZA23*complexconjugate(Vv46)*complexconjugate(Vv64) + C31*ZA23*complexconjugate(Vv46)*complexconjugate(Vv64) + 2*Y1n11*ZA21*(complexconjugate(Vv44)*complexconjugate(Vv61) + complexconjugate(Vv41)*complexconjugate(Vv64)) + 2*Y1n22*ZA21*complexconjugate(Vv42)*complexconjugate(Vv65) - BB12*ZA23*complexconjugate(Vv44)*complexconjugate(Vv65) - BB21*ZA23*complexconjugate(Vv44)*complexconjugate(Vv65) - 2*BB22*ZA23*complexconjugate(Vv45)*complexconjugate(Vv65) + C23*ZA23*complexconjugate(Vv46)*complexconjugate(Vv65) + C32*ZA23*complexconjugate(Vv46)*complexconjugate(Vv65) + 2*Y1n12*ZA21*(complexconjugate(Vv45)*complexconjugate(Vv61) + complexconjugate(Vv41)*complexconjugate(Vv65)) + 2*Y2n33*ZA22*complexconjugate(Vv43)*complexconjugate(Vv66) + C13*ZA23*complexconjugate(Vv44)*complexconjugate(Vv66) + C31*ZA23*complexconjugate(Vv44)*complexconjugate(Vv66) + C23*ZA23*complexconjugate(Vv45)*complexconjugate(Vv66) + C32*ZA23*complexconjugate(Vv45)*complexconjugate(Vv66))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_524 = Coupling(name = 'GC_524',
	 value = '-(Vv46*Vv64*ZA33*complexconjugate(C13) + Vv46*Vv65*ZA33*complexconjugate(C23) + Vv46*Vv64*ZA33*complexconjugate(C31) + Vv46*Vv65*ZA33*complexconjugate(C32) + 2*Vv41*Vv64*ZA31*complexconjugate(Y1n11) + 2*Vv41*Vv65*ZA31*complexconjugate(Y1n12) + 2*Vv42*Vv64*ZA31*complexconjugate(Y1n21) + Vv44*(ZA33*(2*Vv64*complexconjugate(BB11) - Vv65*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv66*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv61*ZA31*complexconjugate(Y1n11) + 2*Vv62*ZA31*complexconjugate(Y1n21)) + 2*Vv42*Vv65*ZA31*complexconjugate(Y1n22) + Vv45*(ZA33*(-(Vv64*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv65*complexconjugate(BB22) + Vv66*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv61*ZA31*complexconjugate(Y1n12) + 2*Vv62*ZA31*complexconjugate(Y1n22)) + 2*Vv46*Vv63*ZA32*complexconjugate(Y2n33) + 2*Vv43*Vv66*ZA32*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_525 = Coupling(name = 'GC_525',
	 value = '(2*Y1n21*ZA31*complexconjugate(Vv44)*complexconjugate(Vv62) + 2*Y1n22*ZA31*complexconjugate(Vv45)*complexconjugate(Vv62) + 2*Y2n33*ZA32*complexconjugate(Vv46)*complexconjugate(Vv63) + 2*Y1n21*ZA31*complexconjugate(Vv42)*complexconjugate(Vv64) + 2*BB11*ZA33*complexconjugate(Vv44)*complexconjugate(Vv64) - BB12*ZA33*complexconjugate(Vv45)*complexconjugate(Vv64) - BB21*ZA33*complexconjugate(Vv45)*complexconjugate(Vv64) + C13*ZA33*complexconjugate(Vv46)*complexconjugate(Vv64) + C31*ZA33*complexconjugate(Vv46)*complexconjugate(Vv64) + 2*Y1n11*ZA31*(complexconjugate(Vv44)*complexconjugate(Vv61) + complexconjugate(Vv41)*complexconjugate(Vv64)) + 2*Y1n22*ZA31*complexconjugate(Vv42)*complexconjugate(Vv65) - BB12*ZA33*complexconjugate(Vv44)*complexconjugate(Vv65) - BB21*ZA33*complexconjugate(Vv44)*complexconjugate(Vv65) - 2*BB22*ZA33*complexconjugate(Vv45)*complexconjugate(Vv65) + C23*ZA33*complexconjugate(Vv46)*complexconjugate(Vv65) + C32*ZA33*complexconjugate(Vv46)*complexconjugate(Vv65) + 2*Y1n12*ZA31*(complexconjugate(Vv45)*complexconjugate(Vv61) + complexconjugate(Vv41)*complexconjugate(Vv65)) + 2*Y2n33*ZA32*complexconjugate(Vv43)*complexconjugate(Vv66) + C13*ZA33*complexconjugate(Vv44)*complexconjugate(Vv66) + C31*ZA33*complexconjugate(Vv44)*complexconjugate(Vv66) + C23*ZA33*complexconjugate(Vv45)*complexconjugate(Vv66) + C32*ZA33*complexconjugate(Vv45)*complexconjugate(Vv66))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_526 = Coupling(name = 'GC_526',
	 value = '-(Vv54*Vv56*ZA13*complexconjugate(C13) + Vv55*Vv56*ZA13*complexconjugate(C23) + Vv54*Vv56*ZA13*complexconjugate(C31) + Vv55*Vv56*ZA13*complexconjugate(C32) + 2*Vv51*Vv54*ZA11*complexconjugate(Y1n11) + 2*Vv51*Vv55*ZA11*complexconjugate(Y1n12) + 2*Vv52*Vv54*ZA11*complexconjugate(Y1n21) + Vv54*(ZA13*(2*Vv54*complexconjugate(BB11) - Vv55*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv56*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv51*ZA11*complexconjugate(Y1n11) + 2*Vv52*ZA11*complexconjugate(Y1n21)) + 2*Vv52*Vv55*ZA11*complexconjugate(Y1n22) + Vv55*(ZA13*(-(Vv54*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv55*complexconjugate(BB22) + Vv56*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv51*ZA11*complexconjugate(Y1n12) + 2*Vv52*ZA11*complexconjugate(Y1n22)) + 4*Vv53*Vv56*ZA12*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_527 = Coupling(name = 'GC_527',
	 value = '(4*Y1n11*ZA11*complexconjugate(Vv51)*complexconjugate(Vv54) + 4*Y1n21*ZA11*complexconjugate(Vv52)*complexconjugate(Vv54) + 2*BB11*ZA13*complexconjugate(Vv54)**2 + 4*Y1n12*ZA11*complexconjugate(Vv51)*complexconjugate(Vv55) + 4*Y1n22*ZA11*complexconjugate(Vv52)*complexconjugate(Vv55) - 2*BB12*ZA13*complexconjugate(Vv54)*complexconjugate(Vv55) - 2*BB21*ZA13*complexconjugate(Vv54)*complexconjugate(Vv55) - 2*BB22*ZA13*complexconjugate(Vv55)**2 + 4*Y2n33*ZA12*complexconjugate(Vv53)*complexconjugate(Vv56) + 2*C13*ZA13*complexconjugate(Vv54)*complexconjugate(Vv56) + 2*C31*ZA13*complexconjugate(Vv54)*complexconjugate(Vv56) + 2*C23*ZA13*complexconjugate(Vv55)*complexconjugate(Vv56) + 2*C32*ZA13*complexconjugate(Vv55)*complexconjugate(Vv56))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_528 = Coupling(name = 'GC_528',
	 value = '-(Vv54*Vv56*ZA23*complexconjugate(C13) + Vv55*Vv56*ZA23*complexconjugate(C23) + Vv54*Vv56*ZA23*complexconjugate(C31) + Vv55*Vv56*ZA23*complexconjugate(C32) + 2*Vv51*Vv54*ZA21*complexconjugate(Y1n11) + 2*Vv51*Vv55*ZA21*complexconjugate(Y1n12) + 2*Vv52*Vv54*ZA21*complexconjugate(Y1n21) + Vv54*(ZA23*(2*Vv54*complexconjugate(BB11) - Vv55*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv56*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv51*ZA21*complexconjugate(Y1n11) + 2*Vv52*ZA21*complexconjugate(Y1n21)) + 2*Vv52*Vv55*ZA21*complexconjugate(Y1n22) + Vv55*(ZA23*(-(Vv54*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv55*complexconjugate(BB22) + Vv56*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv51*ZA21*complexconjugate(Y1n12) + 2*Vv52*ZA21*complexconjugate(Y1n22)) + 4*Vv53*Vv56*ZA22*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_529 = Coupling(name = 'GC_529',
	 value = '(4*Y1n11*ZA21*complexconjugate(Vv51)*complexconjugate(Vv54) + 4*Y1n21*ZA21*complexconjugate(Vv52)*complexconjugate(Vv54) + 2*BB11*ZA23*complexconjugate(Vv54)**2 + 4*Y1n12*ZA21*complexconjugate(Vv51)*complexconjugate(Vv55) + 4*Y1n22*ZA21*complexconjugate(Vv52)*complexconjugate(Vv55) - 2*BB12*ZA23*complexconjugate(Vv54)*complexconjugate(Vv55) - 2*BB21*ZA23*complexconjugate(Vv54)*complexconjugate(Vv55) - 2*BB22*ZA23*complexconjugate(Vv55)**2 + 4*Y2n33*ZA22*complexconjugate(Vv53)*complexconjugate(Vv56) + 2*C13*ZA23*complexconjugate(Vv54)*complexconjugate(Vv56) + 2*C31*ZA23*complexconjugate(Vv54)*complexconjugate(Vv56) + 2*C23*ZA23*complexconjugate(Vv55)*complexconjugate(Vv56) + 2*C32*ZA23*complexconjugate(Vv55)*complexconjugate(Vv56))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_530 = Coupling(name = 'GC_530',
	 value = '-(Vv54*Vv56*ZA33*complexconjugate(C13) + Vv55*Vv56*ZA33*complexconjugate(C23) + Vv54*Vv56*ZA33*complexconjugate(C31) + Vv55*Vv56*ZA33*complexconjugate(C32) + 2*Vv51*Vv54*ZA31*complexconjugate(Y1n11) + 2*Vv51*Vv55*ZA31*complexconjugate(Y1n12) + 2*Vv52*Vv54*ZA31*complexconjugate(Y1n21) + Vv54*(ZA33*(2*Vv54*complexconjugate(BB11) - Vv55*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv56*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv51*ZA31*complexconjugate(Y1n11) + 2*Vv52*ZA31*complexconjugate(Y1n21)) + 2*Vv52*Vv55*ZA31*complexconjugate(Y1n22) + Vv55*(ZA33*(-(Vv54*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv55*complexconjugate(BB22) + Vv56*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv51*ZA31*complexconjugate(Y1n12) + 2*Vv52*ZA31*complexconjugate(Y1n22)) + 4*Vv53*Vv56*ZA32*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_531 = Coupling(name = 'GC_531',
	 value = '(4*Y1n11*ZA31*complexconjugate(Vv51)*complexconjugate(Vv54) + 4*Y1n21*ZA31*complexconjugate(Vv52)*complexconjugate(Vv54) + 2*BB11*ZA33*complexconjugate(Vv54)**2 + 4*Y1n12*ZA31*complexconjugate(Vv51)*complexconjugate(Vv55) + 4*Y1n22*ZA31*complexconjugate(Vv52)*complexconjugate(Vv55) - 2*BB12*ZA33*complexconjugate(Vv54)*complexconjugate(Vv55) - 2*BB21*ZA33*complexconjugate(Vv54)*complexconjugate(Vv55) - 2*BB22*ZA33*complexconjugate(Vv55)**2 + 4*Y2n33*ZA32*complexconjugate(Vv53)*complexconjugate(Vv56) + 2*C13*ZA33*complexconjugate(Vv54)*complexconjugate(Vv56) + 2*C31*ZA33*complexconjugate(Vv54)*complexconjugate(Vv56) + 2*C23*ZA33*complexconjugate(Vv55)*complexconjugate(Vv56) + 2*C32*ZA33*complexconjugate(Vv55)*complexconjugate(Vv56))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_532 = Coupling(name = 'GC_532',
	 value = '-(Vv56*Vv64*ZA13*complexconjugate(C13) + Vv56*Vv65*ZA13*complexconjugate(C23) + Vv56*Vv64*ZA13*complexconjugate(C31) + Vv56*Vv65*ZA13*complexconjugate(C32) + 2*Vv51*Vv64*ZA11*complexconjugate(Y1n11) + 2*Vv51*Vv65*ZA11*complexconjugate(Y1n12) + 2*Vv52*Vv64*ZA11*complexconjugate(Y1n21) + Vv54*(ZA13*(2*Vv64*complexconjugate(BB11) - Vv65*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv66*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv61*ZA11*complexconjugate(Y1n11) + 2*Vv62*ZA11*complexconjugate(Y1n21)) + 2*Vv52*Vv65*ZA11*complexconjugate(Y1n22) + Vv55*(ZA13*(-(Vv64*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv65*complexconjugate(BB22) + Vv66*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv61*ZA11*complexconjugate(Y1n12) + 2*Vv62*ZA11*complexconjugate(Y1n22)) + 2*Vv56*Vv63*ZA12*complexconjugate(Y2n33) + 2*Vv53*Vv66*ZA12*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_533 = Coupling(name = 'GC_533',
	 value = '(2*Y1n21*ZA11*complexconjugate(Vv54)*complexconjugate(Vv62) + 2*Y1n22*ZA11*complexconjugate(Vv55)*complexconjugate(Vv62) + 2*Y2n33*ZA12*complexconjugate(Vv56)*complexconjugate(Vv63) + 2*Y1n21*ZA11*complexconjugate(Vv52)*complexconjugate(Vv64) + 2*BB11*ZA13*complexconjugate(Vv54)*complexconjugate(Vv64) - BB12*ZA13*complexconjugate(Vv55)*complexconjugate(Vv64) - BB21*ZA13*complexconjugate(Vv55)*complexconjugate(Vv64) + C13*ZA13*complexconjugate(Vv56)*complexconjugate(Vv64) + C31*ZA13*complexconjugate(Vv56)*complexconjugate(Vv64) + 2*Y1n11*ZA11*(complexconjugate(Vv54)*complexconjugate(Vv61) + complexconjugate(Vv51)*complexconjugate(Vv64)) + 2*Y1n22*ZA11*complexconjugate(Vv52)*complexconjugate(Vv65) - BB12*ZA13*complexconjugate(Vv54)*complexconjugate(Vv65) - BB21*ZA13*complexconjugate(Vv54)*complexconjugate(Vv65) - 2*BB22*ZA13*complexconjugate(Vv55)*complexconjugate(Vv65) + C23*ZA13*complexconjugate(Vv56)*complexconjugate(Vv65) + C32*ZA13*complexconjugate(Vv56)*complexconjugate(Vv65) + 2*Y1n12*ZA11*(complexconjugate(Vv55)*complexconjugate(Vv61) + complexconjugate(Vv51)*complexconjugate(Vv65)) + 2*Y2n33*ZA12*complexconjugate(Vv53)*complexconjugate(Vv66) + C13*ZA13*complexconjugate(Vv54)*complexconjugate(Vv66) + C31*ZA13*complexconjugate(Vv54)*complexconjugate(Vv66) + C23*ZA13*complexconjugate(Vv55)*complexconjugate(Vv66) + C32*ZA13*complexconjugate(Vv55)*complexconjugate(Vv66))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_534 = Coupling(name = 'GC_534',
	 value = '-(Vv56*Vv64*ZA23*complexconjugate(C13) + Vv56*Vv65*ZA23*complexconjugate(C23) + Vv56*Vv64*ZA23*complexconjugate(C31) + Vv56*Vv65*ZA23*complexconjugate(C32) + 2*Vv51*Vv64*ZA21*complexconjugate(Y1n11) + 2*Vv51*Vv65*ZA21*complexconjugate(Y1n12) + 2*Vv52*Vv64*ZA21*complexconjugate(Y1n21) + Vv54*(ZA23*(2*Vv64*complexconjugate(BB11) - Vv65*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv66*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv61*ZA21*complexconjugate(Y1n11) + 2*Vv62*ZA21*complexconjugate(Y1n21)) + 2*Vv52*Vv65*ZA21*complexconjugate(Y1n22) + Vv55*(ZA23*(-(Vv64*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv65*complexconjugate(BB22) + Vv66*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv61*ZA21*complexconjugate(Y1n12) + 2*Vv62*ZA21*complexconjugate(Y1n22)) + 2*Vv56*Vv63*ZA22*complexconjugate(Y2n33) + 2*Vv53*Vv66*ZA22*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_535 = Coupling(name = 'GC_535',
	 value = '(2*Y1n21*ZA21*complexconjugate(Vv54)*complexconjugate(Vv62) + 2*Y1n22*ZA21*complexconjugate(Vv55)*complexconjugate(Vv62) + 2*Y2n33*ZA22*complexconjugate(Vv56)*complexconjugate(Vv63) + 2*Y1n21*ZA21*complexconjugate(Vv52)*complexconjugate(Vv64) + 2*BB11*ZA23*complexconjugate(Vv54)*complexconjugate(Vv64) - BB12*ZA23*complexconjugate(Vv55)*complexconjugate(Vv64) - BB21*ZA23*complexconjugate(Vv55)*complexconjugate(Vv64) + C13*ZA23*complexconjugate(Vv56)*complexconjugate(Vv64) + C31*ZA23*complexconjugate(Vv56)*complexconjugate(Vv64) + 2*Y1n11*ZA21*(complexconjugate(Vv54)*complexconjugate(Vv61) + complexconjugate(Vv51)*complexconjugate(Vv64)) + 2*Y1n22*ZA21*complexconjugate(Vv52)*complexconjugate(Vv65) - BB12*ZA23*complexconjugate(Vv54)*complexconjugate(Vv65) - BB21*ZA23*complexconjugate(Vv54)*complexconjugate(Vv65) - 2*BB22*ZA23*complexconjugate(Vv55)*complexconjugate(Vv65) + C23*ZA23*complexconjugate(Vv56)*complexconjugate(Vv65) + C32*ZA23*complexconjugate(Vv56)*complexconjugate(Vv65) + 2*Y1n12*ZA21*(complexconjugate(Vv55)*complexconjugate(Vv61) + complexconjugate(Vv51)*complexconjugate(Vv65)) + 2*Y2n33*ZA22*complexconjugate(Vv53)*complexconjugate(Vv66) + C13*ZA23*complexconjugate(Vv54)*complexconjugate(Vv66) + C31*ZA23*complexconjugate(Vv54)*complexconjugate(Vv66) + C23*ZA23*complexconjugate(Vv55)*complexconjugate(Vv66) + C32*ZA23*complexconjugate(Vv55)*complexconjugate(Vv66))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_536 = Coupling(name = 'GC_536',
	 value = '-(Vv56*Vv64*ZA33*complexconjugate(C13) + Vv56*Vv65*ZA33*complexconjugate(C23) + Vv56*Vv64*ZA33*complexconjugate(C31) + Vv56*Vv65*ZA33*complexconjugate(C32) + 2*Vv51*Vv64*ZA31*complexconjugate(Y1n11) + 2*Vv51*Vv65*ZA31*complexconjugate(Y1n12) + 2*Vv52*Vv64*ZA31*complexconjugate(Y1n21) + Vv54*(ZA33*(2*Vv64*complexconjugate(BB11) - Vv65*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv66*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv61*ZA31*complexconjugate(Y1n11) + 2*Vv62*ZA31*complexconjugate(Y1n21)) + 2*Vv52*Vv65*ZA31*complexconjugate(Y1n22) + Vv55*(ZA33*(-(Vv64*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv65*complexconjugate(BB22) + Vv66*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv61*ZA31*complexconjugate(Y1n12) + 2*Vv62*ZA31*complexconjugate(Y1n22)) + 2*Vv56*Vv63*ZA32*complexconjugate(Y2n33) + 2*Vv53*Vv66*ZA32*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_537 = Coupling(name = 'GC_537',
	 value = '(2*Y1n21*ZA31*complexconjugate(Vv54)*complexconjugate(Vv62) + 2*Y1n22*ZA31*complexconjugate(Vv55)*complexconjugate(Vv62) + 2*Y2n33*ZA32*complexconjugate(Vv56)*complexconjugate(Vv63) + 2*Y1n21*ZA31*complexconjugate(Vv52)*complexconjugate(Vv64) + 2*BB11*ZA33*complexconjugate(Vv54)*complexconjugate(Vv64) - BB12*ZA33*complexconjugate(Vv55)*complexconjugate(Vv64) - BB21*ZA33*complexconjugate(Vv55)*complexconjugate(Vv64) + C13*ZA33*complexconjugate(Vv56)*complexconjugate(Vv64) + C31*ZA33*complexconjugate(Vv56)*complexconjugate(Vv64) + 2*Y1n11*ZA31*(complexconjugate(Vv54)*complexconjugate(Vv61) + complexconjugate(Vv51)*complexconjugate(Vv64)) + 2*Y1n22*ZA31*complexconjugate(Vv52)*complexconjugate(Vv65) - BB12*ZA33*complexconjugate(Vv54)*complexconjugate(Vv65) - BB21*ZA33*complexconjugate(Vv54)*complexconjugate(Vv65) - 2*BB22*ZA33*complexconjugate(Vv55)*complexconjugate(Vv65) + C23*ZA33*complexconjugate(Vv56)*complexconjugate(Vv65) + C32*ZA33*complexconjugate(Vv56)*complexconjugate(Vv65) + 2*Y1n12*ZA31*(complexconjugate(Vv55)*complexconjugate(Vv61) + complexconjugate(Vv51)*complexconjugate(Vv65)) + 2*Y2n33*ZA32*complexconjugate(Vv53)*complexconjugate(Vv66) + C13*ZA33*complexconjugate(Vv54)*complexconjugate(Vv66) + C31*ZA33*complexconjugate(Vv54)*complexconjugate(Vv66) + C23*ZA33*complexconjugate(Vv55)*complexconjugate(Vv66) + C32*ZA33*complexconjugate(Vv55)*complexconjugate(Vv66))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_538 = Coupling(name = 'GC_538',
	 value = '-(Vv64*Vv66*ZA13*complexconjugate(C13) + Vv65*Vv66*ZA13*complexconjugate(C23) + Vv64*Vv66*ZA13*complexconjugate(C31) + Vv65*Vv66*ZA13*complexconjugate(C32) + 2*Vv61*Vv64*ZA11*complexconjugate(Y1n11) + 2*Vv61*Vv65*ZA11*complexconjugate(Y1n12) + 2*Vv62*Vv64*ZA11*complexconjugate(Y1n21) + Vv64*(ZA13*(2*Vv64*complexconjugate(BB11) - Vv65*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv66*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv61*ZA11*complexconjugate(Y1n11) + 2*Vv62*ZA11*complexconjugate(Y1n21)) + 2*Vv62*Vv65*ZA11*complexconjugate(Y1n22) + Vv65*(ZA13*(-(Vv64*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv65*complexconjugate(BB22) + Vv66*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv61*ZA11*complexconjugate(Y1n12) + 2*Vv62*ZA11*complexconjugate(Y1n22)) + 4*Vv63*Vv66*ZA12*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_539 = Coupling(name = 'GC_539',
	 value = '(4*Y1n11*ZA11*complexconjugate(Vv61)*complexconjugate(Vv64) + 4*Y1n21*ZA11*complexconjugate(Vv62)*complexconjugate(Vv64) + 2*BB11*ZA13*complexconjugate(Vv64)**2 + 4*Y1n12*ZA11*complexconjugate(Vv61)*complexconjugate(Vv65) + 4*Y1n22*ZA11*complexconjugate(Vv62)*complexconjugate(Vv65) - 2*BB12*ZA13*complexconjugate(Vv64)*complexconjugate(Vv65) - 2*BB21*ZA13*complexconjugate(Vv64)*complexconjugate(Vv65) - 2*BB22*ZA13*complexconjugate(Vv65)**2 + 4*Y2n33*ZA12*complexconjugate(Vv63)*complexconjugate(Vv66) + 2*C13*ZA13*complexconjugate(Vv64)*complexconjugate(Vv66) + 2*C31*ZA13*complexconjugate(Vv64)*complexconjugate(Vv66) + 2*C23*ZA13*complexconjugate(Vv65)*complexconjugate(Vv66) + 2*C32*ZA13*complexconjugate(Vv65)*complexconjugate(Vv66))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_540 = Coupling(name = 'GC_540',
	 value = '-(Vv64*Vv66*ZA23*complexconjugate(C13) + Vv65*Vv66*ZA23*complexconjugate(C23) + Vv64*Vv66*ZA23*complexconjugate(C31) + Vv65*Vv66*ZA23*complexconjugate(C32) + 2*Vv61*Vv64*ZA21*complexconjugate(Y1n11) + 2*Vv61*Vv65*ZA21*complexconjugate(Y1n12) + 2*Vv62*Vv64*ZA21*complexconjugate(Y1n21) + Vv64*(ZA23*(2*Vv64*complexconjugate(BB11) - Vv65*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv66*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv61*ZA21*complexconjugate(Y1n11) + 2*Vv62*ZA21*complexconjugate(Y1n21)) + 2*Vv62*Vv65*ZA21*complexconjugate(Y1n22) + Vv65*(ZA23*(-(Vv64*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv65*complexconjugate(BB22) + Vv66*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv61*ZA21*complexconjugate(Y1n12) + 2*Vv62*ZA21*complexconjugate(Y1n22)) + 4*Vv63*Vv66*ZA22*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_541 = Coupling(name = 'GC_541',
	 value = '(4*Y1n11*ZA21*complexconjugate(Vv61)*complexconjugate(Vv64) + 4*Y1n21*ZA21*complexconjugate(Vv62)*complexconjugate(Vv64) + 2*BB11*ZA23*complexconjugate(Vv64)**2 + 4*Y1n12*ZA21*complexconjugate(Vv61)*complexconjugate(Vv65) + 4*Y1n22*ZA21*complexconjugate(Vv62)*complexconjugate(Vv65) - 2*BB12*ZA23*complexconjugate(Vv64)*complexconjugate(Vv65) - 2*BB21*ZA23*complexconjugate(Vv64)*complexconjugate(Vv65) - 2*BB22*ZA23*complexconjugate(Vv65)**2 + 4*Y2n33*ZA22*complexconjugate(Vv63)*complexconjugate(Vv66) + 2*C13*ZA23*complexconjugate(Vv64)*complexconjugate(Vv66) + 2*C31*ZA23*complexconjugate(Vv64)*complexconjugate(Vv66) + 2*C23*ZA23*complexconjugate(Vv65)*complexconjugate(Vv66) + 2*C32*ZA23*complexconjugate(Vv65)*complexconjugate(Vv66))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_542 = Coupling(name = 'GC_542',
	 value = '-(Vv64*Vv66*ZA33*complexconjugate(C13) + Vv65*Vv66*ZA33*complexconjugate(C23) + Vv64*Vv66*ZA33*complexconjugate(C31) + Vv65*Vv66*ZA33*complexconjugate(C32) + 2*Vv61*Vv64*ZA31*complexconjugate(Y1n11) + 2*Vv61*Vv65*ZA31*complexconjugate(Y1n12) + 2*Vv62*Vv64*ZA31*complexconjugate(Y1n21) + Vv64*(ZA33*(2*Vv64*complexconjugate(BB11) - Vv65*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv66*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv61*ZA31*complexconjugate(Y1n11) + 2*Vv62*ZA31*complexconjugate(Y1n21)) + 2*Vv62*Vv65*ZA31*complexconjugate(Y1n22) + Vv65*(ZA33*(-(Vv64*(complexconjugate(BB12) + complexconjugate(BB21))) - 2*Vv65*complexconjugate(BB22) + Vv66*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv61*ZA31*complexconjugate(Y1n12) + 2*Vv62*ZA31*complexconjugate(Y1n22)) + 4*Vv63*Vv66*ZA32*complexconjugate(Y2n33))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_543 = Coupling(name = 'GC_543',
	 value = '(4*Y1n11*ZA31*complexconjugate(Vv61)*complexconjugate(Vv64) + 4*Y1n21*ZA31*complexconjugate(Vv62)*complexconjugate(Vv64) + 2*BB11*ZA33*complexconjugate(Vv64)**2 + 4*Y1n12*ZA31*complexconjugate(Vv61)*complexconjugate(Vv65) + 4*Y1n22*ZA31*complexconjugate(Vv62)*complexconjugate(Vv65) - 2*BB12*ZA33*complexconjugate(Vv64)*complexconjugate(Vv65) - 2*BB21*ZA33*complexconjugate(Vv64)*complexconjugate(Vv65) - 2*BB22*ZA33*complexconjugate(Vv65)**2 + 4*Y2n33*ZA32*complexconjugate(Vv63)*complexconjugate(Vv66) + 2*C13*ZA33*complexconjugate(Vv64)*complexconjugate(Vv66) + 2*C31*ZA33*complexconjugate(Vv64)*complexconjugate(Vv66) + 2*C23*ZA33*complexconjugate(Vv65)*complexconjugate(Vv66) + 2*C32*ZA33*complexconjugate(Vv65)*complexconjugate(Vv66))/(2.*cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_544 = Coupling(name = 'GC_544',
	 value = '(-1*complex(0,1)*(ZDR11*(ZDL11*ZH11*complexconjugate(Y1d11) + ZDL12*ZH11*complexconjugate(Y1d21) + ZDL13*ZH12*complexconjugate(Y2d31)) + ZDR12*(ZDL11*ZH11*complexconjugate(Y1d12) + ZDL12*ZH11*complexconjugate(Y1d22) + ZDL13*ZH12*complexconjugate(Y2d32)) + ZDR13*(ZDL11*ZH11*complexconjugate(Y1d13) + ZDL12*ZH11*complexconjugate(Y1d23) + ZDL13*ZH12*complexconjugate(Y2d33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_545 = Coupling(name = 'GC_545',
	 value = '(-1*complex(0,1)*(Y1d11*ZH11*complexconjugate(ZDL11)*complexconjugate(ZDR11) + Y1d21*ZH11*complexconjugate(ZDL12)*complexconjugate(ZDR11) + Y2d31*ZH12*complexconjugate(ZDL13)*complexconjugate(ZDR11) + Y1d12*ZH11*complexconjugate(ZDL11)*complexconjugate(ZDR12) + Y1d22*ZH11*complexconjugate(ZDL12)*complexconjugate(ZDR12) + Y2d32*ZH12*complexconjugate(ZDL13)*complexconjugate(ZDR12) + Y1d13*ZH11*complexconjugate(ZDL11)*complexconjugate(ZDR13) + Y1d23*ZH11*complexconjugate(ZDL12)*complexconjugate(ZDR13) + Y2d33*ZH12*complexconjugate(ZDL13)*complexconjugate(ZDR13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_546 = Coupling(name = 'GC_546',
	 value = '(-1*complex(0,1)*(ZDR11*(ZDL11*ZH21*complexconjugate(Y1d11) + ZDL12*ZH21*complexconjugate(Y1d21) + ZDL13*ZH22*complexconjugate(Y2d31)) + ZDR12*(ZDL11*ZH21*complexconjugate(Y1d12) + ZDL12*ZH21*complexconjugate(Y1d22) + ZDL13*ZH22*complexconjugate(Y2d32)) + ZDR13*(ZDL11*ZH21*complexconjugate(Y1d13) + ZDL12*ZH21*complexconjugate(Y1d23) + ZDL13*ZH22*complexconjugate(Y2d33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_547 = Coupling(name = 'GC_547',
	 value = '(-1*complex(0,1)*(Y1d11*ZH21*complexconjugate(ZDL11)*complexconjugate(ZDR11) + Y1d21*ZH21*complexconjugate(ZDL12)*complexconjugate(ZDR11) + Y2d31*ZH22*complexconjugate(ZDL13)*complexconjugate(ZDR11) + Y1d12*ZH21*complexconjugate(ZDL11)*complexconjugate(ZDR12) + Y1d22*ZH21*complexconjugate(ZDL12)*complexconjugate(ZDR12) + Y2d32*ZH22*complexconjugate(ZDL13)*complexconjugate(ZDR12) + Y1d13*ZH21*complexconjugate(ZDL11)*complexconjugate(ZDR13) + Y1d23*ZH21*complexconjugate(ZDL12)*complexconjugate(ZDR13) + Y2d33*ZH22*complexconjugate(ZDL13)*complexconjugate(ZDR13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_548 = Coupling(name = 'GC_548',
	 value = '(-1*complex(0,1)*(ZDR11*(ZDL11*ZH31*complexconjugate(Y1d11) + ZDL12*ZH31*complexconjugate(Y1d21) + ZDL13*ZH32*complexconjugate(Y2d31)) + ZDR12*(ZDL11*ZH31*complexconjugate(Y1d12) + ZDL12*ZH31*complexconjugate(Y1d22) + ZDL13*ZH32*complexconjugate(Y2d32)) + ZDR13*(ZDL11*ZH31*complexconjugate(Y1d13) + ZDL12*ZH31*complexconjugate(Y1d23) + ZDL13*ZH32*complexconjugate(Y2d33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_549 = Coupling(name = 'GC_549',
	 value = '(-1*complex(0,1)*(Y1d11*ZH31*complexconjugate(ZDL11)*complexconjugate(ZDR11) + Y1d21*ZH31*complexconjugate(ZDL12)*complexconjugate(ZDR11) + Y2d31*ZH32*complexconjugate(ZDL13)*complexconjugate(ZDR11) + Y1d12*ZH31*complexconjugate(ZDL11)*complexconjugate(ZDR12) + Y1d22*ZH31*complexconjugate(ZDL12)*complexconjugate(ZDR12) + Y2d32*ZH32*complexconjugate(ZDL13)*complexconjugate(ZDR12) + Y1d13*ZH31*complexconjugate(ZDL11)*complexconjugate(ZDR13) + Y1d23*ZH31*complexconjugate(ZDL12)*complexconjugate(ZDR13) + Y2d33*ZH32*complexconjugate(ZDL13)*complexconjugate(ZDR13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_550 = Coupling(name = 'GC_550',
	 value = '(-1*complex(0,1)*(ZDR11*(ZDL21*ZH11*complexconjugate(Y1d11) + ZDL22*ZH11*complexconjugate(Y1d21) + ZDL23*ZH12*complexconjugate(Y2d31)) + ZDR12*(ZDL21*ZH11*complexconjugate(Y1d12) + ZDL22*ZH11*complexconjugate(Y1d22) + ZDL23*ZH12*complexconjugate(Y2d32)) + ZDR13*(ZDL21*ZH11*complexconjugate(Y1d13) + ZDL22*ZH11*complexconjugate(Y1d23) + ZDL23*ZH12*complexconjugate(Y2d33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_551 = Coupling(name = 'GC_551',
	 value = '(-1*complex(0,1)*(Y1d11*ZH11*complexconjugate(ZDL11)*complexconjugate(ZDR21) + Y1d21*ZH11*complexconjugate(ZDL12)*complexconjugate(ZDR21) + Y2d31*ZH12*complexconjugate(ZDL13)*complexconjugate(ZDR21) + Y1d12*ZH11*complexconjugate(ZDL11)*complexconjugate(ZDR22) + Y1d22*ZH11*complexconjugate(ZDL12)*complexconjugate(ZDR22) + Y2d32*ZH12*complexconjugate(ZDL13)*complexconjugate(ZDR22) + Y1d13*ZH11*complexconjugate(ZDL11)*complexconjugate(ZDR23) + Y1d23*ZH11*complexconjugate(ZDL12)*complexconjugate(ZDR23) + Y2d33*ZH12*complexconjugate(ZDL13)*complexconjugate(ZDR23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_552 = Coupling(name = 'GC_552',
	 value = '(-1*complex(0,1)*(ZDR11*(ZDL21*ZH21*complexconjugate(Y1d11) + ZDL22*ZH21*complexconjugate(Y1d21) + ZDL23*ZH22*complexconjugate(Y2d31)) + ZDR12*(ZDL21*ZH21*complexconjugate(Y1d12) + ZDL22*ZH21*complexconjugate(Y1d22) + ZDL23*ZH22*complexconjugate(Y2d32)) + ZDR13*(ZDL21*ZH21*complexconjugate(Y1d13) + ZDL22*ZH21*complexconjugate(Y1d23) + ZDL23*ZH22*complexconjugate(Y2d33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_553 = Coupling(name = 'GC_553',
	 value = '(-1*complex(0,1)*(Y1d11*ZH21*complexconjugate(ZDL11)*complexconjugate(ZDR21) + Y1d21*ZH21*complexconjugate(ZDL12)*complexconjugate(ZDR21) + Y2d31*ZH22*complexconjugate(ZDL13)*complexconjugate(ZDR21) + Y1d12*ZH21*complexconjugate(ZDL11)*complexconjugate(ZDR22) + Y1d22*ZH21*complexconjugate(ZDL12)*complexconjugate(ZDR22) + Y2d32*ZH22*complexconjugate(ZDL13)*complexconjugate(ZDR22) + Y1d13*ZH21*complexconjugate(ZDL11)*complexconjugate(ZDR23) + Y1d23*ZH21*complexconjugate(ZDL12)*complexconjugate(ZDR23) + Y2d33*ZH22*complexconjugate(ZDL13)*complexconjugate(ZDR23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_554 = Coupling(name = 'GC_554',
	 value = '(-1*complex(0,1)*(ZDR11*(ZDL21*ZH31*complexconjugate(Y1d11) + ZDL22*ZH31*complexconjugate(Y1d21) + ZDL23*ZH32*complexconjugate(Y2d31)) + ZDR12*(ZDL21*ZH31*complexconjugate(Y1d12) + ZDL22*ZH31*complexconjugate(Y1d22) + ZDL23*ZH32*complexconjugate(Y2d32)) + ZDR13*(ZDL21*ZH31*complexconjugate(Y1d13) + ZDL22*ZH31*complexconjugate(Y1d23) + ZDL23*ZH32*complexconjugate(Y2d33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_555 = Coupling(name = 'GC_555',
	 value = '(-1*complex(0,1)*(Y1d11*ZH31*complexconjugate(ZDL11)*complexconjugate(ZDR21) + Y1d21*ZH31*complexconjugate(ZDL12)*complexconjugate(ZDR21) + Y2d31*ZH32*complexconjugate(ZDL13)*complexconjugate(ZDR21) + Y1d12*ZH31*complexconjugate(ZDL11)*complexconjugate(ZDR22) + Y1d22*ZH31*complexconjugate(ZDL12)*complexconjugate(ZDR22) + Y2d32*ZH32*complexconjugate(ZDL13)*complexconjugate(ZDR22) + Y1d13*ZH31*complexconjugate(ZDL11)*complexconjugate(ZDR23) + Y1d23*ZH31*complexconjugate(ZDL12)*complexconjugate(ZDR23) + Y2d33*ZH32*complexconjugate(ZDL13)*complexconjugate(ZDR23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_556 = Coupling(name = 'GC_556',
	 value = '(-1*complex(0,1)*(ZDR11*(ZDL31*ZH11*complexconjugate(Y1d11) + ZDL32*ZH11*complexconjugate(Y1d21) + ZDL33*ZH12*complexconjugate(Y2d31)) + ZDR12*(ZDL31*ZH11*complexconjugate(Y1d12) + ZDL32*ZH11*complexconjugate(Y1d22) + ZDL33*ZH12*complexconjugate(Y2d32)) + ZDR13*(ZDL31*ZH11*complexconjugate(Y1d13) + ZDL32*ZH11*complexconjugate(Y1d23) + ZDL33*ZH12*complexconjugate(Y2d33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_557 = Coupling(name = 'GC_557',
	 value = '(-1*complex(0,1)*(Y1d11*ZH11*complexconjugate(ZDL11)*complexconjugate(ZDR31) + Y1d21*ZH11*complexconjugate(ZDL12)*complexconjugate(ZDR31) + Y2d31*ZH12*complexconjugate(ZDL13)*complexconjugate(ZDR31) + Y1d12*ZH11*complexconjugate(ZDL11)*complexconjugate(ZDR32) + Y1d22*ZH11*complexconjugate(ZDL12)*complexconjugate(ZDR32) + Y2d32*ZH12*complexconjugate(ZDL13)*complexconjugate(ZDR32) + Y1d13*ZH11*complexconjugate(ZDL11)*complexconjugate(ZDR33) + Y1d23*ZH11*complexconjugate(ZDL12)*complexconjugate(ZDR33) + Y2d33*ZH12*complexconjugate(ZDL13)*complexconjugate(ZDR33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_558 = Coupling(name = 'GC_558',
	 value = '(-1*complex(0,1)*(ZDR11*(ZDL31*ZH21*complexconjugate(Y1d11) + ZDL32*ZH21*complexconjugate(Y1d21) + ZDL33*ZH22*complexconjugate(Y2d31)) + ZDR12*(ZDL31*ZH21*complexconjugate(Y1d12) + ZDL32*ZH21*complexconjugate(Y1d22) + ZDL33*ZH22*complexconjugate(Y2d32)) + ZDR13*(ZDL31*ZH21*complexconjugate(Y1d13) + ZDL32*ZH21*complexconjugate(Y1d23) + ZDL33*ZH22*complexconjugate(Y2d33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_559 = Coupling(name = 'GC_559',
	 value = '(-1*complex(0,1)*(Y1d11*ZH21*complexconjugate(ZDL11)*complexconjugate(ZDR31) + Y1d21*ZH21*complexconjugate(ZDL12)*complexconjugate(ZDR31) + Y2d31*ZH22*complexconjugate(ZDL13)*complexconjugate(ZDR31) + Y1d12*ZH21*complexconjugate(ZDL11)*complexconjugate(ZDR32) + Y1d22*ZH21*complexconjugate(ZDL12)*complexconjugate(ZDR32) + Y2d32*ZH22*complexconjugate(ZDL13)*complexconjugate(ZDR32) + Y1d13*ZH21*complexconjugate(ZDL11)*complexconjugate(ZDR33) + Y1d23*ZH21*complexconjugate(ZDL12)*complexconjugate(ZDR33) + Y2d33*ZH22*complexconjugate(ZDL13)*complexconjugate(ZDR33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_560 = Coupling(name = 'GC_560',
	 value = '(-1*complex(0,1)*(ZDR11*(ZDL31*ZH31*complexconjugate(Y1d11) + ZDL32*ZH31*complexconjugate(Y1d21) + ZDL33*ZH32*complexconjugate(Y2d31)) + ZDR12*(ZDL31*ZH31*complexconjugate(Y1d12) + ZDL32*ZH31*complexconjugate(Y1d22) + ZDL33*ZH32*complexconjugate(Y2d32)) + ZDR13*(ZDL31*ZH31*complexconjugate(Y1d13) + ZDL32*ZH31*complexconjugate(Y1d23) + ZDL33*ZH32*complexconjugate(Y2d33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_561 = Coupling(name = 'GC_561',
	 value = '(-1*complex(0,1)*(Y1d11*ZH31*complexconjugate(ZDL11)*complexconjugate(ZDR31) + Y1d21*ZH31*complexconjugate(ZDL12)*complexconjugate(ZDR31) + Y2d31*ZH32*complexconjugate(ZDL13)*complexconjugate(ZDR31) + Y1d12*ZH31*complexconjugate(ZDL11)*complexconjugate(ZDR32) + Y1d22*ZH31*complexconjugate(ZDL12)*complexconjugate(ZDR32) + Y2d32*ZH32*complexconjugate(ZDL13)*complexconjugate(ZDR32) + Y1d13*ZH31*complexconjugate(ZDL11)*complexconjugate(ZDR33) + Y1d23*ZH31*complexconjugate(ZDL12)*complexconjugate(ZDR33) + Y2d33*ZH32*complexconjugate(ZDL13)*complexconjugate(ZDR33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_562 = Coupling(name = 'GC_562',
	 value = '(-1*complex(0,1)*(ZDR21*(ZDL11*ZH11*complexconjugate(Y1d11) + ZDL12*ZH11*complexconjugate(Y1d21) + ZDL13*ZH12*complexconjugate(Y2d31)) + ZDR22*(ZDL11*ZH11*complexconjugate(Y1d12) + ZDL12*ZH11*complexconjugate(Y1d22) + ZDL13*ZH12*complexconjugate(Y2d32)) + ZDR23*(ZDL11*ZH11*complexconjugate(Y1d13) + ZDL12*ZH11*complexconjugate(Y1d23) + ZDL13*ZH12*complexconjugate(Y2d33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_563 = Coupling(name = 'GC_563',
	 value = '(-1*complex(0,1)*(Y1d11*ZH11*complexconjugate(ZDL21)*complexconjugate(ZDR11) + Y1d21*ZH11*complexconjugate(ZDL22)*complexconjugate(ZDR11) + Y2d31*ZH12*complexconjugate(ZDL23)*complexconjugate(ZDR11) + Y1d12*ZH11*complexconjugate(ZDL21)*complexconjugate(ZDR12) + Y1d22*ZH11*complexconjugate(ZDL22)*complexconjugate(ZDR12) + Y2d32*ZH12*complexconjugate(ZDL23)*complexconjugate(ZDR12) + Y1d13*ZH11*complexconjugate(ZDL21)*complexconjugate(ZDR13) + Y1d23*ZH11*complexconjugate(ZDL22)*complexconjugate(ZDR13) + Y2d33*ZH12*complexconjugate(ZDL23)*complexconjugate(ZDR13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_564 = Coupling(name = 'GC_564',
	 value = '(-1*complex(0,1)*(ZDR21*(ZDL11*ZH21*complexconjugate(Y1d11) + ZDL12*ZH21*complexconjugate(Y1d21) + ZDL13*ZH22*complexconjugate(Y2d31)) + ZDR22*(ZDL11*ZH21*complexconjugate(Y1d12) + ZDL12*ZH21*complexconjugate(Y1d22) + ZDL13*ZH22*complexconjugate(Y2d32)) + ZDR23*(ZDL11*ZH21*complexconjugate(Y1d13) + ZDL12*ZH21*complexconjugate(Y1d23) + ZDL13*ZH22*complexconjugate(Y2d33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_565 = Coupling(name = 'GC_565',
	 value = '(-1*complex(0,1)*(Y1d11*ZH21*complexconjugate(ZDL21)*complexconjugate(ZDR11) + Y1d21*ZH21*complexconjugate(ZDL22)*complexconjugate(ZDR11) + Y2d31*ZH22*complexconjugate(ZDL23)*complexconjugate(ZDR11) + Y1d12*ZH21*complexconjugate(ZDL21)*complexconjugate(ZDR12) + Y1d22*ZH21*complexconjugate(ZDL22)*complexconjugate(ZDR12) + Y2d32*ZH22*complexconjugate(ZDL23)*complexconjugate(ZDR12) + Y1d13*ZH21*complexconjugate(ZDL21)*complexconjugate(ZDR13) + Y1d23*ZH21*complexconjugate(ZDL22)*complexconjugate(ZDR13) + Y2d33*ZH22*complexconjugate(ZDL23)*complexconjugate(ZDR13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_566 = Coupling(name = 'GC_566',
	 value = '(-1*complex(0,1)*(ZDR21*(ZDL11*ZH31*complexconjugate(Y1d11) + ZDL12*ZH31*complexconjugate(Y1d21) + ZDL13*ZH32*complexconjugate(Y2d31)) + ZDR22*(ZDL11*ZH31*complexconjugate(Y1d12) + ZDL12*ZH31*complexconjugate(Y1d22) + ZDL13*ZH32*complexconjugate(Y2d32)) + ZDR23*(ZDL11*ZH31*complexconjugate(Y1d13) + ZDL12*ZH31*complexconjugate(Y1d23) + ZDL13*ZH32*complexconjugate(Y2d33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_567 = Coupling(name = 'GC_567',
	 value = '(-1*complex(0,1)*(Y1d11*ZH31*complexconjugate(ZDL21)*complexconjugate(ZDR11) + Y1d21*ZH31*complexconjugate(ZDL22)*complexconjugate(ZDR11) + Y2d31*ZH32*complexconjugate(ZDL23)*complexconjugate(ZDR11) + Y1d12*ZH31*complexconjugate(ZDL21)*complexconjugate(ZDR12) + Y1d22*ZH31*complexconjugate(ZDL22)*complexconjugate(ZDR12) + Y2d32*ZH32*complexconjugate(ZDL23)*complexconjugate(ZDR12) + Y1d13*ZH31*complexconjugate(ZDL21)*complexconjugate(ZDR13) + Y1d23*ZH31*complexconjugate(ZDL22)*complexconjugate(ZDR13) + Y2d33*ZH32*complexconjugate(ZDL23)*complexconjugate(ZDR13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_568 = Coupling(name = 'GC_568',
	 value = '(-1*complex(0,1)*(ZDR21*(ZDL21*ZH11*complexconjugate(Y1d11) + ZDL22*ZH11*complexconjugate(Y1d21) + ZDL23*ZH12*complexconjugate(Y2d31)) + ZDR22*(ZDL21*ZH11*complexconjugate(Y1d12) + ZDL22*ZH11*complexconjugate(Y1d22) + ZDL23*ZH12*complexconjugate(Y2d32)) + ZDR23*(ZDL21*ZH11*complexconjugate(Y1d13) + ZDL22*ZH11*complexconjugate(Y1d23) + ZDL23*ZH12*complexconjugate(Y2d33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_569 = Coupling(name = 'GC_569',
	 value = '(-1*complex(0,1)*(Y1d11*ZH11*complexconjugate(ZDL21)*complexconjugate(ZDR21) + Y1d21*ZH11*complexconjugate(ZDL22)*complexconjugate(ZDR21) + Y2d31*ZH12*complexconjugate(ZDL23)*complexconjugate(ZDR21) + Y1d12*ZH11*complexconjugate(ZDL21)*complexconjugate(ZDR22) + Y1d22*ZH11*complexconjugate(ZDL22)*complexconjugate(ZDR22) + Y2d32*ZH12*complexconjugate(ZDL23)*complexconjugate(ZDR22) + Y1d13*ZH11*complexconjugate(ZDL21)*complexconjugate(ZDR23) + Y1d23*ZH11*complexconjugate(ZDL22)*complexconjugate(ZDR23) + Y2d33*ZH12*complexconjugate(ZDL23)*complexconjugate(ZDR23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_570 = Coupling(name = 'GC_570',
	 value = '(-1*complex(0,1)*(ZDR21*(ZDL21*ZH21*complexconjugate(Y1d11) + ZDL22*ZH21*complexconjugate(Y1d21) + ZDL23*ZH22*complexconjugate(Y2d31)) + ZDR22*(ZDL21*ZH21*complexconjugate(Y1d12) + ZDL22*ZH21*complexconjugate(Y1d22) + ZDL23*ZH22*complexconjugate(Y2d32)) + ZDR23*(ZDL21*ZH21*complexconjugate(Y1d13) + ZDL22*ZH21*complexconjugate(Y1d23) + ZDL23*ZH22*complexconjugate(Y2d33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_571 = Coupling(name = 'GC_571',
	 value = '(-1*complex(0,1)*(Y1d11*ZH21*complexconjugate(ZDL21)*complexconjugate(ZDR21) + Y1d21*ZH21*complexconjugate(ZDL22)*complexconjugate(ZDR21) + Y2d31*ZH22*complexconjugate(ZDL23)*complexconjugate(ZDR21) + Y1d12*ZH21*complexconjugate(ZDL21)*complexconjugate(ZDR22) + Y1d22*ZH21*complexconjugate(ZDL22)*complexconjugate(ZDR22) + Y2d32*ZH22*complexconjugate(ZDL23)*complexconjugate(ZDR22) + Y1d13*ZH21*complexconjugate(ZDL21)*complexconjugate(ZDR23) + Y1d23*ZH21*complexconjugate(ZDL22)*complexconjugate(ZDR23) + Y2d33*ZH22*complexconjugate(ZDL23)*complexconjugate(ZDR23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_572 = Coupling(name = 'GC_572',
	 value = '(-1*complex(0,1)*(ZDR21*(ZDL21*ZH31*complexconjugate(Y1d11) + ZDL22*ZH31*complexconjugate(Y1d21) + ZDL23*ZH32*complexconjugate(Y2d31)) + ZDR22*(ZDL21*ZH31*complexconjugate(Y1d12) + ZDL22*ZH31*complexconjugate(Y1d22) + ZDL23*ZH32*complexconjugate(Y2d32)) + ZDR23*(ZDL21*ZH31*complexconjugate(Y1d13) + ZDL22*ZH31*complexconjugate(Y1d23) + ZDL23*ZH32*complexconjugate(Y2d33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_573 = Coupling(name = 'GC_573',
	 value = '(-1*complex(0,1)*(Y1d11*ZH31*complexconjugate(ZDL21)*complexconjugate(ZDR21) + Y1d21*ZH31*complexconjugate(ZDL22)*complexconjugate(ZDR21) + Y2d31*ZH32*complexconjugate(ZDL23)*complexconjugate(ZDR21) + Y1d12*ZH31*complexconjugate(ZDL21)*complexconjugate(ZDR22) + Y1d22*ZH31*complexconjugate(ZDL22)*complexconjugate(ZDR22) + Y2d32*ZH32*complexconjugate(ZDL23)*complexconjugate(ZDR22) + Y1d13*ZH31*complexconjugate(ZDL21)*complexconjugate(ZDR23) + Y1d23*ZH31*complexconjugate(ZDL22)*complexconjugate(ZDR23) + Y2d33*ZH32*complexconjugate(ZDL23)*complexconjugate(ZDR23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_574 = Coupling(name = 'GC_574',
	 value = '(-1*complex(0,1)*(ZDR21*(ZDL31*ZH11*complexconjugate(Y1d11) + ZDL32*ZH11*complexconjugate(Y1d21) + ZDL33*ZH12*complexconjugate(Y2d31)) + ZDR22*(ZDL31*ZH11*complexconjugate(Y1d12) + ZDL32*ZH11*complexconjugate(Y1d22) + ZDL33*ZH12*complexconjugate(Y2d32)) + ZDR23*(ZDL31*ZH11*complexconjugate(Y1d13) + ZDL32*ZH11*complexconjugate(Y1d23) + ZDL33*ZH12*complexconjugate(Y2d33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_575 = Coupling(name = 'GC_575',
	 value = '(-1*complex(0,1)*(Y1d11*ZH11*complexconjugate(ZDL21)*complexconjugate(ZDR31) + Y1d21*ZH11*complexconjugate(ZDL22)*complexconjugate(ZDR31) + Y2d31*ZH12*complexconjugate(ZDL23)*complexconjugate(ZDR31) + Y1d12*ZH11*complexconjugate(ZDL21)*complexconjugate(ZDR32) + Y1d22*ZH11*complexconjugate(ZDL22)*complexconjugate(ZDR32) + Y2d32*ZH12*complexconjugate(ZDL23)*complexconjugate(ZDR32) + Y1d13*ZH11*complexconjugate(ZDL21)*complexconjugate(ZDR33) + Y1d23*ZH11*complexconjugate(ZDL22)*complexconjugate(ZDR33) + Y2d33*ZH12*complexconjugate(ZDL23)*complexconjugate(ZDR33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_576 = Coupling(name = 'GC_576',
	 value = '(-1*complex(0,1)*(ZDR21*(ZDL31*ZH21*complexconjugate(Y1d11) + ZDL32*ZH21*complexconjugate(Y1d21) + ZDL33*ZH22*complexconjugate(Y2d31)) + ZDR22*(ZDL31*ZH21*complexconjugate(Y1d12) + ZDL32*ZH21*complexconjugate(Y1d22) + ZDL33*ZH22*complexconjugate(Y2d32)) + ZDR23*(ZDL31*ZH21*complexconjugate(Y1d13) + ZDL32*ZH21*complexconjugate(Y1d23) + ZDL33*ZH22*complexconjugate(Y2d33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_577 = Coupling(name = 'GC_577',
	 value = '(-1*complex(0,1)*(Y1d11*ZH21*complexconjugate(ZDL21)*complexconjugate(ZDR31) + Y1d21*ZH21*complexconjugate(ZDL22)*complexconjugate(ZDR31) + Y2d31*ZH22*complexconjugate(ZDL23)*complexconjugate(ZDR31) + Y1d12*ZH21*complexconjugate(ZDL21)*complexconjugate(ZDR32) + Y1d22*ZH21*complexconjugate(ZDL22)*complexconjugate(ZDR32) + Y2d32*ZH22*complexconjugate(ZDL23)*complexconjugate(ZDR32) + Y1d13*ZH21*complexconjugate(ZDL21)*complexconjugate(ZDR33) + Y1d23*ZH21*complexconjugate(ZDL22)*complexconjugate(ZDR33) + Y2d33*ZH22*complexconjugate(ZDL23)*complexconjugate(ZDR33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_578 = Coupling(name = 'GC_578',
	 value = '(-1*complex(0,1)*(ZDR21*(ZDL31*ZH31*complexconjugate(Y1d11) + ZDL32*ZH31*complexconjugate(Y1d21) + ZDL33*ZH32*complexconjugate(Y2d31)) + ZDR22*(ZDL31*ZH31*complexconjugate(Y1d12) + ZDL32*ZH31*complexconjugate(Y1d22) + ZDL33*ZH32*complexconjugate(Y2d32)) + ZDR23*(ZDL31*ZH31*complexconjugate(Y1d13) + ZDL32*ZH31*complexconjugate(Y1d23) + ZDL33*ZH32*complexconjugate(Y2d33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_579 = Coupling(name = 'GC_579',
	 value = '(-1*complex(0,1)*(Y1d11*ZH31*complexconjugate(ZDL21)*complexconjugate(ZDR31) + Y1d21*ZH31*complexconjugate(ZDL22)*complexconjugate(ZDR31) + Y2d31*ZH32*complexconjugate(ZDL23)*complexconjugate(ZDR31) + Y1d12*ZH31*complexconjugate(ZDL21)*complexconjugate(ZDR32) + Y1d22*ZH31*complexconjugate(ZDL22)*complexconjugate(ZDR32) + Y2d32*ZH32*complexconjugate(ZDL23)*complexconjugate(ZDR32) + Y1d13*ZH31*complexconjugate(ZDL21)*complexconjugate(ZDR33) + Y1d23*ZH31*complexconjugate(ZDL22)*complexconjugate(ZDR33) + Y2d33*ZH32*complexconjugate(ZDL23)*complexconjugate(ZDR33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_580 = Coupling(name = 'GC_580',
	 value = '(-1*complex(0,1)*(ZDR31*(ZDL11*ZH11*complexconjugate(Y1d11) + ZDL12*ZH11*complexconjugate(Y1d21) + ZDL13*ZH12*complexconjugate(Y2d31)) + ZDR32*(ZDL11*ZH11*complexconjugate(Y1d12) + ZDL12*ZH11*complexconjugate(Y1d22) + ZDL13*ZH12*complexconjugate(Y2d32)) + ZDR33*(ZDL11*ZH11*complexconjugate(Y1d13) + ZDL12*ZH11*complexconjugate(Y1d23) + ZDL13*ZH12*complexconjugate(Y2d33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_581 = Coupling(name = 'GC_581',
	 value = '(-1*complex(0,1)*(Y1d11*ZH11*complexconjugate(ZDL31)*complexconjugate(ZDR11) + Y1d21*ZH11*complexconjugate(ZDL32)*complexconjugate(ZDR11) + Y2d31*ZH12*complexconjugate(ZDL33)*complexconjugate(ZDR11) + Y1d12*ZH11*complexconjugate(ZDL31)*complexconjugate(ZDR12) + Y1d22*ZH11*complexconjugate(ZDL32)*complexconjugate(ZDR12) + Y2d32*ZH12*complexconjugate(ZDL33)*complexconjugate(ZDR12) + Y1d13*ZH11*complexconjugate(ZDL31)*complexconjugate(ZDR13) + Y1d23*ZH11*complexconjugate(ZDL32)*complexconjugate(ZDR13) + Y2d33*ZH12*complexconjugate(ZDL33)*complexconjugate(ZDR13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_582 = Coupling(name = 'GC_582',
	 value = '(-1*complex(0,1)*(ZDR31*(ZDL11*ZH21*complexconjugate(Y1d11) + ZDL12*ZH21*complexconjugate(Y1d21) + ZDL13*ZH22*complexconjugate(Y2d31)) + ZDR32*(ZDL11*ZH21*complexconjugate(Y1d12) + ZDL12*ZH21*complexconjugate(Y1d22) + ZDL13*ZH22*complexconjugate(Y2d32)) + ZDR33*(ZDL11*ZH21*complexconjugate(Y1d13) + ZDL12*ZH21*complexconjugate(Y1d23) + ZDL13*ZH22*complexconjugate(Y2d33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_583 = Coupling(name = 'GC_583',
	 value = '(-1*complex(0,1)*(Y1d11*ZH21*complexconjugate(ZDL31)*complexconjugate(ZDR11) + Y1d21*ZH21*complexconjugate(ZDL32)*complexconjugate(ZDR11) + Y2d31*ZH22*complexconjugate(ZDL33)*complexconjugate(ZDR11) + Y1d12*ZH21*complexconjugate(ZDL31)*complexconjugate(ZDR12) + Y1d22*ZH21*complexconjugate(ZDL32)*complexconjugate(ZDR12) + Y2d32*ZH22*complexconjugate(ZDL33)*complexconjugate(ZDR12) + Y1d13*ZH21*complexconjugate(ZDL31)*complexconjugate(ZDR13) + Y1d23*ZH21*complexconjugate(ZDL32)*complexconjugate(ZDR13) + Y2d33*ZH22*complexconjugate(ZDL33)*complexconjugate(ZDR13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_584 = Coupling(name = 'GC_584',
	 value = '(-1*complex(0,1)*(ZDR31*(ZDL11*ZH31*complexconjugate(Y1d11) + ZDL12*ZH31*complexconjugate(Y1d21) + ZDL13*ZH32*complexconjugate(Y2d31)) + ZDR32*(ZDL11*ZH31*complexconjugate(Y1d12) + ZDL12*ZH31*complexconjugate(Y1d22) + ZDL13*ZH32*complexconjugate(Y2d32)) + ZDR33*(ZDL11*ZH31*complexconjugate(Y1d13) + ZDL12*ZH31*complexconjugate(Y1d23) + ZDL13*ZH32*complexconjugate(Y2d33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_585 = Coupling(name = 'GC_585',
	 value = '(-1*complex(0,1)*(Y1d11*ZH31*complexconjugate(ZDL31)*complexconjugate(ZDR11) + Y1d21*ZH31*complexconjugate(ZDL32)*complexconjugate(ZDR11) + Y2d31*ZH32*complexconjugate(ZDL33)*complexconjugate(ZDR11) + Y1d12*ZH31*complexconjugate(ZDL31)*complexconjugate(ZDR12) + Y1d22*ZH31*complexconjugate(ZDL32)*complexconjugate(ZDR12) + Y2d32*ZH32*complexconjugate(ZDL33)*complexconjugate(ZDR12) + Y1d13*ZH31*complexconjugate(ZDL31)*complexconjugate(ZDR13) + Y1d23*ZH31*complexconjugate(ZDL32)*complexconjugate(ZDR13) + Y2d33*ZH32*complexconjugate(ZDL33)*complexconjugate(ZDR13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_586 = Coupling(name = 'GC_586',
	 value = '(-1*complex(0,1)*(ZDR31*(ZDL21*ZH11*complexconjugate(Y1d11) + ZDL22*ZH11*complexconjugate(Y1d21) + ZDL23*ZH12*complexconjugate(Y2d31)) + ZDR32*(ZDL21*ZH11*complexconjugate(Y1d12) + ZDL22*ZH11*complexconjugate(Y1d22) + ZDL23*ZH12*complexconjugate(Y2d32)) + ZDR33*(ZDL21*ZH11*complexconjugate(Y1d13) + ZDL22*ZH11*complexconjugate(Y1d23) + ZDL23*ZH12*complexconjugate(Y2d33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_587 = Coupling(name = 'GC_587',
	 value = '(-1*complex(0,1)*(Y1d11*ZH11*complexconjugate(ZDL31)*complexconjugate(ZDR21) + Y1d21*ZH11*complexconjugate(ZDL32)*complexconjugate(ZDR21) + Y2d31*ZH12*complexconjugate(ZDL33)*complexconjugate(ZDR21) + Y1d12*ZH11*complexconjugate(ZDL31)*complexconjugate(ZDR22) + Y1d22*ZH11*complexconjugate(ZDL32)*complexconjugate(ZDR22) + Y2d32*ZH12*complexconjugate(ZDL33)*complexconjugate(ZDR22) + Y1d13*ZH11*complexconjugate(ZDL31)*complexconjugate(ZDR23) + Y1d23*ZH11*complexconjugate(ZDL32)*complexconjugate(ZDR23) + Y2d33*ZH12*complexconjugate(ZDL33)*complexconjugate(ZDR23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_588 = Coupling(name = 'GC_588',
	 value = '(-1*complex(0,1)*(ZDR31*(ZDL21*ZH21*complexconjugate(Y1d11) + ZDL22*ZH21*complexconjugate(Y1d21) + ZDL23*ZH22*complexconjugate(Y2d31)) + ZDR32*(ZDL21*ZH21*complexconjugate(Y1d12) + ZDL22*ZH21*complexconjugate(Y1d22) + ZDL23*ZH22*complexconjugate(Y2d32)) + ZDR33*(ZDL21*ZH21*complexconjugate(Y1d13) + ZDL22*ZH21*complexconjugate(Y1d23) + ZDL23*ZH22*complexconjugate(Y2d33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_589 = Coupling(name = 'GC_589',
	 value = '(-1*complex(0,1)*(Y1d11*ZH21*complexconjugate(ZDL31)*complexconjugate(ZDR21) + Y1d21*ZH21*complexconjugate(ZDL32)*complexconjugate(ZDR21) + Y2d31*ZH22*complexconjugate(ZDL33)*complexconjugate(ZDR21) + Y1d12*ZH21*complexconjugate(ZDL31)*complexconjugate(ZDR22) + Y1d22*ZH21*complexconjugate(ZDL32)*complexconjugate(ZDR22) + Y2d32*ZH22*complexconjugate(ZDL33)*complexconjugate(ZDR22) + Y1d13*ZH21*complexconjugate(ZDL31)*complexconjugate(ZDR23) + Y1d23*ZH21*complexconjugate(ZDL32)*complexconjugate(ZDR23) + Y2d33*ZH22*complexconjugate(ZDL33)*complexconjugate(ZDR23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_590 = Coupling(name = 'GC_590',
	 value = '(-1*complex(0,1)*(ZDR31*(ZDL21*ZH31*complexconjugate(Y1d11) + ZDL22*ZH31*complexconjugate(Y1d21) + ZDL23*ZH32*complexconjugate(Y2d31)) + ZDR32*(ZDL21*ZH31*complexconjugate(Y1d12) + ZDL22*ZH31*complexconjugate(Y1d22) + ZDL23*ZH32*complexconjugate(Y2d32)) + ZDR33*(ZDL21*ZH31*complexconjugate(Y1d13) + ZDL22*ZH31*complexconjugate(Y1d23) + ZDL23*ZH32*complexconjugate(Y2d33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_591 = Coupling(name = 'GC_591',
	 value = '(-1*complex(0,1)*(Y1d11*ZH31*complexconjugate(ZDL31)*complexconjugate(ZDR21) + Y1d21*ZH31*complexconjugate(ZDL32)*complexconjugate(ZDR21) + Y2d31*ZH32*complexconjugate(ZDL33)*complexconjugate(ZDR21) + Y1d12*ZH31*complexconjugate(ZDL31)*complexconjugate(ZDR22) + Y1d22*ZH31*complexconjugate(ZDL32)*complexconjugate(ZDR22) + Y2d32*ZH32*complexconjugate(ZDL33)*complexconjugate(ZDR22) + Y1d13*ZH31*complexconjugate(ZDL31)*complexconjugate(ZDR23) + Y1d23*ZH31*complexconjugate(ZDL32)*complexconjugate(ZDR23) + Y2d33*ZH32*complexconjugate(ZDL33)*complexconjugate(ZDR23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_592 = Coupling(name = 'GC_592',
	 value = '(-1*complex(0,1)*(ZDR31*(ZDL31*ZH11*complexconjugate(Y1d11) + ZDL32*ZH11*complexconjugate(Y1d21) + ZDL33*ZH12*complexconjugate(Y2d31)) + ZDR32*(ZDL31*ZH11*complexconjugate(Y1d12) + ZDL32*ZH11*complexconjugate(Y1d22) + ZDL33*ZH12*complexconjugate(Y2d32)) + ZDR33*(ZDL31*ZH11*complexconjugate(Y1d13) + ZDL32*ZH11*complexconjugate(Y1d23) + ZDL33*ZH12*complexconjugate(Y2d33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_593 = Coupling(name = 'GC_593',
	 value = '(-1*complex(0,1)*(Y1d11*ZH11*complexconjugate(ZDL31)*complexconjugate(ZDR31) + Y1d21*ZH11*complexconjugate(ZDL32)*complexconjugate(ZDR31) + Y2d31*ZH12*complexconjugate(ZDL33)*complexconjugate(ZDR31) + Y1d12*ZH11*complexconjugate(ZDL31)*complexconjugate(ZDR32) + Y1d22*ZH11*complexconjugate(ZDL32)*complexconjugate(ZDR32) + Y2d32*ZH12*complexconjugate(ZDL33)*complexconjugate(ZDR32) + Y1d13*ZH11*complexconjugate(ZDL31)*complexconjugate(ZDR33) + Y1d23*ZH11*complexconjugate(ZDL32)*complexconjugate(ZDR33) + Y2d33*ZH12*complexconjugate(ZDL33)*complexconjugate(ZDR33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_594 = Coupling(name = 'GC_594',
	 value = '(-1*complex(0,1)*(ZDR31*(ZDL31*ZH21*complexconjugate(Y1d11) + ZDL32*ZH21*complexconjugate(Y1d21) + ZDL33*ZH22*complexconjugate(Y2d31)) + ZDR32*(ZDL31*ZH21*complexconjugate(Y1d12) + ZDL32*ZH21*complexconjugate(Y1d22) + ZDL33*ZH22*complexconjugate(Y2d32)) + ZDR33*(ZDL31*ZH21*complexconjugate(Y1d13) + ZDL32*ZH21*complexconjugate(Y1d23) + ZDL33*ZH22*complexconjugate(Y2d33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_595 = Coupling(name = 'GC_595',
	 value = '(-1*complex(0,1)*(Y1d11*ZH21*complexconjugate(ZDL31)*complexconjugate(ZDR31) + Y1d21*ZH21*complexconjugate(ZDL32)*complexconjugate(ZDR31) + Y2d31*ZH22*complexconjugate(ZDL33)*complexconjugate(ZDR31) + Y1d12*ZH21*complexconjugate(ZDL31)*complexconjugate(ZDR32) + Y1d22*ZH21*complexconjugate(ZDL32)*complexconjugate(ZDR32) + Y2d32*ZH22*complexconjugate(ZDL33)*complexconjugate(ZDR32) + Y1d13*ZH21*complexconjugate(ZDL31)*complexconjugate(ZDR33) + Y1d23*ZH21*complexconjugate(ZDL32)*complexconjugate(ZDR33) + Y2d33*ZH22*complexconjugate(ZDL33)*complexconjugate(ZDR33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_596 = Coupling(name = 'GC_596',
	 value = '(-1*complex(0,1)*(ZDR31*(ZDL31*ZH31*complexconjugate(Y1d11) + ZDL32*ZH31*complexconjugate(Y1d21) + ZDL33*ZH32*complexconjugate(Y2d31)) + ZDR32*(ZDL31*ZH31*complexconjugate(Y1d12) + ZDL32*ZH31*complexconjugate(Y1d22) + ZDL33*ZH32*complexconjugate(Y2d32)) + ZDR33*(ZDL31*ZH31*complexconjugate(Y1d13) + ZDL32*ZH31*complexconjugate(Y1d23) + ZDL33*ZH32*complexconjugate(Y2d33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_597 = Coupling(name = 'GC_597',
	 value = '(-1*complex(0,1)*(Y1d11*ZH31*complexconjugate(ZDL31)*complexconjugate(ZDR31) + Y1d21*ZH31*complexconjugate(ZDL32)*complexconjugate(ZDR31) + Y2d31*ZH32*complexconjugate(ZDL33)*complexconjugate(ZDR31) + Y1d12*ZH31*complexconjugate(ZDL31)*complexconjugate(ZDR32) + Y1d22*ZH31*complexconjugate(ZDL32)*complexconjugate(ZDR32) + Y2d32*ZH32*complexconjugate(ZDL33)*complexconjugate(ZDR32) + Y1d13*ZH31*complexconjugate(ZDL31)*complexconjugate(ZDR33) + Y1d23*ZH31*complexconjugate(ZDL32)*complexconjugate(ZDR33) + Y2d33*ZH32*complexconjugate(ZDL33)*complexconjugate(ZDR33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_598 = Coupling(name = 'GC_598',
	 value = '-1*complex(0,1)*(ZUR11*(ZDL11*complexconjugate(Y1u11) + ZDL12*complexconjugate(Y1u21))*complexconjugate(ZP11) + ZUR12*(ZDL11*complexconjugate(Y1u12) + ZDL12*complexconjugate(Y1u22))*complexconjugate(ZP11) + ZDL13*ZUR13*complexconjugate(Y2u33)*complexconjugate(ZP12))', 
	 order = {'QED':1} ) 
 
GC_599 = Coupling(name = 'GC_599',
	 value = '-1*complex(0,1)*(Y1d11*complexconjugate(ZDR11)*complexconjugate(ZP11)*complexconjugate(ZUL11) + Y1d12*complexconjugate(ZDR12)*complexconjugate(ZP11)*complexconjugate(ZUL11) + Y1d13*complexconjugate(ZDR13)*complexconjugate(ZP11)*complexconjugate(ZUL11) + Y1d21*complexconjugate(ZDR11)*complexconjugate(ZP11)*complexconjugate(ZUL12) + Y1d22*complexconjugate(ZDR12)*complexconjugate(ZP11)*complexconjugate(ZUL12) + Y1d23*complexconjugate(ZDR13)*complexconjugate(ZP11)*complexconjugate(ZUL12) + Y2d31*complexconjugate(ZDR11)*complexconjugate(ZP12)*complexconjugate(ZUL13) + Y2d32*complexconjugate(ZDR12)*complexconjugate(ZP12)*complexconjugate(ZUL13) + Y2d33*complexconjugate(ZDR13)*complexconjugate(ZP12)*complexconjugate(ZUL13))', 
	 order = {'QED':1} ) 
 
GC_600 = Coupling(name = 'GC_600',
	 value = '-1*complex(0,1)*(ZUR11*(ZDL11*complexconjugate(Y1u11) + ZDL12*complexconjugate(Y1u21))*complexconjugate(ZP21) + ZUR12*(ZDL11*complexconjugate(Y1u12) + ZDL12*complexconjugate(Y1u22))*complexconjugate(ZP21) + ZDL13*ZUR13*complexconjugate(Y2u33)*complexconjugate(ZP22))', 
	 order = {'QED':1} ) 
 
GC_601 = Coupling(name = 'GC_601',
	 value = '-1*complex(0,1)*(Y1d11*complexconjugate(ZDR11)*complexconjugate(ZP21)*complexconjugate(ZUL11) + Y1d12*complexconjugate(ZDR12)*complexconjugate(ZP21)*complexconjugate(ZUL11) + Y1d13*complexconjugate(ZDR13)*complexconjugate(ZP21)*complexconjugate(ZUL11) + Y1d21*complexconjugate(ZDR11)*complexconjugate(ZP21)*complexconjugate(ZUL12) + Y1d22*complexconjugate(ZDR12)*complexconjugate(ZP21)*complexconjugate(ZUL12) + Y1d23*complexconjugate(ZDR13)*complexconjugate(ZP21)*complexconjugate(ZUL12) + Y2d31*complexconjugate(ZDR11)*complexconjugate(ZP22)*complexconjugate(ZUL13) + Y2d32*complexconjugate(ZDR12)*complexconjugate(ZP22)*complexconjugate(ZUL13) + Y2d33*complexconjugate(ZDR13)*complexconjugate(ZP22)*complexconjugate(ZUL13))', 
	 order = {'QED':1} ) 
 
GC_602 = Coupling(name = 'GC_602',
	 value = '-1*complex(0,1)*(ZUR11*(ZDL21*complexconjugate(Y1u11) + ZDL22*complexconjugate(Y1u21))*complexconjugate(ZP11) + ZUR12*(ZDL21*complexconjugate(Y1u12) + ZDL22*complexconjugate(Y1u22))*complexconjugate(ZP11) + ZDL23*ZUR13*complexconjugate(Y2u33)*complexconjugate(ZP12))', 
	 order = {'QED':1} ) 
 
GC_603 = Coupling(name = 'GC_603',
	 value = '-1*complex(0,1)*(Y1d11*complexconjugate(ZDR21)*complexconjugate(ZP11)*complexconjugate(ZUL11) + Y1d12*complexconjugate(ZDR22)*complexconjugate(ZP11)*complexconjugate(ZUL11) + Y1d13*complexconjugate(ZDR23)*complexconjugate(ZP11)*complexconjugate(ZUL11) + Y1d21*complexconjugate(ZDR21)*complexconjugate(ZP11)*complexconjugate(ZUL12) + Y1d22*complexconjugate(ZDR22)*complexconjugate(ZP11)*complexconjugate(ZUL12) + Y1d23*complexconjugate(ZDR23)*complexconjugate(ZP11)*complexconjugate(ZUL12) + Y2d31*complexconjugate(ZDR21)*complexconjugate(ZP12)*complexconjugate(ZUL13) + Y2d32*complexconjugate(ZDR22)*complexconjugate(ZP12)*complexconjugate(ZUL13) + Y2d33*complexconjugate(ZDR23)*complexconjugate(ZP12)*complexconjugate(ZUL13))', 
	 order = {'QED':1} ) 
 
GC_604 = Coupling(name = 'GC_604',
	 value = '-1*complex(0,1)*(ZUR11*(ZDL21*complexconjugate(Y1u11) + ZDL22*complexconjugate(Y1u21))*complexconjugate(ZP21) + ZUR12*(ZDL21*complexconjugate(Y1u12) + ZDL22*complexconjugate(Y1u22))*complexconjugate(ZP21) + ZDL23*ZUR13*complexconjugate(Y2u33)*complexconjugate(ZP22))', 
	 order = {'QED':1} ) 
 
GC_605 = Coupling(name = 'GC_605',
	 value = '-1*complex(0,1)*(Y1d11*complexconjugate(ZDR21)*complexconjugate(ZP21)*complexconjugate(ZUL11) + Y1d12*complexconjugate(ZDR22)*complexconjugate(ZP21)*complexconjugate(ZUL11) + Y1d13*complexconjugate(ZDR23)*complexconjugate(ZP21)*complexconjugate(ZUL11) + Y1d21*complexconjugate(ZDR21)*complexconjugate(ZP21)*complexconjugate(ZUL12) + Y1d22*complexconjugate(ZDR22)*complexconjugate(ZP21)*complexconjugate(ZUL12) + Y1d23*complexconjugate(ZDR23)*complexconjugate(ZP21)*complexconjugate(ZUL12) + Y2d31*complexconjugate(ZDR21)*complexconjugate(ZP22)*complexconjugate(ZUL13) + Y2d32*complexconjugate(ZDR22)*complexconjugate(ZP22)*complexconjugate(ZUL13) + Y2d33*complexconjugate(ZDR23)*complexconjugate(ZP22)*complexconjugate(ZUL13))', 
	 order = {'QED':1} ) 
 
GC_606 = Coupling(name = 'GC_606',
	 value = '-1*complex(0,1)*(ZUR11*(ZDL31*complexconjugate(Y1u11) + ZDL32*complexconjugate(Y1u21))*complexconjugate(ZP11) + ZUR12*(ZDL31*complexconjugate(Y1u12) + ZDL32*complexconjugate(Y1u22))*complexconjugate(ZP11) + ZDL33*ZUR13*complexconjugate(Y2u33)*complexconjugate(ZP12))', 
	 order = {'QED':1} ) 
 
GC_607 = Coupling(name = 'GC_607',
	 value = '-1*complex(0,1)*(Y1d11*complexconjugate(ZDR31)*complexconjugate(ZP11)*complexconjugate(ZUL11) + Y1d12*complexconjugate(ZDR32)*complexconjugate(ZP11)*complexconjugate(ZUL11) + Y1d13*complexconjugate(ZDR33)*complexconjugate(ZP11)*complexconjugate(ZUL11) + Y1d21*complexconjugate(ZDR31)*complexconjugate(ZP11)*complexconjugate(ZUL12) + Y1d22*complexconjugate(ZDR32)*complexconjugate(ZP11)*complexconjugate(ZUL12) + Y1d23*complexconjugate(ZDR33)*complexconjugate(ZP11)*complexconjugate(ZUL12) + Y2d31*complexconjugate(ZDR31)*complexconjugate(ZP12)*complexconjugate(ZUL13) + Y2d32*complexconjugate(ZDR32)*complexconjugate(ZP12)*complexconjugate(ZUL13) + Y2d33*complexconjugate(ZDR33)*complexconjugate(ZP12)*complexconjugate(ZUL13))', 
	 order = {'QED':1} ) 
 
GC_608 = Coupling(name = 'GC_608',
	 value = '-1*complex(0,1)*(ZUR11*(ZDL31*complexconjugate(Y1u11) + ZDL32*complexconjugate(Y1u21))*complexconjugate(ZP21) + ZUR12*(ZDL31*complexconjugate(Y1u12) + ZDL32*complexconjugate(Y1u22))*complexconjugate(ZP21) + ZDL33*ZUR13*complexconjugate(Y2u33)*complexconjugate(ZP22))', 
	 order = {'QED':1} ) 
 
GC_609 = Coupling(name = 'GC_609',
	 value = '-1*complex(0,1)*(Y1d11*complexconjugate(ZDR31)*complexconjugate(ZP21)*complexconjugate(ZUL11) + Y1d12*complexconjugate(ZDR32)*complexconjugate(ZP21)*complexconjugate(ZUL11) + Y1d13*complexconjugate(ZDR33)*complexconjugate(ZP21)*complexconjugate(ZUL11) + Y1d21*complexconjugate(ZDR31)*complexconjugate(ZP21)*complexconjugate(ZUL12) + Y1d22*complexconjugate(ZDR32)*complexconjugate(ZP21)*complexconjugate(ZUL12) + Y1d23*complexconjugate(ZDR33)*complexconjugate(ZP21)*complexconjugate(ZUL12) + Y2d31*complexconjugate(ZDR31)*complexconjugate(ZP22)*complexconjugate(ZUL13) + Y2d32*complexconjugate(ZDR32)*complexconjugate(ZP22)*complexconjugate(ZUL13) + Y2d33*complexconjugate(ZDR33)*complexconjugate(ZP22)*complexconjugate(ZUL13))', 
	 order = {'QED':1} ) 
 
GC_610 = Coupling(name = 'GC_610',
	 value = '-1*complex(0,1)*(ZUR21*(ZDL11*complexconjugate(Y1u11) + ZDL12*complexconjugate(Y1u21))*complexconjugate(ZP11) + ZUR22*(ZDL11*complexconjugate(Y1u12) + ZDL12*complexconjugate(Y1u22))*complexconjugate(ZP11) + ZDL13*ZUR23*complexconjugate(Y2u33)*complexconjugate(ZP12))', 
	 order = {'QED':1} ) 
 
GC_611 = Coupling(name = 'GC_611',
	 value = '-1*complex(0,1)*(Y1d11*complexconjugate(ZDR11)*complexconjugate(ZP11)*complexconjugate(ZUL21) + Y1d12*complexconjugate(ZDR12)*complexconjugate(ZP11)*complexconjugate(ZUL21) + Y1d13*complexconjugate(ZDR13)*complexconjugate(ZP11)*complexconjugate(ZUL21) + Y1d21*complexconjugate(ZDR11)*complexconjugate(ZP11)*complexconjugate(ZUL22) + Y1d22*complexconjugate(ZDR12)*complexconjugate(ZP11)*complexconjugate(ZUL22) + Y1d23*complexconjugate(ZDR13)*complexconjugate(ZP11)*complexconjugate(ZUL22) + Y2d31*complexconjugate(ZDR11)*complexconjugate(ZP12)*complexconjugate(ZUL23) + Y2d32*complexconjugate(ZDR12)*complexconjugate(ZP12)*complexconjugate(ZUL23) + Y2d33*complexconjugate(ZDR13)*complexconjugate(ZP12)*complexconjugate(ZUL23))', 
	 order = {'QED':1} ) 
 
GC_612 = Coupling(name = 'GC_612',
	 value = '-1*complex(0,1)*(ZUR21*(ZDL11*complexconjugate(Y1u11) + ZDL12*complexconjugate(Y1u21))*complexconjugate(ZP21) + ZUR22*(ZDL11*complexconjugate(Y1u12) + ZDL12*complexconjugate(Y1u22))*complexconjugate(ZP21) + ZDL13*ZUR23*complexconjugate(Y2u33)*complexconjugate(ZP22))', 
	 order = {'QED':1} ) 
 
GC_613 = Coupling(name = 'GC_613',
	 value = '-1*complex(0,1)*(Y1d11*complexconjugate(ZDR11)*complexconjugate(ZP21)*complexconjugate(ZUL21) + Y1d12*complexconjugate(ZDR12)*complexconjugate(ZP21)*complexconjugate(ZUL21) + Y1d13*complexconjugate(ZDR13)*complexconjugate(ZP21)*complexconjugate(ZUL21) + Y1d21*complexconjugate(ZDR11)*complexconjugate(ZP21)*complexconjugate(ZUL22) + Y1d22*complexconjugate(ZDR12)*complexconjugate(ZP21)*complexconjugate(ZUL22) + Y1d23*complexconjugate(ZDR13)*complexconjugate(ZP21)*complexconjugate(ZUL22) + Y2d31*complexconjugate(ZDR11)*complexconjugate(ZP22)*complexconjugate(ZUL23) + Y2d32*complexconjugate(ZDR12)*complexconjugate(ZP22)*complexconjugate(ZUL23) + Y2d33*complexconjugate(ZDR13)*complexconjugate(ZP22)*complexconjugate(ZUL23))', 
	 order = {'QED':1} ) 
 
GC_614 = Coupling(name = 'GC_614',
	 value = '-1*complex(0,1)*(ZUR21*(ZDL21*complexconjugate(Y1u11) + ZDL22*complexconjugate(Y1u21))*complexconjugate(ZP11) + ZUR22*(ZDL21*complexconjugate(Y1u12) + ZDL22*complexconjugate(Y1u22))*complexconjugate(ZP11) + ZDL23*ZUR23*complexconjugate(Y2u33)*complexconjugate(ZP12))', 
	 order = {'QED':1} ) 
 
GC_615 = Coupling(name = 'GC_615',
	 value = '-1*complex(0,1)*(Y1d11*complexconjugate(ZDR21)*complexconjugate(ZP11)*complexconjugate(ZUL21) + Y1d12*complexconjugate(ZDR22)*complexconjugate(ZP11)*complexconjugate(ZUL21) + Y1d13*complexconjugate(ZDR23)*complexconjugate(ZP11)*complexconjugate(ZUL21) + Y1d21*complexconjugate(ZDR21)*complexconjugate(ZP11)*complexconjugate(ZUL22) + Y1d22*complexconjugate(ZDR22)*complexconjugate(ZP11)*complexconjugate(ZUL22) + Y1d23*complexconjugate(ZDR23)*complexconjugate(ZP11)*complexconjugate(ZUL22) + Y2d31*complexconjugate(ZDR21)*complexconjugate(ZP12)*complexconjugate(ZUL23) + Y2d32*complexconjugate(ZDR22)*complexconjugate(ZP12)*complexconjugate(ZUL23) + Y2d33*complexconjugate(ZDR23)*complexconjugate(ZP12)*complexconjugate(ZUL23))', 
	 order = {'QED':1} ) 
 
GC_616 = Coupling(name = 'GC_616',
	 value = '-1*complex(0,1)*(ZUR21*(ZDL21*complexconjugate(Y1u11) + ZDL22*complexconjugate(Y1u21))*complexconjugate(ZP21) + ZUR22*(ZDL21*complexconjugate(Y1u12) + ZDL22*complexconjugate(Y1u22))*complexconjugate(ZP21) + ZDL23*ZUR23*complexconjugate(Y2u33)*complexconjugate(ZP22))', 
	 order = {'QED':1} ) 
 
GC_617 = Coupling(name = 'GC_617',
	 value = '-1*complex(0,1)*(Y1d11*complexconjugate(ZDR21)*complexconjugate(ZP21)*complexconjugate(ZUL21) + Y1d12*complexconjugate(ZDR22)*complexconjugate(ZP21)*complexconjugate(ZUL21) + Y1d13*complexconjugate(ZDR23)*complexconjugate(ZP21)*complexconjugate(ZUL21) + Y1d21*complexconjugate(ZDR21)*complexconjugate(ZP21)*complexconjugate(ZUL22) + Y1d22*complexconjugate(ZDR22)*complexconjugate(ZP21)*complexconjugate(ZUL22) + Y1d23*complexconjugate(ZDR23)*complexconjugate(ZP21)*complexconjugate(ZUL22) + Y2d31*complexconjugate(ZDR21)*complexconjugate(ZP22)*complexconjugate(ZUL23) + Y2d32*complexconjugate(ZDR22)*complexconjugate(ZP22)*complexconjugate(ZUL23) + Y2d33*complexconjugate(ZDR23)*complexconjugate(ZP22)*complexconjugate(ZUL23))', 
	 order = {'QED':1} ) 
 
GC_618 = Coupling(name = 'GC_618',
	 value = '-1*complex(0,1)*(ZUR21*(ZDL31*complexconjugate(Y1u11) + ZDL32*complexconjugate(Y1u21))*complexconjugate(ZP11) + ZUR22*(ZDL31*complexconjugate(Y1u12) + ZDL32*complexconjugate(Y1u22))*complexconjugate(ZP11) + ZDL33*ZUR23*complexconjugate(Y2u33)*complexconjugate(ZP12))', 
	 order = {'QED':1} ) 
 
GC_619 = Coupling(name = 'GC_619',
	 value = '-1*complex(0,1)*(Y1d11*complexconjugate(ZDR31)*complexconjugate(ZP11)*complexconjugate(ZUL21) + Y1d12*complexconjugate(ZDR32)*complexconjugate(ZP11)*complexconjugate(ZUL21) + Y1d13*complexconjugate(ZDR33)*complexconjugate(ZP11)*complexconjugate(ZUL21) + Y1d21*complexconjugate(ZDR31)*complexconjugate(ZP11)*complexconjugate(ZUL22) + Y1d22*complexconjugate(ZDR32)*complexconjugate(ZP11)*complexconjugate(ZUL22) + Y1d23*complexconjugate(ZDR33)*complexconjugate(ZP11)*complexconjugate(ZUL22) + Y2d31*complexconjugate(ZDR31)*complexconjugate(ZP12)*complexconjugate(ZUL23) + Y2d32*complexconjugate(ZDR32)*complexconjugate(ZP12)*complexconjugate(ZUL23) + Y2d33*complexconjugate(ZDR33)*complexconjugate(ZP12)*complexconjugate(ZUL23))', 
	 order = {'QED':1} ) 
 
GC_620 = Coupling(name = 'GC_620',
	 value = '-1*complex(0,1)*(ZUR21*(ZDL31*complexconjugate(Y1u11) + ZDL32*complexconjugate(Y1u21))*complexconjugate(ZP21) + ZUR22*(ZDL31*complexconjugate(Y1u12) + ZDL32*complexconjugate(Y1u22))*complexconjugate(ZP21) + ZDL33*ZUR23*complexconjugate(Y2u33)*complexconjugate(ZP22))', 
	 order = {'QED':1} ) 
 
GC_621 = Coupling(name = 'GC_621',
	 value = '-1*complex(0,1)*(Y1d11*complexconjugate(ZDR31)*complexconjugate(ZP21)*complexconjugate(ZUL21) + Y1d12*complexconjugate(ZDR32)*complexconjugate(ZP21)*complexconjugate(ZUL21) + Y1d13*complexconjugate(ZDR33)*complexconjugate(ZP21)*complexconjugate(ZUL21) + Y1d21*complexconjugate(ZDR31)*complexconjugate(ZP21)*complexconjugate(ZUL22) + Y1d22*complexconjugate(ZDR32)*complexconjugate(ZP21)*complexconjugate(ZUL22) + Y1d23*complexconjugate(ZDR33)*complexconjugate(ZP21)*complexconjugate(ZUL22) + Y2d31*complexconjugate(ZDR31)*complexconjugate(ZP22)*complexconjugate(ZUL23) + Y2d32*complexconjugate(ZDR32)*complexconjugate(ZP22)*complexconjugate(ZUL23) + Y2d33*complexconjugate(ZDR33)*complexconjugate(ZP22)*complexconjugate(ZUL23))', 
	 order = {'QED':1} ) 
 
GC_622 = Coupling(name = 'GC_622',
	 value = '-1*complex(0,1)*(ZUR31*(ZDL11*complexconjugate(Y1u11) + ZDL12*complexconjugate(Y1u21))*complexconjugate(ZP11) + ZUR32*(ZDL11*complexconjugate(Y1u12) + ZDL12*complexconjugate(Y1u22))*complexconjugate(ZP11) + ZDL13*ZUR33*complexconjugate(Y2u33)*complexconjugate(ZP12))', 
	 order = {'QED':1} ) 
 
GC_623 = Coupling(name = 'GC_623',
	 value = '-1*complex(0,1)*(Y1d11*complexconjugate(ZDR11)*complexconjugate(ZP11)*complexconjugate(ZUL31) + Y1d12*complexconjugate(ZDR12)*complexconjugate(ZP11)*complexconjugate(ZUL31) + Y1d13*complexconjugate(ZDR13)*complexconjugate(ZP11)*complexconjugate(ZUL31) + Y1d21*complexconjugate(ZDR11)*complexconjugate(ZP11)*complexconjugate(ZUL32) + Y1d22*complexconjugate(ZDR12)*complexconjugate(ZP11)*complexconjugate(ZUL32) + Y1d23*complexconjugate(ZDR13)*complexconjugate(ZP11)*complexconjugate(ZUL32) + Y2d31*complexconjugate(ZDR11)*complexconjugate(ZP12)*complexconjugate(ZUL33) + Y2d32*complexconjugate(ZDR12)*complexconjugate(ZP12)*complexconjugate(ZUL33) + Y2d33*complexconjugate(ZDR13)*complexconjugate(ZP12)*complexconjugate(ZUL33))', 
	 order = {'QED':1} ) 
 
GC_624 = Coupling(name = 'GC_624',
	 value = '-1*complex(0,1)*(ZUR31*(ZDL11*complexconjugate(Y1u11) + ZDL12*complexconjugate(Y1u21))*complexconjugate(ZP21) + ZUR32*(ZDL11*complexconjugate(Y1u12) + ZDL12*complexconjugate(Y1u22))*complexconjugate(ZP21) + ZDL13*ZUR33*complexconjugate(Y2u33)*complexconjugate(ZP22))', 
	 order = {'QED':1} ) 
 
GC_625 = Coupling(name = 'GC_625',
	 value = '-1*complex(0,1)*(Y1d11*complexconjugate(ZDR11)*complexconjugate(ZP21)*complexconjugate(ZUL31) + Y1d12*complexconjugate(ZDR12)*complexconjugate(ZP21)*complexconjugate(ZUL31) + Y1d13*complexconjugate(ZDR13)*complexconjugate(ZP21)*complexconjugate(ZUL31) + Y1d21*complexconjugate(ZDR11)*complexconjugate(ZP21)*complexconjugate(ZUL32) + Y1d22*complexconjugate(ZDR12)*complexconjugate(ZP21)*complexconjugate(ZUL32) + Y1d23*complexconjugate(ZDR13)*complexconjugate(ZP21)*complexconjugate(ZUL32) + Y2d31*complexconjugate(ZDR11)*complexconjugate(ZP22)*complexconjugate(ZUL33) + Y2d32*complexconjugate(ZDR12)*complexconjugate(ZP22)*complexconjugate(ZUL33) + Y2d33*complexconjugate(ZDR13)*complexconjugate(ZP22)*complexconjugate(ZUL33))', 
	 order = {'QED':1} ) 
 
GC_626 = Coupling(name = 'GC_626',
	 value = '-1*complex(0,1)*(ZUR31*(ZDL21*complexconjugate(Y1u11) + ZDL22*complexconjugate(Y1u21))*complexconjugate(ZP11) + ZUR32*(ZDL21*complexconjugate(Y1u12) + ZDL22*complexconjugate(Y1u22))*complexconjugate(ZP11) + ZDL23*ZUR33*complexconjugate(Y2u33)*complexconjugate(ZP12))', 
	 order = {'QED':1} ) 
 
GC_627 = Coupling(name = 'GC_627',
	 value = '-1*complex(0,1)*(Y1d11*complexconjugate(ZDR21)*complexconjugate(ZP11)*complexconjugate(ZUL31) + Y1d12*complexconjugate(ZDR22)*complexconjugate(ZP11)*complexconjugate(ZUL31) + Y1d13*complexconjugate(ZDR23)*complexconjugate(ZP11)*complexconjugate(ZUL31) + Y1d21*complexconjugate(ZDR21)*complexconjugate(ZP11)*complexconjugate(ZUL32) + Y1d22*complexconjugate(ZDR22)*complexconjugate(ZP11)*complexconjugate(ZUL32) + Y1d23*complexconjugate(ZDR23)*complexconjugate(ZP11)*complexconjugate(ZUL32) + Y2d31*complexconjugate(ZDR21)*complexconjugate(ZP12)*complexconjugate(ZUL33) + Y2d32*complexconjugate(ZDR22)*complexconjugate(ZP12)*complexconjugate(ZUL33) + Y2d33*complexconjugate(ZDR23)*complexconjugate(ZP12)*complexconjugate(ZUL33))', 
	 order = {'QED':1} ) 
 
GC_628 = Coupling(name = 'GC_628',
	 value = '-1*complex(0,1)*(ZUR31*(ZDL21*complexconjugate(Y1u11) + ZDL22*complexconjugate(Y1u21))*complexconjugate(ZP21) + ZUR32*(ZDL21*complexconjugate(Y1u12) + ZDL22*complexconjugate(Y1u22))*complexconjugate(ZP21) + ZDL23*ZUR33*complexconjugate(Y2u33)*complexconjugate(ZP22))', 
	 order = {'QED':1} ) 
 
GC_629 = Coupling(name = 'GC_629',
	 value = '-1*complex(0,1)*(Y1d11*complexconjugate(ZDR21)*complexconjugate(ZP21)*complexconjugate(ZUL31) + Y1d12*complexconjugate(ZDR22)*complexconjugate(ZP21)*complexconjugate(ZUL31) + Y1d13*complexconjugate(ZDR23)*complexconjugate(ZP21)*complexconjugate(ZUL31) + Y1d21*complexconjugate(ZDR21)*complexconjugate(ZP21)*complexconjugate(ZUL32) + Y1d22*complexconjugate(ZDR22)*complexconjugate(ZP21)*complexconjugate(ZUL32) + Y1d23*complexconjugate(ZDR23)*complexconjugate(ZP21)*complexconjugate(ZUL32) + Y2d31*complexconjugate(ZDR21)*complexconjugate(ZP22)*complexconjugate(ZUL33) + Y2d32*complexconjugate(ZDR22)*complexconjugate(ZP22)*complexconjugate(ZUL33) + Y2d33*complexconjugate(ZDR23)*complexconjugate(ZP22)*complexconjugate(ZUL33))', 
	 order = {'QED':1} ) 
 
GC_630 = Coupling(name = 'GC_630',
	 value = '-1*complex(0,1)*(ZUR31*(ZDL31*complexconjugate(Y1u11) + ZDL32*complexconjugate(Y1u21))*complexconjugate(ZP11) + ZUR32*(ZDL31*complexconjugate(Y1u12) + ZDL32*complexconjugate(Y1u22))*complexconjugate(ZP11) + ZDL33*ZUR33*complexconjugate(Y2u33)*complexconjugate(ZP12))', 
	 order = {'QED':1} ) 
 
GC_631 = Coupling(name = 'GC_631',
	 value = '-1*complex(0,1)*(Y1d11*complexconjugate(ZDR31)*complexconjugate(ZP11)*complexconjugate(ZUL31) + Y1d12*complexconjugate(ZDR32)*complexconjugate(ZP11)*complexconjugate(ZUL31) + Y1d13*complexconjugate(ZDR33)*complexconjugate(ZP11)*complexconjugate(ZUL31) + Y1d21*complexconjugate(ZDR31)*complexconjugate(ZP11)*complexconjugate(ZUL32) + Y1d22*complexconjugate(ZDR32)*complexconjugate(ZP11)*complexconjugate(ZUL32) + Y1d23*complexconjugate(ZDR33)*complexconjugate(ZP11)*complexconjugate(ZUL32) + Y2d31*complexconjugate(ZDR31)*complexconjugate(ZP12)*complexconjugate(ZUL33) + Y2d32*complexconjugate(ZDR32)*complexconjugate(ZP12)*complexconjugate(ZUL33) + Y2d33*complexconjugate(ZDR33)*complexconjugate(ZP12)*complexconjugate(ZUL33))', 
	 order = {'QED':1} ) 
 
GC_632 = Coupling(name = 'GC_632',
	 value = '-1*complex(0,1)*(ZUR31*(ZDL31*complexconjugate(Y1u11) + ZDL32*complexconjugate(Y1u21))*complexconjugate(ZP21) + ZUR32*(ZDL31*complexconjugate(Y1u12) + ZDL32*complexconjugate(Y1u22))*complexconjugate(ZP21) + ZDL33*ZUR33*complexconjugate(Y2u33)*complexconjugate(ZP22))', 
	 order = {'QED':1} ) 
 
GC_633 = Coupling(name = 'GC_633',
	 value = '-1*complex(0,1)*(Y1d11*complexconjugate(ZDR31)*complexconjugate(ZP21)*complexconjugate(ZUL31) + Y1d12*complexconjugate(ZDR32)*complexconjugate(ZP21)*complexconjugate(ZUL31) + Y1d13*complexconjugate(ZDR33)*complexconjugate(ZP21)*complexconjugate(ZUL31) + Y1d21*complexconjugate(ZDR31)*complexconjugate(ZP21)*complexconjugate(ZUL32) + Y1d22*complexconjugate(ZDR32)*complexconjugate(ZP21)*complexconjugate(ZUL32) + Y1d23*complexconjugate(ZDR33)*complexconjugate(ZP21)*complexconjugate(ZUL32) + Y2d31*complexconjugate(ZDR31)*complexconjugate(ZP22)*complexconjugate(ZUL33) + Y2d32*complexconjugate(ZDR32)*complexconjugate(ZP22)*complexconjugate(ZUL33) + Y2d33*complexconjugate(ZDR33)*complexconjugate(ZP22)*complexconjugate(ZUL33))', 
	 order = {'QED':1} ) 
 
GC_634 = Coupling(name = 'GC_634',
	 value = '1*complex(0,1)*(-(ZEL11*(Vv14*complexconjugate(Y1n11) + Vv15*complexconjugate(Y1n12))*complexconjugate(ZP11)) - ZEL12*(Vv14*complexconjugate(Y1n21) + Vv15*complexconjugate(Y1n22))*complexconjugate(ZP11) - Vv16*ZEL13*complexconjugate(Y2n33)*complexconjugate(ZP12))', 
	 order = {'QED':1} ) 
 
GC_635 = Coupling(name = 'GC_635',
	 value = '1*complex(0,1)*(-(Y1e11*complexconjugate(Vv11)*complexconjugate(ZER11)*complexconjugate(ZP11)) - Y1e21*complexconjugate(Vv12)*complexconjugate(ZER11)*complexconjugate(ZP11) - Y1e12*complexconjugate(Vv11)*complexconjugate(ZER12)*complexconjugate(ZP11) - Y1e22*complexconjugate(Vv12)*complexconjugate(ZER12)*complexconjugate(ZP11) - Y2e33*complexconjugate(Vv13)*complexconjugate(ZER13)*complexconjugate(ZP12))', 
	 order = {'QED':1} ) 
 
GC_636 = Coupling(name = 'GC_636',
	 value = '1*complex(0,1)*(-(ZEL11*(Vv14*complexconjugate(Y1n11) + Vv15*complexconjugate(Y1n12))*complexconjugate(ZP21)) - ZEL12*(Vv14*complexconjugate(Y1n21) + Vv15*complexconjugate(Y1n22))*complexconjugate(ZP21) - Vv16*ZEL13*complexconjugate(Y2n33)*complexconjugate(ZP22))', 
	 order = {'QED':1} ) 
 
GC_637 = Coupling(name = 'GC_637',
	 value = '1*complex(0,1)*(-(Y1e11*complexconjugate(Vv11)*complexconjugate(ZER11)*complexconjugate(ZP21)) - Y1e21*complexconjugate(Vv12)*complexconjugate(ZER11)*complexconjugate(ZP21) - Y1e12*complexconjugate(Vv11)*complexconjugate(ZER12)*complexconjugate(ZP21) - Y1e22*complexconjugate(Vv12)*complexconjugate(ZER12)*complexconjugate(ZP21) - Y2e33*complexconjugate(Vv13)*complexconjugate(ZER13)*complexconjugate(ZP22))', 
	 order = {'QED':1} ) 
 
GC_638 = Coupling(name = 'GC_638',
	 value = '1*complex(0,1)*(-(ZEL21*(Vv14*complexconjugate(Y1n11) + Vv15*complexconjugate(Y1n12))*complexconjugate(ZP11)) - ZEL22*(Vv14*complexconjugate(Y1n21) + Vv15*complexconjugate(Y1n22))*complexconjugate(ZP11) - Vv16*ZEL23*complexconjugate(Y2n33)*complexconjugate(ZP12))', 
	 order = {'QED':1} ) 
 
GC_639 = Coupling(name = 'GC_639',
	 value = '1*complex(0,1)*(-(Y1e11*complexconjugate(Vv11)*complexconjugate(ZER21)*complexconjugate(ZP11)) - Y1e21*complexconjugate(Vv12)*complexconjugate(ZER21)*complexconjugate(ZP11) - Y1e12*complexconjugate(Vv11)*complexconjugate(ZER22)*complexconjugate(ZP11) - Y1e22*complexconjugate(Vv12)*complexconjugate(ZER22)*complexconjugate(ZP11) - Y2e33*complexconjugate(Vv13)*complexconjugate(ZER23)*complexconjugate(ZP12))', 
	 order = {'QED':1} ) 
 
GC_640 = Coupling(name = 'GC_640',
	 value = '1*complex(0,1)*(-(ZEL21*(Vv14*complexconjugate(Y1n11) + Vv15*complexconjugate(Y1n12))*complexconjugate(ZP21)) - ZEL22*(Vv14*complexconjugate(Y1n21) + Vv15*complexconjugate(Y1n22))*complexconjugate(ZP21) - Vv16*ZEL23*complexconjugate(Y2n33)*complexconjugate(ZP22))', 
	 order = {'QED':1} ) 
 
GC_641 = Coupling(name = 'GC_641',
	 value = '1*complex(0,1)*(-(Y1e11*complexconjugate(Vv11)*complexconjugate(ZER21)*complexconjugate(ZP21)) - Y1e21*complexconjugate(Vv12)*complexconjugate(ZER21)*complexconjugate(ZP21) - Y1e12*complexconjugate(Vv11)*complexconjugate(ZER22)*complexconjugate(ZP21) - Y1e22*complexconjugate(Vv12)*complexconjugate(ZER22)*complexconjugate(ZP21) - Y2e33*complexconjugate(Vv13)*complexconjugate(ZER23)*complexconjugate(ZP22))', 
	 order = {'QED':1} ) 
 
GC_642 = Coupling(name = 'GC_642',
	 value = '1*complex(0,1)*(-(ZEL31*(Vv14*complexconjugate(Y1n11) + Vv15*complexconjugate(Y1n12))*complexconjugate(ZP11)) - ZEL32*(Vv14*complexconjugate(Y1n21) + Vv15*complexconjugate(Y1n22))*complexconjugate(ZP11) - Vv16*ZEL33*complexconjugate(Y2n33)*complexconjugate(ZP12))', 
	 order = {'QED':1} ) 
 
GC_643 = Coupling(name = 'GC_643',
	 value = '1*complex(0,1)*(-(Y1e11*complexconjugate(Vv11)*complexconjugate(ZER31)*complexconjugate(ZP11)) - Y1e21*complexconjugate(Vv12)*complexconjugate(ZER31)*complexconjugate(ZP11) - Y1e12*complexconjugate(Vv11)*complexconjugate(ZER32)*complexconjugate(ZP11) - Y1e22*complexconjugate(Vv12)*complexconjugate(ZER32)*complexconjugate(ZP11) - Y2e33*complexconjugate(Vv13)*complexconjugate(ZER33)*complexconjugate(ZP12))', 
	 order = {'QED':1} ) 
 
GC_644 = Coupling(name = 'GC_644',
	 value = '1*complex(0,1)*(-(ZEL31*(Vv14*complexconjugate(Y1n11) + Vv15*complexconjugate(Y1n12))*complexconjugate(ZP21)) - ZEL32*(Vv14*complexconjugate(Y1n21) + Vv15*complexconjugate(Y1n22))*complexconjugate(ZP21) - Vv16*ZEL33*complexconjugate(Y2n33)*complexconjugate(ZP22))', 
	 order = {'QED':1} ) 
 
GC_645 = Coupling(name = 'GC_645',
	 value = '1*complex(0,1)*(-(Y1e11*complexconjugate(Vv11)*complexconjugate(ZER31)*complexconjugate(ZP21)) - Y1e21*complexconjugate(Vv12)*complexconjugate(ZER31)*complexconjugate(ZP21) - Y1e12*complexconjugate(Vv11)*complexconjugate(ZER32)*complexconjugate(ZP21) - Y1e22*complexconjugate(Vv12)*complexconjugate(ZER32)*complexconjugate(ZP21) - Y2e33*complexconjugate(Vv13)*complexconjugate(ZER33)*complexconjugate(ZP22))', 
	 order = {'QED':1} ) 
 
GC_646 = Coupling(name = 'GC_646',
	 value = '1*complex(0,1)*(-(ZEL11*(Vv24*complexconjugate(Y1n11) + Vv25*complexconjugate(Y1n12))*complexconjugate(ZP11)) - ZEL12*(Vv24*complexconjugate(Y1n21) + Vv25*complexconjugate(Y1n22))*complexconjugate(ZP11) - Vv26*ZEL13*complexconjugate(Y2n33)*complexconjugate(ZP12))', 
	 order = {'QED':1} ) 
 
GC_647 = Coupling(name = 'GC_647',
	 value = '1*complex(0,1)*(-(Y1e11*complexconjugate(Vv21)*complexconjugate(ZER11)*complexconjugate(ZP11)) - Y1e21*complexconjugate(Vv22)*complexconjugate(ZER11)*complexconjugate(ZP11) - Y1e12*complexconjugate(Vv21)*complexconjugate(ZER12)*complexconjugate(ZP11) - Y1e22*complexconjugate(Vv22)*complexconjugate(ZER12)*complexconjugate(ZP11) - Y2e33*complexconjugate(Vv23)*complexconjugate(ZER13)*complexconjugate(ZP12))', 
	 order = {'QED':1} ) 
 
GC_648 = Coupling(name = 'GC_648',
	 value = '1*complex(0,1)*(-(ZEL11*(Vv24*complexconjugate(Y1n11) + Vv25*complexconjugate(Y1n12))*complexconjugate(ZP21)) - ZEL12*(Vv24*complexconjugate(Y1n21) + Vv25*complexconjugate(Y1n22))*complexconjugate(ZP21) - Vv26*ZEL13*complexconjugate(Y2n33)*complexconjugate(ZP22))', 
	 order = {'QED':1} ) 
 
GC_649 = Coupling(name = 'GC_649',
	 value = '1*complex(0,1)*(-(Y1e11*complexconjugate(Vv21)*complexconjugate(ZER11)*complexconjugate(ZP21)) - Y1e21*complexconjugate(Vv22)*complexconjugate(ZER11)*complexconjugate(ZP21) - Y1e12*complexconjugate(Vv21)*complexconjugate(ZER12)*complexconjugate(ZP21) - Y1e22*complexconjugate(Vv22)*complexconjugate(ZER12)*complexconjugate(ZP21) - Y2e33*complexconjugate(Vv23)*complexconjugate(ZER13)*complexconjugate(ZP22))', 
	 order = {'QED':1} ) 
 
GC_650 = Coupling(name = 'GC_650',
	 value = '1*complex(0,1)*(-(ZEL21*(Vv24*complexconjugate(Y1n11) + Vv25*complexconjugate(Y1n12))*complexconjugate(ZP11)) - ZEL22*(Vv24*complexconjugate(Y1n21) + Vv25*complexconjugate(Y1n22))*complexconjugate(ZP11) - Vv26*ZEL23*complexconjugate(Y2n33)*complexconjugate(ZP12))', 
	 order = {'QED':1} ) 
 
GC_651 = Coupling(name = 'GC_651',
	 value = '1*complex(0,1)*(-(Y1e11*complexconjugate(Vv21)*complexconjugate(ZER21)*complexconjugate(ZP11)) - Y1e21*complexconjugate(Vv22)*complexconjugate(ZER21)*complexconjugate(ZP11) - Y1e12*complexconjugate(Vv21)*complexconjugate(ZER22)*complexconjugate(ZP11) - Y1e22*complexconjugate(Vv22)*complexconjugate(ZER22)*complexconjugate(ZP11) - Y2e33*complexconjugate(Vv23)*complexconjugate(ZER23)*complexconjugate(ZP12))', 
	 order = {'QED':1} ) 
 
GC_652 = Coupling(name = 'GC_652',
	 value = '1*complex(0,1)*(-(ZEL21*(Vv24*complexconjugate(Y1n11) + Vv25*complexconjugate(Y1n12))*complexconjugate(ZP21)) - ZEL22*(Vv24*complexconjugate(Y1n21) + Vv25*complexconjugate(Y1n22))*complexconjugate(ZP21) - Vv26*ZEL23*complexconjugate(Y2n33)*complexconjugate(ZP22))', 
	 order = {'QED':1} ) 
 
GC_653 = Coupling(name = 'GC_653',
	 value = '1*complex(0,1)*(-(Y1e11*complexconjugate(Vv21)*complexconjugate(ZER21)*complexconjugate(ZP21)) - Y1e21*complexconjugate(Vv22)*complexconjugate(ZER21)*complexconjugate(ZP21) - Y1e12*complexconjugate(Vv21)*complexconjugate(ZER22)*complexconjugate(ZP21) - Y1e22*complexconjugate(Vv22)*complexconjugate(ZER22)*complexconjugate(ZP21) - Y2e33*complexconjugate(Vv23)*complexconjugate(ZER23)*complexconjugate(ZP22))', 
	 order = {'QED':1} ) 
 
GC_654 = Coupling(name = 'GC_654',
	 value = '1*complex(0,1)*(-(ZEL31*(Vv24*complexconjugate(Y1n11) + Vv25*complexconjugate(Y1n12))*complexconjugate(ZP11)) - ZEL32*(Vv24*complexconjugate(Y1n21) + Vv25*complexconjugate(Y1n22))*complexconjugate(ZP11) - Vv26*ZEL33*complexconjugate(Y2n33)*complexconjugate(ZP12))', 
	 order = {'QED':1} ) 
 
GC_655 = Coupling(name = 'GC_655',
	 value = '1*complex(0,1)*(-(Y1e11*complexconjugate(Vv21)*complexconjugate(ZER31)*complexconjugate(ZP11)) - Y1e21*complexconjugate(Vv22)*complexconjugate(ZER31)*complexconjugate(ZP11) - Y1e12*complexconjugate(Vv21)*complexconjugate(ZER32)*complexconjugate(ZP11) - Y1e22*complexconjugate(Vv22)*complexconjugate(ZER32)*complexconjugate(ZP11) - Y2e33*complexconjugate(Vv23)*complexconjugate(ZER33)*complexconjugate(ZP12))', 
	 order = {'QED':1} ) 
 
GC_656 = Coupling(name = 'GC_656',
	 value = '1*complex(0,1)*(-(ZEL31*(Vv24*complexconjugate(Y1n11) + Vv25*complexconjugate(Y1n12))*complexconjugate(ZP21)) - ZEL32*(Vv24*complexconjugate(Y1n21) + Vv25*complexconjugate(Y1n22))*complexconjugate(ZP21) - Vv26*ZEL33*complexconjugate(Y2n33)*complexconjugate(ZP22))', 
	 order = {'QED':1} ) 
 
GC_657 = Coupling(name = 'GC_657',
	 value = '1*complex(0,1)*(-(Y1e11*complexconjugate(Vv21)*complexconjugate(ZER31)*complexconjugate(ZP21)) - Y1e21*complexconjugate(Vv22)*complexconjugate(ZER31)*complexconjugate(ZP21) - Y1e12*complexconjugate(Vv21)*complexconjugate(ZER32)*complexconjugate(ZP21) - Y1e22*complexconjugate(Vv22)*complexconjugate(ZER32)*complexconjugate(ZP21) - Y2e33*complexconjugate(Vv23)*complexconjugate(ZER33)*complexconjugate(ZP22))', 
	 order = {'QED':1} ) 
 
GC_658 = Coupling(name = 'GC_658',
	 value = '1*complex(0,1)*(-(ZEL11*(Vv34*complexconjugate(Y1n11) + Vv35*complexconjugate(Y1n12))*complexconjugate(ZP11)) - ZEL12*(Vv34*complexconjugate(Y1n21) + Vv35*complexconjugate(Y1n22))*complexconjugate(ZP11) - Vv36*ZEL13*complexconjugate(Y2n33)*complexconjugate(ZP12))', 
	 order = {'QED':1} ) 
 
GC_659 = Coupling(name = 'GC_659',
	 value = '1*complex(0,1)*(-(Y1e11*complexconjugate(Vv31)*complexconjugate(ZER11)*complexconjugate(ZP11)) - Y1e21*complexconjugate(Vv32)*complexconjugate(ZER11)*complexconjugate(ZP11) - Y1e12*complexconjugate(Vv31)*complexconjugate(ZER12)*complexconjugate(ZP11) - Y1e22*complexconjugate(Vv32)*complexconjugate(ZER12)*complexconjugate(ZP11) - Y2e33*complexconjugate(Vv33)*complexconjugate(ZER13)*complexconjugate(ZP12))', 
	 order = {'QED':1} ) 
 
GC_660 = Coupling(name = 'GC_660',
	 value = '1*complex(0,1)*(-(ZEL11*(Vv34*complexconjugate(Y1n11) + Vv35*complexconjugate(Y1n12))*complexconjugate(ZP21)) - ZEL12*(Vv34*complexconjugate(Y1n21) + Vv35*complexconjugate(Y1n22))*complexconjugate(ZP21) - Vv36*ZEL13*complexconjugate(Y2n33)*complexconjugate(ZP22))', 
	 order = {'QED':1} ) 
 
GC_661 = Coupling(name = 'GC_661',
	 value = '1*complex(0,1)*(-(Y1e11*complexconjugate(Vv31)*complexconjugate(ZER11)*complexconjugate(ZP21)) - Y1e21*complexconjugate(Vv32)*complexconjugate(ZER11)*complexconjugate(ZP21) - Y1e12*complexconjugate(Vv31)*complexconjugate(ZER12)*complexconjugate(ZP21) - Y1e22*complexconjugate(Vv32)*complexconjugate(ZER12)*complexconjugate(ZP21) - Y2e33*complexconjugate(Vv33)*complexconjugate(ZER13)*complexconjugate(ZP22))', 
	 order = {'QED':1} ) 
 
GC_662 = Coupling(name = 'GC_662',
	 value = '1*complex(0,1)*(-(ZEL21*(Vv34*complexconjugate(Y1n11) + Vv35*complexconjugate(Y1n12))*complexconjugate(ZP11)) - ZEL22*(Vv34*complexconjugate(Y1n21) + Vv35*complexconjugate(Y1n22))*complexconjugate(ZP11) - Vv36*ZEL23*complexconjugate(Y2n33)*complexconjugate(ZP12))', 
	 order = {'QED':1} ) 
 
GC_663 = Coupling(name = 'GC_663',
	 value = '1*complex(0,1)*(-(Y1e11*complexconjugate(Vv31)*complexconjugate(ZER21)*complexconjugate(ZP11)) - Y1e21*complexconjugate(Vv32)*complexconjugate(ZER21)*complexconjugate(ZP11) - Y1e12*complexconjugate(Vv31)*complexconjugate(ZER22)*complexconjugate(ZP11) - Y1e22*complexconjugate(Vv32)*complexconjugate(ZER22)*complexconjugate(ZP11) - Y2e33*complexconjugate(Vv33)*complexconjugate(ZER23)*complexconjugate(ZP12))', 
	 order = {'QED':1} ) 
 
GC_664 = Coupling(name = 'GC_664',
	 value = '1*complex(0,1)*(-(ZEL21*(Vv34*complexconjugate(Y1n11) + Vv35*complexconjugate(Y1n12))*complexconjugate(ZP21)) - ZEL22*(Vv34*complexconjugate(Y1n21) + Vv35*complexconjugate(Y1n22))*complexconjugate(ZP21) - Vv36*ZEL23*complexconjugate(Y2n33)*complexconjugate(ZP22))', 
	 order = {'QED':1} ) 
 
GC_665 = Coupling(name = 'GC_665',
	 value = '1*complex(0,1)*(-(Y1e11*complexconjugate(Vv31)*complexconjugate(ZER21)*complexconjugate(ZP21)) - Y1e21*complexconjugate(Vv32)*complexconjugate(ZER21)*complexconjugate(ZP21) - Y1e12*complexconjugate(Vv31)*complexconjugate(ZER22)*complexconjugate(ZP21) - Y1e22*complexconjugate(Vv32)*complexconjugate(ZER22)*complexconjugate(ZP21) - Y2e33*complexconjugate(Vv33)*complexconjugate(ZER23)*complexconjugate(ZP22))', 
	 order = {'QED':1} ) 
 
GC_666 = Coupling(name = 'GC_666',
	 value = '1*complex(0,1)*(-(ZEL31*(Vv34*complexconjugate(Y1n11) + Vv35*complexconjugate(Y1n12))*complexconjugate(ZP11)) - ZEL32*(Vv34*complexconjugate(Y1n21) + Vv35*complexconjugate(Y1n22))*complexconjugate(ZP11) - Vv36*ZEL33*complexconjugate(Y2n33)*complexconjugate(ZP12))', 
	 order = {'QED':1} ) 
 
GC_667 = Coupling(name = 'GC_667',
	 value = '1*complex(0,1)*(-(Y1e11*complexconjugate(Vv31)*complexconjugate(ZER31)*complexconjugate(ZP11)) - Y1e21*complexconjugate(Vv32)*complexconjugate(ZER31)*complexconjugate(ZP11) - Y1e12*complexconjugate(Vv31)*complexconjugate(ZER32)*complexconjugate(ZP11) - Y1e22*complexconjugate(Vv32)*complexconjugate(ZER32)*complexconjugate(ZP11) - Y2e33*complexconjugate(Vv33)*complexconjugate(ZER33)*complexconjugate(ZP12))', 
	 order = {'QED':1} ) 
 
GC_668 = Coupling(name = 'GC_668',
	 value = '1*complex(0,1)*(-(ZEL31*(Vv34*complexconjugate(Y1n11) + Vv35*complexconjugate(Y1n12))*complexconjugate(ZP21)) - ZEL32*(Vv34*complexconjugate(Y1n21) + Vv35*complexconjugate(Y1n22))*complexconjugate(ZP21) - Vv36*ZEL33*complexconjugate(Y2n33)*complexconjugate(ZP22))', 
	 order = {'QED':1} ) 
 
GC_669 = Coupling(name = 'GC_669',
	 value = '1*complex(0,1)*(-(Y1e11*complexconjugate(Vv31)*complexconjugate(ZER31)*complexconjugate(ZP21)) - Y1e21*complexconjugate(Vv32)*complexconjugate(ZER31)*complexconjugate(ZP21) - Y1e12*complexconjugate(Vv31)*complexconjugate(ZER32)*complexconjugate(ZP21) - Y1e22*complexconjugate(Vv32)*complexconjugate(ZER32)*complexconjugate(ZP21) - Y2e33*complexconjugate(Vv33)*complexconjugate(ZER33)*complexconjugate(ZP22))', 
	 order = {'QED':1} ) 
 
GC_670 = Coupling(name = 'GC_670',
	 value = '1*complex(0,1)*(-(ZEL11*(Vv44*complexconjugate(Y1n11) + Vv45*complexconjugate(Y1n12))*complexconjugate(ZP11)) - ZEL12*(Vv44*complexconjugate(Y1n21) + Vv45*complexconjugate(Y1n22))*complexconjugate(ZP11) - Vv46*ZEL13*complexconjugate(Y2n33)*complexconjugate(ZP12))', 
	 order = {'QED':1} ) 
 
GC_671 = Coupling(name = 'GC_671',
	 value = '1*complex(0,1)*(-(Y1e11*complexconjugate(Vv41)*complexconjugate(ZER11)*complexconjugate(ZP11)) - Y1e21*complexconjugate(Vv42)*complexconjugate(ZER11)*complexconjugate(ZP11) - Y1e12*complexconjugate(Vv41)*complexconjugate(ZER12)*complexconjugate(ZP11) - Y1e22*complexconjugate(Vv42)*complexconjugate(ZER12)*complexconjugate(ZP11) - Y2e33*complexconjugate(Vv43)*complexconjugate(ZER13)*complexconjugate(ZP12))', 
	 order = {'QED':1} ) 
 
GC_672 = Coupling(name = 'GC_672',
	 value = '1*complex(0,1)*(-(ZEL11*(Vv44*complexconjugate(Y1n11) + Vv45*complexconjugate(Y1n12))*complexconjugate(ZP21)) - ZEL12*(Vv44*complexconjugate(Y1n21) + Vv45*complexconjugate(Y1n22))*complexconjugate(ZP21) - Vv46*ZEL13*complexconjugate(Y2n33)*complexconjugate(ZP22))', 
	 order = {'QED':1} ) 
 
GC_673 = Coupling(name = 'GC_673',
	 value = '1*complex(0,1)*(-(Y1e11*complexconjugate(Vv41)*complexconjugate(ZER11)*complexconjugate(ZP21)) - Y1e21*complexconjugate(Vv42)*complexconjugate(ZER11)*complexconjugate(ZP21) - Y1e12*complexconjugate(Vv41)*complexconjugate(ZER12)*complexconjugate(ZP21) - Y1e22*complexconjugate(Vv42)*complexconjugate(ZER12)*complexconjugate(ZP21) - Y2e33*complexconjugate(Vv43)*complexconjugate(ZER13)*complexconjugate(ZP22))', 
	 order = {'QED':1} ) 
 
GC_674 = Coupling(name = 'GC_674',
	 value = '1*complex(0,1)*(-(ZEL21*(Vv44*complexconjugate(Y1n11) + Vv45*complexconjugate(Y1n12))*complexconjugate(ZP11)) - ZEL22*(Vv44*complexconjugate(Y1n21) + Vv45*complexconjugate(Y1n22))*complexconjugate(ZP11) - Vv46*ZEL23*complexconjugate(Y2n33)*complexconjugate(ZP12))', 
	 order = {'QED':1} ) 
 
GC_675 = Coupling(name = 'GC_675',
	 value = '1*complex(0,1)*(-(Y1e11*complexconjugate(Vv41)*complexconjugate(ZER21)*complexconjugate(ZP11)) - Y1e21*complexconjugate(Vv42)*complexconjugate(ZER21)*complexconjugate(ZP11) - Y1e12*complexconjugate(Vv41)*complexconjugate(ZER22)*complexconjugate(ZP11) - Y1e22*complexconjugate(Vv42)*complexconjugate(ZER22)*complexconjugate(ZP11) - Y2e33*complexconjugate(Vv43)*complexconjugate(ZER23)*complexconjugate(ZP12))', 
	 order = {'QED':1} ) 
 
GC_676 = Coupling(name = 'GC_676',
	 value = '1*complex(0,1)*(-(ZEL21*(Vv44*complexconjugate(Y1n11) + Vv45*complexconjugate(Y1n12))*complexconjugate(ZP21)) - ZEL22*(Vv44*complexconjugate(Y1n21) + Vv45*complexconjugate(Y1n22))*complexconjugate(ZP21) - Vv46*ZEL23*complexconjugate(Y2n33)*complexconjugate(ZP22))', 
	 order = {'QED':1} ) 
 
GC_677 = Coupling(name = 'GC_677',
	 value = '1*complex(0,1)*(-(Y1e11*complexconjugate(Vv41)*complexconjugate(ZER21)*complexconjugate(ZP21)) - Y1e21*complexconjugate(Vv42)*complexconjugate(ZER21)*complexconjugate(ZP21) - Y1e12*complexconjugate(Vv41)*complexconjugate(ZER22)*complexconjugate(ZP21) - Y1e22*complexconjugate(Vv42)*complexconjugate(ZER22)*complexconjugate(ZP21) - Y2e33*complexconjugate(Vv43)*complexconjugate(ZER23)*complexconjugate(ZP22))', 
	 order = {'QED':1} ) 
 
GC_678 = Coupling(name = 'GC_678',
	 value = '1*complex(0,1)*(-(ZEL31*(Vv44*complexconjugate(Y1n11) + Vv45*complexconjugate(Y1n12))*complexconjugate(ZP11)) - ZEL32*(Vv44*complexconjugate(Y1n21) + Vv45*complexconjugate(Y1n22))*complexconjugate(ZP11) - Vv46*ZEL33*complexconjugate(Y2n33)*complexconjugate(ZP12))', 
	 order = {'QED':1} ) 
 
GC_679 = Coupling(name = 'GC_679',
	 value = '1*complex(0,1)*(-(Y1e11*complexconjugate(Vv41)*complexconjugate(ZER31)*complexconjugate(ZP11)) - Y1e21*complexconjugate(Vv42)*complexconjugate(ZER31)*complexconjugate(ZP11) - Y1e12*complexconjugate(Vv41)*complexconjugate(ZER32)*complexconjugate(ZP11) - Y1e22*complexconjugate(Vv42)*complexconjugate(ZER32)*complexconjugate(ZP11) - Y2e33*complexconjugate(Vv43)*complexconjugate(ZER33)*complexconjugate(ZP12))', 
	 order = {'QED':1} ) 
 
GC_680 = Coupling(name = 'GC_680',
	 value = '1*complex(0,1)*(-(ZEL31*(Vv44*complexconjugate(Y1n11) + Vv45*complexconjugate(Y1n12))*complexconjugate(ZP21)) - ZEL32*(Vv44*complexconjugate(Y1n21) + Vv45*complexconjugate(Y1n22))*complexconjugate(ZP21) - Vv46*ZEL33*complexconjugate(Y2n33)*complexconjugate(ZP22))', 
	 order = {'QED':1} ) 
 
GC_681 = Coupling(name = 'GC_681',
	 value = '1*complex(0,1)*(-(Y1e11*complexconjugate(Vv41)*complexconjugate(ZER31)*complexconjugate(ZP21)) - Y1e21*complexconjugate(Vv42)*complexconjugate(ZER31)*complexconjugate(ZP21) - Y1e12*complexconjugate(Vv41)*complexconjugate(ZER32)*complexconjugate(ZP21) - Y1e22*complexconjugate(Vv42)*complexconjugate(ZER32)*complexconjugate(ZP21) - Y2e33*complexconjugate(Vv43)*complexconjugate(ZER33)*complexconjugate(ZP22))', 
	 order = {'QED':1} ) 
 
GC_682 = Coupling(name = 'GC_682',
	 value = '1*complex(0,1)*(-(ZEL11*(Vv54*complexconjugate(Y1n11) + Vv55*complexconjugate(Y1n12))*complexconjugate(ZP11)) - ZEL12*(Vv54*complexconjugate(Y1n21) + Vv55*complexconjugate(Y1n22))*complexconjugate(ZP11) - Vv56*ZEL13*complexconjugate(Y2n33)*complexconjugate(ZP12))', 
	 order = {'QED':1} ) 
 
GC_683 = Coupling(name = 'GC_683',
	 value = '1*complex(0,1)*(-(Y1e11*complexconjugate(Vv51)*complexconjugate(ZER11)*complexconjugate(ZP11)) - Y1e21*complexconjugate(Vv52)*complexconjugate(ZER11)*complexconjugate(ZP11) - Y1e12*complexconjugate(Vv51)*complexconjugate(ZER12)*complexconjugate(ZP11) - Y1e22*complexconjugate(Vv52)*complexconjugate(ZER12)*complexconjugate(ZP11) - Y2e33*complexconjugate(Vv53)*complexconjugate(ZER13)*complexconjugate(ZP12))', 
	 order = {'QED':1} ) 
 
GC_684 = Coupling(name = 'GC_684',
	 value = '1*complex(0,1)*(-(ZEL11*(Vv54*complexconjugate(Y1n11) + Vv55*complexconjugate(Y1n12))*complexconjugate(ZP21)) - ZEL12*(Vv54*complexconjugate(Y1n21) + Vv55*complexconjugate(Y1n22))*complexconjugate(ZP21) - Vv56*ZEL13*complexconjugate(Y2n33)*complexconjugate(ZP22))', 
	 order = {'QED':1} ) 
 
GC_685 = Coupling(name = 'GC_685',
	 value = '1*complex(0,1)*(-(Y1e11*complexconjugate(Vv51)*complexconjugate(ZER11)*complexconjugate(ZP21)) - Y1e21*complexconjugate(Vv52)*complexconjugate(ZER11)*complexconjugate(ZP21) - Y1e12*complexconjugate(Vv51)*complexconjugate(ZER12)*complexconjugate(ZP21) - Y1e22*complexconjugate(Vv52)*complexconjugate(ZER12)*complexconjugate(ZP21) - Y2e33*complexconjugate(Vv53)*complexconjugate(ZER13)*complexconjugate(ZP22))', 
	 order = {'QED':1} ) 
 
GC_686 = Coupling(name = 'GC_686',
	 value = '1*complex(0,1)*(-(ZEL21*(Vv54*complexconjugate(Y1n11) + Vv55*complexconjugate(Y1n12))*complexconjugate(ZP11)) - ZEL22*(Vv54*complexconjugate(Y1n21) + Vv55*complexconjugate(Y1n22))*complexconjugate(ZP11) - Vv56*ZEL23*complexconjugate(Y2n33)*complexconjugate(ZP12))', 
	 order = {'QED':1} ) 
 
GC_687 = Coupling(name = 'GC_687',
	 value = '1*complex(0,1)*(-(Y1e11*complexconjugate(Vv51)*complexconjugate(ZER21)*complexconjugate(ZP11)) - Y1e21*complexconjugate(Vv52)*complexconjugate(ZER21)*complexconjugate(ZP11) - Y1e12*complexconjugate(Vv51)*complexconjugate(ZER22)*complexconjugate(ZP11) - Y1e22*complexconjugate(Vv52)*complexconjugate(ZER22)*complexconjugate(ZP11) - Y2e33*complexconjugate(Vv53)*complexconjugate(ZER23)*complexconjugate(ZP12))', 
	 order = {'QED':1} ) 
 
GC_688 = Coupling(name = 'GC_688',
	 value = '1*complex(0,1)*(-(ZEL21*(Vv54*complexconjugate(Y1n11) + Vv55*complexconjugate(Y1n12))*complexconjugate(ZP21)) - ZEL22*(Vv54*complexconjugate(Y1n21) + Vv55*complexconjugate(Y1n22))*complexconjugate(ZP21) - Vv56*ZEL23*complexconjugate(Y2n33)*complexconjugate(ZP22))', 
	 order = {'QED':1} ) 
 
GC_689 = Coupling(name = 'GC_689',
	 value = '1*complex(0,1)*(-(Y1e11*complexconjugate(Vv51)*complexconjugate(ZER21)*complexconjugate(ZP21)) - Y1e21*complexconjugate(Vv52)*complexconjugate(ZER21)*complexconjugate(ZP21) - Y1e12*complexconjugate(Vv51)*complexconjugate(ZER22)*complexconjugate(ZP21) - Y1e22*complexconjugate(Vv52)*complexconjugate(ZER22)*complexconjugate(ZP21) - Y2e33*complexconjugate(Vv53)*complexconjugate(ZER23)*complexconjugate(ZP22))', 
	 order = {'QED':1} ) 
 
GC_690 = Coupling(name = 'GC_690',
	 value = '1*complex(0,1)*(-(ZEL31*(Vv54*complexconjugate(Y1n11) + Vv55*complexconjugate(Y1n12))*complexconjugate(ZP11)) - ZEL32*(Vv54*complexconjugate(Y1n21) + Vv55*complexconjugate(Y1n22))*complexconjugate(ZP11) - Vv56*ZEL33*complexconjugate(Y2n33)*complexconjugate(ZP12))', 
	 order = {'QED':1} ) 
 
GC_691 = Coupling(name = 'GC_691',
	 value = '1*complex(0,1)*(-(Y1e11*complexconjugate(Vv51)*complexconjugate(ZER31)*complexconjugate(ZP11)) - Y1e21*complexconjugate(Vv52)*complexconjugate(ZER31)*complexconjugate(ZP11) - Y1e12*complexconjugate(Vv51)*complexconjugate(ZER32)*complexconjugate(ZP11) - Y1e22*complexconjugate(Vv52)*complexconjugate(ZER32)*complexconjugate(ZP11) - Y2e33*complexconjugate(Vv53)*complexconjugate(ZER33)*complexconjugate(ZP12))', 
	 order = {'QED':1} ) 
 
GC_692 = Coupling(name = 'GC_692',
	 value = '1*complex(0,1)*(-(ZEL31*(Vv54*complexconjugate(Y1n11) + Vv55*complexconjugate(Y1n12))*complexconjugate(ZP21)) - ZEL32*(Vv54*complexconjugate(Y1n21) + Vv55*complexconjugate(Y1n22))*complexconjugate(ZP21) - Vv56*ZEL33*complexconjugate(Y2n33)*complexconjugate(ZP22))', 
	 order = {'QED':1} ) 
 
GC_693 = Coupling(name = 'GC_693',
	 value = '1*complex(0,1)*(-(Y1e11*complexconjugate(Vv51)*complexconjugate(ZER31)*complexconjugate(ZP21)) - Y1e21*complexconjugate(Vv52)*complexconjugate(ZER31)*complexconjugate(ZP21) - Y1e12*complexconjugate(Vv51)*complexconjugate(ZER32)*complexconjugate(ZP21) - Y1e22*complexconjugate(Vv52)*complexconjugate(ZER32)*complexconjugate(ZP21) - Y2e33*complexconjugate(Vv53)*complexconjugate(ZER33)*complexconjugate(ZP22))', 
	 order = {'QED':1} ) 
 
GC_694 = Coupling(name = 'GC_694',
	 value = '1*complex(0,1)*(-(ZEL11*(Vv64*complexconjugate(Y1n11) + Vv65*complexconjugate(Y1n12))*complexconjugate(ZP11)) - ZEL12*(Vv64*complexconjugate(Y1n21) + Vv65*complexconjugate(Y1n22))*complexconjugate(ZP11) - Vv66*ZEL13*complexconjugate(Y2n33)*complexconjugate(ZP12))', 
	 order = {'QED':1} ) 
 
GC_695 = Coupling(name = 'GC_695',
	 value = '1*complex(0,1)*(-(Y1e11*complexconjugate(Vv61)*complexconjugate(ZER11)*complexconjugate(ZP11)) - Y1e21*complexconjugate(Vv62)*complexconjugate(ZER11)*complexconjugate(ZP11) - Y1e12*complexconjugate(Vv61)*complexconjugate(ZER12)*complexconjugate(ZP11) - Y1e22*complexconjugate(Vv62)*complexconjugate(ZER12)*complexconjugate(ZP11) - Y2e33*complexconjugate(Vv63)*complexconjugate(ZER13)*complexconjugate(ZP12))', 
	 order = {'QED':1} ) 
 
GC_696 = Coupling(name = 'GC_696',
	 value = '1*complex(0,1)*(-(ZEL11*(Vv64*complexconjugate(Y1n11) + Vv65*complexconjugate(Y1n12))*complexconjugate(ZP21)) - ZEL12*(Vv64*complexconjugate(Y1n21) + Vv65*complexconjugate(Y1n22))*complexconjugate(ZP21) - Vv66*ZEL13*complexconjugate(Y2n33)*complexconjugate(ZP22))', 
	 order = {'QED':1} ) 
 
GC_697 = Coupling(name = 'GC_697',
	 value = '1*complex(0,1)*(-(Y1e11*complexconjugate(Vv61)*complexconjugate(ZER11)*complexconjugate(ZP21)) - Y1e21*complexconjugate(Vv62)*complexconjugate(ZER11)*complexconjugate(ZP21) - Y1e12*complexconjugate(Vv61)*complexconjugate(ZER12)*complexconjugate(ZP21) - Y1e22*complexconjugate(Vv62)*complexconjugate(ZER12)*complexconjugate(ZP21) - Y2e33*complexconjugate(Vv63)*complexconjugate(ZER13)*complexconjugate(ZP22))', 
	 order = {'QED':1} ) 
 
GC_698 = Coupling(name = 'GC_698',
	 value = '1*complex(0,1)*(-(ZEL21*(Vv64*complexconjugate(Y1n11) + Vv65*complexconjugate(Y1n12))*complexconjugate(ZP11)) - ZEL22*(Vv64*complexconjugate(Y1n21) + Vv65*complexconjugate(Y1n22))*complexconjugate(ZP11) - Vv66*ZEL23*complexconjugate(Y2n33)*complexconjugate(ZP12))', 
	 order = {'QED':1} ) 
 
GC_699 = Coupling(name = 'GC_699',
	 value = '1*complex(0,1)*(-(Y1e11*complexconjugate(Vv61)*complexconjugate(ZER21)*complexconjugate(ZP11)) - Y1e21*complexconjugate(Vv62)*complexconjugate(ZER21)*complexconjugate(ZP11) - Y1e12*complexconjugate(Vv61)*complexconjugate(ZER22)*complexconjugate(ZP11) - Y1e22*complexconjugate(Vv62)*complexconjugate(ZER22)*complexconjugate(ZP11) - Y2e33*complexconjugate(Vv63)*complexconjugate(ZER23)*complexconjugate(ZP12))', 
	 order = {'QED':1} ) 
 
GC_700 = Coupling(name = 'GC_700',
	 value = '1*complex(0,1)*(-(ZEL21*(Vv64*complexconjugate(Y1n11) + Vv65*complexconjugate(Y1n12))*complexconjugate(ZP21)) - ZEL22*(Vv64*complexconjugate(Y1n21) + Vv65*complexconjugate(Y1n22))*complexconjugate(ZP21) - Vv66*ZEL23*complexconjugate(Y2n33)*complexconjugate(ZP22))', 
	 order = {'QED':1} ) 
 
GC_701 = Coupling(name = 'GC_701',
	 value = '1*complex(0,1)*(-(Y1e11*complexconjugate(Vv61)*complexconjugate(ZER21)*complexconjugate(ZP21)) - Y1e21*complexconjugate(Vv62)*complexconjugate(ZER21)*complexconjugate(ZP21) - Y1e12*complexconjugate(Vv61)*complexconjugate(ZER22)*complexconjugate(ZP21) - Y1e22*complexconjugate(Vv62)*complexconjugate(ZER22)*complexconjugate(ZP21) - Y2e33*complexconjugate(Vv63)*complexconjugate(ZER23)*complexconjugate(ZP22))', 
	 order = {'QED':1} ) 
 
GC_702 = Coupling(name = 'GC_702',
	 value = '1*complex(0,1)*(-(ZEL31*(Vv64*complexconjugate(Y1n11) + Vv65*complexconjugate(Y1n12))*complexconjugate(ZP11)) - ZEL32*(Vv64*complexconjugate(Y1n21) + Vv65*complexconjugate(Y1n22))*complexconjugate(ZP11) - Vv66*ZEL33*complexconjugate(Y2n33)*complexconjugate(ZP12))', 
	 order = {'QED':1} ) 
 
GC_703 = Coupling(name = 'GC_703',
	 value = '1*complex(0,1)*(-(Y1e11*complexconjugate(Vv61)*complexconjugate(ZER31)*complexconjugate(ZP11)) - Y1e21*complexconjugate(Vv62)*complexconjugate(ZER31)*complexconjugate(ZP11) - Y1e12*complexconjugate(Vv61)*complexconjugate(ZER32)*complexconjugate(ZP11) - Y1e22*complexconjugate(Vv62)*complexconjugate(ZER32)*complexconjugate(ZP11) - Y2e33*complexconjugate(Vv63)*complexconjugate(ZER33)*complexconjugate(ZP12))', 
	 order = {'QED':1} ) 
 
GC_704 = Coupling(name = 'GC_704',
	 value = '1*complex(0,1)*(-(ZEL31*(Vv64*complexconjugate(Y1n11) + Vv65*complexconjugate(Y1n12))*complexconjugate(ZP21)) - ZEL32*(Vv64*complexconjugate(Y1n21) + Vv65*complexconjugate(Y1n22))*complexconjugate(ZP21) - Vv66*ZEL33*complexconjugate(Y2n33)*complexconjugate(ZP22))', 
	 order = {'QED':1} ) 
 
GC_705 = Coupling(name = 'GC_705',
	 value = '1*complex(0,1)*(-(Y1e11*complexconjugate(Vv61)*complexconjugate(ZER31)*complexconjugate(ZP21)) - Y1e21*complexconjugate(Vv62)*complexconjugate(ZER31)*complexconjugate(ZP21) - Y1e12*complexconjugate(Vv61)*complexconjugate(ZER32)*complexconjugate(ZP21) - Y1e22*complexconjugate(Vv62)*complexconjugate(ZER32)*complexconjugate(ZP21) - Y2e33*complexconjugate(Vv63)*complexconjugate(ZER33)*complexconjugate(ZP22))', 
	 order = {'QED':1} ) 
 
GC_706 = Coupling(name = 'GC_706',
	 value = '(-1*complex(0,1)*(ZER11*ZH11*(ZEL11*complexconjugate(Y1e11) + ZEL12*complexconjugate(Y1e21)) + ZER12*ZH11*(ZEL11*complexconjugate(Y1e12) + ZEL12*complexconjugate(Y1e22)) + ZEL13*ZER13*ZH12*complexconjugate(Y2e33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_707 = Coupling(name = 'GC_707',
	 value = '(-1*complex(0,1)*(Y1e11*ZH11*complexconjugate(ZEL11)*complexconjugate(ZER11) + Y1e21*ZH11*complexconjugate(ZEL12)*complexconjugate(ZER11) + Y1e12*ZH11*complexconjugate(ZEL11)*complexconjugate(ZER12) + Y1e22*ZH11*complexconjugate(ZEL12)*complexconjugate(ZER12) + Y2e33*ZH12*complexconjugate(ZEL13)*complexconjugate(ZER13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_708 = Coupling(name = 'GC_708',
	 value = '(-1*complex(0,1)*(ZER11*ZH21*(ZEL11*complexconjugate(Y1e11) + ZEL12*complexconjugate(Y1e21)) + ZER12*ZH21*(ZEL11*complexconjugate(Y1e12) + ZEL12*complexconjugate(Y1e22)) + ZEL13*ZER13*ZH22*complexconjugate(Y2e33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_709 = Coupling(name = 'GC_709',
	 value = '(-1*complex(0,1)*(Y1e11*ZH21*complexconjugate(ZEL11)*complexconjugate(ZER11) + Y1e21*ZH21*complexconjugate(ZEL12)*complexconjugate(ZER11) + Y1e12*ZH21*complexconjugate(ZEL11)*complexconjugate(ZER12) + Y1e22*ZH21*complexconjugate(ZEL12)*complexconjugate(ZER12) + Y2e33*ZH22*complexconjugate(ZEL13)*complexconjugate(ZER13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_710 = Coupling(name = 'GC_710',
	 value = '(-1*complex(0,1)*(ZER11*ZH31*(ZEL11*complexconjugate(Y1e11) + ZEL12*complexconjugate(Y1e21)) + ZER12*ZH31*(ZEL11*complexconjugate(Y1e12) + ZEL12*complexconjugate(Y1e22)) + ZEL13*ZER13*ZH32*complexconjugate(Y2e33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_711 = Coupling(name = 'GC_711',
	 value = '(-1*complex(0,1)*(Y1e11*ZH31*complexconjugate(ZEL11)*complexconjugate(ZER11) + Y1e21*ZH31*complexconjugate(ZEL12)*complexconjugate(ZER11) + Y1e12*ZH31*complexconjugate(ZEL11)*complexconjugate(ZER12) + Y1e22*ZH31*complexconjugate(ZEL12)*complexconjugate(ZER12) + Y2e33*ZH32*complexconjugate(ZEL13)*complexconjugate(ZER13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_712 = Coupling(name = 'GC_712',
	 value = '(-1*complex(0,1)*(ZER11*ZH11*(ZEL21*complexconjugate(Y1e11) + ZEL22*complexconjugate(Y1e21)) + ZER12*ZH11*(ZEL21*complexconjugate(Y1e12) + ZEL22*complexconjugate(Y1e22)) + ZEL23*ZER13*ZH12*complexconjugate(Y2e33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_713 = Coupling(name = 'GC_713',
	 value = '(-1*complex(0,1)*(Y1e11*ZH11*complexconjugate(ZEL11)*complexconjugate(ZER21) + Y1e21*ZH11*complexconjugate(ZEL12)*complexconjugate(ZER21) + Y1e12*ZH11*complexconjugate(ZEL11)*complexconjugate(ZER22) + Y1e22*ZH11*complexconjugate(ZEL12)*complexconjugate(ZER22) + Y2e33*ZH12*complexconjugate(ZEL13)*complexconjugate(ZER23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_714 = Coupling(name = 'GC_714',
	 value = '(-1*complex(0,1)*(ZER11*ZH21*(ZEL21*complexconjugate(Y1e11) + ZEL22*complexconjugate(Y1e21)) + ZER12*ZH21*(ZEL21*complexconjugate(Y1e12) + ZEL22*complexconjugate(Y1e22)) + ZEL23*ZER13*ZH22*complexconjugate(Y2e33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_715 = Coupling(name = 'GC_715',
	 value = '(-1*complex(0,1)*(Y1e11*ZH21*complexconjugate(ZEL11)*complexconjugate(ZER21) + Y1e21*ZH21*complexconjugate(ZEL12)*complexconjugate(ZER21) + Y1e12*ZH21*complexconjugate(ZEL11)*complexconjugate(ZER22) + Y1e22*ZH21*complexconjugate(ZEL12)*complexconjugate(ZER22) + Y2e33*ZH22*complexconjugate(ZEL13)*complexconjugate(ZER23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_716 = Coupling(name = 'GC_716',
	 value = '(-1*complex(0,1)*(ZER11*ZH31*(ZEL21*complexconjugate(Y1e11) + ZEL22*complexconjugate(Y1e21)) + ZER12*ZH31*(ZEL21*complexconjugate(Y1e12) + ZEL22*complexconjugate(Y1e22)) + ZEL23*ZER13*ZH32*complexconjugate(Y2e33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_717 = Coupling(name = 'GC_717',
	 value = '(-1*complex(0,1)*(Y1e11*ZH31*complexconjugate(ZEL11)*complexconjugate(ZER21) + Y1e21*ZH31*complexconjugate(ZEL12)*complexconjugate(ZER21) + Y1e12*ZH31*complexconjugate(ZEL11)*complexconjugate(ZER22) + Y1e22*ZH31*complexconjugate(ZEL12)*complexconjugate(ZER22) + Y2e33*ZH32*complexconjugate(ZEL13)*complexconjugate(ZER23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_718 = Coupling(name = 'GC_718',
	 value = '(-1*complex(0,1)*(ZER11*ZH11*(ZEL31*complexconjugate(Y1e11) + ZEL32*complexconjugate(Y1e21)) + ZER12*ZH11*(ZEL31*complexconjugate(Y1e12) + ZEL32*complexconjugate(Y1e22)) + ZEL33*ZER13*ZH12*complexconjugate(Y2e33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_719 = Coupling(name = 'GC_719',
	 value = '(-1*complex(0,1)*(Y1e11*ZH11*complexconjugate(ZEL11)*complexconjugate(ZER31) + Y1e21*ZH11*complexconjugate(ZEL12)*complexconjugate(ZER31) + Y1e12*ZH11*complexconjugate(ZEL11)*complexconjugate(ZER32) + Y1e22*ZH11*complexconjugate(ZEL12)*complexconjugate(ZER32) + Y2e33*ZH12*complexconjugate(ZEL13)*complexconjugate(ZER33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_720 = Coupling(name = 'GC_720',
	 value = '(-1*complex(0,1)*(ZER11*ZH21*(ZEL31*complexconjugate(Y1e11) + ZEL32*complexconjugate(Y1e21)) + ZER12*ZH21*(ZEL31*complexconjugate(Y1e12) + ZEL32*complexconjugate(Y1e22)) + ZEL33*ZER13*ZH22*complexconjugate(Y2e33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_721 = Coupling(name = 'GC_721',
	 value = '(-1*complex(0,1)*(Y1e11*ZH21*complexconjugate(ZEL11)*complexconjugate(ZER31) + Y1e21*ZH21*complexconjugate(ZEL12)*complexconjugate(ZER31) + Y1e12*ZH21*complexconjugate(ZEL11)*complexconjugate(ZER32) + Y1e22*ZH21*complexconjugate(ZEL12)*complexconjugate(ZER32) + Y2e33*ZH22*complexconjugate(ZEL13)*complexconjugate(ZER33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_722 = Coupling(name = 'GC_722',
	 value = '(-1*complex(0,1)*(ZER11*ZH31*(ZEL31*complexconjugate(Y1e11) + ZEL32*complexconjugate(Y1e21)) + ZER12*ZH31*(ZEL31*complexconjugate(Y1e12) + ZEL32*complexconjugate(Y1e22)) + ZEL33*ZER13*ZH32*complexconjugate(Y2e33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_723 = Coupling(name = 'GC_723',
	 value = '(-1*complex(0,1)*(Y1e11*ZH31*complexconjugate(ZEL11)*complexconjugate(ZER31) + Y1e21*ZH31*complexconjugate(ZEL12)*complexconjugate(ZER31) + Y1e12*ZH31*complexconjugate(ZEL11)*complexconjugate(ZER32) + Y1e22*ZH31*complexconjugate(ZEL12)*complexconjugate(ZER32) + Y2e33*ZH32*complexconjugate(ZEL13)*complexconjugate(ZER33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_724 = Coupling(name = 'GC_724',
	 value = '(-1*complex(0,1)*(ZER21*ZH11*(ZEL11*complexconjugate(Y1e11) + ZEL12*complexconjugate(Y1e21)) + ZER22*ZH11*(ZEL11*complexconjugate(Y1e12) + ZEL12*complexconjugate(Y1e22)) + ZEL13*ZER23*ZH12*complexconjugate(Y2e33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_725 = Coupling(name = 'GC_725',
	 value = '(-1*complex(0,1)*(Y1e11*ZH11*complexconjugate(ZEL21)*complexconjugate(ZER11) + Y1e21*ZH11*complexconjugate(ZEL22)*complexconjugate(ZER11) + Y1e12*ZH11*complexconjugate(ZEL21)*complexconjugate(ZER12) + Y1e22*ZH11*complexconjugate(ZEL22)*complexconjugate(ZER12) + Y2e33*ZH12*complexconjugate(ZEL23)*complexconjugate(ZER13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_726 = Coupling(name = 'GC_726',
	 value = '(-1*complex(0,1)*(ZER21*ZH21*(ZEL11*complexconjugate(Y1e11) + ZEL12*complexconjugate(Y1e21)) + ZER22*ZH21*(ZEL11*complexconjugate(Y1e12) + ZEL12*complexconjugate(Y1e22)) + ZEL13*ZER23*ZH22*complexconjugate(Y2e33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_727 = Coupling(name = 'GC_727',
	 value = '(-1*complex(0,1)*(Y1e11*ZH21*complexconjugate(ZEL21)*complexconjugate(ZER11) + Y1e21*ZH21*complexconjugate(ZEL22)*complexconjugate(ZER11) + Y1e12*ZH21*complexconjugate(ZEL21)*complexconjugate(ZER12) + Y1e22*ZH21*complexconjugate(ZEL22)*complexconjugate(ZER12) + Y2e33*ZH22*complexconjugate(ZEL23)*complexconjugate(ZER13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_728 = Coupling(name = 'GC_728',
	 value = '(-1*complex(0,1)*(ZER21*ZH31*(ZEL11*complexconjugate(Y1e11) + ZEL12*complexconjugate(Y1e21)) + ZER22*ZH31*(ZEL11*complexconjugate(Y1e12) + ZEL12*complexconjugate(Y1e22)) + ZEL13*ZER23*ZH32*complexconjugate(Y2e33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_729 = Coupling(name = 'GC_729',
	 value = '(-1*complex(0,1)*(Y1e11*ZH31*complexconjugate(ZEL21)*complexconjugate(ZER11) + Y1e21*ZH31*complexconjugate(ZEL22)*complexconjugate(ZER11) + Y1e12*ZH31*complexconjugate(ZEL21)*complexconjugate(ZER12) + Y1e22*ZH31*complexconjugate(ZEL22)*complexconjugate(ZER12) + Y2e33*ZH32*complexconjugate(ZEL23)*complexconjugate(ZER13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_730 = Coupling(name = 'GC_730',
	 value = '(-1*complex(0,1)*(ZER21*ZH11*(ZEL21*complexconjugate(Y1e11) + ZEL22*complexconjugate(Y1e21)) + ZER22*ZH11*(ZEL21*complexconjugate(Y1e12) + ZEL22*complexconjugate(Y1e22)) + ZEL23*ZER23*ZH12*complexconjugate(Y2e33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_731 = Coupling(name = 'GC_731',
	 value = '(-1*complex(0,1)*(Y1e11*ZH11*complexconjugate(ZEL21)*complexconjugate(ZER21) + Y1e21*ZH11*complexconjugate(ZEL22)*complexconjugate(ZER21) + Y1e12*ZH11*complexconjugate(ZEL21)*complexconjugate(ZER22) + Y1e22*ZH11*complexconjugate(ZEL22)*complexconjugate(ZER22) + Y2e33*ZH12*complexconjugate(ZEL23)*complexconjugate(ZER23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_732 = Coupling(name = 'GC_732',
	 value = '(-1*complex(0,1)*(ZER21*ZH21*(ZEL21*complexconjugate(Y1e11) + ZEL22*complexconjugate(Y1e21)) + ZER22*ZH21*(ZEL21*complexconjugate(Y1e12) + ZEL22*complexconjugate(Y1e22)) + ZEL23*ZER23*ZH22*complexconjugate(Y2e33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_733 = Coupling(name = 'GC_733',
	 value = '(-1*complex(0,1)*(Y1e11*ZH21*complexconjugate(ZEL21)*complexconjugate(ZER21) + Y1e21*ZH21*complexconjugate(ZEL22)*complexconjugate(ZER21) + Y1e12*ZH21*complexconjugate(ZEL21)*complexconjugate(ZER22) + Y1e22*ZH21*complexconjugate(ZEL22)*complexconjugate(ZER22) + Y2e33*ZH22*complexconjugate(ZEL23)*complexconjugate(ZER23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_734 = Coupling(name = 'GC_734',
	 value = '(-1*complex(0,1)*(ZER21*ZH31*(ZEL21*complexconjugate(Y1e11) + ZEL22*complexconjugate(Y1e21)) + ZER22*ZH31*(ZEL21*complexconjugate(Y1e12) + ZEL22*complexconjugate(Y1e22)) + ZEL23*ZER23*ZH32*complexconjugate(Y2e33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_735 = Coupling(name = 'GC_735',
	 value = '(-1*complex(0,1)*(Y1e11*ZH31*complexconjugate(ZEL21)*complexconjugate(ZER21) + Y1e21*ZH31*complexconjugate(ZEL22)*complexconjugate(ZER21) + Y1e12*ZH31*complexconjugate(ZEL21)*complexconjugate(ZER22) + Y1e22*ZH31*complexconjugate(ZEL22)*complexconjugate(ZER22) + Y2e33*ZH32*complexconjugate(ZEL23)*complexconjugate(ZER23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_736 = Coupling(name = 'GC_736',
	 value = '(-1*complex(0,1)*(ZER21*ZH11*(ZEL31*complexconjugate(Y1e11) + ZEL32*complexconjugate(Y1e21)) + ZER22*ZH11*(ZEL31*complexconjugate(Y1e12) + ZEL32*complexconjugate(Y1e22)) + ZEL33*ZER23*ZH12*complexconjugate(Y2e33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_737 = Coupling(name = 'GC_737',
	 value = '(-1*complex(0,1)*(Y1e11*ZH11*complexconjugate(ZEL21)*complexconjugate(ZER31) + Y1e21*ZH11*complexconjugate(ZEL22)*complexconjugate(ZER31) + Y1e12*ZH11*complexconjugate(ZEL21)*complexconjugate(ZER32) + Y1e22*ZH11*complexconjugate(ZEL22)*complexconjugate(ZER32) + Y2e33*ZH12*complexconjugate(ZEL23)*complexconjugate(ZER33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_738 = Coupling(name = 'GC_738',
	 value = '(-1*complex(0,1)*(ZER21*ZH21*(ZEL31*complexconjugate(Y1e11) + ZEL32*complexconjugate(Y1e21)) + ZER22*ZH21*(ZEL31*complexconjugate(Y1e12) + ZEL32*complexconjugate(Y1e22)) + ZEL33*ZER23*ZH22*complexconjugate(Y2e33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_739 = Coupling(name = 'GC_739',
	 value = '(-1*complex(0,1)*(Y1e11*ZH21*complexconjugate(ZEL21)*complexconjugate(ZER31) + Y1e21*ZH21*complexconjugate(ZEL22)*complexconjugate(ZER31) + Y1e12*ZH21*complexconjugate(ZEL21)*complexconjugate(ZER32) + Y1e22*ZH21*complexconjugate(ZEL22)*complexconjugate(ZER32) + Y2e33*ZH22*complexconjugate(ZEL23)*complexconjugate(ZER33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_740 = Coupling(name = 'GC_740',
	 value = '(-1*complex(0,1)*(ZER21*ZH31*(ZEL31*complexconjugate(Y1e11) + ZEL32*complexconjugate(Y1e21)) + ZER22*ZH31*(ZEL31*complexconjugate(Y1e12) + ZEL32*complexconjugate(Y1e22)) + ZEL33*ZER23*ZH32*complexconjugate(Y2e33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_741 = Coupling(name = 'GC_741',
	 value = '(-1*complex(0,1)*(Y1e11*ZH31*complexconjugate(ZEL21)*complexconjugate(ZER31) + Y1e21*ZH31*complexconjugate(ZEL22)*complexconjugate(ZER31) + Y1e12*ZH31*complexconjugate(ZEL21)*complexconjugate(ZER32) + Y1e22*ZH31*complexconjugate(ZEL22)*complexconjugate(ZER32) + Y2e33*ZH32*complexconjugate(ZEL23)*complexconjugate(ZER33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_742 = Coupling(name = 'GC_742',
	 value = '(-1*complex(0,1)*(ZER31*ZH11*(ZEL11*complexconjugate(Y1e11) + ZEL12*complexconjugate(Y1e21)) + ZER32*ZH11*(ZEL11*complexconjugate(Y1e12) + ZEL12*complexconjugate(Y1e22)) + ZEL13*ZER33*ZH12*complexconjugate(Y2e33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_743 = Coupling(name = 'GC_743',
	 value = '(-1*complex(0,1)*(Y1e11*ZH11*complexconjugate(ZEL31)*complexconjugate(ZER11) + Y1e21*ZH11*complexconjugate(ZEL32)*complexconjugate(ZER11) + Y1e12*ZH11*complexconjugate(ZEL31)*complexconjugate(ZER12) + Y1e22*ZH11*complexconjugate(ZEL32)*complexconjugate(ZER12) + Y2e33*ZH12*complexconjugate(ZEL33)*complexconjugate(ZER13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_744 = Coupling(name = 'GC_744',
	 value = '(-1*complex(0,1)*(ZER31*ZH21*(ZEL11*complexconjugate(Y1e11) + ZEL12*complexconjugate(Y1e21)) + ZER32*ZH21*(ZEL11*complexconjugate(Y1e12) + ZEL12*complexconjugate(Y1e22)) + ZEL13*ZER33*ZH22*complexconjugate(Y2e33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_745 = Coupling(name = 'GC_745',
	 value = '(-1*complex(0,1)*(Y1e11*ZH21*complexconjugate(ZEL31)*complexconjugate(ZER11) + Y1e21*ZH21*complexconjugate(ZEL32)*complexconjugate(ZER11) + Y1e12*ZH21*complexconjugate(ZEL31)*complexconjugate(ZER12) + Y1e22*ZH21*complexconjugate(ZEL32)*complexconjugate(ZER12) + Y2e33*ZH22*complexconjugate(ZEL33)*complexconjugate(ZER13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_746 = Coupling(name = 'GC_746',
	 value = '(-1*complex(0,1)*(ZER31*ZH31*(ZEL11*complexconjugate(Y1e11) + ZEL12*complexconjugate(Y1e21)) + ZER32*ZH31*(ZEL11*complexconjugate(Y1e12) + ZEL12*complexconjugate(Y1e22)) + ZEL13*ZER33*ZH32*complexconjugate(Y2e33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_747 = Coupling(name = 'GC_747',
	 value = '(-1*complex(0,1)*(Y1e11*ZH31*complexconjugate(ZEL31)*complexconjugate(ZER11) + Y1e21*ZH31*complexconjugate(ZEL32)*complexconjugate(ZER11) + Y1e12*ZH31*complexconjugate(ZEL31)*complexconjugate(ZER12) + Y1e22*ZH31*complexconjugate(ZEL32)*complexconjugate(ZER12) + Y2e33*ZH32*complexconjugate(ZEL33)*complexconjugate(ZER13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_748 = Coupling(name = 'GC_748',
	 value = '(-1*complex(0,1)*(ZER31*ZH11*(ZEL21*complexconjugate(Y1e11) + ZEL22*complexconjugate(Y1e21)) + ZER32*ZH11*(ZEL21*complexconjugate(Y1e12) + ZEL22*complexconjugate(Y1e22)) + ZEL23*ZER33*ZH12*complexconjugate(Y2e33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_749 = Coupling(name = 'GC_749',
	 value = '(-1*complex(0,1)*(Y1e11*ZH11*complexconjugate(ZEL31)*complexconjugate(ZER21) + Y1e21*ZH11*complexconjugate(ZEL32)*complexconjugate(ZER21) + Y1e12*ZH11*complexconjugate(ZEL31)*complexconjugate(ZER22) + Y1e22*ZH11*complexconjugate(ZEL32)*complexconjugate(ZER22) + Y2e33*ZH12*complexconjugate(ZEL33)*complexconjugate(ZER23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_750 = Coupling(name = 'GC_750',
	 value = '(-1*complex(0,1)*(ZER31*ZH21*(ZEL21*complexconjugate(Y1e11) + ZEL22*complexconjugate(Y1e21)) + ZER32*ZH21*(ZEL21*complexconjugate(Y1e12) + ZEL22*complexconjugate(Y1e22)) + ZEL23*ZER33*ZH22*complexconjugate(Y2e33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_751 = Coupling(name = 'GC_751',
	 value = '(-1*complex(0,1)*(Y1e11*ZH21*complexconjugate(ZEL31)*complexconjugate(ZER21) + Y1e21*ZH21*complexconjugate(ZEL32)*complexconjugate(ZER21) + Y1e12*ZH21*complexconjugate(ZEL31)*complexconjugate(ZER22) + Y1e22*ZH21*complexconjugate(ZEL32)*complexconjugate(ZER22) + Y2e33*ZH22*complexconjugate(ZEL33)*complexconjugate(ZER23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_752 = Coupling(name = 'GC_752',
	 value = '(-1*complex(0,1)*(ZER31*ZH31*(ZEL21*complexconjugate(Y1e11) + ZEL22*complexconjugate(Y1e21)) + ZER32*ZH31*(ZEL21*complexconjugate(Y1e12) + ZEL22*complexconjugate(Y1e22)) + ZEL23*ZER33*ZH32*complexconjugate(Y2e33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_753 = Coupling(name = 'GC_753',
	 value = '(-1*complex(0,1)*(Y1e11*ZH31*complexconjugate(ZEL31)*complexconjugate(ZER21) + Y1e21*ZH31*complexconjugate(ZEL32)*complexconjugate(ZER21) + Y1e12*ZH31*complexconjugate(ZEL31)*complexconjugate(ZER22) + Y1e22*ZH31*complexconjugate(ZEL32)*complexconjugate(ZER22) + Y2e33*ZH32*complexconjugate(ZEL33)*complexconjugate(ZER23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_754 = Coupling(name = 'GC_754',
	 value = '(-1*complex(0,1)*(ZER31*ZH11*(ZEL31*complexconjugate(Y1e11) + ZEL32*complexconjugate(Y1e21)) + ZER32*ZH11*(ZEL31*complexconjugate(Y1e12) + ZEL32*complexconjugate(Y1e22)) + ZEL33*ZER33*ZH12*complexconjugate(Y2e33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_755 = Coupling(name = 'GC_755',
	 value = '(-1*complex(0,1)*(Y1e11*ZH11*complexconjugate(ZEL31)*complexconjugate(ZER31) + Y1e21*ZH11*complexconjugate(ZEL32)*complexconjugate(ZER31) + Y1e12*ZH11*complexconjugate(ZEL31)*complexconjugate(ZER32) + Y1e22*ZH11*complexconjugate(ZEL32)*complexconjugate(ZER32) + Y2e33*ZH12*complexconjugate(ZEL33)*complexconjugate(ZER33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_756 = Coupling(name = 'GC_756',
	 value = '(-1*complex(0,1)*(ZER31*ZH21*(ZEL31*complexconjugate(Y1e11) + ZEL32*complexconjugate(Y1e21)) + ZER32*ZH21*(ZEL31*complexconjugate(Y1e12) + ZEL32*complexconjugate(Y1e22)) + ZEL33*ZER33*ZH22*complexconjugate(Y2e33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_757 = Coupling(name = 'GC_757',
	 value = '(-1*complex(0,1)*(Y1e11*ZH21*complexconjugate(ZEL31)*complexconjugate(ZER31) + Y1e21*ZH21*complexconjugate(ZEL32)*complexconjugate(ZER31) + Y1e12*ZH21*complexconjugate(ZEL31)*complexconjugate(ZER32) + Y1e22*ZH21*complexconjugate(ZEL32)*complexconjugate(ZER32) + Y2e33*ZH22*complexconjugate(ZEL33)*complexconjugate(ZER33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_758 = Coupling(name = 'GC_758',
	 value = '(-1*complex(0,1)*(ZER31*ZH31*(ZEL31*complexconjugate(Y1e11) + ZEL32*complexconjugate(Y1e21)) + ZER32*ZH31*(ZEL31*complexconjugate(Y1e12) + ZEL32*complexconjugate(Y1e22)) + ZEL33*ZER33*ZH32*complexconjugate(Y2e33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_759 = Coupling(name = 'GC_759',
	 value = '(-1*complex(0,1)*(Y1e11*ZH31*complexconjugate(ZEL31)*complexconjugate(ZER31) + Y1e21*ZH31*complexconjugate(ZEL32)*complexconjugate(ZER31) + Y1e12*ZH31*complexconjugate(ZEL31)*complexconjugate(ZER32) + Y1e22*ZH31*complexconjugate(ZEL32)*complexconjugate(ZER32) + Y2e33*ZH32*complexconjugate(ZEL33)*complexconjugate(ZER33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_760 = Coupling(name = 'GC_760',
	 value = '(1*complex(0,1)*(ZH11*ZUR11*(ZUL11*complexconjugate(Y1u11) + ZUL12*complexconjugate(Y1u21)) + ZH11*ZUR12*(ZUL11*complexconjugate(Y1u12) + ZUL12*complexconjugate(Y1u22)) + ZH12*ZUL13*ZUR13*complexconjugate(Y2u33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_761 = Coupling(name = 'GC_761',
	 value = '(1*complex(0,1)*(Y1u11*ZH11*complexconjugate(ZUL11)*complexconjugate(ZUR11) + Y1u21*ZH11*complexconjugate(ZUL12)*complexconjugate(ZUR11) + Y1u12*ZH11*complexconjugate(ZUL11)*complexconjugate(ZUR12) + Y1u22*ZH11*complexconjugate(ZUL12)*complexconjugate(ZUR12) + Y2u33*ZH12*complexconjugate(ZUL13)*complexconjugate(ZUR13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_762 = Coupling(name = 'GC_762',
	 value = '(1*complex(0,1)*(ZH21*ZUR11*(ZUL11*complexconjugate(Y1u11) + ZUL12*complexconjugate(Y1u21)) + ZH21*ZUR12*(ZUL11*complexconjugate(Y1u12) + ZUL12*complexconjugate(Y1u22)) + ZH22*ZUL13*ZUR13*complexconjugate(Y2u33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_763 = Coupling(name = 'GC_763',
	 value = '(1*complex(0,1)*(Y1u11*ZH21*complexconjugate(ZUL11)*complexconjugate(ZUR11) + Y1u21*ZH21*complexconjugate(ZUL12)*complexconjugate(ZUR11) + Y1u12*ZH21*complexconjugate(ZUL11)*complexconjugate(ZUR12) + Y1u22*ZH21*complexconjugate(ZUL12)*complexconjugate(ZUR12) + Y2u33*ZH22*complexconjugate(ZUL13)*complexconjugate(ZUR13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_764 = Coupling(name = 'GC_764',
	 value = '(1*complex(0,1)*(ZH31*ZUR11*(ZUL11*complexconjugate(Y1u11) + ZUL12*complexconjugate(Y1u21)) + ZH31*ZUR12*(ZUL11*complexconjugate(Y1u12) + ZUL12*complexconjugate(Y1u22)) + ZH32*ZUL13*ZUR13*complexconjugate(Y2u33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_765 = Coupling(name = 'GC_765',
	 value = '(1*complex(0,1)*(Y1u11*ZH31*complexconjugate(ZUL11)*complexconjugate(ZUR11) + Y1u21*ZH31*complexconjugate(ZUL12)*complexconjugate(ZUR11) + Y1u12*ZH31*complexconjugate(ZUL11)*complexconjugate(ZUR12) + Y1u22*ZH31*complexconjugate(ZUL12)*complexconjugate(ZUR12) + Y2u33*ZH32*complexconjugate(ZUL13)*complexconjugate(ZUR13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_766 = Coupling(name = 'GC_766',
	 value = '(1*complex(0,1)*(ZH11*ZUR11*(ZUL21*complexconjugate(Y1u11) + ZUL22*complexconjugate(Y1u21)) + ZH11*ZUR12*(ZUL21*complexconjugate(Y1u12) + ZUL22*complexconjugate(Y1u22)) + ZH12*ZUL23*ZUR13*complexconjugate(Y2u33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_767 = Coupling(name = 'GC_767',
	 value = '(1*complex(0,1)*(Y1u11*ZH11*complexconjugate(ZUL11)*complexconjugate(ZUR21) + Y1u21*ZH11*complexconjugate(ZUL12)*complexconjugate(ZUR21) + Y1u12*ZH11*complexconjugate(ZUL11)*complexconjugate(ZUR22) + Y1u22*ZH11*complexconjugate(ZUL12)*complexconjugate(ZUR22) + Y2u33*ZH12*complexconjugate(ZUL13)*complexconjugate(ZUR23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_768 = Coupling(name = 'GC_768',
	 value = '(1*complex(0,1)*(ZH21*ZUR11*(ZUL21*complexconjugate(Y1u11) + ZUL22*complexconjugate(Y1u21)) + ZH21*ZUR12*(ZUL21*complexconjugate(Y1u12) + ZUL22*complexconjugate(Y1u22)) + ZH22*ZUL23*ZUR13*complexconjugate(Y2u33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_769 = Coupling(name = 'GC_769',
	 value = '(1*complex(0,1)*(Y1u11*ZH21*complexconjugate(ZUL11)*complexconjugate(ZUR21) + Y1u21*ZH21*complexconjugate(ZUL12)*complexconjugate(ZUR21) + Y1u12*ZH21*complexconjugate(ZUL11)*complexconjugate(ZUR22) + Y1u22*ZH21*complexconjugate(ZUL12)*complexconjugate(ZUR22) + Y2u33*ZH22*complexconjugate(ZUL13)*complexconjugate(ZUR23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_770 = Coupling(name = 'GC_770',
	 value = '(1*complex(0,1)*(ZH31*ZUR11*(ZUL21*complexconjugate(Y1u11) + ZUL22*complexconjugate(Y1u21)) + ZH31*ZUR12*(ZUL21*complexconjugate(Y1u12) + ZUL22*complexconjugate(Y1u22)) + ZH32*ZUL23*ZUR13*complexconjugate(Y2u33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_771 = Coupling(name = 'GC_771',
	 value = '(1*complex(0,1)*(Y1u11*ZH31*complexconjugate(ZUL11)*complexconjugate(ZUR21) + Y1u21*ZH31*complexconjugate(ZUL12)*complexconjugate(ZUR21) + Y1u12*ZH31*complexconjugate(ZUL11)*complexconjugate(ZUR22) + Y1u22*ZH31*complexconjugate(ZUL12)*complexconjugate(ZUR22) + Y2u33*ZH32*complexconjugate(ZUL13)*complexconjugate(ZUR23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_772 = Coupling(name = 'GC_772',
	 value = '(1*complex(0,1)*(ZH11*ZUR11*(ZUL31*complexconjugate(Y1u11) + ZUL32*complexconjugate(Y1u21)) + ZH11*ZUR12*(ZUL31*complexconjugate(Y1u12) + ZUL32*complexconjugate(Y1u22)) + ZH12*ZUL33*ZUR13*complexconjugate(Y2u33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_773 = Coupling(name = 'GC_773',
	 value = '(1*complex(0,1)*(Y1u11*ZH11*complexconjugate(ZUL11)*complexconjugate(ZUR31) + Y1u21*ZH11*complexconjugate(ZUL12)*complexconjugate(ZUR31) + Y1u12*ZH11*complexconjugate(ZUL11)*complexconjugate(ZUR32) + Y1u22*ZH11*complexconjugate(ZUL12)*complexconjugate(ZUR32) + Y2u33*ZH12*complexconjugate(ZUL13)*complexconjugate(ZUR33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_774 = Coupling(name = 'GC_774',
	 value = '(1*complex(0,1)*(ZH21*ZUR11*(ZUL31*complexconjugate(Y1u11) + ZUL32*complexconjugate(Y1u21)) + ZH21*ZUR12*(ZUL31*complexconjugate(Y1u12) + ZUL32*complexconjugate(Y1u22)) + ZH22*ZUL33*ZUR13*complexconjugate(Y2u33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_775 = Coupling(name = 'GC_775',
	 value = '(1*complex(0,1)*(Y1u11*ZH21*complexconjugate(ZUL11)*complexconjugate(ZUR31) + Y1u21*ZH21*complexconjugate(ZUL12)*complexconjugate(ZUR31) + Y1u12*ZH21*complexconjugate(ZUL11)*complexconjugate(ZUR32) + Y1u22*ZH21*complexconjugate(ZUL12)*complexconjugate(ZUR32) + Y2u33*ZH22*complexconjugate(ZUL13)*complexconjugate(ZUR33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_776 = Coupling(name = 'GC_776',
	 value = '(1*complex(0,1)*(ZH31*ZUR11*(ZUL31*complexconjugate(Y1u11) + ZUL32*complexconjugate(Y1u21)) + ZH31*ZUR12*(ZUL31*complexconjugate(Y1u12) + ZUL32*complexconjugate(Y1u22)) + ZH32*ZUL33*ZUR13*complexconjugate(Y2u33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_777 = Coupling(name = 'GC_777',
	 value = '(1*complex(0,1)*(Y1u11*ZH31*complexconjugate(ZUL11)*complexconjugate(ZUR31) + Y1u21*ZH31*complexconjugate(ZUL12)*complexconjugate(ZUR31) + Y1u12*ZH31*complexconjugate(ZUL11)*complexconjugate(ZUR32) + Y1u22*ZH31*complexconjugate(ZUL12)*complexconjugate(ZUR32) + Y2u33*ZH32*complexconjugate(ZUL13)*complexconjugate(ZUR33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_778 = Coupling(name = 'GC_778',
	 value = '(1*complex(0,1)*(ZH11*ZUR21*(ZUL11*complexconjugate(Y1u11) + ZUL12*complexconjugate(Y1u21)) + ZH11*ZUR22*(ZUL11*complexconjugate(Y1u12) + ZUL12*complexconjugate(Y1u22)) + ZH12*ZUL13*ZUR23*complexconjugate(Y2u33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_779 = Coupling(name = 'GC_779',
	 value = '(1*complex(0,1)*(Y1u11*ZH11*complexconjugate(ZUL21)*complexconjugate(ZUR11) + Y1u21*ZH11*complexconjugate(ZUL22)*complexconjugate(ZUR11) + Y1u12*ZH11*complexconjugate(ZUL21)*complexconjugate(ZUR12) + Y1u22*ZH11*complexconjugate(ZUL22)*complexconjugate(ZUR12) + Y2u33*ZH12*complexconjugate(ZUL23)*complexconjugate(ZUR13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_780 = Coupling(name = 'GC_780',
	 value = '(1*complex(0,1)*(ZH21*ZUR21*(ZUL11*complexconjugate(Y1u11) + ZUL12*complexconjugate(Y1u21)) + ZH21*ZUR22*(ZUL11*complexconjugate(Y1u12) + ZUL12*complexconjugate(Y1u22)) + ZH22*ZUL13*ZUR23*complexconjugate(Y2u33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_781 = Coupling(name = 'GC_781',
	 value = '(1*complex(0,1)*(Y1u11*ZH21*complexconjugate(ZUL21)*complexconjugate(ZUR11) + Y1u21*ZH21*complexconjugate(ZUL22)*complexconjugate(ZUR11) + Y1u12*ZH21*complexconjugate(ZUL21)*complexconjugate(ZUR12) + Y1u22*ZH21*complexconjugate(ZUL22)*complexconjugate(ZUR12) + Y2u33*ZH22*complexconjugate(ZUL23)*complexconjugate(ZUR13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_782 = Coupling(name = 'GC_782',
	 value = '(1*complex(0,1)*(ZH31*ZUR21*(ZUL11*complexconjugate(Y1u11) + ZUL12*complexconjugate(Y1u21)) + ZH31*ZUR22*(ZUL11*complexconjugate(Y1u12) + ZUL12*complexconjugate(Y1u22)) + ZH32*ZUL13*ZUR23*complexconjugate(Y2u33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_783 = Coupling(name = 'GC_783',
	 value = '(1*complex(0,1)*(Y1u11*ZH31*complexconjugate(ZUL21)*complexconjugate(ZUR11) + Y1u21*ZH31*complexconjugate(ZUL22)*complexconjugate(ZUR11) + Y1u12*ZH31*complexconjugate(ZUL21)*complexconjugate(ZUR12) + Y1u22*ZH31*complexconjugate(ZUL22)*complexconjugate(ZUR12) + Y2u33*ZH32*complexconjugate(ZUL23)*complexconjugate(ZUR13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_784 = Coupling(name = 'GC_784',
	 value = '(1*complex(0,1)*(ZH11*ZUR21*(ZUL21*complexconjugate(Y1u11) + ZUL22*complexconjugate(Y1u21)) + ZH11*ZUR22*(ZUL21*complexconjugate(Y1u12) + ZUL22*complexconjugate(Y1u22)) + ZH12*ZUL23*ZUR23*complexconjugate(Y2u33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_785 = Coupling(name = 'GC_785',
	 value = '(1*complex(0,1)*(Y1u11*ZH11*complexconjugate(ZUL21)*complexconjugate(ZUR21) + Y1u21*ZH11*complexconjugate(ZUL22)*complexconjugate(ZUR21) + Y1u12*ZH11*complexconjugate(ZUL21)*complexconjugate(ZUR22) + Y1u22*ZH11*complexconjugate(ZUL22)*complexconjugate(ZUR22) + Y2u33*ZH12*complexconjugate(ZUL23)*complexconjugate(ZUR23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_786 = Coupling(name = 'GC_786',
	 value = '(1*complex(0,1)*(ZH21*ZUR21*(ZUL21*complexconjugate(Y1u11) + ZUL22*complexconjugate(Y1u21)) + ZH21*ZUR22*(ZUL21*complexconjugate(Y1u12) + ZUL22*complexconjugate(Y1u22)) + ZH22*ZUL23*ZUR23*complexconjugate(Y2u33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_787 = Coupling(name = 'GC_787',
	 value = '(1*complex(0,1)*(Y1u11*ZH21*complexconjugate(ZUL21)*complexconjugate(ZUR21) + Y1u21*ZH21*complexconjugate(ZUL22)*complexconjugate(ZUR21) + Y1u12*ZH21*complexconjugate(ZUL21)*complexconjugate(ZUR22) + Y1u22*ZH21*complexconjugate(ZUL22)*complexconjugate(ZUR22) + Y2u33*ZH22*complexconjugate(ZUL23)*complexconjugate(ZUR23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_788 = Coupling(name = 'GC_788',
	 value = '(1*complex(0,1)*(ZH31*ZUR21*(ZUL21*complexconjugate(Y1u11) + ZUL22*complexconjugate(Y1u21)) + ZH31*ZUR22*(ZUL21*complexconjugate(Y1u12) + ZUL22*complexconjugate(Y1u22)) + ZH32*ZUL23*ZUR23*complexconjugate(Y2u33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_789 = Coupling(name = 'GC_789',
	 value = '(1*complex(0,1)*(Y1u11*ZH31*complexconjugate(ZUL21)*complexconjugate(ZUR21) + Y1u21*ZH31*complexconjugate(ZUL22)*complexconjugate(ZUR21) + Y1u12*ZH31*complexconjugate(ZUL21)*complexconjugate(ZUR22) + Y1u22*ZH31*complexconjugate(ZUL22)*complexconjugate(ZUR22) + Y2u33*ZH32*complexconjugate(ZUL23)*complexconjugate(ZUR23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_790 = Coupling(name = 'GC_790',
	 value = '(1*complex(0,1)*(ZH11*ZUR21*(ZUL31*complexconjugate(Y1u11) + ZUL32*complexconjugate(Y1u21)) + ZH11*ZUR22*(ZUL31*complexconjugate(Y1u12) + ZUL32*complexconjugate(Y1u22)) + ZH12*ZUL33*ZUR23*complexconjugate(Y2u33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_791 = Coupling(name = 'GC_791',
	 value = '(1*complex(0,1)*(Y1u11*ZH11*complexconjugate(ZUL21)*complexconjugate(ZUR31) + Y1u21*ZH11*complexconjugate(ZUL22)*complexconjugate(ZUR31) + Y1u12*ZH11*complexconjugate(ZUL21)*complexconjugate(ZUR32) + Y1u22*ZH11*complexconjugate(ZUL22)*complexconjugate(ZUR32) + Y2u33*ZH12*complexconjugate(ZUL23)*complexconjugate(ZUR33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_792 = Coupling(name = 'GC_792',
	 value = '(1*complex(0,1)*(ZH21*ZUR21*(ZUL31*complexconjugate(Y1u11) + ZUL32*complexconjugate(Y1u21)) + ZH21*ZUR22*(ZUL31*complexconjugate(Y1u12) + ZUL32*complexconjugate(Y1u22)) + ZH22*ZUL33*ZUR23*complexconjugate(Y2u33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_793 = Coupling(name = 'GC_793',
	 value = '(1*complex(0,1)*(Y1u11*ZH21*complexconjugate(ZUL21)*complexconjugate(ZUR31) + Y1u21*ZH21*complexconjugate(ZUL22)*complexconjugate(ZUR31) + Y1u12*ZH21*complexconjugate(ZUL21)*complexconjugate(ZUR32) + Y1u22*ZH21*complexconjugate(ZUL22)*complexconjugate(ZUR32) + Y2u33*ZH22*complexconjugate(ZUL23)*complexconjugate(ZUR33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_794 = Coupling(name = 'GC_794',
	 value = '(1*complex(0,1)*(ZH31*ZUR21*(ZUL31*complexconjugate(Y1u11) + ZUL32*complexconjugate(Y1u21)) + ZH31*ZUR22*(ZUL31*complexconjugate(Y1u12) + ZUL32*complexconjugate(Y1u22)) + ZH32*ZUL33*ZUR23*complexconjugate(Y2u33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_795 = Coupling(name = 'GC_795',
	 value = '(1*complex(0,1)*(Y1u11*ZH31*complexconjugate(ZUL21)*complexconjugate(ZUR31) + Y1u21*ZH31*complexconjugate(ZUL22)*complexconjugate(ZUR31) + Y1u12*ZH31*complexconjugate(ZUL21)*complexconjugate(ZUR32) + Y1u22*ZH31*complexconjugate(ZUL22)*complexconjugate(ZUR32) + Y2u33*ZH32*complexconjugate(ZUL23)*complexconjugate(ZUR33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_796 = Coupling(name = 'GC_796',
	 value = '(1*complex(0,1)*(ZH11*ZUR31*(ZUL11*complexconjugate(Y1u11) + ZUL12*complexconjugate(Y1u21)) + ZH11*ZUR32*(ZUL11*complexconjugate(Y1u12) + ZUL12*complexconjugate(Y1u22)) + ZH12*ZUL13*ZUR33*complexconjugate(Y2u33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_797 = Coupling(name = 'GC_797',
	 value = '(1*complex(0,1)*(Y1u11*ZH11*complexconjugate(ZUL31)*complexconjugate(ZUR11) + Y1u21*ZH11*complexconjugate(ZUL32)*complexconjugate(ZUR11) + Y1u12*ZH11*complexconjugate(ZUL31)*complexconjugate(ZUR12) + Y1u22*ZH11*complexconjugate(ZUL32)*complexconjugate(ZUR12) + Y2u33*ZH12*complexconjugate(ZUL33)*complexconjugate(ZUR13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_798 = Coupling(name = 'GC_798',
	 value = '(1*complex(0,1)*(ZH21*ZUR31*(ZUL11*complexconjugate(Y1u11) + ZUL12*complexconjugate(Y1u21)) + ZH21*ZUR32*(ZUL11*complexconjugate(Y1u12) + ZUL12*complexconjugate(Y1u22)) + ZH22*ZUL13*ZUR33*complexconjugate(Y2u33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_799 = Coupling(name = 'GC_799',
	 value = '(1*complex(0,1)*(Y1u11*ZH21*complexconjugate(ZUL31)*complexconjugate(ZUR11) + Y1u21*ZH21*complexconjugate(ZUL32)*complexconjugate(ZUR11) + Y1u12*ZH21*complexconjugate(ZUL31)*complexconjugate(ZUR12) + Y1u22*ZH21*complexconjugate(ZUL32)*complexconjugate(ZUR12) + Y2u33*ZH22*complexconjugate(ZUL33)*complexconjugate(ZUR13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_800 = Coupling(name = 'GC_800',
	 value = '(1*complex(0,1)*(ZH31*ZUR31*(ZUL11*complexconjugate(Y1u11) + ZUL12*complexconjugate(Y1u21)) + ZH31*ZUR32*(ZUL11*complexconjugate(Y1u12) + ZUL12*complexconjugate(Y1u22)) + ZH32*ZUL13*ZUR33*complexconjugate(Y2u33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_801 = Coupling(name = 'GC_801',
	 value = '(1*complex(0,1)*(Y1u11*ZH31*complexconjugate(ZUL31)*complexconjugate(ZUR11) + Y1u21*ZH31*complexconjugate(ZUL32)*complexconjugate(ZUR11) + Y1u12*ZH31*complexconjugate(ZUL31)*complexconjugate(ZUR12) + Y1u22*ZH31*complexconjugate(ZUL32)*complexconjugate(ZUR12) + Y2u33*ZH32*complexconjugate(ZUL33)*complexconjugate(ZUR13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_802 = Coupling(name = 'GC_802',
	 value = '(1*complex(0,1)*(ZH11*ZUR31*(ZUL21*complexconjugate(Y1u11) + ZUL22*complexconjugate(Y1u21)) + ZH11*ZUR32*(ZUL21*complexconjugate(Y1u12) + ZUL22*complexconjugate(Y1u22)) + ZH12*ZUL23*ZUR33*complexconjugate(Y2u33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_803 = Coupling(name = 'GC_803',
	 value = '(1*complex(0,1)*(Y1u11*ZH11*complexconjugate(ZUL31)*complexconjugate(ZUR21) + Y1u21*ZH11*complexconjugate(ZUL32)*complexconjugate(ZUR21) + Y1u12*ZH11*complexconjugate(ZUL31)*complexconjugate(ZUR22) + Y1u22*ZH11*complexconjugate(ZUL32)*complexconjugate(ZUR22) + Y2u33*ZH12*complexconjugate(ZUL33)*complexconjugate(ZUR23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_804 = Coupling(name = 'GC_804',
	 value = '(1*complex(0,1)*(ZH21*ZUR31*(ZUL21*complexconjugate(Y1u11) + ZUL22*complexconjugate(Y1u21)) + ZH21*ZUR32*(ZUL21*complexconjugate(Y1u12) + ZUL22*complexconjugate(Y1u22)) + ZH22*ZUL23*ZUR33*complexconjugate(Y2u33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_805 = Coupling(name = 'GC_805',
	 value = '(1*complex(0,1)*(Y1u11*ZH21*complexconjugate(ZUL31)*complexconjugate(ZUR21) + Y1u21*ZH21*complexconjugate(ZUL32)*complexconjugate(ZUR21) + Y1u12*ZH21*complexconjugate(ZUL31)*complexconjugate(ZUR22) + Y1u22*ZH21*complexconjugate(ZUL32)*complexconjugate(ZUR22) + Y2u33*ZH22*complexconjugate(ZUL33)*complexconjugate(ZUR23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_806 = Coupling(name = 'GC_806',
	 value = '(1*complex(0,1)*(ZH31*ZUR31*(ZUL21*complexconjugate(Y1u11) + ZUL22*complexconjugate(Y1u21)) + ZH31*ZUR32*(ZUL21*complexconjugate(Y1u12) + ZUL22*complexconjugate(Y1u22)) + ZH32*ZUL23*ZUR33*complexconjugate(Y2u33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_807 = Coupling(name = 'GC_807',
	 value = '(1*complex(0,1)*(Y1u11*ZH31*complexconjugate(ZUL31)*complexconjugate(ZUR21) + Y1u21*ZH31*complexconjugate(ZUL32)*complexconjugate(ZUR21) + Y1u12*ZH31*complexconjugate(ZUL31)*complexconjugate(ZUR22) + Y1u22*ZH31*complexconjugate(ZUL32)*complexconjugate(ZUR22) + Y2u33*ZH32*complexconjugate(ZUL33)*complexconjugate(ZUR23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_808 = Coupling(name = 'GC_808',
	 value = '(1*complex(0,1)*(ZH11*ZUR31*(ZUL31*complexconjugate(Y1u11) + ZUL32*complexconjugate(Y1u21)) + ZH11*ZUR32*(ZUL31*complexconjugate(Y1u12) + ZUL32*complexconjugate(Y1u22)) + ZH12*ZUL33*ZUR33*complexconjugate(Y2u33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_809 = Coupling(name = 'GC_809',
	 value = '(1*complex(0,1)*(Y1u11*ZH11*complexconjugate(ZUL31)*complexconjugate(ZUR31) + Y1u21*ZH11*complexconjugate(ZUL32)*complexconjugate(ZUR31) + Y1u12*ZH11*complexconjugate(ZUL31)*complexconjugate(ZUR32) + Y1u22*ZH11*complexconjugate(ZUL32)*complexconjugate(ZUR32) + Y2u33*ZH12*complexconjugate(ZUL33)*complexconjugate(ZUR33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_810 = Coupling(name = 'GC_810',
	 value = '(1*complex(0,1)*(ZH21*ZUR31*(ZUL31*complexconjugate(Y1u11) + ZUL32*complexconjugate(Y1u21)) + ZH21*ZUR32*(ZUL31*complexconjugate(Y1u12) + ZUL32*complexconjugate(Y1u22)) + ZH22*ZUL33*ZUR33*complexconjugate(Y2u33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_811 = Coupling(name = 'GC_811',
	 value = '(1*complex(0,1)*(Y1u11*ZH21*complexconjugate(ZUL31)*complexconjugate(ZUR31) + Y1u21*ZH21*complexconjugate(ZUL32)*complexconjugate(ZUR31) + Y1u12*ZH21*complexconjugate(ZUL31)*complexconjugate(ZUR32) + Y1u22*ZH21*complexconjugate(ZUL32)*complexconjugate(ZUR32) + Y2u33*ZH22*complexconjugate(ZUL33)*complexconjugate(ZUR33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_812 = Coupling(name = 'GC_812',
	 value = '(1*complex(0,1)*(ZH31*ZUR31*(ZUL31*complexconjugate(Y1u11) + ZUL32*complexconjugate(Y1u21)) + ZH31*ZUR32*(ZUL31*complexconjugate(Y1u12) + ZUL32*complexconjugate(Y1u22)) + ZH32*ZUL33*ZUR33*complexconjugate(Y2u33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_813 = Coupling(name = 'GC_813',
	 value = '(1*complex(0,1)*(Y1u11*ZH31*complexconjugate(ZUL31)*complexconjugate(ZUR31) + Y1u21*ZH31*complexconjugate(ZUL32)*complexconjugate(ZUR31) + Y1u12*ZH31*complexconjugate(ZUL31)*complexconjugate(ZUR32) + Y1u22*ZH31*complexconjugate(ZUL32)*complexconjugate(ZUR32) + Y2u33*ZH32*complexconjugate(ZUL33)*complexconjugate(ZUR33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_814 = Coupling(name = 'GC_814',
	 value = '-1*complex(0,1)*(ZDR11*(ZP11*ZUL11*complexconjugate(Y1d11) + ZP11*ZUL12*complexconjugate(Y1d21) + ZP12*ZUL13*complexconjugate(Y2d31)) + ZDR12*(ZP11*ZUL11*complexconjugate(Y1d12) + ZP11*ZUL12*complexconjugate(Y1d22) + ZP12*ZUL13*complexconjugate(Y2d32)) + ZDR13*(ZP11*ZUL11*complexconjugate(Y1d13) + ZP11*ZUL12*complexconjugate(Y1d23) + ZP12*ZUL13*complexconjugate(Y2d33)))', 
	 order = {'QED':1} ) 
 
GC_815 = Coupling(name = 'GC_815',
	 value = '-1*complex(0,1)*(Y1u11*ZP11*complexconjugate(ZDL11)*complexconjugate(ZUR11) + Y1u21*ZP11*complexconjugate(ZDL12)*complexconjugate(ZUR11) + Y1u12*ZP11*complexconjugate(ZDL11)*complexconjugate(ZUR12) + Y1u22*ZP11*complexconjugate(ZDL12)*complexconjugate(ZUR12) + Y2u33*ZP12*complexconjugate(ZDL13)*complexconjugate(ZUR13))', 
	 order = {'QED':1} ) 
 
GC_816 = Coupling(name = 'GC_816',
	 value = '-1*complex(0,1)*(ZDR11*(ZP21*ZUL11*complexconjugate(Y1d11) + ZP21*ZUL12*complexconjugate(Y1d21) + ZP22*ZUL13*complexconjugate(Y2d31)) + ZDR12*(ZP21*ZUL11*complexconjugate(Y1d12) + ZP21*ZUL12*complexconjugate(Y1d22) + ZP22*ZUL13*complexconjugate(Y2d32)) + ZDR13*(ZP21*ZUL11*complexconjugate(Y1d13) + ZP21*ZUL12*complexconjugate(Y1d23) + ZP22*ZUL13*complexconjugate(Y2d33)))', 
	 order = {'QED':1} ) 
 
GC_817 = Coupling(name = 'GC_817',
	 value = '-1*complex(0,1)*(Y1u11*ZP21*complexconjugate(ZDL11)*complexconjugate(ZUR11) + Y1u21*ZP21*complexconjugate(ZDL12)*complexconjugate(ZUR11) + Y1u12*ZP21*complexconjugate(ZDL11)*complexconjugate(ZUR12) + Y1u22*ZP21*complexconjugate(ZDL12)*complexconjugate(ZUR12) + Y2u33*ZP22*complexconjugate(ZDL13)*complexconjugate(ZUR13))', 
	 order = {'QED':1} ) 
 
GC_818 = Coupling(name = 'GC_818',
	 value = '-1*complex(0,1)*(ZDR11*(ZP11*ZUL21*complexconjugate(Y1d11) + ZP11*ZUL22*complexconjugate(Y1d21) + ZP12*ZUL23*complexconjugate(Y2d31)) + ZDR12*(ZP11*ZUL21*complexconjugate(Y1d12) + ZP11*ZUL22*complexconjugate(Y1d22) + ZP12*ZUL23*complexconjugate(Y2d32)) + ZDR13*(ZP11*ZUL21*complexconjugate(Y1d13) + ZP11*ZUL22*complexconjugate(Y1d23) + ZP12*ZUL23*complexconjugate(Y2d33)))', 
	 order = {'QED':1} ) 
 
GC_819 = Coupling(name = 'GC_819',
	 value = '-1*complex(0,1)*(Y1u11*ZP11*complexconjugate(ZDL11)*complexconjugate(ZUR21) + Y1u21*ZP11*complexconjugate(ZDL12)*complexconjugate(ZUR21) + Y1u12*ZP11*complexconjugate(ZDL11)*complexconjugate(ZUR22) + Y1u22*ZP11*complexconjugate(ZDL12)*complexconjugate(ZUR22) + Y2u33*ZP12*complexconjugate(ZDL13)*complexconjugate(ZUR23))', 
	 order = {'QED':1} ) 
 
GC_820 = Coupling(name = 'GC_820',
	 value = '-1*complex(0,1)*(ZDR11*(ZP21*ZUL21*complexconjugate(Y1d11) + ZP21*ZUL22*complexconjugate(Y1d21) + ZP22*ZUL23*complexconjugate(Y2d31)) + ZDR12*(ZP21*ZUL21*complexconjugate(Y1d12) + ZP21*ZUL22*complexconjugate(Y1d22) + ZP22*ZUL23*complexconjugate(Y2d32)) + ZDR13*(ZP21*ZUL21*complexconjugate(Y1d13) + ZP21*ZUL22*complexconjugate(Y1d23) + ZP22*ZUL23*complexconjugate(Y2d33)))', 
	 order = {'QED':1} ) 
 
GC_821 = Coupling(name = 'GC_821',
	 value = '-1*complex(0,1)*(Y1u11*ZP21*complexconjugate(ZDL11)*complexconjugate(ZUR21) + Y1u21*ZP21*complexconjugate(ZDL12)*complexconjugate(ZUR21) + Y1u12*ZP21*complexconjugate(ZDL11)*complexconjugate(ZUR22) + Y1u22*ZP21*complexconjugate(ZDL12)*complexconjugate(ZUR22) + Y2u33*ZP22*complexconjugate(ZDL13)*complexconjugate(ZUR23))', 
	 order = {'QED':1} ) 
 
GC_822 = Coupling(name = 'GC_822',
	 value = '-1*complex(0,1)*(ZDR11*(ZP11*ZUL31*complexconjugate(Y1d11) + ZP11*ZUL32*complexconjugate(Y1d21) + ZP12*ZUL33*complexconjugate(Y2d31)) + ZDR12*(ZP11*ZUL31*complexconjugate(Y1d12) + ZP11*ZUL32*complexconjugate(Y1d22) + ZP12*ZUL33*complexconjugate(Y2d32)) + ZDR13*(ZP11*ZUL31*complexconjugate(Y1d13) + ZP11*ZUL32*complexconjugate(Y1d23) + ZP12*ZUL33*complexconjugate(Y2d33)))', 
	 order = {'QED':1} ) 
 
GC_823 = Coupling(name = 'GC_823',
	 value = '-1*complex(0,1)*(Y1u11*ZP11*complexconjugate(ZDL11)*complexconjugate(ZUR31) + Y1u21*ZP11*complexconjugate(ZDL12)*complexconjugate(ZUR31) + Y1u12*ZP11*complexconjugate(ZDL11)*complexconjugate(ZUR32) + Y1u22*ZP11*complexconjugate(ZDL12)*complexconjugate(ZUR32) + Y2u33*ZP12*complexconjugate(ZDL13)*complexconjugate(ZUR33))', 
	 order = {'QED':1} ) 
 
GC_824 = Coupling(name = 'GC_824',
	 value = '-1*complex(0,1)*(ZDR11*(ZP21*ZUL31*complexconjugate(Y1d11) + ZP21*ZUL32*complexconjugate(Y1d21) + ZP22*ZUL33*complexconjugate(Y2d31)) + ZDR12*(ZP21*ZUL31*complexconjugate(Y1d12) + ZP21*ZUL32*complexconjugate(Y1d22) + ZP22*ZUL33*complexconjugate(Y2d32)) + ZDR13*(ZP21*ZUL31*complexconjugate(Y1d13) + ZP21*ZUL32*complexconjugate(Y1d23) + ZP22*ZUL33*complexconjugate(Y2d33)))', 
	 order = {'QED':1} ) 
 
GC_825 = Coupling(name = 'GC_825',
	 value = '-1*complex(0,1)*(Y1u11*ZP21*complexconjugate(ZDL11)*complexconjugate(ZUR31) + Y1u21*ZP21*complexconjugate(ZDL12)*complexconjugate(ZUR31) + Y1u12*ZP21*complexconjugate(ZDL11)*complexconjugate(ZUR32) + Y1u22*ZP21*complexconjugate(ZDL12)*complexconjugate(ZUR32) + Y2u33*ZP22*complexconjugate(ZDL13)*complexconjugate(ZUR33))', 
	 order = {'QED':1} ) 
 
GC_826 = Coupling(name = 'GC_826',
	 value = '-1*complex(0,1)*(ZDR21*(ZP11*ZUL11*complexconjugate(Y1d11) + ZP11*ZUL12*complexconjugate(Y1d21) + ZP12*ZUL13*complexconjugate(Y2d31)) + ZDR22*(ZP11*ZUL11*complexconjugate(Y1d12) + ZP11*ZUL12*complexconjugate(Y1d22) + ZP12*ZUL13*complexconjugate(Y2d32)) + ZDR23*(ZP11*ZUL11*complexconjugate(Y1d13) + ZP11*ZUL12*complexconjugate(Y1d23) + ZP12*ZUL13*complexconjugate(Y2d33)))', 
	 order = {'QED':1} ) 
 
GC_827 = Coupling(name = 'GC_827',
	 value = '-1*complex(0,1)*(Y1u11*ZP11*complexconjugate(ZDL21)*complexconjugate(ZUR11) + Y1u21*ZP11*complexconjugate(ZDL22)*complexconjugate(ZUR11) + Y1u12*ZP11*complexconjugate(ZDL21)*complexconjugate(ZUR12) + Y1u22*ZP11*complexconjugate(ZDL22)*complexconjugate(ZUR12) + Y2u33*ZP12*complexconjugate(ZDL23)*complexconjugate(ZUR13))', 
	 order = {'QED':1} ) 
 
GC_828 = Coupling(name = 'GC_828',
	 value = '-1*complex(0,1)*(ZDR21*(ZP21*ZUL11*complexconjugate(Y1d11) + ZP21*ZUL12*complexconjugate(Y1d21) + ZP22*ZUL13*complexconjugate(Y2d31)) + ZDR22*(ZP21*ZUL11*complexconjugate(Y1d12) + ZP21*ZUL12*complexconjugate(Y1d22) + ZP22*ZUL13*complexconjugate(Y2d32)) + ZDR23*(ZP21*ZUL11*complexconjugate(Y1d13) + ZP21*ZUL12*complexconjugate(Y1d23) + ZP22*ZUL13*complexconjugate(Y2d33)))', 
	 order = {'QED':1} ) 
 
GC_829 = Coupling(name = 'GC_829',
	 value = '-1*complex(0,1)*(Y1u11*ZP21*complexconjugate(ZDL21)*complexconjugate(ZUR11) + Y1u21*ZP21*complexconjugate(ZDL22)*complexconjugate(ZUR11) + Y1u12*ZP21*complexconjugate(ZDL21)*complexconjugate(ZUR12) + Y1u22*ZP21*complexconjugate(ZDL22)*complexconjugate(ZUR12) + Y2u33*ZP22*complexconjugate(ZDL23)*complexconjugate(ZUR13))', 
	 order = {'QED':1} ) 
 
GC_830 = Coupling(name = 'GC_830',
	 value = '-1*complex(0,1)*(ZDR21*(ZP11*ZUL21*complexconjugate(Y1d11) + ZP11*ZUL22*complexconjugate(Y1d21) + ZP12*ZUL23*complexconjugate(Y2d31)) + ZDR22*(ZP11*ZUL21*complexconjugate(Y1d12) + ZP11*ZUL22*complexconjugate(Y1d22) + ZP12*ZUL23*complexconjugate(Y2d32)) + ZDR23*(ZP11*ZUL21*complexconjugate(Y1d13) + ZP11*ZUL22*complexconjugate(Y1d23) + ZP12*ZUL23*complexconjugate(Y2d33)))', 
	 order = {'QED':1} ) 
 
GC_831 = Coupling(name = 'GC_831',
	 value = '-1*complex(0,1)*(Y1u11*ZP11*complexconjugate(ZDL21)*complexconjugate(ZUR21) + Y1u21*ZP11*complexconjugate(ZDL22)*complexconjugate(ZUR21) + Y1u12*ZP11*complexconjugate(ZDL21)*complexconjugate(ZUR22) + Y1u22*ZP11*complexconjugate(ZDL22)*complexconjugate(ZUR22) + Y2u33*ZP12*complexconjugate(ZDL23)*complexconjugate(ZUR23))', 
	 order = {'QED':1} ) 
 
GC_832 = Coupling(name = 'GC_832',
	 value = '-1*complex(0,1)*(ZDR21*(ZP21*ZUL21*complexconjugate(Y1d11) + ZP21*ZUL22*complexconjugate(Y1d21) + ZP22*ZUL23*complexconjugate(Y2d31)) + ZDR22*(ZP21*ZUL21*complexconjugate(Y1d12) + ZP21*ZUL22*complexconjugate(Y1d22) + ZP22*ZUL23*complexconjugate(Y2d32)) + ZDR23*(ZP21*ZUL21*complexconjugate(Y1d13) + ZP21*ZUL22*complexconjugate(Y1d23) + ZP22*ZUL23*complexconjugate(Y2d33)))', 
	 order = {'QED':1} ) 
 
GC_833 = Coupling(name = 'GC_833',
	 value = '-1*complex(0,1)*(Y1u11*ZP21*complexconjugate(ZDL21)*complexconjugate(ZUR21) + Y1u21*ZP21*complexconjugate(ZDL22)*complexconjugate(ZUR21) + Y1u12*ZP21*complexconjugate(ZDL21)*complexconjugate(ZUR22) + Y1u22*ZP21*complexconjugate(ZDL22)*complexconjugate(ZUR22) + Y2u33*ZP22*complexconjugate(ZDL23)*complexconjugate(ZUR23))', 
	 order = {'QED':1} ) 
 
GC_834 = Coupling(name = 'GC_834',
	 value = '-1*complex(0,1)*(ZDR21*(ZP11*ZUL31*complexconjugate(Y1d11) + ZP11*ZUL32*complexconjugate(Y1d21) + ZP12*ZUL33*complexconjugate(Y2d31)) + ZDR22*(ZP11*ZUL31*complexconjugate(Y1d12) + ZP11*ZUL32*complexconjugate(Y1d22) + ZP12*ZUL33*complexconjugate(Y2d32)) + ZDR23*(ZP11*ZUL31*complexconjugate(Y1d13) + ZP11*ZUL32*complexconjugate(Y1d23) + ZP12*ZUL33*complexconjugate(Y2d33)))', 
	 order = {'QED':1} ) 
 
GC_835 = Coupling(name = 'GC_835',
	 value = '-1*complex(0,1)*(Y1u11*ZP11*complexconjugate(ZDL21)*complexconjugate(ZUR31) + Y1u21*ZP11*complexconjugate(ZDL22)*complexconjugate(ZUR31) + Y1u12*ZP11*complexconjugate(ZDL21)*complexconjugate(ZUR32) + Y1u22*ZP11*complexconjugate(ZDL22)*complexconjugate(ZUR32) + Y2u33*ZP12*complexconjugate(ZDL23)*complexconjugate(ZUR33))', 
	 order = {'QED':1} ) 
 
GC_836 = Coupling(name = 'GC_836',
	 value = '-1*complex(0,1)*(ZDR21*(ZP21*ZUL31*complexconjugate(Y1d11) + ZP21*ZUL32*complexconjugate(Y1d21) + ZP22*ZUL33*complexconjugate(Y2d31)) + ZDR22*(ZP21*ZUL31*complexconjugate(Y1d12) + ZP21*ZUL32*complexconjugate(Y1d22) + ZP22*ZUL33*complexconjugate(Y2d32)) + ZDR23*(ZP21*ZUL31*complexconjugate(Y1d13) + ZP21*ZUL32*complexconjugate(Y1d23) + ZP22*ZUL33*complexconjugate(Y2d33)))', 
	 order = {'QED':1} ) 
 
GC_837 = Coupling(name = 'GC_837',
	 value = '-1*complex(0,1)*(Y1u11*ZP21*complexconjugate(ZDL21)*complexconjugate(ZUR31) + Y1u21*ZP21*complexconjugate(ZDL22)*complexconjugate(ZUR31) + Y1u12*ZP21*complexconjugate(ZDL21)*complexconjugate(ZUR32) + Y1u22*ZP21*complexconjugate(ZDL22)*complexconjugate(ZUR32) + Y2u33*ZP22*complexconjugate(ZDL23)*complexconjugate(ZUR33))', 
	 order = {'QED':1} ) 
 
GC_838 = Coupling(name = 'GC_838',
	 value = '-1*complex(0,1)*(ZDR31*(ZP11*ZUL11*complexconjugate(Y1d11) + ZP11*ZUL12*complexconjugate(Y1d21) + ZP12*ZUL13*complexconjugate(Y2d31)) + ZDR32*(ZP11*ZUL11*complexconjugate(Y1d12) + ZP11*ZUL12*complexconjugate(Y1d22) + ZP12*ZUL13*complexconjugate(Y2d32)) + ZDR33*(ZP11*ZUL11*complexconjugate(Y1d13) + ZP11*ZUL12*complexconjugate(Y1d23) + ZP12*ZUL13*complexconjugate(Y2d33)))', 
	 order = {'QED':1} ) 
 
GC_839 = Coupling(name = 'GC_839',
	 value = '-1*complex(0,1)*(Y1u11*ZP11*complexconjugate(ZDL31)*complexconjugate(ZUR11) + Y1u21*ZP11*complexconjugate(ZDL32)*complexconjugate(ZUR11) + Y1u12*ZP11*complexconjugate(ZDL31)*complexconjugate(ZUR12) + Y1u22*ZP11*complexconjugate(ZDL32)*complexconjugate(ZUR12) + Y2u33*ZP12*complexconjugate(ZDL33)*complexconjugate(ZUR13))', 
	 order = {'QED':1} ) 
 
GC_840 = Coupling(name = 'GC_840',
	 value = '-1*complex(0,1)*(ZDR31*(ZP21*ZUL11*complexconjugate(Y1d11) + ZP21*ZUL12*complexconjugate(Y1d21) + ZP22*ZUL13*complexconjugate(Y2d31)) + ZDR32*(ZP21*ZUL11*complexconjugate(Y1d12) + ZP21*ZUL12*complexconjugate(Y1d22) + ZP22*ZUL13*complexconjugate(Y2d32)) + ZDR33*(ZP21*ZUL11*complexconjugate(Y1d13) + ZP21*ZUL12*complexconjugate(Y1d23) + ZP22*ZUL13*complexconjugate(Y2d33)))', 
	 order = {'QED':1} ) 
 
GC_841 = Coupling(name = 'GC_841',
	 value = '-1*complex(0,1)*(Y1u11*ZP21*complexconjugate(ZDL31)*complexconjugate(ZUR11) + Y1u21*ZP21*complexconjugate(ZDL32)*complexconjugate(ZUR11) + Y1u12*ZP21*complexconjugate(ZDL31)*complexconjugate(ZUR12) + Y1u22*ZP21*complexconjugate(ZDL32)*complexconjugate(ZUR12) + Y2u33*ZP22*complexconjugate(ZDL33)*complexconjugate(ZUR13))', 
	 order = {'QED':1} ) 
 
GC_842 = Coupling(name = 'GC_842',
	 value = '-1*complex(0,1)*(ZDR31*(ZP11*ZUL21*complexconjugate(Y1d11) + ZP11*ZUL22*complexconjugate(Y1d21) + ZP12*ZUL23*complexconjugate(Y2d31)) + ZDR32*(ZP11*ZUL21*complexconjugate(Y1d12) + ZP11*ZUL22*complexconjugate(Y1d22) + ZP12*ZUL23*complexconjugate(Y2d32)) + ZDR33*(ZP11*ZUL21*complexconjugate(Y1d13) + ZP11*ZUL22*complexconjugate(Y1d23) + ZP12*ZUL23*complexconjugate(Y2d33)))', 
	 order = {'QED':1} ) 
 
GC_843 = Coupling(name = 'GC_843',
	 value = '-1*complex(0,1)*(Y1u11*ZP11*complexconjugate(ZDL31)*complexconjugate(ZUR21) + Y1u21*ZP11*complexconjugate(ZDL32)*complexconjugate(ZUR21) + Y1u12*ZP11*complexconjugate(ZDL31)*complexconjugate(ZUR22) + Y1u22*ZP11*complexconjugate(ZDL32)*complexconjugate(ZUR22) + Y2u33*ZP12*complexconjugate(ZDL33)*complexconjugate(ZUR23))', 
	 order = {'QED':1} ) 
 
GC_844 = Coupling(name = 'GC_844',
	 value = '-1*complex(0,1)*(ZDR31*(ZP21*ZUL21*complexconjugate(Y1d11) + ZP21*ZUL22*complexconjugate(Y1d21) + ZP22*ZUL23*complexconjugate(Y2d31)) + ZDR32*(ZP21*ZUL21*complexconjugate(Y1d12) + ZP21*ZUL22*complexconjugate(Y1d22) + ZP22*ZUL23*complexconjugate(Y2d32)) + ZDR33*(ZP21*ZUL21*complexconjugate(Y1d13) + ZP21*ZUL22*complexconjugate(Y1d23) + ZP22*ZUL23*complexconjugate(Y2d33)))', 
	 order = {'QED':1} ) 
 
GC_845 = Coupling(name = 'GC_845',
	 value = '-1*complex(0,1)*(Y1u11*ZP21*complexconjugate(ZDL31)*complexconjugate(ZUR21) + Y1u21*ZP21*complexconjugate(ZDL32)*complexconjugate(ZUR21) + Y1u12*ZP21*complexconjugate(ZDL31)*complexconjugate(ZUR22) + Y1u22*ZP21*complexconjugate(ZDL32)*complexconjugate(ZUR22) + Y2u33*ZP22*complexconjugate(ZDL33)*complexconjugate(ZUR23))', 
	 order = {'QED':1} ) 
 
GC_846 = Coupling(name = 'GC_846',
	 value = '-1*complex(0,1)*(ZDR31*(ZP11*ZUL31*complexconjugate(Y1d11) + ZP11*ZUL32*complexconjugate(Y1d21) + ZP12*ZUL33*complexconjugate(Y2d31)) + ZDR32*(ZP11*ZUL31*complexconjugate(Y1d12) + ZP11*ZUL32*complexconjugate(Y1d22) + ZP12*ZUL33*complexconjugate(Y2d32)) + ZDR33*(ZP11*ZUL31*complexconjugate(Y1d13) + ZP11*ZUL32*complexconjugate(Y1d23) + ZP12*ZUL33*complexconjugate(Y2d33)))', 
	 order = {'QED':1} ) 
 
GC_847 = Coupling(name = 'GC_847',
	 value = '-1*complex(0,1)*(Y1u11*ZP11*complexconjugate(ZDL31)*complexconjugate(ZUR31) + Y1u21*ZP11*complexconjugate(ZDL32)*complexconjugate(ZUR31) + Y1u12*ZP11*complexconjugate(ZDL31)*complexconjugate(ZUR32) + Y1u22*ZP11*complexconjugate(ZDL32)*complexconjugate(ZUR32) + Y2u33*ZP12*complexconjugate(ZDL33)*complexconjugate(ZUR33))', 
	 order = {'QED':1} ) 
 
GC_848 = Coupling(name = 'GC_848',
	 value = '-1*complex(0,1)*(ZDR31*(ZP21*ZUL31*complexconjugate(Y1d11) + ZP21*ZUL32*complexconjugate(Y1d21) + ZP22*ZUL33*complexconjugate(Y2d31)) + ZDR32*(ZP21*ZUL31*complexconjugate(Y1d12) + ZP21*ZUL32*complexconjugate(Y1d22) + ZP22*ZUL33*complexconjugate(Y2d32)) + ZDR33*(ZP21*ZUL31*complexconjugate(Y1d13) + ZP21*ZUL32*complexconjugate(Y1d23) + ZP22*ZUL33*complexconjugate(Y2d33)))', 
	 order = {'QED':1} ) 
 
GC_849 = Coupling(name = 'GC_849',
	 value = '-1*complex(0,1)*(Y1u11*ZP21*complexconjugate(ZDL31)*complexconjugate(ZUR31) + Y1u21*ZP21*complexconjugate(ZDL32)*complexconjugate(ZUR31) + Y1u12*ZP21*complexconjugate(ZDL31)*complexconjugate(ZUR32) + Y1u22*ZP21*complexconjugate(ZDL32)*complexconjugate(ZUR32) + Y2u33*ZP22*complexconjugate(ZDL33)*complexconjugate(ZUR33))', 
	 order = {'QED':1} ) 
 
GC_850 = Coupling(name = 'GC_850',
	 value = '(1./2.*complex(0,1)*(Vv14*Vv16*ZH13*complexconjugate(C13) + Vv15*Vv16*ZH13*complexconjugate(C23) + Vv14*Vv16*ZH13*complexconjugate(C31) + Vv15*Vv16*ZH13*complexconjugate(C32) + 2*Vv11*Vv14*ZH11*complexconjugate(Y1n11) + 2*Vv11*Vv15*ZH11*complexconjugate(Y1n12) + 2*Vv12*Vv14*ZH11*complexconjugate(Y1n21) + Vv14*(ZH13*(-2*Vv14*complexconjugate(BB11) + Vv15*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv16*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv11*ZH11*complexconjugate(Y1n11) + 2*Vv12*ZH11*complexconjugate(Y1n21)) + 2*Vv12*Vv15*ZH11*complexconjugate(Y1n22) + Vv15*(ZH13*(Vv14*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv15*complexconjugate(BB22) + Vv16*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv11*ZH11*complexconjugate(Y1n12) + 2*Vv12*ZH11*complexconjugate(Y1n22)) + 4*Vv13*Vv16*ZH12*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_851 = Coupling(name = 'GC_851',
	 value = '(1./2.*complex(0,1)*(4*Y1n11*ZH11*complexconjugate(Vv11)*complexconjugate(Vv14) + 4*Y1n21*ZH11*complexconjugate(Vv12)*complexconjugate(Vv14) - 2*BB11*ZH13*complexconjugate(Vv14)**2 + 4*Y1n12*ZH11*complexconjugate(Vv11)*complexconjugate(Vv15) + 4*Y1n22*ZH11*complexconjugate(Vv12)*complexconjugate(Vv15) + 2*BB12*ZH13*complexconjugate(Vv14)*complexconjugate(Vv15) + 2*BB21*ZH13*complexconjugate(Vv14)*complexconjugate(Vv15) + 2*BB22*ZH13*complexconjugate(Vv15)**2 + 4*Y2n33*ZH12*complexconjugate(Vv13)*complexconjugate(Vv16) + 2*C13*ZH13*complexconjugate(Vv14)*complexconjugate(Vv16) + 2*C31*ZH13*complexconjugate(Vv14)*complexconjugate(Vv16) + 2*C23*ZH13*complexconjugate(Vv15)*complexconjugate(Vv16) + 2*C32*ZH13*complexconjugate(Vv15)*complexconjugate(Vv16)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_852 = Coupling(name = 'GC_852',
	 value = '(1./2.*complex(0,1)*(Vv14*Vv16*ZH23*complexconjugate(C13) + Vv15*Vv16*ZH23*complexconjugate(C23) + Vv14*Vv16*ZH23*complexconjugate(C31) + Vv15*Vv16*ZH23*complexconjugate(C32) + 2*Vv11*Vv14*ZH21*complexconjugate(Y1n11) + 2*Vv11*Vv15*ZH21*complexconjugate(Y1n12) + 2*Vv12*Vv14*ZH21*complexconjugate(Y1n21) + Vv14*(ZH23*(-2*Vv14*complexconjugate(BB11) + Vv15*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv16*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv11*ZH21*complexconjugate(Y1n11) + 2*Vv12*ZH21*complexconjugate(Y1n21)) + 2*Vv12*Vv15*ZH21*complexconjugate(Y1n22) + Vv15*(ZH23*(Vv14*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv15*complexconjugate(BB22) + Vv16*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv11*ZH21*complexconjugate(Y1n12) + 2*Vv12*ZH21*complexconjugate(Y1n22)) + 4*Vv13*Vv16*ZH22*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_853 = Coupling(name = 'GC_853',
	 value = '(1./2.*complex(0,1)*(4*Y1n11*ZH21*complexconjugate(Vv11)*complexconjugate(Vv14) + 4*Y1n21*ZH21*complexconjugate(Vv12)*complexconjugate(Vv14) - 2*BB11*ZH23*complexconjugate(Vv14)**2 + 4*Y1n12*ZH21*complexconjugate(Vv11)*complexconjugate(Vv15) + 4*Y1n22*ZH21*complexconjugate(Vv12)*complexconjugate(Vv15) + 2*BB12*ZH23*complexconjugate(Vv14)*complexconjugate(Vv15) + 2*BB21*ZH23*complexconjugate(Vv14)*complexconjugate(Vv15) + 2*BB22*ZH23*complexconjugate(Vv15)**2 + 4*Y2n33*ZH22*complexconjugate(Vv13)*complexconjugate(Vv16) + 2*C13*ZH23*complexconjugate(Vv14)*complexconjugate(Vv16) + 2*C31*ZH23*complexconjugate(Vv14)*complexconjugate(Vv16) + 2*C23*ZH23*complexconjugate(Vv15)*complexconjugate(Vv16) + 2*C32*ZH23*complexconjugate(Vv15)*complexconjugate(Vv16)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_854 = Coupling(name = 'GC_854',
	 value = '(1./2.*complex(0,1)*(Vv14*Vv16*ZH33*complexconjugate(C13) + Vv15*Vv16*ZH33*complexconjugate(C23) + Vv14*Vv16*ZH33*complexconjugate(C31) + Vv15*Vv16*ZH33*complexconjugate(C32) + 2*Vv11*Vv14*ZH31*complexconjugate(Y1n11) + 2*Vv11*Vv15*ZH31*complexconjugate(Y1n12) + 2*Vv12*Vv14*ZH31*complexconjugate(Y1n21) + Vv14*(ZH33*(-2*Vv14*complexconjugate(BB11) + Vv15*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv16*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv11*ZH31*complexconjugate(Y1n11) + 2*Vv12*ZH31*complexconjugate(Y1n21)) + 2*Vv12*Vv15*ZH31*complexconjugate(Y1n22) + Vv15*(ZH33*(Vv14*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv15*complexconjugate(BB22) + Vv16*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv11*ZH31*complexconjugate(Y1n12) + 2*Vv12*ZH31*complexconjugate(Y1n22)) + 4*Vv13*Vv16*ZH32*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_855 = Coupling(name = 'GC_855',
	 value = '(1./2.*complex(0,1)*(4*Y1n11*ZH31*complexconjugate(Vv11)*complexconjugate(Vv14) + 4*Y1n21*ZH31*complexconjugate(Vv12)*complexconjugate(Vv14) - 2*BB11*ZH33*complexconjugate(Vv14)**2 + 4*Y1n12*ZH31*complexconjugate(Vv11)*complexconjugate(Vv15) + 4*Y1n22*ZH31*complexconjugate(Vv12)*complexconjugate(Vv15) + 2*BB12*ZH33*complexconjugate(Vv14)*complexconjugate(Vv15) + 2*BB21*ZH33*complexconjugate(Vv14)*complexconjugate(Vv15) + 2*BB22*ZH33*complexconjugate(Vv15)**2 + 4*Y2n33*ZH32*complexconjugate(Vv13)*complexconjugate(Vv16) + 2*C13*ZH33*complexconjugate(Vv14)*complexconjugate(Vv16) + 2*C31*ZH33*complexconjugate(Vv14)*complexconjugate(Vv16) + 2*C23*ZH33*complexconjugate(Vv15)*complexconjugate(Vv16) + 2*C32*ZH33*complexconjugate(Vv15)*complexconjugate(Vv16)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_856 = Coupling(name = 'GC_856',
	 value = '(1./2.*complex(0,1)*(Vv16*Vv24*ZH13*complexconjugate(C13) + Vv16*Vv25*ZH13*complexconjugate(C23) + Vv16*Vv24*ZH13*complexconjugate(C31) + Vv16*Vv25*ZH13*complexconjugate(C32) + 2*Vv11*Vv24*ZH11*complexconjugate(Y1n11) + 2*Vv11*Vv25*ZH11*complexconjugate(Y1n12) + 2*Vv12*Vv24*ZH11*complexconjugate(Y1n21) + Vv14*(ZH13*(-2*Vv24*complexconjugate(BB11) + Vv25*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv26*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv21*ZH11*complexconjugate(Y1n11) + 2*Vv22*ZH11*complexconjugate(Y1n21)) + 2*Vv12*Vv25*ZH11*complexconjugate(Y1n22) + Vv15*(ZH13*(Vv24*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv25*complexconjugate(BB22) + Vv26*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv21*ZH11*complexconjugate(Y1n12) + 2*Vv22*ZH11*complexconjugate(Y1n22)) + 2*Vv16*Vv23*ZH12*complexconjugate(Y2n33) + 2*Vv13*Vv26*ZH12*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_857 = Coupling(name = 'GC_857',
	 value = '(1./2.*complex(0,1)*(2*Y1n21*ZH11*complexconjugate(Vv14)*complexconjugate(Vv22) + 2*Y1n22*ZH11*complexconjugate(Vv15)*complexconjugate(Vv22) + 2*Y2n33*ZH12*complexconjugate(Vv16)*complexconjugate(Vv23) + 2*Y1n21*ZH11*complexconjugate(Vv12)*complexconjugate(Vv24) - 2*BB11*ZH13*complexconjugate(Vv14)*complexconjugate(Vv24) + BB12*ZH13*complexconjugate(Vv15)*complexconjugate(Vv24) + BB21*ZH13*complexconjugate(Vv15)*complexconjugate(Vv24) + C13*ZH13*complexconjugate(Vv16)*complexconjugate(Vv24) + C31*ZH13*complexconjugate(Vv16)*complexconjugate(Vv24) + 2*Y1n11*ZH11*(complexconjugate(Vv14)*complexconjugate(Vv21) + complexconjugate(Vv11)*complexconjugate(Vv24)) + 2*Y1n22*ZH11*complexconjugate(Vv12)*complexconjugate(Vv25) + BB12*ZH13*complexconjugate(Vv14)*complexconjugate(Vv25) + BB21*ZH13*complexconjugate(Vv14)*complexconjugate(Vv25) + 2*BB22*ZH13*complexconjugate(Vv15)*complexconjugate(Vv25) + C23*ZH13*complexconjugate(Vv16)*complexconjugate(Vv25) + C32*ZH13*complexconjugate(Vv16)*complexconjugate(Vv25) + 2*Y1n12*ZH11*(complexconjugate(Vv15)*complexconjugate(Vv21) + complexconjugate(Vv11)*complexconjugate(Vv25)) + 2*Y2n33*ZH12*complexconjugate(Vv13)*complexconjugate(Vv26) + C13*ZH13*complexconjugate(Vv14)*complexconjugate(Vv26) + C31*ZH13*complexconjugate(Vv14)*complexconjugate(Vv26) + C23*ZH13*complexconjugate(Vv15)*complexconjugate(Vv26) + C32*ZH13*complexconjugate(Vv15)*complexconjugate(Vv26)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_858 = Coupling(name = 'GC_858',
	 value = '(1./2.*complex(0,1)*(Vv16*Vv24*ZH23*complexconjugate(C13) + Vv16*Vv25*ZH23*complexconjugate(C23) + Vv16*Vv24*ZH23*complexconjugate(C31) + Vv16*Vv25*ZH23*complexconjugate(C32) + 2*Vv11*Vv24*ZH21*complexconjugate(Y1n11) + 2*Vv11*Vv25*ZH21*complexconjugate(Y1n12) + 2*Vv12*Vv24*ZH21*complexconjugate(Y1n21) + Vv14*(ZH23*(-2*Vv24*complexconjugate(BB11) + Vv25*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv26*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv21*ZH21*complexconjugate(Y1n11) + 2*Vv22*ZH21*complexconjugate(Y1n21)) + 2*Vv12*Vv25*ZH21*complexconjugate(Y1n22) + Vv15*(ZH23*(Vv24*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv25*complexconjugate(BB22) + Vv26*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv21*ZH21*complexconjugate(Y1n12) + 2*Vv22*ZH21*complexconjugate(Y1n22)) + 2*Vv16*Vv23*ZH22*complexconjugate(Y2n33) + 2*Vv13*Vv26*ZH22*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_859 = Coupling(name = 'GC_859',
	 value = '(1./2.*complex(0,1)*(2*Y1n21*ZH21*complexconjugate(Vv14)*complexconjugate(Vv22) + 2*Y1n22*ZH21*complexconjugate(Vv15)*complexconjugate(Vv22) + 2*Y2n33*ZH22*complexconjugate(Vv16)*complexconjugate(Vv23) + 2*Y1n21*ZH21*complexconjugate(Vv12)*complexconjugate(Vv24) - 2*BB11*ZH23*complexconjugate(Vv14)*complexconjugate(Vv24) + BB12*ZH23*complexconjugate(Vv15)*complexconjugate(Vv24) + BB21*ZH23*complexconjugate(Vv15)*complexconjugate(Vv24) + C13*ZH23*complexconjugate(Vv16)*complexconjugate(Vv24) + C31*ZH23*complexconjugate(Vv16)*complexconjugate(Vv24) + 2*Y1n11*ZH21*(complexconjugate(Vv14)*complexconjugate(Vv21) + complexconjugate(Vv11)*complexconjugate(Vv24)) + 2*Y1n22*ZH21*complexconjugate(Vv12)*complexconjugate(Vv25) + BB12*ZH23*complexconjugate(Vv14)*complexconjugate(Vv25) + BB21*ZH23*complexconjugate(Vv14)*complexconjugate(Vv25) + 2*BB22*ZH23*complexconjugate(Vv15)*complexconjugate(Vv25) + C23*ZH23*complexconjugate(Vv16)*complexconjugate(Vv25) + C32*ZH23*complexconjugate(Vv16)*complexconjugate(Vv25) + 2*Y1n12*ZH21*(complexconjugate(Vv15)*complexconjugate(Vv21) + complexconjugate(Vv11)*complexconjugate(Vv25)) + 2*Y2n33*ZH22*complexconjugate(Vv13)*complexconjugate(Vv26) + C13*ZH23*complexconjugate(Vv14)*complexconjugate(Vv26) + C31*ZH23*complexconjugate(Vv14)*complexconjugate(Vv26) + C23*ZH23*complexconjugate(Vv15)*complexconjugate(Vv26) + C32*ZH23*complexconjugate(Vv15)*complexconjugate(Vv26)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_860 = Coupling(name = 'GC_860',
	 value = '(1./2.*complex(0,1)*(Vv16*Vv24*ZH33*complexconjugate(C13) + Vv16*Vv25*ZH33*complexconjugate(C23) + Vv16*Vv24*ZH33*complexconjugate(C31) + Vv16*Vv25*ZH33*complexconjugate(C32) + 2*Vv11*Vv24*ZH31*complexconjugate(Y1n11) + 2*Vv11*Vv25*ZH31*complexconjugate(Y1n12) + 2*Vv12*Vv24*ZH31*complexconjugate(Y1n21) + Vv14*(ZH33*(-2*Vv24*complexconjugate(BB11) + Vv25*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv26*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv21*ZH31*complexconjugate(Y1n11) + 2*Vv22*ZH31*complexconjugate(Y1n21)) + 2*Vv12*Vv25*ZH31*complexconjugate(Y1n22) + Vv15*(ZH33*(Vv24*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv25*complexconjugate(BB22) + Vv26*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv21*ZH31*complexconjugate(Y1n12) + 2*Vv22*ZH31*complexconjugate(Y1n22)) + 2*Vv16*Vv23*ZH32*complexconjugate(Y2n33) + 2*Vv13*Vv26*ZH32*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_861 = Coupling(name = 'GC_861',
	 value = '(1./2.*complex(0,1)*(2*Y1n21*ZH31*complexconjugate(Vv14)*complexconjugate(Vv22) + 2*Y1n22*ZH31*complexconjugate(Vv15)*complexconjugate(Vv22) + 2*Y2n33*ZH32*complexconjugate(Vv16)*complexconjugate(Vv23) + 2*Y1n21*ZH31*complexconjugate(Vv12)*complexconjugate(Vv24) - 2*BB11*ZH33*complexconjugate(Vv14)*complexconjugate(Vv24) + BB12*ZH33*complexconjugate(Vv15)*complexconjugate(Vv24) + BB21*ZH33*complexconjugate(Vv15)*complexconjugate(Vv24) + C13*ZH33*complexconjugate(Vv16)*complexconjugate(Vv24) + C31*ZH33*complexconjugate(Vv16)*complexconjugate(Vv24) + 2*Y1n11*ZH31*(complexconjugate(Vv14)*complexconjugate(Vv21) + complexconjugate(Vv11)*complexconjugate(Vv24)) + 2*Y1n22*ZH31*complexconjugate(Vv12)*complexconjugate(Vv25) + BB12*ZH33*complexconjugate(Vv14)*complexconjugate(Vv25) + BB21*ZH33*complexconjugate(Vv14)*complexconjugate(Vv25) + 2*BB22*ZH33*complexconjugate(Vv15)*complexconjugate(Vv25) + C23*ZH33*complexconjugate(Vv16)*complexconjugate(Vv25) + C32*ZH33*complexconjugate(Vv16)*complexconjugate(Vv25) + 2*Y1n12*ZH31*(complexconjugate(Vv15)*complexconjugate(Vv21) + complexconjugate(Vv11)*complexconjugate(Vv25)) + 2*Y2n33*ZH32*complexconjugate(Vv13)*complexconjugate(Vv26) + C13*ZH33*complexconjugate(Vv14)*complexconjugate(Vv26) + C31*ZH33*complexconjugate(Vv14)*complexconjugate(Vv26) + C23*ZH33*complexconjugate(Vv15)*complexconjugate(Vv26) + C32*ZH33*complexconjugate(Vv15)*complexconjugate(Vv26)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_862 = Coupling(name = 'GC_862',
	 value = '(1./2.*complex(0,1)*(Vv16*Vv34*ZH13*complexconjugate(C13) + Vv16*Vv35*ZH13*complexconjugate(C23) + Vv16*Vv34*ZH13*complexconjugate(C31) + Vv16*Vv35*ZH13*complexconjugate(C32) + 2*Vv11*Vv34*ZH11*complexconjugate(Y1n11) + 2*Vv11*Vv35*ZH11*complexconjugate(Y1n12) + 2*Vv12*Vv34*ZH11*complexconjugate(Y1n21) + Vv14*(ZH13*(-2*Vv34*complexconjugate(BB11) + Vv35*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv36*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv31*ZH11*complexconjugate(Y1n11) + 2*Vv32*ZH11*complexconjugate(Y1n21)) + 2*Vv12*Vv35*ZH11*complexconjugate(Y1n22) + Vv15*(ZH13*(Vv34*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv35*complexconjugate(BB22) + Vv36*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv31*ZH11*complexconjugate(Y1n12) + 2*Vv32*ZH11*complexconjugate(Y1n22)) + 2*Vv16*Vv33*ZH12*complexconjugate(Y2n33) + 2*Vv13*Vv36*ZH12*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_863 = Coupling(name = 'GC_863',
	 value = '(1./2.*complex(0,1)*(2*Y1n21*ZH11*complexconjugate(Vv14)*complexconjugate(Vv32) + 2*Y1n22*ZH11*complexconjugate(Vv15)*complexconjugate(Vv32) + 2*Y2n33*ZH12*complexconjugate(Vv16)*complexconjugate(Vv33) + 2*Y1n21*ZH11*complexconjugate(Vv12)*complexconjugate(Vv34) - 2*BB11*ZH13*complexconjugate(Vv14)*complexconjugate(Vv34) + BB12*ZH13*complexconjugate(Vv15)*complexconjugate(Vv34) + BB21*ZH13*complexconjugate(Vv15)*complexconjugate(Vv34) + C13*ZH13*complexconjugate(Vv16)*complexconjugate(Vv34) + C31*ZH13*complexconjugate(Vv16)*complexconjugate(Vv34) + 2*Y1n11*ZH11*(complexconjugate(Vv14)*complexconjugate(Vv31) + complexconjugate(Vv11)*complexconjugate(Vv34)) + 2*Y1n22*ZH11*complexconjugate(Vv12)*complexconjugate(Vv35) + BB12*ZH13*complexconjugate(Vv14)*complexconjugate(Vv35) + BB21*ZH13*complexconjugate(Vv14)*complexconjugate(Vv35) + 2*BB22*ZH13*complexconjugate(Vv15)*complexconjugate(Vv35) + C23*ZH13*complexconjugate(Vv16)*complexconjugate(Vv35) + C32*ZH13*complexconjugate(Vv16)*complexconjugate(Vv35) + 2*Y1n12*ZH11*(complexconjugate(Vv15)*complexconjugate(Vv31) + complexconjugate(Vv11)*complexconjugate(Vv35)) + 2*Y2n33*ZH12*complexconjugate(Vv13)*complexconjugate(Vv36) + C13*ZH13*complexconjugate(Vv14)*complexconjugate(Vv36) + C31*ZH13*complexconjugate(Vv14)*complexconjugate(Vv36) + C23*ZH13*complexconjugate(Vv15)*complexconjugate(Vv36) + C32*ZH13*complexconjugate(Vv15)*complexconjugate(Vv36)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_864 = Coupling(name = 'GC_864',
	 value = '(1./2.*complex(0,1)*(Vv16*Vv34*ZH23*complexconjugate(C13) + Vv16*Vv35*ZH23*complexconjugate(C23) + Vv16*Vv34*ZH23*complexconjugate(C31) + Vv16*Vv35*ZH23*complexconjugate(C32) + 2*Vv11*Vv34*ZH21*complexconjugate(Y1n11) + 2*Vv11*Vv35*ZH21*complexconjugate(Y1n12) + 2*Vv12*Vv34*ZH21*complexconjugate(Y1n21) + Vv14*(ZH23*(-2*Vv34*complexconjugate(BB11) + Vv35*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv36*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv31*ZH21*complexconjugate(Y1n11) + 2*Vv32*ZH21*complexconjugate(Y1n21)) + 2*Vv12*Vv35*ZH21*complexconjugate(Y1n22) + Vv15*(ZH23*(Vv34*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv35*complexconjugate(BB22) + Vv36*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv31*ZH21*complexconjugate(Y1n12) + 2*Vv32*ZH21*complexconjugate(Y1n22)) + 2*Vv16*Vv33*ZH22*complexconjugate(Y2n33) + 2*Vv13*Vv36*ZH22*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_865 = Coupling(name = 'GC_865',
	 value = '(1./2.*complex(0,1)*(2*Y1n21*ZH21*complexconjugate(Vv14)*complexconjugate(Vv32) + 2*Y1n22*ZH21*complexconjugate(Vv15)*complexconjugate(Vv32) + 2*Y2n33*ZH22*complexconjugate(Vv16)*complexconjugate(Vv33) + 2*Y1n21*ZH21*complexconjugate(Vv12)*complexconjugate(Vv34) - 2*BB11*ZH23*complexconjugate(Vv14)*complexconjugate(Vv34) + BB12*ZH23*complexconjugate(Vv15)*complexconjugate(Vv34) + BB21*ZH23*complexconjugate(Vv15)*complexconjugate(Vv34) + C13*ZH23*complexconjugate(Vv16)*complexconjugate(Vv34) + C31*ZH23*complexconjugate(Vv16)*complexconjugate(Vv34) + 2*Y1n11*ZH21*(complexconjugate(Vv14)*complexconjugate(Vv31) + complexconjugate(Vv11)*complexconjugate(Vv34)) + 2*Y1n22*ZH21*complexconjugate(Vv12)*complexconjugate(Vv35) + BB12*ZH23*complexconjugate(Vv14)*complexconjugate(Vv35) + BB21*ZH23*complexconjugate(Vv14)*complexconjugate(Vv35) + 2*BB22*ZH23*complexconjugate(Vv15)*complexconjugate(Vv35) + C23*ZH23*complexconjugate(Vv16)*complexconjugate(Vv35) + C32*ZH23*complexconjugate(Vv16)*complexconjugate(Vv35) + 2*Y1n12*ZH21*(complexconjugate(Vv15)*complexconjugate(Vv31) + complexconjugate(Vv11)*complexconjugate(Vv35)) + 2*Y2n33*ZH22*complexconjugate(Vv13)*complexconjugate(Vv36) + C13*ZH23*complexconjugate(Vv14)*complexconjugate(Vv36) + C31*ZH23*complexconjugate(Vv14)*complexconjugate(Vv36) + C23*ZH23*complexconjugate(Vv15)*complexconjugate(Vv36) + C32*ZH23*complexconjugate(Vv15)*complexconjugate(Vv36)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_866 = Coupling(name = 'GC_866',
	 value = '(1./2.*complex(0,1)*(Vv16*Vv34*ZH33*complexconjugate(C13) + Vv16*Vv35*ZH33*complexconjugate(C23) + Vv16*Vv34*ZH33*complexconjugate(C31) + Vv16*Vv35*ZH33*complexconjugate(C32) + 2*Vv11*Vv34*ZH31*complexconjugate(Y1n11) + 2*Vv11*Vv35*ZH31*complexconjugate(Y1n12) + 2*Vv12*Vv34*ZH31*complexconjugate(Y1n21) + Vv14*(ZH33*(-2*Vv34*complexconjugate(BB11) + Vv35*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv36*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv31*ZH31*complexconjugate(Y1n11) + 2*Vv32*ZH31*complexconjugate(Y1n21)) + 2*Vv12*Vv35*ZH31*complexconjugate(Y1n22) + Vv15*(ZH33*(Vv34*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv35*complexconjugate(BB22) + Vv36*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv31*ZH31*complexconjugate(Y1n12) + 2*Vv32*ZH31*complexconjugate(Y1n22)) + 2*Vv16*Vv33*ZH32*complexconjugate(Y2n33) + 2*Vv13*Vv36*ZH32*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_867 = Coupling(name = 'GC_867',
	 value = '(1./2.*complex(0,1)*(2*Y1n21*ZH31*complexconjugate(Vv14)*complexconjugate(Vv32) + 2*Y1n22*ZH31*complexconjugate(Vv15)*complexconjugate(Vv32) + 2*Y2n33*ZH32*complexconjugate(Vv16)*complexconjugate(Vv33) + 2*Y1n21*ZH31*complexconjugate(Vv12)*complexconjugate(Vv34) - 2*BB11*ZH33*complexconjugate(Vv14)*complexconjugate(Vv34) + BB12*ZH33*complexconjugate(Vv15)*complexconjugate(Vv34) + BB21*ZH33*complexconjugate(Vv15)*complexconjugate(Vv34) + C13*ZH33*complexconjugate(Vv16)*complexconjugate(Vv34) + C31*ZH33*complexconjugate(Vv16)*complexconjugate(Vv34) + 2*Y1n11*ZH31*(complexconjugate(Vv14)*complexconjugate(Vv31) + complexconjugate(Vv11)*complexconjugate(Vv34)) + 2*Y1n22*ZH31*complexconjugate(Vv12)*complexconjugate(Vv35) + BB12*ZH33*complexconjugate(Vv14)*complexconjugate(Vv35) + BB21*ZH33*complexconjugate(Vv14)*complexconjugate(Vv35) + 2*BB22*ZH33*complexconjugate(Vv15)*complexconjugate(Vv35) + C23*ZH33*complexconjugate(Vv16)*complexconjugate(Vv35) + C32*ZH33*complexconjugate(Vv16)*complexconjugate(Vv35) + 2*Y1n12*ZH31*(complexconjugate(Vv15)*complexconjugate(Vv31) + complexconjugate(Vv11)*complexconjugate(Vv35)) + 2*Y2n33*ZH32*complexconjugate(Vv13)*complexconjugate(Vv36) + C13*ZH33*complexconjugate(Vv14)*complexconjugate(Vv36) + C31*ZH33*complexconjugate(Vv14)*complexconjugate(Vv36) + C23*ZH33*complexconjugate(Vv15)*complexconjugate(Vv36) + C32*ZH33*complexconjugate(Vv15)*complexconjugate(Vv36)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_868 = Coupling(name = 'GC_868',
	 value = '(1./2.*complex(0,1)*(Vv16*Vv44*ZH13*complexconjugate(C13) + Vv16*Vv45*ZH13*complexconjugate(C23) + Vv16*Vv44*ZH13*complexconjugate(C31) + Vv16*Vv45*ZH13*complexconjugate(C32) + 2*Vv11*Vv44*ZH11*complexconjugate(Y1n11) + 2*Vv11*Vv45*ZH11*complexconjugate(Y1n12) + 2*Vv12*Vv44*ZH11*complexconjugate(Y1n21) + Vv14*(ZH13*(-2*Vv44*complexconjugate(BB11) + Vv45*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv46*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv41*ZH11*complexconjugate(Y1n11) + 2*Vv42*ZH11*complexconjugate(Y1n21)) + 2*Vv12*Vv45*ZH11*complexconjugate(Y1n22) + Vv15*(ZH13*(Vv44*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv45*complexconjugate(BB22) + Vv46*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv41*ZH11*complexconjugate(Y1n12) + 2*Vv42*ZH11*complexconjugate(Y1n22)) + 2*Vv16*Vv43*ZH12*complexconjugate(Y2n33) + 2*Vv13*Vv46*ZH12*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_869 = Coupling(name = 'GC_869',
	 value = '(1./2.*complex(0,1)*(2*Y1n21*ZH11*complexconjugate(Vv14)*complexconjugate(Vv42) + 2*Y1n22*ZH11*complexconjugate(Vv15)*complexconjugate(Vv42) + 2*Y2n33*ZH12*complexconjugate(Vv16)*complexconjugate(Vv43) + 2*Y1n21*ZH11*complexconjugate(Vv12)*complexconjugate(Vv44) - 2*BB11*ZH13*complexconjugate(Vv14)*complexconjugate(Vv44) + BB12*ZH13*complexconjugate(Vv15)*complexconjugate(Vv44) + BB21*ZH13*complexconjugate(Vv15)*complexconjugate(Vv44) + C13*ZH13*complexconjugate(Vv16)*complexconjugate(Vv44) + C31*ZH13*complexconjugate(Vv16)*complexconjugate(Vv44) + 2*Y1n11*ZH11*(complexconjugate(Vv14)*complexconjugate(Vv41) + complexconjugate(Vv11)*complexconjugate(Vv44)) + 2*Y1n22*ZH11*complexconjugate(Vv12)*complexconjugate(Vv45) + BB12*ZH13*complexconjugate(Vv14)*complexconjugate(Vv45) + BB21*ZH13*complexconjugate(Vv14)*complexconjugate(Vv45) + 2*BB22*ZH13*complexconjugate(Vv15)*complexconjugate(Vv45) + C23*ZH13*complexconjugate(Vv16)*complexconjugate(Vv45) + C32*ZH13*complexconjugate(Vv16)*complexconjugate(Vv45) + 2*Y1n12*ZH11*(complexconjugate(Vv15)*complexconjugate(Vv41) + complexconjugate(Vv11)*complexconjugate(Vv45)) + 2*Y2n33*ZH12*complexconjugate(Vv13)*complexconjugate(Vv46) + C13*ZH13*complexconjugate(Vv14)*complexconjugate(Vv46) + C31*ZH13*complexconjugate(Vv14)*complexconjugate(Vv46) + C23*ZH13*complexconjugate(Vv15)*complexconjugate(Vv46) + C32*ZH13*complexconjugate(Vv15)*complexconjugate(Vv46)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_870 = Coupling(name = 'GC_870',
	 value = '(1./2.*complex(0,1)*(Vv16*Vv44*ZH23*complexconjugate(C13) + Vv16*Vv45*ZH23*complexconjugate(C23) + Vv16*Vv44*ZH23*complexconjugate(C31) + Vv16*Vv45*ZH23*complexconjugate(C32) + 2*Vv11*Vv44*ZH21*complexconjugate(Y1n11) + 2*Vv11*Vv45*ZH21*complexconjugate(Y1n12) + 2*Vv12*Vv44*ZH21*complexconjugate(Y1n21) + Vv14*(ZH23*(-2*Vv44*complexconjugate(BB11) + Vv45*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv46*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv41*ZH21*complexconjugate(Y1n11) + 2*Vv42*ZH21*complexconjugate(Y1n21)) + 2*Vv12*Vv45*ZH21*complexconjugate(Y1n22) + Vv15*(ZH23*(Vv44*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv45*complexconjugate(BB22) + Vv46*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv41*ZH21*complexconjugate(Y1n12) + 2*Vv42*ZH21*complexconjugate(Y1n22)) + 2*Vv16*Vv43*ZH22*complexconjugate(Y2n33) + 2*Vv13*Vv46*ZH22*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_871 = Coupling(name = 'GC_871',
	 value = '(1./2.*complex(0,1)*(2*Y1n21*ZH21*complexconjugate(Vv14)*complexconjugate(Vv42) + 2*Y1n22*ZH21*complexconjugate(Vv15)*complexconjugate(Vv42) + 2*Y2n33*ZH22*complexconjugate(Vv16)*complexconjugate(Vv43) + 2*Y1n21*ZH21*complexconjugate(Vv12)*complexconjugate(Vv44) - 2*BB11*ZH23*complexconjugate(Vv14)*complexconjugate(Vv44) + BB12*ZH23*complexconjugate(Vv15)*complexconjugate(Vv44) + BB21*ZH23*complexconjugate(Vv15)*complexconjugate(Vv44) + C13*ZH23*complexconjugate(Vv16)*complexconjugate(Vv44) + C31*ZH23*complexconjugate(Vv16)*complexconjugate(Vv44) + 2*Y1n11*ZH21*(complexconjugate(Vv14)*complexconjugate(Vv41) + complexconjugate(Vv11)*complexconjugate(Vv44)) + 2*Y1n22*ZH21*complexconjugate(Vv12)*complexconjugate(Vv45) + BB12*ZH23*complexconjugate(Vv14)*complexconjugate(Vv45) + BB21*ZH23*complexconjugate(Vv14)*complexconjugate(Vv45) + 2*BB22*ZH23*complexconjugate(Vv15)*complexconjugate(Vv45) + C23*ZH23*complexconjugate(Vv16)*complexconjugate(Vv45) + C32*ZH23*complexconjugate(Vv16)*complexconjugate(Vv45) + 2*Y1n12*ZH21*(complexconjugate(Vv15)*complexconjugate(Vv41) + complexconjugate(Vv11)*complexconjugate(Vv45)) + 2*Y2n33*ZH22*complexconjugate(Vv13)*complexconjugate(Vv46) + C13*ZH23*complexconjugate(Vv14)*complexconjugate(Vv46) + C31*ZH23*complexconjugate(Vv14)*complexconjugate(Vv46) + C23*ZH23*complexconjugate(Vv15)*complexconjugate(Vv46) + C32*ZH23*complexconjugate(Vv15)*complexconjugate(Vv46)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_872 = Coupling(name = 'GC_872',
	 value = '(1./2.*complex(0,1)*(Vv16*Vv44*ZH33*complexconjugate(C13) + Vv16*Vv45*ZH33*complexconjugate(C23) + Vv16*Vv44*ZH33*complexconjugate(C31) + Vv16*Vv45*ZH33*complexconjugate(C32) + 2*Vv11*Vv44*ZH31*complexconjugate(Y1n11) + 2*Vv11*Vv45*ZH31*complexconjugate(Y1n12) + 2*Vv12*Vv44*ZH31*complexconjugate(Y1n21) + Vv14*(ZH33*(-2*Vv44*complexconjugate(BB11) + Vv45*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv46*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv41*ZH31*complexconjugate(Y1n11) + 2*Vv42*ZH31*complexconjugate(Y1n21)) + 2*Vv12*Vv45*ZH31*complexconjugate(Y1n22) + Vv15*(ZH33*(Vv44*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv45*complexconjugate(BB22) + Vv46*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv41*ZH31*complexconjugate(Y1n12) + 2*Vv42*ZH31*complexconjugate(Y1n22)) + 2*Vv16*Vv43*ZH32*complexconjugate(Y2n33) + 2*Vv13*Vv46*ZH32*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_873 = Coupling(name = 'GC_873',
	 value = '(1./2.*complex(0,1)*(2*Y1n21*ZH31*complexconjugate(Vv14)*complexconjugate(Vv42) + 2*Y1n22*ZH31*complexconjugate(Vv15)*complexconjugate(Vv42) + 2*Y2n33*ZH32*complexconjugate(Vv16)*complexconjugate(Vv43) + 2*Y1n21*ZH31*complexconjugate(Vv12)*complexconjugate(Vv44) - 2*BB11*ZH33*complexconjugate(Vv14)*complexconjugate(Vv44) + BB12*ZH33*complexconjugate(Vv15)*complexconjugate(Vv44) + BB21*ZH33*complexconjugate(Vv15)*complexconjugate(Vv44) + C13*ZH33*complexconjugate(Vv16)*complexconjugate(Vv44) + C31*ZH33*complexconjugate(Vv16)*complexconjugate(Vv44) + 2*Y1n11*ZH31*(complexconjugate(Vv14)*complexconjugate(Vv41) + complexconjugate(Vv11)*complexconjugate(Vv44)) + 2*Y1n22*ZH31*complexconjugate(Vv12)*complexconjugate(Vv45) + BB12*ZH33*complexconjugate(Vv14)*complexconjugate(Vv45) + BB21*ZH33*complexconjugate(Vv14)*complexconjugate(Vv45) + 2*BB22*ZH33*complexconjugate(Vv15)*complexconjugate(Vv45) + C23*ZH33*complexconjugate(Vv16)*complexconjugate(Vv45) + C32*ZH33*complexconjugate(Vv16)*complexconjugate(Vv45) + 2*Y1n12*ZH31*(complexconjugate(Vv15)*complexconjugate(Vv41) + complexconjugate(Vv11)*complexconjugate(Vv45)) + 2*Y2n33*ZH32*complexconjugate(Vv13)*complexconjugate(Vv46) + C13*ZH33*complexconjugate(Vv14)*complexconjugate(Vv46) + C31*ZH33*complexconjugate(Vv14)*complexconjugate(Vv46) + C23*ZH33*complexconjugate(Vv15)*complexconjugate(Vv46) + C32*ZH33*complexconjugate(Vv15)*complexconjugate(Vv46)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_874 = Coupling(name = 'GC_874',
	 value = '(1./2.*complex(0,1)*(Vv16*Vv54*ZH13*complexconjugate(C13) + Vv16*Vv55*ZH13*complexconjugate(C23) + Vv16*Vv54*ZH13*complexconjugate(C31) + Vv16*Vv55*ZH13*complexconjugate(C32) + 2*Vv11*Vv54*ZH11*complexconjugate(Y1n11) + 2*Vv11*Vv55*ZH11*complexconjugate(Y1n12) + 2*Vv12*Vv54*ZH11*complexconjugate(Y1n21) + Vv14*(ZH13*(-2*Vv54*complexconjugate(BB11) + Vv55*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv56*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv51*ZH11*complexconjugate(Y1n11) + 2*Vv52*ZH11*complexconjugate(Y1n21)) + 2*Vv12*Vv55*ZH11*complexconjugate(Y1n22) + Vv15*(ZH13*(Vv54*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv55*complexconjugate(BB22) + Vv56*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv51*ZH11*complexconjugate(Y1n12) + 2*Vv52*ZH11*complexconjugate(Y1n22)) + 2*Vv16*Vv53*ZH12*complexconjugate(Y2n33) + 2*Vv13*Vv56*ZH12*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_875 = Coupling(name = 'GC_875',
	 value = '(1./2.*complex(0,1)*(2*Y1n21*ZH11*complexconjugate(Vv14)*complexconjugate(Vv52) + 2*Y1n22*ZH11*complexconjugate(Vv15)*complexconjugate(Vv52) + 2*Y2n33*ZH12*complexconjugate(Vv16)*complexconjugate(Vv53) + 2*Y1n21*ZH11*complexconjugate(Vv12)*complexconjugate(Vv54) - 2*BB11*ZH13*complexconjugate(Vv14)*complexconjugate(Vv54) + BB12*ZH13*complexconjugate(Vv15)*complexconjugate(Vv54) + BB21*ZH13*complexconjugate(Vv15)*complexconjugate(Vv54) + C13*ZH13*complexconjugate(Vv16)*complexconjugate(Vv54) + C31*ZH13*complexconjugate(Vv16)*complexconjugate(Vv54) + 2*Y1n11*ZH11*(complexconjugate(Vv14)*complexconjugate(Vv51) + complexconjugate(Vv11)*complexconjugate(Vv54)) + 2*Y1n22*ZH11*complexconjugate(Vv12)*complexconjugate(Vv55) + BB12*ZH13*complexconjugate(Vv14)*complexconjugate(Vv55) + BB21*ZH13*complexconjugate(Vv14)*complexconjugate(Vv55) + 2*BB22*ZH13*complexconjugate(Vv15)*complexconjugate(Vv55) + C23*ZH13*complexconjugate(Vv16)*complexconjugate(Vv55) + C32*ZH13*complexconjugate(Vv16)*complexconjugate(Vv55) + 2*Y1n12*ZH11*(complexconjugate(Vv15)*complexconjugate(Vv51) + complexconjugate(Vv11)*complexconjugate(Vv55)) + 2*Y2n33*ZH12*complexconjugate(Vv13)*complexconjugate(Vv56) + C13*ZH13*complexconjugate(Vv14)*complexconjugate(Vv56) + C31*ZH13*complexconjugate(Vv14)*complexconjugate(Vv56) + C23*ZH13*complexconjugate(Vv15)*complexconjugate(Vv56) + C32*ZH13*complexconjugate(Vv15)*complexconjugate(Vv56)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_876 = Coupling(name = 'GC_876',
	 value = '(1./2.*complex(0,1)*(Vv16*Vv54*ZH23*complexconjugate(C13) + Vv16*Vv55*ZH23*complexconjugate(C23) + Vv16*Vv54*ZH23*complexconjugate(C31) + Vv16*Vv55*ZH23*complexconjugate(C32) + 2*Vv11*Vv54*ZH21*complexconjugate(Y1n11) + 2*Vv11*Vv55*ZH21*complexconjugate(Y1n12) + 2*Vv12*Vv54*ZH21*complexconjugate(Y1n21) + Vv14*(ZH23*(-2*Vv54*complexconjugate(BB11) + Vv55*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv56*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv51*ZH21*complexconjugate(Y1n11) + 2*Vv52*ZH21*complexconjugate(Y1n21)) + 2*Vv12*Vv55*ZH21*complexconjugate(Y1n22) + Vv15*(ZH23*(Vv54*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv55*complexconjugate(BB22) + Vv56*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv51*ZH21*complexconjugate(Y1n12) + 2*Vv52*ZH21*complexconjugate(Y1n22)) + 2*Vv16*Vv53*ZH22*complexconjugate(Y2n33) + 2*Vv13*Vv56*ZH22*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_877 = Coupling(name = 'GC_877',
	 value = '(1./2.*complex(0,1)*(2*Y1n21*ZH21*complexconjugate(Vv14)*complexconjugate(Vv52) + 2*Y1n22*ZH21*complexconjugate(Vv15)*complexconjugate(Vv52) + 2*Y2n33*ZH22*complexconjugate(Vv16)*complexconjugate(Vv53) + 2*Y1n21*ZH21*complexconjugate(Vv12)*complexconjugate(Vv54) - 2*BB11*ZH23*complexconjugate(Vv14)*complexconjugate(Vv54) + BB12*ZH23*complexconjugate(Vv15)*complexconjugate(Vv54) + BB21*ZH23*complexconjugate(Vv15)*complexconjugate(Vv54) + C13*ZH23*complexconjugate(Vv16)*complexconjugate(Vv54) + C31*ZH23*complexconjugate(Vv16)*complexconjugate(Vv54) + 2*Y1n11*ZH21*(complexconjugate(Vv14)*complexconjugate(Vv51) + complexconjugate(Vv11)*complexconjugate(Vv54)) + 2*Y1n22*ZH21*complexconjugate(Vv12)*complexconjugate(Vv55) + BB12*ZH23*complexconjugate(Vv14)*complexconjugate(Vv55) + BB21*ZH23*complexconjugate(Vv14)*complexconjugate(Vv55) + 2*BB22*ZH23*complexconjugate(Vv15)*complexconjugate(Vv55) + C23*ZH23*complexconjugate(Vv16)*complexconjugate(Vv55) + C32*ZH23*complexconjugate(Vv16)*complexconjugate(Vv55) + 2*Y1n12*ZH21*(complexconjugate(Vv15)*complexconjugate(Vv51) + complexconjugate(Vv11)*complexconjugate(Vv55)) + 2*Y2n33*ZH22*complexconjugate(Vv13)*complexconjugate(Vv56) + C13*ZH23*complexconjugate(Vv14)*complexconjugate(Vv56) + C31*ZH23*complexconjugate(Vv14)*complexconjugate(Vv56) + C23*ZH23*complexconjugate(Vv15)*complexconjugate(Vv56) + C32*ZH23*complexconjugate(Vv15)*complexconjugate(Vv56)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_878 = Coupling(name = 'GC_878',
	 value = '(1./2.*complex(0,1)*(Vv16*Vv54*ZH33*complexconjugate(C13) + Vv16*Vv55*ZH33*complexconjugate(C23) + Vv16*Vv54*ZH33*complexconjugate(C31) + Vv16*Vv55*ZH33*complexconjugate(C32) + 2*Vv11*Vv54*ZH31*complexconjugate(Y1n11) + 2*Vv11*Vv55*ZH31*complexconjugate(Y1n12) + 2*Vv12*Vv54*ZH31*complexconjugate(Y1n21) + Vv14*(ZH33*(-2*Vv54*complexconjugate(BB11) + Vv55*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv56*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv51*ZH31*complexconjugate(Y1n11) + 2*Vv52*ZH31*complexconjugate(Y1n21)) + 2*Vv12*Vv55*ZH31*complexconjugate(Y1n22) + Vv15*(ZH33*(Vv54*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv55*complexconjugate(BB22) + Vv56*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv51*ZH31*complexconjugate(Y1n12) + 2*Vv52*ZH31*complexconjugate(Y1n22)) + 2*Vv16*Vv53*ZH32*complexconjugate(Y2n33) + 2*Vv13*Vv56*ZH32*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_879 = Coupling(name = 'GC_879',
	 value = '(1./2.*complex(0,1)*(2*Y1n21*ZH31*complexconjugate(Vv14)*complexconjugate(Vv52) + 2*Y1n22*ZH31*complexconjugate(Vv15)*complexconjugate(Vv52) + 2*Y2n33*ZH32*complexconjugate(Vv16)*complexconjugate(Vv53) + 2*Y1n21*ZH31*complexconjugate(Vv12)*complexconjugate(Vv54) - 2*BB11*ZH33*complexconjugate(Vv14)*complexconjugate(Vv54) + BB12*ZH33*complexconjugate(Vv15)*complexconjugate(Vv54) + BB21*ZH33*complexconjugate(Vv15)*complexconjugate(Vv54) + C13*ZH33*complexconjugate(Vv16)*complexconjugate(Vv54) + C31*ZH33*complexconjugate(Vv16)*complexconjugate(Vv54) + 2*Y1n11*ZH31*(complexconjugate(Vv14)*complexconjugate(Vv51) + complexconjugate(Vv11)*complexconjugate(Vv54)) + 2*Y1n22*ZH31*complexconjugate(Vv12)*complexconjugate(Vv55) + BB12*ZH33*complexconjugate(Vv14)*complexconjugate(Vv55) + BB21*ZH33*complexconjugate(Vv14)*complexconjugate(Vv55) + 2*BB22*ZH33*complexconjugate(Vv15)*complexconjugate(Vv55) + C23*ZH33*complexconjugate(Vv16)*complexconjugate(Vv55) + C32*ZH33*complexconjugate(Vv16)*complexconjugate(Vv55) + 2*Y1n12*ZH31*(complexconjugate(Vv15)*complexconjugate(Vv51) + complexconjugate(Vv11)*complexconjugate(Vv55)) + 2*Y2n33*ZH32*complexconjugate(Vv13)*complexconjugate(Vv56) + C13*ZH33*complexconjugate(Vv14)*complexconjugate(Vv56) + C31*ZH33*complexconjugate(Vv14)*complexconjugate(Vv56) + C23*ZH33*complexconjugate(Vv15)*complexconjugate(Vv56) + C32*ZH33*complexconjugate(Vv15)*complexconjugate(Vv56)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_880 = Coupling(name = 'GC_880',
	 value = '(1./2.*complex(0,1)*(Vv16*Vv64*ZH13*complexconjugate(C13) + Vv16*Vv65*ZH13*complexconjugate(C23) + Vv16*Vv64*ZH13*complexconjugate(C31) + Vv16*Vv65*ZH13*complexconjugate(C32) + 2*Vv11*Vv64*ZH11*complexconjugate(Y1n11) + 2*Vv11*Vv65*ZH11*complexconjugate(Y1n12) + 2*Vv12*Vv64*ZH11*complexconjugate(Y1n21) + Vv14*(ZH13*(-2*Vv64*complexconjugate(BB11) + Vv65*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv66*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv61*ZH11*complexconjugate(Y1n11) + 2*Vv62*ZH11*complexconjugate(Y1n21)) + 2*Vv12*Vv65*ZH11*complexconjugate(Y1n22) + Vv15*(ZH13*(Vv64*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv65*complexconjugate(BB22) + Vv66*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv61*ZH11*complexconjugate(Y1n12) + 2*Vv62*ZH11*complexconjugate(Y1n22)) + 2*Vv16*Vv63*ZH12*complexconjugate(Y2n33) + 2*Vv13*Vv66*ZH12*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_881 = Coupling(name = 'GC_881',
	 value = '(1./2.*complex(0,1)*(2*Y1n21*ZH11*complexconjugate(Vv14)*complexconjugate(Vv62) + 2*Y1n22*ZH11*complexconjugate(Vv15)*complexconjugate(Vv62) + 2*Y2n33*ZH12*complexconjugate(Vv16)*complexconjugate(Vv63) + 2*Y1n21*ZH11*complexconjugate(Vv12)*complexconjugate(Vv64) - 2*BB11*ZH13*complexconjugate(Vv14)*complexconjugate(Vv64) + BB12*ZH13*complexconjugate(Vv15)*complexconjugate(Vv64) + BB21*ZH13*complexconjugate(Vv15)*complexconjugate(Vv64) + C13*ZH13*complexconjugate(Vv16)*complexconjugate(Vv64) + C31*ZH13*complexconjugate(Vv16)*complexconjugate(Vv64) + 2*Y1n11*ZH11*(complexconjugate(Vv14)*complexconjugate(Vv61) + complexconjugate(Vv11)*complexconjugate(Vv64)) + 2*Y1n22*ZH11*complexconjugate(Vv12)*complexconjugate(Vv65) + BB12*ZH13*complexconjugate(Vv14)*complexconjugate(Vv65) + BB21*ZH13*complexconjugate(Vv14)*complexconjugate(Vv65) + 2*BB22*ZH13*complexconjugate(Vv15)*complexconjugate(Vv65) + C23*ZH13*complexconjugate(Vv16)*complexconjugate(Vv65) + C32*ZH13*complexconjugate(Vv16)*complexconjugate(Vv65) + 2*Y1n12*ZH11*(complexconjugate(Vv15)*complexconjugate(Vv61) + complexconjugate(Vv11)*complexconjugate(Vv65)) + 2*Y2n33*ZH12*complexconjugate(Vv13)*complexconjugate(Vv66) + C13*ZH13*complexconjugate(Vv14)*complexconjugate(Vv66) + C31*ZH13*complexconjugate(Vv14)*complexconjugate(Vv66) + C23*ZH13*complexconjugate(Vv15)*complexconjugate(Vv66) + C32*ZH13*complexconjugate(Vv15)*complexconjugate(Vv66)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_882 = Coupling(name = 'GC_882',
	 value = '(1./2.*complex(0,1)*(Vv16*Vv64*ZH23*complexconjugate(C13) + Vv16*Vv65*ZH23*complexconjugate(C23) + Vv16*Vv64*ZH23*complexconjugate(C31) + Vv16*Vv65*ZH23*complexconjugate(C32) + 2*Vv11*Vv64*ZH21*complexconjugate(Y1n11) + 2*Vv11*Vv65*ZH21*complexconjugate(Y1n12) + 2*Vv12*Vv64*ZH21*complexconjugate(Y1n21) + Vv14*(ZH23*(-2*Vv64*complexconjugate(BB11) + Vv65*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv66*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv61*ZH21*complexconjugate(Y1n11) + 2*Vv62*ZH21*complexconjugate(Y1n21)) + 2*Vv12*Vv65*ZH21*complexconjugate(Y1n22) + Vv15*(ZH23*(Vv64*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv65*complexconjugate(BB22) + Vv66*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv61*ZH21*complexconjugate(Y1n12) + 2*Vv62*ZH21*complexconjugate(Y1n22)) + 2*Vv16*Vv63*ZH22*complexconjugate(Y2n33) + 2*Vv13*Vv66*ZH22*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_883 = Coupling(name = 'GC_883',
	 value = '(1./2.*complex(0,1)*(2*Y1n21*ZH21*complexconjugate(Vv14)*complexconjugate(Vv62) + 2*Y1n22*ZH21*complexconjugate(Vv15)*complexconjugate(Vv62) + 2*Y2n33*ZH22*complexconjugate(Vv16)*complexconjugate(Vv63) + 2*Y1n21*ZH21*complexconjugate(Vv12)*complexconjugate(Vv64) - 2*BB11*ZH23*complexconjugate(Vv14)*complexconjugate(Vv64) + BB12*ZH23*complexconjugate(Vv15)*complexconjugate(Vv64) + BB21*ZH23*complexconjugate(Vv15)*complexconjugate(Vv64) + C13*ZH23*complexconjugate(Vv16)*complexconjugate(Vv64) + C31*ZH23*complexconjugate(Vv16)*complexconjugate(Vv64) + 2*Y1n11*ZH21*(complexconjugate(Vv14)*complexconjugate(Vv61) + complexconjugate(Vv11)*complexconjugate(Vv64)) + 2*Y1n22*ZH21*complexconjugate(Vv12)*complexconjugate(Vv65) + BB12*ZH23*complexconjugate(Vv14)*complexconjugate(Vv65) + BB21*ZH23*complexconjugate(Vv14)*complexconjugate(Vv65) + 2*BB22*ZH23*complexconjugate(Vv15)*complexconjugate(Vv65) + C23*ZH23*complexconjugate(Vv16)*complexconjugate(Vv65) + C32*ZH23*complexconjugate(Vv16)*complexconjugate(Vv65) + 2*Y1n12*ZH21*(complexconjugate(Vv15)*complexconjugate(Vv61) + complexconjugate(Vv11)*complexconjugate(Vv65)) + 2*Y2n33*ZH22*complexconjugate(Vv13)*complexconjugate(Vv66) + C13*ZH23*complexconjugate(Vv14)*complexconjugate(Vv66) + C31*ZH23*complexconjugate(Vv14)*complexconjugate(Vv66) + C23*ZH23*complexconjugate(Vv15)*complexconjugate(Vv66) + C32*ZH23*complexconjugate(Vv15)*complexconjugate(Vv66)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_884 = Coupling(name = 'GC_884',
	 value = '(1./2.*complex(0,1)*(Vv16*Vv64*ZH33*complexconjugate(C13) + Vv16*Vv65*ZH33*complexconjugate(C23) + Vv16*Vv64*ZH33*complexconjugate(C31) + Vv16*Vv65*ZH33*complexconjugate(C32) + 2*Vv11*Vv64*ZH31*complexconjugate(Y1n11) + 2*Vv11*Vv65*ZH31*complexconjugate(Y1n12) + 2*Vv12*Vv64*ZH31*complexconjugate(Y1n21) + Vv14*(ZH33*(-2*Vv64*complexconjugate(BB11) + Vv65*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv66*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv61*ZH31*complexconjugate(Y1n11) + 2*Vv62*ZH31*complexconjugate(Y1n21)) + 2*Vv12*Vv65*ZH31*complexconjugate(Y1n22) + Vv15*(ZH33*(Vv64*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv65*complexconjugate(BB22) + Vv66*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv61*ZH31*complexconjugate(Y1n12) + 2*Vv62*ZH31*complexconjugate(Y1n22)) + 2*Vv16*Vv63*ZH32*complexconjugate(Y2n33) + 2*Vv13*Vv66*ZH32*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_885 = Coupling(name = 'GC_885',
	 value = '(1./2.*complex(0,1)*(2*Y1n21*ZH31*complexconjugate(Vv14)*complexconjugate(Vv62) + 2*Y1n22*ZH31*complexconjugate(Vv15)*complexconjugate(Vv62) + 2*Y2n33*ZH32*complexconjugate(Vv16)*complexconjugate(Vv63) + 2*Y1n21*ZH31*complexconjugate(Vv12)*complexconjugate(Vv64) - 2*BB11*ZH33*complexconjugate(Vv14)*complexconjugate(Vv64) + BB12*ZH33*complexconjugate(Vv15)*complexconjugate(Vv64) + BB21*ZH33*complexconjugate(Vv15)*complexconjugate(Vv64) + C13*ZH33*complexconjugate(Vv16)*complexconjugate(Vv64) + C31*ZH33*complexconjugate(Vv16)*complexconjugate(Vv64) + 2*Y1n11*ZH31*(complexconjugate(Vv14)*complexconjugate(Vv61) + complexconjugate(Vv11)*complexconjugate(Vv64)) + 2*Y1n22*ZH31*complexconjugate(Vv12)*complexconjugate(Vv65) + BB12*ZH33*complexconjugate(Vv14)*complexconjugate(Vv65) + BB21*ZH33*complexconjugate(Vv14)*complexconjugate(Vv65) + 2*BB22*ZH33*complexconjugate(Vv15)*complexconjugate(Vv65) + C23*ZH33*complexconjugate(Vv16)*complexconjugate(Vv65) + C32*ZH33*complexconjugate(Vv16)*complexconjugate(Vv65) + 2*Y1n12*ZH31*(complexconjugate(Vv15)*complexconjugate(Vv61) + complexconjugate(Vv11)*complexconjugate(Vv65)) + 2*Y2n33*ZH32*complexconjugate(Vv13)*complexconjugate(Vv66) + C13*ZH33*complexconjugate(Vv14)*complexconjugate(Vv66) + C31*ZH33*complexconjugate(Vv14)*complexconjugate(Vv66) + C23*ZH33*complexconjugate(Vv15)*complexconjugate(Vv66) + C32*ZH33*complexconjugate(Vv15)*complexconjugate(Vv66)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_886 = Coupling(name = 'GC_886',
	 value = '(1./2.*complex(0,1)*(Vv24*Vv26*ZH13*complexconjugate(C13) + Vv25*Vv26*ZH13*complexconjugate(C23) + Vv24*Vv26*ZH13*complexconjugate(C31) + Vv25*Vv26*ZH13*complexconjugate(C32) + 2*Vv21*Vv24*ZH11*complexconjugate(Y1n11) + 2*Vv21*Vv25*ZH11*complexconjugate(Y1n12) + 2*Vv22*Vv24*ZH11*complexconjugate(Y1n21) + Vv24*(ZH13*(-2*Vv24*complexconjugate(BB11) + Vv25*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv26*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv21*ZH11*complexconjugate(Y1n11) + 2*Vv22*ZH11*complexconjugate(Y1n21)) + 2*Vv22*Vv25*ZH11*complexconjugate(Y1n22) + Vv25*(ZH13*(Vv24*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv25*complexconjugate(BB22) + Vv26*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv21*ZH11*complexconjugate(Y1n12) + 2*Vv22*ZH11*complexconjugate(Y1n22)) + 4*Vv23*Vv26*ZH12*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_887 = Coupling(name = 'GC_887',
	 value = '(1./2.*complex(0,1)*(4*Y1n11*ZH11*complexconjugate(Vv21)*complexconjugate(Vv24) + 4*Y1n21*ZH11*complexconjugate(Vv22)*complexconjugate(Vv24) - 2*BB11*ZH13*complexconjugate(Vv24)**2 + 4*Y1n12*ZH11*complexconjugate(Vv21)*complexconjugate(Vv25) + 4*Y1n22*ZH11*complexconjugate(Vv22)*complexconjugate(Vv25) + 2*BB12*ZH13*complexconjugate(Vv24)*complexconjugate(Vv25) + 2*BB21*ZH13*complexconjugate(Vv24)*complexconjugate(Vv25) + 2*BB22*ZH13*complexconjugate(Vv25)**2 + 4*Y2n33*ZH12*complexconjugate(Vv23)*complexconjugate(Vv26) + 2*C13*ZH13*complexconjugate(Vv24)*complexconjugate(Vv26) + 2*C31*ZH13*complexconjugate(Vv24)*complexconjugate(Vv26) + 2*C23*ZH13*complexconjugate(Vv25)*complexconjugate(Vv26) + 2*C32*ZH13*complexconjugate(Vv25)*complexconjugate(Vv26)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_888 = Coupling(name = 'GC_888',
	 value = '(1./2.*complex(0,1)*(Vv24*Vv26*ZH23*complexconjugate(C13) + Vv25*Vv26*ZH23*complexconjugate(C23) + Vv24*Vv26*ZH23*complexconjugate(C31) + Vv25*Vv26*ZH23*complexconjugate(C32) + 2*Vv21*Vv24*ZH21*complexconjugate(Y1n11) + 2*Vv21*Vv25*ZH21*complexconjugate(Y1n12) + 2*Vv22*Vv24*ZH21*complexconjugate(Y1n21) + Vv24*(ZH23*(-2*Vv24*complexconjugate(BB11) + Vv25*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv26*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv21*ZH21*complexconjugate(Y1n11) + 2*Vv22*ZH21*complexconjugate(Y1n21)) + 2*Vv22*Vv25*ZH21*complexconjugate(Y1n22) + Vv25*(ZH23*(Vv24*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv25*complexconjugate(BB22) + Vv26*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv21*ZH21*complexconjugate(Y1n12) + 2*Vv22*ZH21*complexconjugate(Y1n22)) + 4*Vv23*Vv26*ZH22*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_889 = Coupling(name = 'GC_889',
	 value = '(1./2.*complex(0,1)*(4*Y1n11*ZH21*complexconjugate(Vv21)*complexconjugate(Vv24) + 4*Y1n21*ZH21*complexconjugate(Vv22)*complexconjugate(Vv24) - 2*BB11*ZH23*complexconjugate(Vv24)**2 + 4*Y1n12*ZH21*complexconjugate(Vv21)*complexconjugate(Vv25) + 4*Y1n22*ZH21*complexconjugate(Vv22)*complexconjugate(Vv25) + 2*BB12*ZH23*complexconjugate(Vv24)*complexconjugate(Vv25) + 2*BB21*ZH23*complexconjugate(Vv24)*complexconjugate(Vv25) + 2*BB22*ZH23*complexconjugate(Vv25)**2 + 4*Y2n33*ZH22*complexconjugate(Vv23)*complexconjugate(Vv26) + 2*C13*ZH23*complexconjugate(Vv24)*complexconjugate(Vv26) + 2*C31*ZH23*complexconjugate(Vv24)*complexconjugate(Vv26) + 2*C23*ZH23*complexconjugate(Vv25)*complexconjugate(Vv26) + 2*C32*ZH23*complexconjugate(Vv25)*complexconjugate(Vv26)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_890 = Coupling(name = 'GC_890',
	 value = '(1./2.*complex(0,1)*(Vv24*Vv26*ZH33*complexconjugate(C13) + Vv25*Vv26*ZH33*complexconjugate(C23) + Vv24*Vv26*ZH33*complexconjugate(C31) + Vv25*Vv26*ZH33*complexconjugate(C32) + 2*Vv21*Vv24*ZH31*complexconjugate(Y1n11) + 2*Vv21*Vv25*ZH31*complexconjugate(Y1n12) + 2*Vv22*Vv24*ZH31*complexconjugate(Y1n21) + Vv24*(ZH33*(-2*Vv24*complexconjugate(BB11) + Vv25*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv26*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv21*ZH31*complexconjugate(Y1n11) + 2*Vv22*ZH31*complexconjugate(Y1n21)) + 2*Vv22*Vv25*ZH31*complexconjugate(Y1n22) + Vv25*(ZH33*(Vv24*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv25*complexconjugate(BB22) + Vv26*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv21*ZH31*complexconjugate(Y1n12) + 2*Vv22*ZH31*complexconjugate(Y1n22)) + 4*Vv23*Vv26*ZH32*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_891 = Coupling(name = 'GC_891',
	 value = '(1./2.*complex(0,1)*(4*Y1n11*ZH31*complexconjugate(Vv21)*complexconjugate(Vv24) + 4*Y1n21*ZH31*complexconjugate(Vv22)*complexconjugate(Vv24) - 2*BB11*ZH33*complexconjugate(Vv24)**2 + 4*Y1n12*ZH31*complexconjugate(Vv21)*complexconjugate(Vv25) + 4*Y1n22*ZH31*complexconjugate(Vv22)*complexconjugate(Vv25) + 2*BB12*ZH33*complexconjugate(Vv24)*complexconjugate(Vv25) + 2*BB21*ZH33*complexconjugate(Vv24)*complexconjugate(Vv25) + 2*BB22*ZH33*complexconjugate(Vv25)**2 + 4*Y2n33*ZH32*complexconjugate(Vv23)*complexconjugate(Vv26) + 2*C13*ZH33*complexconjugate(Vv24)*complexconjugate(Vv26) + 2*C31*ZH33*complexconjugate(Vv24)*complexconjugate(Vv26) + 2*C23*ZH33*complexconjugate(Vv25)*complexconjugate(Vv26) + 2*C32*ZH33*complexconjugate(Vv25)*complexconjugate(Vv26)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_892 = Coupling(name = 'GC_892',
	 value = '(1./2.*complex(0,1)*(Vv26*Vv34*ZH13*complexconjugate(C13) + Vv26*Vv35*ZH13*complexconjugate(C23) + Vv26*Vv34*ZH13*complexconjugate(C31) + Vv26*Vv35*ZH13*complexconjugate(C32) + 2*Vv21*Vv34*ZH11*complexconjugate(Y1n11) + 2*Vv21*Vv35*ZH11*complexconjugate(Y1n12) + 2*Vv22*Vv34*ZH11*complexconjugate(Y1n21) + Vv24*(ZH13*(-2*Vv34*complexconjugate(BB11) + Vv35*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv36*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv31*ZH11*complexconjugate(Y1n11) + 2*Vv32*ZH11*complexconjugate(Y1n21)) + 2*Vv22*Vv35*ZH11*complexconjugate(Y1n22) + Vv25*(ZH13*(Vv34*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv35*complexconjugate(BB22) + Vv36*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv31*ZH11*complexconjugate(Y1n12) + 2*Vv32*ZH11*complexconjugate(Y1n22)) + 2*Vv26*Vv33*ZH12*complexconjugate(Y2n33) + 2*Vv23*Vv36*ZH12*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_893 = Coupling(name = 'GC_893',
	 value = '(1./2.*complex(0,1)*(2*Y1n21*ZH11*complexconjugate(Vv24)*complexconjugate(Vv32) + 2*Y1n22*ZH11*complexconjugate(Vv25)*complexconjugate(Vv32) + 2*Y2n33*ZH12*complexconjugate(Vv26)*complexconjugate(Vv33) + 2*Y1n21*ZH11*complexconjugate(Vv22)*complexconjugate(Vv34) - 2*BB11*ZH13*complexconjugate(Vv24)*complexconjugate(Vv34) + BB12*ZH13*complexconjugate(Vv25)*complexconjugate(Vv34) + BB21*ZH13*complexconjugate(Vv25)*complexconjugate(Vv34) + C13*ZH13*complexconjugate(Vv26)*complexconjugate(Vv34) + C31*ZH13*complexconjugate(Vv26)*complexconjugate(Vv34) + 2*Y1n11*ZH11*(complexconjugate(Vv24)*complexconjugate(Vv31) + complexconjugate(Vv21)*complexconjugate(Vv34)) + 2*Y1n22*ZH11*complexconjugate(Vv22)*complexconjugate(Vv35) + BB12*ZH13*complexconjugate(Vv24)*complexconjugate(Vv35) + BB21*ZH13*complexconjugate(Vv24)*complexconjugate(Vv35) + 2*BB22*ZH13*complexconjugate(Vv25)*complexconjugate(Vv35) + C23*ZH13*complexconjugate(Vv26)*complexconjugate(Vv35) + C32*ZH13*complexconjugate(Vv26)*complexconjugate(Vv35) + 2*Y1n12*ZH11*(complexconjugate(Vv25)*complexconjugate(Vv31) + complexconjugate(Vv21)*complexconjugate(Vv35)) + 2*Y2n33*ZH12*complexconjugate(Vv23)*complexconjugate(Vv36) + C13*ZH13*complexconjugate(Vv24)*complexconjugate(Vv36) + C31*ZH13*complexconjugate(Vv24)*complexconjugate(Vv36) + C23*ZH13*complexconjugate(Vv25)*complexconjugate(Vv36) + C32*ZH13*complexconjugate(Vv25)*complexconjugate(Vv36)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_894 = Coupling(name = 'GC_894',
	 value = '(1./2.*complex(0,1)*(Vv26*Vv34*ZH23*complexconjugate(C13) + Vv26*Vv35*ZH23*complexconjugate(C23) + Vv26*Vv34*ZH23*complexconjugate(C31) + Vv26*Vv35*ZH23*complexconjugate(C32) + 2*Vv21*Vv34*ZH21*complexconjugate(Y1n11) + 2*Vv21*Vv35*ZH21*complexconjugate(Y1n12) + 2*Vv22*Vv34*ZH21*complexconjugate(Y1n21) + Vv24*(ZH23*(-2*Vv34*complexconjugate(BB11) + Vv35*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv36*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv31*ZH21*complexconjugate(Y1n11) + 2*Vv32*ZH21*complexconjugate(Y1n21)) + 2*Vv22*Vv35*ZH21*complexconjugate(Y1n22) + Vv25*(ZH23*(Vv34*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv35*complexconjugate(BB22) + Vv36*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv31*ZH21*complexconjugate(Y1n12) + 2*Vv32*ZH21*complexconjugate(Y1n22)) + 2*Vv26*Vv33*ZH22*complexconjugate(Y2n33) + 2*Vv23*Vv36*ZH22*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_895 = Coupling(name = 'GC_895',
	 value = '(1./2.*complex(0,1)*(2*Y1n21*ZH21*complexconjugate(Vv24)*complexconjugate(Vv32) + 2*Y1n22*ZH21*complexconjugate(Vv25)*complexconjugate(Vv32) + 2*Y2n33*ZH22*complexconjugate(Vv26)*complexconjugate(Vv33) + 2*Y1n21*ZH21*complexconjugate(Vv22)*complexconjugate(Vv34) - 2*BB11*ZH23*complexconjugate(Vv24)*complexconjugate(Vv34) + BB12*ZH23*complexconjugate(Vv25)*complexconjugate(Vv34) + BB21*ZH23*complexconjugate(Vv25)*complexconjugate(Vv34) + C13*ZH23*complexconjugate(Vv26)*complexconjugate(Vv34) + C31*ZH23*complexconjugate(Vv26)*complexconjugate(Vv34) + 2*Y1n11*ZH21*(complexconjugate(Vv24)*complexconjugate(Vv31) + complexconjugate(Vv21)*complexconjugate(Vv34)) + 2*Y1n22*ZH21*complexconjugate(Vv22)*complexconjugate(Vv35) + BB12*ZH23*complexconjugate(Vv24)*complexconjugate(Vv35) + BB21*ZH23*complexconjugate(Vv24)*complexconjugate(Vv35) + 2*BB22*ZH23*complexconjugate(Vv25)*complexconjugate(Vv35) + C23*ZH23*complexconjugate(Vv26)*complexconjugate(Vv35) + C32*ZH23*complexconjugate(Vv26)*complexconjugate(Vv35) + 2*Y1n12*ZH21*(complexconjugate(Vv25)*complexconjugate(Vv31) + complexconjugate(Vv21)*complexconjugate(Vv35)) + 2*Y2n33*ZH22*complexconjugate(Vv23)*complexconjugate(Vv36) + C13*ZH23*complexconjugate(Vv24)*complexconjugate(Vv36) + C31*ZH23*complexconjugate(Vv24)*complexconjugate(Vv36) + C23*ZH23*complexconjugate(Vv25)*complexconjugate(Vv36) + C32*ZH23*complexconjugate(Vv25)*complexconjugate(Vv36)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_896 = Coupling(name = 'GC_896',
	 value = '(1./2.*complex(0,1)*(Vv26*Vv34*ZH33*complexconjugate(C13) + Vv26*Vv35*ZH33*complexconjugate(C23) + Vv26*Vv34*ZH33*complexconjugate(C31) + Vv26*Vv35*ZH33*complexconjugate(C32) + 2*Vv21*Vv34*ZH31*complexconjugate(Y1n11) + 2*Vv21*Vv35*ZH31*complexconjugate(Y1n12) + 2*Vv22*Vv34*ZH31*complexconjugate(Y1n21) + Vv24*(ZH33*(-2*Vv34*complexconjugate(BB11) + Vv35*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv36*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv31*ZH31*complexconjugate(Y1n11) + 2*Vv32*ZH31*complexconjugate(Y1n21)) + 2*Vv22*Vv35*ZH31*complexconjugate(Y1n22) + Vv25*(ZH33*(Vv34*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv35*complexconjugate(BB22) + Vv36*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv31*ZH31*complexconjugate(Y1n12) + 2*Vv32*ZH31*complexconjugate(Y1n22)) + 2*Vv26*Vv33*ZH32*complexconjugate(Y2n33) + 2*Vv23*Vv36*ZH32*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_897 = Coupling(name = 'GC_897',
	 value = '(1./2.*complex(0,1)*(2*Y1n21*ZH31*complexconjugate(Vv24)*complexconjugate(Vv32) + 2*Y1n22*ZH31*complexconjugate(Vv25)*complexconjugate(Vv32) + 2*Y2n33*ZH32*complexconjugate(Vv26)*complexconjugate(Vv33) + 2*Y1n21*ZH31*complexconjugate(Vv22)*complexconjugate(Vv34) - 2*BB11*ZH33*complexconjugate(Vv24)*complexconjugate(Vv34) + BB12*ZH33*complexconjugate(Vv25)*complexconjugate(Vv34) + BB21*ZH33*complexconjugate(Vv25)*complexconjugate(Vv34) + C13*ZH33*complexconjugate(Vv26)*complexconjugate(Vv34) + C31*ZH33*complexconjugate(Vv26)*complexconjugate(Vv34) + 2*Y1n11*ZH31*(complexconjugate(Vv24)*complexconjugate(Vv31) + complexconjugate(Vv21)*complexconjugate(Vv34)) + 2*Y1n22*ZH31*complexconjugate(Vv22)*complexconjugate(Vv35) + BB12*ZH33*complexconjugate(Vv24)*complexconjugate(Vv35) + BB21*ZH33*complexconjugate(Vv24)*complexconjugate(Vv35) + 2*BB22*ZH33*complexconjugate(Vv25)*complexconjugate(Vv35) + C23*ZH33*complexconjugate(Vv26)*complexconjugate(Vv35) + C32*ZH33*complexconjugate(Vv26)*complexconjugate(Vv35) + 2*Y1n12*ZH31*(complexconjugate(Vv25)*complexconjugate(Vv31) + complexconjugate(Vv21)*complexconjugate(Vv35)) + 2*Y2n33*ZH32*complexconjugate(Vv23)*complexconjugate(Vv36) + C13*ZH33*complexconjugate(Vv24)*complexconjugate(Vv36) + C31*ZH33*complexconjugate(Vv24)*complexconjugate(Vv36) + C23*ZH33*complexconjugate(Vv25)*complexconjugate(Vv36) + C32*ZH33*complexconjugate(Vv25)*complexconjugate(Vv36)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_898 = Coupling(name = 'GC_898',
	 value = '(1./2.*complex(0,1)*(Vv26*Vv44*ZH13*complexconjugate(C13) + Vv26*Vv45*ZH13*complexconjugate(C23) + Vv26*Vv44*ZH13*complexconjugate(C31) + Vv26*Vv45*ZH13*complexconjugate(C32) + 2*Vv21*Vv44*ZH11*complexconjugate(Y1n11) + 2*Vv21*Vv45*ZH11*complexconjugate(Y1n12) + 2*Vv22*Vv44*ZH11*complexconjugate(Y1n21) + Vv24*(ZH13*(-2*Vv44*complexconjugate(BB11) + Vv45*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv46*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv41*ZH11*complexconjugate(Y1n11) + 2*Vv42*ZH11*complexconjugate(Y1n21)) + 2*Vv22*Vv45*ZH11*complexconjugate(Y1n22) + Vv25*(ZH13*(Vv44*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv45*complexconjugate(BB22) + Vv46*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv41*ZH11*complexconjugate(Y1n12) + 2*Vv42*ZH11*complexconjugate(Y1n22)) + 2*Vv26*Vv43*ZH12*complexconjugate(Y2n33) + 2*Vv23*Vv46*ZH12*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_899 = Coupling(name = 'GC_899',
	 value = '(1./2.*complex(0,1)*(2*Y1n21*ZH11*complexconjugate(Vv24)*complexconjugate(Vv42) + 2*Y1n22*ZH11*complexconjugate(Vv25)*complexconjugate(Vv42) + 2*Y2n33*ZH12*complexconjugate(Vv26)*complexconjugate(Vv43) + 2*Y1n21*ZH11*complexconjugate(Vv22)*complexconjugate(Vv44) - 2*BB11*ZH13*complexconjugate(Vv24)*complexconjugate(Vv44) + BB12*ZH13*complexconjugate(Vv25)*complexconjugate(Vv44) + BB21*ZH13*complexconjugate(Vv25)*complexconjugate(Vv44) + C13*ZH13*complexconjugate(Vv26)*complexconjugate(Vv44) + C31*ZH13*complexconjugate(Vv26)*complexconjugate(Vv44) + 2*Y1n11*ZH11*(complexconjugate(Vv24)*complexconjugate(Vv41) + complexconjugate(Vv21)*complexconjugate(Vv44)) + 2*Y1n22*ZH11*complexconjugate(Vv22)*complexconjugate(Vv45) + BB12*ZH13*complexconjugate(Vv24)*complexconjugate(Vv45) + BB21*ZH13*complexconjugate(Vv24)*complexconjugate(Vv45) + 2*BB22*ZH13*complexconjugate(Vv25)*complexconjugate(Vv45) + C23*ZH13*complexconjugate(Vv26)*complexconjugate(Vv45) + C32*ZH13*complexconjugate(Vv26)*complexconjugate(Vv45) + 2*Y1n12*ZH11*(complexconjugate(Vv25)*complexconjugate(Vv41) + complexconjugate(Vv21)*complexconjugate(Vv45)) + 2*Y2n33*ZH12*complexconjugate(Vv23)*complexconjugate(Vv46) + C13*ZH13*complexconjugate(Vv24)*complexconjugate(Vv46) + C31*ZH13*complexconjugate(Vv24)*complexconjugate(Vv46) + C23*ZH13*complexconjugate(Vv25)*complexconjugate(Vv46) + C32*ZH13*complexconjugate(Vv25)*complexconjugate(Vv46)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_900 = Coupling(name = 'GC_900',
	 value = '(1./2.*complex(0,1)*(Vv26*Vv44*ZH23*complexconjugate(C13) + Vv26*Vv45*ZH23*complexconjugate(C23) + Vv26*Vv44*ZH23*complexconjugate(C31) + Vv26*Vv45*ZH23*complexconjugate(C32) + 2*Vv21*Vv44*ZH21*complexconjugate(Y1n11) + 2*Vv21*Vv45*ZH21*complexconjugate(Y1n12) + 2*Vv22*Vv44*ZH21*complexconjugate(Y1n21) + Vv24*(ZH23*(-2*Vv44*complexconjugate(BB11) + Vv45*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv46*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv41*ZH21*complexconjugate(Y1n11) + 2*Vv42*ZH21*complexconjugate(Y1n21)) + 2*Vv22*Vv45*ZH21*complexconjugate(Y1n22) + Vv25*(ZH23*(Vv44*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv45*complexconjugate(BB22) + Vv46*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv41*ZH21*complexconjugate(Y1n12) + 2*Vv42*ZH21*complexconjugate(Y1n22)) + 2*Vv26*Vv43*ZH22*complexconjugate(Y2n33) + 2*Vv23*Vv46*ZH22*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_901 = Coupling(name = 'GC_901',
	 value = '(1./2.*complex(0,1)*(2*Y1n21*ZH21*complexconjugate(Vv24)*complexconjugate(Vv42) + 2*Y1n22*ZH21*complexconjugate(Vv25)*complexconjugate(Vv42) + 2*Y2n33*ZH22*complexconjugate(Vv26)*complexconjugate(Vv43) + 2*Y1n21*ZH21*complexconjugate(Vv22)*complexconjugate(Vv44) - 2*BB11*ZH23*complexconjugate(Vv24)*complexconjugate(Vv44) + BB12*ZH23*complexconjugate(Vv25)*complexconjugate(Vv44) + BB21*ZH23*complexconjugate(Vv25)*complexconjugate(Vv44) + C13*ZH23*complexconjugate(Vv26)*complexconjugate(Vv44) + C31*ZH23*complexconjugate(Vv26)*complexconjugate(Vv44) + 2*Y1n11*ZH21*(complexconjugate(Vv24)*complexconjugate(Vv41) + complexconjugate(Vv21)*complexconjugate(Vv44)) + 2*Y1n22*ZH21*complexconjugate(Vv22)*complexconjugate(Vv45) + BB12*ZH23*complexconjugate(Vv24)*complexconjugate(Vv45) + BB21*ZH23*complexconjugate(Vv24)*complexconjugate(Vv45) + 2*BB22*ZH23*complexconjugate(Vv25)*complexconjugate(Vv45) + C23*ZH23*complexconjugate(Vv26)*complexconjugate(Vv45) + C32*ZH23*complexconjugate(Vv26)*complexconjugate(Vv45) + 2*Y1n12*ZH21*(complexconjugate(Vv25)*complexconjugate(Vv41) + complexconjugate(Vv21)*complexconjugate(Vv45)) + 2*Y2n33*ZH22*complexconjugate(Vv23)*complexconjugate(Vv46) + C13*ZH23*complexconjugate(Vv24)*complexconjugate(Vv46) + C31*ZH23*complexconjugate(Vv24)*complexconjugate(Vv46) + C23*ZH23*complexconjugate(Vv25)*complexconjugate(Vv46) + C32*ZH23*complexconjugate(Vv25)*complexconjugate(Vv46)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_902 = Coupling(name = 'GC_902',
	 value = '(1./2.*complex(0,1)*(Vv26*Vv44*ZH33*complexconjugate(C13) + Vv26*Vv45*ZH33*complexconjugate(C23) + Vv26*Vv44*ZH33*complexconjugate(C31) + Vv26*Vv45*ZH33*complexconjugate(C32) + 2*Vv21*Vv44*ZH31*complexconjugate(Y1n11) + 2*Vv21*Vv45*ZH31*complexconjugate(Y1n12) + 2*Vv22*Vv44*ZH31*complexconjugate(Y1n21) + Vv24*(ZH33*(-2*Vv44*complexconjugate(BB11) + Vv45*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv46*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv41*ZH31*complexconjugate(Y1n11) + 2*Vv42*ZH31*complexconjugate(Y1n21)) + 2*Vv22*Vv45*ZH31*complexconjugate(Y1n22) + Vv25*(ZH33*(Vv44*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv45*complexconjugate(BB22) + Vv46*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv41*ZH31*complexconjugate(Y1n12) + 2*Vv42*ZH31*complexconjugate(Y1n22)) + 2*Vv26*Vv43*ZH32*complexconjugate(Y2n33) + 2*Vv23*Vv46*ZH32*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_903 = Coupling(name = 'GC_903',
	 value = '(1./2.*complex(0,1)*(2*Y1n21*ZH31*complexconjugate(Vv24)*complexconjugate(Vv42) + 2*Y1n22*ZH31*complexconjugate(Vv25)*complexconjugate(Vv42) + 2*Y2n33*ZH32*complexconjugate(Vv26)*complexconjugate(Vv43) + 2*Y1n21*ZH31*complexconjugate(Vv22)*complexconjugate(Vv44) - 2*BB11*ZH33*complexconjugate(Vv24)*complexconjugate(Vv44) + BB12*ZH33*complexconjugate(Vv25)*complexconjugate(Vv44) + BB21*ZH33*complexconjugate(Vv25)*complexconjugate(Vv44) + C13*ZH33*complexconjugate(Vv26)*complexconjugate(Vv44) + C31*ZH33*complexconjugate(Vv26)*complexconjugate(Vv44) + 2*Y1n11*ZH31*(complexconjugate(Vv24)*complexconjugate(Vv41) + complexconjugate(Vv21)*complexconjugate(Vv44)) + 2*Y1n22*ZH31*complexconjugate(Vv22)*complexconjugate(Vv45) + BB12*ZH33*complexconjugate(Vv24)*complexconjugate(Vv45) + BB21*ZH33*complexconjugate(Vv24)*complexconjugate(Vv45) + 2*BB22*ZH33*complexconjugate(Vv25)*complexconjugate(Vv45) + C23*ZH33*complexconjugate(Vv26)*complexconjugate(Vv45) + C32*ZH33*complexconjugate(Vv26)*complexconjugate(Vv45) + 2*Y1n12*ZH31*(complexconjugate(Vv25)*complexconjugate(Vv41) + complexconjugate(Vv21)*complexconjugate(Vv45)) + 2*Y2n33*ZH32*complexconjugate(Vv23)*complexconjugate(Vv46) + C13*ZH33*complexconjugate(Vv24)*complexconjugate(Vv46) + C31*ZH33*complexconjugate(Vv24)*complexconjugate(Vv46) + C23*ZH33*complexconjugate(Vv25)*complexconjugate(Vv46) + C32*ZH33*complexconjugate(Vv25)*complexconjugate(Vv46)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_904 = Coupling(name = 'GC_904',
	 value = '(1./2.*complex(0,1)*(Vv26*Vv54*ZH13*complexconjugate(C13) + Vv26*Vv55*ZH13*complexconjugate(C23) + Vv26*Vv54*ZH13*complexconjugate(C31) + Vv26*Vv55*ZH13*complexconjugate(C32) + 2*Vv21*Vv54*ZH11*complexconjugate(Y1n11) + 2*Vv21*Vv55*ZH11*complexconjugate(Y1n12) + 2*Vv22*Vv54*ZH11*complexconjugate(Y1n21) + Vv24*(ZH13*(-2*Vv54*complexconjugate(BB11) + Vv55*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv56*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv51*ZH11*complexconjugate(Y1n11) + 2*Vv52*ZH11*complexconjugate(Y1n21)) + 2*Vv22*Vv55*ZH11*complexconjugate(Y1n22) + Vv25*(ZH13*(Vv54*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv55*complexconjugate(BB22) + Vv56*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv51*ZH11*complexconjugate(Y1n12) + 2*Vv52*ZH11*complexconjugate(Y1n22)) + 2*Vv26*Vv53*ZH12*complexconjugate(Y2n33) + 2*Vv23*Vv56*ZH12*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_905 = Coupling(name = 'GC_905',
	 value = '(1./2.*complex(0,1)*(2*Y1n21*ZH11*complexconjugate(Vv24)*complexconjugate(Vv52) + 2*Y1n22*ZH11*complexconjugate(Vv25)*complexconjugate(Vv52) + 2*Y2n33*ZH12*complexconjugate(Vv26)*complexconjugate(Vv53) + 2*Y1n21*ZH11*complexconjugate(Vv22)*complexconjugate(Vv54) - 2*BB11*ZH13*complexconjugate(Vv24)*complexconjugate(Vv54) + BB12*ZH13*complexconjugate(Vv25)*complexconjugate(Vv54) + BB21*ZH13*complexconjugate(Vv25)*complexconjugate(Vv54) + C13*ZH13*complexconjugate(Vv26)*complexconjugate(Vv54) + C31*ZH13*complexconjugate(Vv26)*complexconjugate(Vv54) + 2*Y1n11*ZH11*(complexconjugate(Vv24)*complexconjugate(Vv51) + complexconjugate(Vv21)*complexconjugate(Vv54)) + 2*Y1n22*ZH11*complexconjugate(Vv22)*complexconjugate(Vv55) + BB12*ZH13*complexconjugate(Vv24)*complexconjugate(Vv55) + BB21*ZH13*complexconjugate(Vv24)*complexconjugate(Vv55) + 2*BB22*ZH13*complexconjugate(Vv25)*complexconjugate(Vv55) + C23*ZH13*complexconjugate(Vv26)*complexconjugate(Vv55) + C32*ZH13*complexconjugate(Vv26)*complexconjugate(Vv55) + 2*Y1n12*ZH11*(complexconjugate(Vv25)*complexconjugate(Vv51) + complexconjugate(Vv21)*complexconjugate(Vv55)) + 2*Y2n33*ZH12*complexconjugate(Vv23)*complexconjugate(Vv56) + C13*ZH13*complexconjugate(Vv24)*complexconjugate(Vv56) + C31*ZH13*complexconjugate(Vv24)*complexconjugate(Vv56) + C23*ZH13*complexconjugate(Vv25)*complexconjugate(Vv56) + C32*ZH13*complexconjugate(Vv25)*complexconjugate(Vv56)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_906 = Coupling(name = 'GC_906',
	 value = '(1./2.*complex(0,1)*(Vv26*Vv54*ZH23*complexconjugate(C13) + Vv26*Vv55*ZH23*complexconjugate(C23) + Vv26*Vv54*ZH23*complexconjugate(C31) + Vv26*Vv55*ZH23*complexconjugate(C32) + 2*Vv21*Vv54*ZH21*complexconjugate(Y1n11) + 2*Vv21*Vv55*ZH21*complexconjugate(Y1n12) + 2*Vv22*Vv54*ZH21*complexconjugate(Y1n21) + Vv24*(ZH23*(-2*Vv54*complexconjugate(BB11) + Vv55*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv56*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv51*ZH21*complexconjugate(Y1n11) + 2*Vv52*ZH21*complexconjugate(Y1n21)) + 2*Vv22*Vv55*ZH21*complexconjugate(Y1n22) + Vv25*(ZH23*(Vv54*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv55*complexconjugate(BB22) + Vv56*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv51*ZH21*complexconjugate(Y1n12) + 2*Vv52*ZH21*complexconjugate(Y1n22)) + 2*Vv26*Vv53*ZH22*complexconjugate(Y2n33) + 2*Vv23*Vv56*ZH22*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_907 = Coupling(name = 'GC_907',
	 value = '(1./2.*complex(0,1)*(2*Y1n21*ZH21*complexconjugate(Vv24)*complexconjugate(Vv52) + 2*Y1n22*ZH21*complexconjugate(Vv25)*complexconjugate(Vv52) + 2*Y2n33*ZH22*complexconjugate(Vv26)*complexconjugate(Vv53) + 2*Y1n21*ZH21*complexconjugate(Vv22)*complexconjugate(Vv54) - 2*BB11*ZH23*complexconjugate(Vv24)*complexconjugate(Vv54) + BB12*ZH23*complexconjugate(Vv25)*complexconjugate(Vv54) + BB21*ZH23*complexconjugate(Vv25)*complexconjugate(Vv54) + C13*ZH23*complexconjugate(Vv26)*complexconjugate(Vv54) + C31*ZH23*complexconjugate(Vv26)*complexconjugate(Vv54) + 2*Y1n11*ZH21*(complexconjugate(Vv24)*complexconjugate(Vv51) + complexconjugate(Vv21)*complexconjugate(Vv54)) + 2*Y1n22*ZH21*complexconjugate(Vv22)*complexconjugate(Vv55) + BB12*ZH23*complexconjugate(Vv24)*complexconjugate(Vv55) + BB21*ZH23*complexconjugate(Vv24)*complexconjugate(Vv55) + 2*BB22*ZH23*complexconjugate(Vv25)*complexconjugate(Vv55) + C23*ZH23*complexconjugate(Vv26)*complexconjugate(Vv55) + C32*ZH23*complexconjugate(Vv26)*complexconjugate(Vv55) + 2*Y1n12*ZH21*(complexconjugate(Vv25)*complexconjugate(Vv51) + complexconjugate(Vv21)*complexconjugate(Vv55)) + 2*Y2n33*ZH22*complexconjugate(Vv23)*complexconjugate(Vv56) + C13*ZH23*complexconjugate(Vv24)*complexconjugate(Vv56) + C31*ZH23*complexconjugate(Vv24)*complexconjugate(Vv56) + C23*ZH23*complexconjugate(Vv25)*complexconjugate(Vv56) + C32*ZH23*complexconjugate(Vv25)*complexconjugate(Vv56)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_908 = Coupling(name = 'GC_908',
	 value = '(1./2.*complex(0,1)*(Vv26*Vv54*ZH33*complexconjugate(C13) + Vv26*Vv55*ZH33*complexconjugate(C23) + Vv26*Vv54*ZH33*complexconjugate(C31) + Vv26*Vv55*ZH33*complexconjugate(C32) + 2*Vv21*Vv54*ZH31*complexconjugate(Y1n11) + 2*Vv21*Vv55*ZH31*complexconjugate(Y1n12) + 2*Vv22*Vv54*ZH31*complexconjugate(Y1n21) + Vv24*(ZH33*(-2*Vv54*complexconjugate(BB11) + Vv55*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv56*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv51*ZH31*complexconjugate(Y1n11) + 2*Vv52*ZH31*complexconjugate(Y1n21)) + 2*Vv22*Vv55*ZH31*complexconjugate(Y1n22) + Vv25*(ZH33*(Vv54*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv55*complexconjugate(BB22) + Vv56*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv51*ZH31*complexconjugate(Y1n12) + 2*Vv52*ZH31*complexconjugate(Y1n22)) + 2*Vv26*Vv53*ZH32*complexconjugate(Y2n33) + 2*Vv23*Vv56*ZH32*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_909 = Coupling(name = 'GC_909',
	 value = '(1./2.*complex(0,1)*(2*Y1n21*ZH31*complexconjugate(Vv24)*complexconjugate(Vv52) + 2*Y1n22*ZH31*complexconjugate(Vv25)*complexconjugate(Vv52) + 2*Y2n33*ZH32*complexconjugate(Vv26)*complexconjugate(Vv53) + 2*Y1n21*ZH31*complexconjugate(Vv22)*complexconjugate(Vv54) - 2*BB11*ZH33*complexconjugate(Vv24)*complexconjugate(Vv54) + BB12*ZH33*complexconjugate(Vv25)*complexconjugate(Vv54) + BB21*ZH33*complexconjugate(Vv25)*complexconjugate(Vv54) + C13*ZH33*complexconjugate(Vv26)*complexconjugate(Vv54) + C31*ZH33*complexconjugate(Vv26)*complexconjugate(Vv54) + 2*Y1n11*ZH31*(complexconjugate(Vv24)*complexconjugate(Vv51) + complexconjugate(Vv21)*complexconjugate(Vv54)) + 2*Y1n22*ZH31*complexconjugate(Vv22)*complexconjugate(Vv55) + BB12*ZH33*complexconjugate(Vv24)*complexconjugate(Vv55) + BB21*ZH33*complexconjugate(Vv24)*complexconjugate(Vv55) + 2*BB22*ZH33*complexconjugate(Vv25)*complexconjugate(Vv55) + C23*ZH33*complexconjugate(Vv26)*complexconjugate(Vv55) + C32*ZH33*complexconjugate(Vv26)*complexconjugate(Vv55) + 2*Y1n12*ZH31*(complexconjugate(Vv25)*complexconjugate(Vv51) + complexconjugate(Vv21)*complexconjugate(Vv55)) + 2*Y2n33*ZH32*complexconjugate(Vv23)*complexconjugate(Vv56) + C13*ZH33*complexconjugate(Vv24)*complexconjugate(Vv56) + C31*ZH33*complexconjugate(Vv24)*complexconjugate(Vv56) + C23*ZH33*complexconjugate(Vv25)*complexconjugate(Vv56) + C32*ZH33*complexconjugate(Vv25)*complexconjugate(Vv56)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_910 = Coupling(name = 'GC_910',
	 value = '(1./2.*complex(0,1)*(Vv26*Vv64*ZH13*complexconjugate(C13) + Vv26*Vv65*ZH13*complexconjugate(C23) + Vv26*Vv64*ZH13*complexconjugate(C31) + Vv26*Vv65*ZH13*complexconjugate(C32) + 2*Vv21*Vv64*ZH11*complexconjugate(Y1n11) + 2*Vv21*Vv65*ZH11*complexconjugate(Y1n12) + 2*Vv22*Vv64*ZH11*complexconjugate(Y1n21) + Vv24*(ZH13*(-2*Vv64*complexconjugate(BB11) + Vv65*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv66*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv61*ZH11*complexconjugate(Y1n11) + 2*Vv62*ZH11*complexconjugate(Y1n21)) + 2*Vv22*Vv65*ZH11*complexconjugate(Y1n22) + Vv25*(ZH13*(Vv64*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv65*complexconjugate(BB22) + Vv66*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv61*ZH11*complexconjugate(Y1n12) + 2*Vv62*ZH11*complexconjugate(Y1n22)) + 2*Vv26*Vv63*ZH12*complexconjugate(Y2n33) + 2*Vv23*Vv66*ZH12*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_911 = Coupling(name = 'GC_911',
	 value = '(1./2.*complex(0,1)*(2*Y1n21*ZH11*complexconjugate(Vv24)*complexconjugate(Vv62) + 2*Y1n22*ZH11*complexconjugate(Vv25)*complexconjugate(Vv62) + 2*Y2n33*ZH12*complexconjugate(Vv26)*complexconjugate(Vv63) + 2*Y1n21*ZH11*complexconjugate(Vv22)*complexconjugate(Vv64) - 2*BB11*ZH13*complexconjugate(Vv24)*complexconjugate(Vv64) + BB12*ZH13*complexconjugate(Vv25)*complexconjugate(Vv64) + BB21*ZH13*complexconjugate(Vv25)*complexconjugate(Vv64) + C13*ZH13*complexconjugate(Vv26)*complexconjugate(Vv64) + C31*ZH13*complexconjugate(Vv26)*complexconjugate(Vv64) + 2*Y1n11*ZH11*(complexconjugate(Vv24)*complexconjugate(Vv61) + complexconjugate(Vv21)*complexconjugate(Vv64)) + 2*Y1n22*ZH11*complexconjugate(Vv22)*complexconjugate(Vv65) + BB12*ZH13*complexconjugate(Vv24)*complexconjugate(Vv65) + BB21*ZH13*complexconjugate(Vv24)*complexconjugate(Vv65) + 2*BB22*ZH13*complexconjugate(Vv25)*complexconjugate(Vv65) + C23*ZH13*complexconjugate(Vv26)*complexconjugate(Vv65) + C32*ZH13*complexconjugate(Vv26)*complexconjugate(Vv65) + 2*Y1n12*ZH11*(complexconjugate(Vv25)*complexconjugate(Vv61) + complexconjugate(Vv21)*complexconjugate(Vv65)) + 2*Y2n33*ZH12*complexconjugate(Vv23)*complexconjugate(Vv66) + C13*ZH13*complexconjugate(Vv24)*complexconjugate(Vv66) + C31*ZH13*complexconjugate(Vv24)*complexconjugate(Vv66) + C23*ZH13*complexconjugate(Vv25)*complexconjugate(Vv66) + C32*ZH13*complexconjugate(Vv25)*complexconjugate(Vv66)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_912 = Coupling(name = 'GC_912',
	 value = '(1./2.*complex(0,1)*(Vv26*Vv64*ZH23*complexconjugate(C13) + Vv26*Vv65*ZH23*complexconjugate(C23) + Vv26*Vv64*ZH23*complexconjugate(C31) + Vv26*Vv65*ZH23*complexconjugate(C32) + 2*Vv21*Vv64*ZH21*complexconjugate(Y1n11) + 2*Vv21*Vv65*ZH21*complexconjugate(Y1n12) + 2*Vv22*Vv64*ZH21*complexconjugate(Y1n21) + Vv24*(ZH23*(-2*Vv64*complexconjugate(BB11) + Vv65*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv66*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv61*ZH21*complexconjugate(Y1n11) + 2*Vv62*ZH21*complexconjugate(Y1n21)) + 2*Vv22*Vv65*ZH21*complexconjugate(Y1n22) + Vv25*(ZH23*(Vv64*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv65*complexconjugate(BB22) + Vv66*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv61*ZH21*complexconjugate(Y1n12) + 2*Vv62*ZH21*complexconjugate(Y1n22)) + 2*Vv26*Vv63*ZH22*complexconjugate(Y2n33) + 2*Vv23*Vv66*ZH22*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_913 = Coupling(name = 'GC_913',
	 value = '(1./2.*complex(0,1)*(2*Y1n21*ZH21*complexconjugate(Vv24)*complexconjugate(Vv62) + 2*Y1n22*ZH21*complexconjugate(Vv25)*complexconjugate(Vv62) + 2*Y2n33*ZH22*complexconjugate(Vv26)*complexconjugate(Vv63) + 2*Y1n21*ZH21*complexconjugate(Vv22)*complexconjugate(Vv64) - 2*BB11*ZH23*complexconjugate(Vv24)*complexconjugate(Vv64) + BB12*ZH23*complexconjugate(Vv25)*complexconjugate(Vv64) + BB21*ZH23*complexconjugate(Vv25)*complexconjugate(Vv64) + C13*ZH23*complexconjugate(Vv26)*complexconjugate(Vv64) + C31*ZH23*complexconjugate(Vv26)*complexconjugate(Vv64) + 2*Y1n11*ZH21*(complexconjugate(Vv24)*complexconjugate(Vv61) + complexconjugate(Vv21)*complexconjugate(Vv64)) + 2*Y1n22*ZH21*complexconjugate(Vv22)*complexconjugate(Vv65) + BB12*ZH23*complexconjugate(Vv24)*complexconjugate(Vv65) + BB21*ZH23*complexconjugate(Vv24)*complexconjugate(Vv65) + 2*BB22*ZH23*complexconjugate(Vv25)*complexconjugate(Vv65) + C23*ZH23*complexconjugate(Vv26)*complexconjugate(Vv65) + C32*ZH23*complexconjugate(Vv26)*complexconjugate(Vv65) + 2*Y1n12*ZH21*(complexconjugate(Vv25)*complexconjugate(Vv61) + complexconjugate(Vv21)*complexconjugate(Vv65)) + 2*Y2n33*ZH22*complexconjugate(Vv23)*complexconjugate(Vv66) + C13*ZH23*complexconjugate(Vv24)*complexconjugate(Vv66) + C31*ZH23*complexconjugate(Vv24)*complexconjugate(Vv66) + C23*ZH23*complexconjugate(Vv25)*complexconjugate(Vv66) + C32*ZH23*complexconjugate(Vv25)*complexconjugate(Vv66)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_914 = Coupling(name = 'GC_914',
	 value = '(1./2.*complex(0,1)*(Vv26*Vv64*ZH33*complexconjugate(C13) + Vv26*Vv65*ZH33*complexconjugate(C23) + Vv26*Vv64*ZH33*complexconjugate(C31) + Vv26*Vv65*ZH33*complexconjugate(C32) + 2*Vv21*Vv64*ZH31*complexconjugate(Y1n11) + 2*Vv21*Vv65*ZH31*complexconjugate(Y1n12) + 2*Vv22*Vv64*ZH31*complexconjugate(Y1n21) + Vv24*(ZH33*(-2*Vv64*complexconjugate(BB11) + Vv65*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv66*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv61*ZH31*complexconjugate(Y1n11) + 2*Vv62*ZH31*complexconjugate(Y1n21)) + 2*Vv22*Vv65*ZH31*complexconjugate(Y1n22) + Vv25*(ZH33*(Vv64*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv65*complexconjugate(BB22) + Vv66*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv61*ZH31*complexconjugate(Y1n12) + 2*Vv62*ZH31*complexconjugate(Y1n22)) + 2*Vv26*Vv63*ZH32*complexconjugate(Y2n33) + 2*Vv23*Vv66*ZH32*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_915 = Coupling(name = 'GC_915',
	 value = '(1./2.*complex(0,1)*(2*Y1n21*ZH31*complexconjugate(Vv24)*complexconjugate(Vv62) + 2*Y1n22*ZH31*complexconjugate(Vv25)*complexconjugate(Vv62) + 2*Y2n33*ZH32*complexconjugate(Vv26)*complexconjugate(Vv63) + 2*Y1n21*ZH31*complexconjugate(Vv22)*complexconjugate(Vv64) - 2*BB11*ZH33*complexconjugate(Vv24)*complexconjugate(Vv64) + BB12*ZH33*complexconjugate(Vv25)*complexconjugate(Vv64) + BB21*ZH33*complexconjugate(Vv25)*complexconjugate(Vv64) + C13*ZH33*complexconjugate(Vv26)*complexconjugate(Vv64) + C31*ZH33*complexconjugate(Vv26)*complexconjugate(Vv64) + 2*Y1n11*ZH31*(complexconjugate(Vv24)*complexconjugate(Vv61) + complexconjugate(Vv21)*complexconjugate(Vv64)) + 2*Y1n22*ZH31*complexconjugate(Vv22)*complexconjugate(Vv65) + BB12*ZH33*complexconjugate(Vv24)*complexconjugate(Vv65) + BB21*ZH33*complexconjugate(Vv24)*complexconjugate(Vv65) + 2*BB22*ZH33*complexconjugate(Vv25)*complexconjugate(Vv65) + C23*ZH33*complexconjugate(Vv26)*complexconjugate(Vv65) + C32*ZH33*complexconjugate(Vv26)*complexconjugate(Vv65) + 2*Y1n12*ZH31*(complexconjugate(Vv25)*complexconjugate(Vv61) + complexconjugate(Vv21)*complexconjugate(Vv65)) + 2*Y2n33*ZH32*complexconjugate(Vv23)*complexconjugate(Vv66) + C13*ZH33*complexconjugate(Vv24)*complexconjugate(Vv66) + C31*ZH33*complexconjugate(Vv24)*complexconjugate(Vv66) + C23*ZH33*complexconjugate(Vv25)*complexconjugate(Vv66) + C32*ZH33*complexconjugate(Vv25)*complexconjugate(Vv66)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_916 = Coupling(name = 'GC_916',
	 value = '(1./2.*complex(0,1)*(Vv34*Vv36*ZH13*complexconjugate(C13) + Vv35*Vv36*ZH13*complexconjugate(C23) + Vv34*Vv36*ZH13*complexconjugate(C31) + Vv35*Vv36*ZH13*complexconjugate(C32) + 2*Vv31*Vv34*ZH11*complexconjugate(Y1n11) + 2*Vv31*Vv35*ZH11*complexconjugate(Y1n12) + 2*Vv32*Vv34*ZH11*complexconjugate(Y1n21) + Vv34*(ZH13*(-2*Vv34*complexconjugate(BB11) + Vv35*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv36*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv31*ZH11*complexconjugate(Y1n11) + 2*Vv32*ZH11*complexconjugate(Y1n21)) + 2*Vv32*Vv35*ZH11*complexconjugate(Y1n22) + Vv35*(ZH13*(Vv34*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv35*complexconjugate(BB22) + Vv36*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv31*ZH11*complexconjugate(Y1n12) + 2*Vv32*ZH11*complexconjugate(Y1n22)) + 4*Vv33*Vv36*ZH12*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_917 = Coupling(name = 'GC_917',
	 value = '(1./2.*complex(0,1)*(4*Y1n11*ZH11*complexconjugate(Vv31)*complexconjugate(Vv34) + 4*Y1n21*ZH11*complexconjugate(Vv32)*complexconjugate(Vv34) - 2*BB11*ZH13*complexconjugate(Vv34)**2 + 4*Y1n12*ZH11*complexconjugate(Vv31)*complexconjugate(Vv35) + 4*Y1n22*ZH11*complexconjugate(Vv32)*complexconjugate(Vv35) + 2*BB12*ZH13*complexconjugate(Vv34)*complexconjugate(Vv35) + 2*BB21*ZH13*complexconjugate(Vv34)*complexconjugate(Vv35) + 2*BB22*ZH13*complexconjugate(Vv35)**2 + 4*Y2n33*ZH12*complexconjugate(Vv33)*complexconjugate(Vv36) + 2*C13*ZH13*complexconjugate(Vv34)*complexconjugate(Vv36) + 2*C31*ZH13*complexconjugate(Vv34)*complexconjugate(Vv36) + 2*C23*ZH13*complexconjugate(Vv35)*complexconjugate(Vv36) + 2*C32*ZH13*complexconjugate(Vv35)*complexconjugate(Vv36)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_918 = Coupling(name = 'GC_918',
	 value = '(1./2.*complex(0,1)*(Vv34*Vv36*ZH23*complexconjugate(C13) + Vv35*Vv36*ZH23*complexconjugate(C23) + Vv34*Vv36*ZH23*complexconjugate(C31) + Vv35*Vv36*ZH23*complexconjugate(C32) + 2*Vv31*Vv34*ZH21*complexconjugate(Y1n11) + 2*Vv31*Vv35*ZH21*complexconjugate(Y1n12) + 2*Vv32*Vv34*ZH21*complexconjugate(Y1n21) + Vv34*(ZH23*(-2*Vv34*complexconjugate(BB11) + Vv35*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv36*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv31*ZH21*complexconjugate(Y1n11) + 2*Vv32*ZH21*complexconjugate(Y1n21)) + 2*Vv32*Vv35*ZH21*complexconjugate(Y1n22) + Vv35*(ZH23*(Vv34*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv35*complexconjugate(BB22) + Vv36*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv31*ZH21*complexconjugate(Y1n12) + 2*Vv32*ZH21*complexconjugate(Y1n22)) + 4*Vv33*Vv36*ZH22*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_919 = Coupling(name = 'GC_919',
	 value = '(1./2.*complex(0,1)*(4*Y1n11*ZH21*complexconjugate(Vv31)*complexconjugate(Vv34) + 4*Y1n21*ZH21*complexconjugate(Vv32)*complexconjugate(Vv34) - 2*BB11*ZH23*complexconjugate(Vv34)**2 + 4*Y1n12*ZH21*complexconjugate(Vv31)*complexconjugate(Vv35) + 4*Y1n22*ZH21*complexconjugate(Vv32)*complexconjugate(Vv35) + 2*BB12*ZH23*complexconjugate(Vv34)*complexconjugate(Vv35) + 2*BB21*ZH23*complexconjugate(Vv34)*complexconjugate(Vv35) + 2*BB22*ZH23*complexconjugate(Vv35)**2 + 4*Y2n33*ZH22*complexconjugate(Vv33)*complexconjugate(Vv36) + 2*C13*ZH23*complexconjugate(Vv34)*complexconjugate(Vv36) + 2*C31*ZH23*complexconjugate(Vv34)*complexconjugate(Vv36) + 2*C23*ZH23*complexconjugate(Vv35)*complexconjugate(Vv36) + 2*C32*ZH23*complexconjugate(Vv35)*complexconjugate(Vv36)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_920 = Coupling(name = 'GC_920',
	 value = '(1./2.*complex(0,1)*(Vv34*Vv36*ZH33*complexconjugate(C13) + Vv35*Vv36*ZH33*complexconjugate(C23) + Vv34*Vv36*ZH33*complexconjugate(C31) + Vv35*Vv36*ZH33*complexconjugate(C32) + 2*Vv31*Vv34*ZH31*complexconjugate(Y1n11) + 2*Vv31*Vv35*ZH31*complexconjugate(Y1n12) + 2*Vv32*Vv34*ZH31*complexconjugate(Y1n21) + Vv34*(ZH33*(-2*Vv34*complexconjugate(BB11) + Vv35*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv36*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv31*ZH31*complexconjugate(Y1n11) + 2*Vv32*ZH31*complexconjugate(Y1n21)) + 2*Vv32*Vv35*ZH31*complexconjugate(Y1n22) + Vv35*(ZH33*(Vv34*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv35*complexconjugate(BB22) + Vv36*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv31*ZH31*complexconjugate(Y1n12) + 2*Vv32*ZH31*complexconjugate(Y1n22)) + 4*Vv33*Vv36*ZH32*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_921 = Coupling(name = 'GC_921',
	 value = '(1./2.*complex(0,1)*(4*Y1n11*ZH31*complexconjugate(Vv31)*complexconjugate(Vv34) + 4*Y1n21*ZH31*complexconjugate(Vv32)*complexconjugate(Vv34) - 2*BB11*ZH33*complexconjugate(Vv34)**2 + 4*Y1n12*ZH31*complexconjugate(Vv31)*complexconjugate(Vv35) + 4*Y1n22*ZH31*complexconjugate(Vv32)*complexconjugate(Vv35) + 2*BB12*ZH33*complexconjugate(Vv34)*complexconjugate(Vv35) + 2*BB21*ZH33*complexconjugate(Vv34)*complexconjugate(Vv35) + 2*BB22*ZH33*complexconjugate(Vv35)**2 + 4*Y2n33*ZH32*complexconjugate(Vv33)*complexconjugate(Vv36) + 2*C13*ZH33*complexconjugate(Vv34)*complexconjugate(Vv36) + 2*C31*ZH33*complexconjugate(Vv34)*complexconjugate(Vv36) + 2*C23*ZH33*complexconjugate(Vv35)*complexconjugate(Vv36) + 2*C32*ZH33*complexconjugate(Vv35)*complexconjugate(Vv36)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_922 = Coupling(name = 'GC_922',
	 value = '(1./2.*complex(0,1)*(Vv36*Vv44*ZH13*complexconjugate(C13) + Vv36*Vv45*ZH13*complexconjugate(C23) + Vv36*Vv44*ZH13*complexconjugate(C31) + Vv36*Vv45*ZH13*complexconjugate(C32) + 2*Vv31*Vv44*ZH11*complexconjugate(Y1n11) + 2*Vv31*Vv45*ZH11*complexconjugate(Y1n12) + 2*Vv32*Vv44*ZH11*complexconjugate(Y1n21) + Vv34*(ZH13*(-2*Vv44*complexconjugate(BB11) + Vv45*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv46*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv41*ZH11*complexconjugate(Y1n11) + 2*Vv42*ZH11*complexconjugate(Y1n21)) + 2*Vv32*Vv45*ZH11*complexconjugate(Y1n22) + Vv35*(ZH13*(Vv44*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv45*complexconjugate(BB22) + Vv46*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv41*ZH11*complexconjugate(Y1n12) + 2*Vv42*ZH11*complexconjugate(Y1n22)) + 2*Vv36*Vv43*ZH12*complexconjugate(Y2n33) + 2*Vv33*Vv46*ZH12*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_923 = Coupling(name = 'GC_923',
	 value = '(1./2.*complex(0,1)*(2*Y1n21*ZH11*complexconjugate(Vv34)*complexconjugate(Vv42) + 2*Y1n22*ZH11*complexconjugate(Vv35)*complexconjugate(Vv42) + 2*Y2n33*ZH12*complexconjugate(Vv36)*complexconjugate(Vv43) + 2*Y1n21*ZH11*complexconjugate(Vv32)*complexconjugate(Vv44) - 2*BB11*ZH13*complexconjugate(Vv34)*complexconjugate(Vv44) + BB12*ZH13*complexconjugate(Vv35)*complexconjugate(Vv44) + BB21*ZH13*complexconjugate(Vv35)*complexconjugate(Vv44) + C13*ZH13*complexconjugate(Vv36)*complexconjugate(Vv44) + C31*ZH13*complexconjugate(Vv36)*complexconjugate(Vv44) + 2*Y1n11*ZH11*(complexconjugate(Vv34)*complexconjugate(Vv41) + complexconjugate(Vv31)*complexconjugate(Vv44)) + 2*Y1n22*ZH11*complexconjugate(Vv32)*complexconjugate(Vv45) + BB12*ZH13*complexconjugate(Vv34)*complexconjugate(Vv45) + BB21*ZH13*complexconjugate(Vv34)*complexconjugate(Vv45) + 2*BB22*ZH13*complexconjugate(Vv35)*complexconjugate(Vv45) + C23*ZH13*complexconjugate(Vv36)*complexconjugate(Vv45) + C32*ZH13*complexconjugate(Vv36)*complexconjugate(Vv45) + 2*Y1n12*ZH11*(complexconjugate(Vv35)*complexconjugate(Vv41) + complexconjugate(Vv31)*complexconjugate(Vv45)) + 2*Y2n33*ZH12*complexconjugate(Vv33)*complexconjugate(Vv46) + C13*ZH13*complexconjugate(Vv34)*complexconjugate(Vv46) + C31*ZH13*complexconjugate(Vv34)*complexconjugate(Vv46) + C23*ZH13*complexconjugate(Vv35)*complexconjugate(Vv46) + C32*ZH13*complexconjugate(Vv35)*complexconjugate(Vv46)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_924 = Coupling(name = 'GC_924',
	 value = '(1./2.*complex(0,1)*(Vv36*Vv44*ZH23*complexconjugate(C13) + Vv36*Vv45*ZH23*complexconjugate(C23) + Vv36*Vv44*ZH23*complexconjugate(C31) + Vv36*Vv45*ZH23*complexconjugate(C32) + 2*Vv31*Vv44*ZH21*complexconjugate(Y1n11) + 2*Vv31*Vv45*ZH21*complexconjugate(Y1n12) + 2*Vv32*Vv44*ZH21*complexconjugate(Y1n21) + Vv34*(ZH23*(-2*Vv44*complexconjugate(BB11) + Vv45*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv46*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv41*ZH21*complexconjugate(Y1n11) + 2*Vv42*ZH21*complexconjugate(Y1n21)) + 2*Vv32*Vv45*ZH21*complexconjugate(Y1n22) + Vv35*(ZH23*(Vv44*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv45*complexconjugate(BB22) + Vv46*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv41*ZH21*complexconjugate(Y1n12) + 2*Vv42*ZH21*complexconjugate(Y1n22)) + 2*Vv36*Vv43*ZH22*complexconjugate(Y2n33) + 2*Vv33*Vv46*ZH22*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_925 = Coupling(name = 'GC_925',
	 value = '(1./2.*complex(0,1)*(2*Y1n21*ZH21*complexconjugate(Vv34)*complexconjugate(Vv42) + 2*Y1n22*ZH21*complexconjugate(Vv35)*complexconjugate(Vv42) + 2*Y2n33*ZH22*complexconjugate(Vv36)*complexconjugate(Vv43) + 2*Y1n21*ZH21*complexconjugate(Vv32)*complexconjugate(Vv44) - 2*BB11*ZH23*complexconjugate(Vv34)*complexconjugate(Vv44) + BB12*ZH23*complexconjugate(Vv35)*complexconjugate(Vv44) + BB21*ZH23*complexconjugate(Vv35)*complexconjugate(Vv44) + C13*ZH23*complexconjugate(Vv36)*complexconjugate(Vv44) + C31*ZH23*complexconjugate(Vv36)*complexconjugate(Vv44) + 2*Y1n11*ZH21*(complexconjugate(Vv34)*complexconjugate(Vv41) + complexconjugate(Vv31)*complexconjugate(Vv44)) + 2*Y1n22*ZH21*complexconjugate(Vv32)*complexconjugate(Vv45) + BB12*ZH23*complexconjugate(Vv34)*complexconjugate(Vv45) + BB21*ZH23*complexconjugate(Vv34)*complexconjugate(Vv45) + 2*BB22*ZH23*complexconjugate(Vv35)*complexconjugate(Vv45) + C23*ZH23*complexconjugate(Vv36)*complexconjugate(Vv45) + C32*ZH23*complexconjugate(Vv36)*complexconjugate(Vv45) + 2*Y1n12*ZH21*(complexconjugate(Vv35)*complexconjugate(Vv41) + complexconjugate(Vv31)*complexconjugate(Vv45)) + 2*Y2n33*ZH22*complexconjugate(Vv33)*complexconjugate(Vv46) + C13*ZH23*complexconjugate(Vv34)*complexconjugate(Vv46) + C31*ZH23*complexconjugate(Vv34)*complexconjugate(Vv46) + C23*ZH23*complexconjugate(Vv35)*complexconjugate(Vv46) + C32*ZH23*complexconjugate(Vv35)*complexconjugate(Vv46)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_926 = Coupling(name = 'GC_926',
	 value = '(1./2.*complex(0,1)*(Vv36*Vv44*ZH33*complexconjugate(C13) + Vv36*Vv45*ZH33*complexconjugate(C23) + Vv36*Vv44*ZH33*complexconjugate(C31) + Vv36*Vv45*ZH33*complexconjugate(C32) + 2*Vv31*Vv44*ZH31*complexconjugate(Y1n11) + 2*Vv31*Vv45*ZH31*complexconjugate(Y1n12) + 2*Vv32*Vv44*ZH31*complexconjugate(Y1n21) + Vv34*(ZH33*(-2*Vv44*complexconjugate(BB11) + Vv45*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv46*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv41*ZH31*complexconjugate(Y1n11) + 2*Vv42*ZH31*complexconjugate(Y1n21)) + 2*Vv32*Vv45*ZH31*complexconjugate(Y1n22) + Vv35*(ZH33*(Vv44*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv45*complexconjugate(BB22) + Vv46*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv41*ZH31*complexconjugate(Y1n12) + 2*Vv42*ZH31*complexconjugate(Y1n22)) + 2*Vv36*Vv43*ZH32*complexconjugate(Y2n33) + 2*Vv33*Vv46*ZH32*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_927 = Coupling(name = 'GC_927',
	 value = '(1./2.*complex(0,1)*(2*Y1n21*ZH31*complexconjugate(Vv34)*complexconjugate(Vv42) + 2*Y1n22*ZH31*complexconjugate(Vv35)*complexconjugate(Vv42) + 2*Y2n33*ZH32*complexconjugate(Vv36)*complexconjugate(Vv43) + 2*Y1n21*ZH31*complexconjugate(Vv32)*complexconjugate(Vv44) - 2*BB11*ZH33*complexconjugate(Vv34)*complexconjugate(Vv44) + BB12*ZH33*complexconjugate(Vv35)*complexconjugate(Vv44) + BB21*ZH33*complexconjugate(Vv35)*complexconjugate(Vv44) + C13*ZH33*complexconjugate(Vv36)*complexconjugate(Vv44) + C31*ZH33*complexconjugate(Vv36)*complexconjugate(Vv44) + 2*Y1n11*ZH31*(complexconjugate(Vv34)*complexconjugate(Vv41) + complexconjugate(Vv31)*complexconjugate(Vv44)) + 2*Y1n22*ZH31*complexconjugate(Vv32)*complexconjugate(Vv45) + BB12*ZH33*complexconjugate(Vv34)*complexconjugate(Vv45) + BB21*ZH33*complexconjugate(Vv34)*complexconjugate(Vv45) + 2*BB22*ZH33*complexconjugate(Vv35)*complexconjugate(Vv45) + C23*ZH33*complexconjugate(Vv36)*complexconjugate(Vv45) + C32*ZH33*complexconjugate(Vv36)*complexconjugate(Vv45) + 2*Y1n12*ZH31*(complexconjugate(Vv35)*complexconjugate(Vv41) + complexconjugate(Vv31)*complexconjugate(Vv45)) + 2*Y2n33*ZH32*complexconjugate(Vv33)*complexconjugate(Vv46) + C13*ZH33*complexconjugate(Vv34)*complexconjugate(Vv46) + C31*ZH33*complexconjugate(Vv34)*complexconjugate(Vv46) + C23*ZH33*complexconjugate(Vv35)*complexconjugate(Vv46) + C32*ZH33*complexconjugate(Vv35)*complexconjugate(Vv46)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_928 = Coupling(name = 'GC_928',
	 value = '(1./2.*complex(0,1)*(Vv36*Vv54*ZH13*complexconjugate(C13) + Vv36*Vv55*ZH13*complexconjugate(C23) + Vv36*Vv54*ZH13*complexconjugate(C31) + Vv36*Vv55*ZH13*complexconjugate(C32) + 2*Vv31*Vv54*ZH11*complexconjugate(Y1n11) + 2*Vv31*Vv55*ZH11*complexconjugate(Y1n12) + 2*Vv32*Vv54*ZH11*complexconjugate(Y1n21) + Vv34*(ZH13*(-2*Vv54*complexconjugate(BB11) + Vv55*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv56*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv51*ZH11*complexconjugate(Y1n11) + 2*Vv52*ZH11*complexconjugate(Y1n21)) + 2*Vv32*Vv55*ZH11*complexconjugate(Y1n22) + Vv35*(ZH13*(Vv54*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv55*complexconjugate(BB22) + Vv56*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv51*ZH11*complexconjugate(Y1n12) + 2*Vv52*ZH11*complexconjugate(Y1n22)) + 2*Vv36*Vv53*ZH12*complexconjugate(Y2n33) + 2*Vv33*Vv56*ZH12*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_929 = Coupling(name = 'GC_929',
	 value = '(1./2.*complex(0,1)*(2*Y1n21*ZH11*complexconjugate(Vv34)*complexconjugate(Vv52) + 2*Y1n22*ZH11*complexconjugate(Vv35)*complexconjugate(Vv52) + 2*Y2n33*ZH12*complexconjugate(Vv36)*complexconjugate(Vv53) + 2*Y1n21*ZH11*complexconjugate(Vv32)*complexconjugate(Vv54) - 2*BB11*ZH13*complexconjugate(Vv34)*complexconjugate(Vv54) + BB12*ZH13*complexconjugate(Vv35)*complexconjugate(Vv54) + BB21*ZH13*complexconjugate(Vv35)*complexconjugate(Vv54) + C13*ZH13*complexconjugate(Vv36)*complexconjugate(Vv54) + C31*ZH13*complexconjugate(Vv36)*complexconjugate(Vv54) + 2*Y1n11*ZH11*(complexconjugate(Vv34)*complexconjugate(Vv51) + complexconjugate(Vv31)*complexconjugate(Vv54)) + 2*Y1n22*ZH11*complexconjugate(Vv32)*complexconjugate(Vv55) + BB12*ZH13*complexconjugate(Vv34)*complexconjugate(Vv55) + BB21*ZH13*complexconjugate(Vv34)*complexconjugate(Vv55) + 2*BB22*ZH13*complexconjugate(Vv35)*complexconjugate(Vv55) + C23*ZH13*complexconjugate(Vv36)*complexconjugate(Vv55) + C32*ZH13*complexconjugate(Vv36)*complexconjugate(Vv55) + 2*Y1n12*ZH11*(complexconjugate(Vv35)*complexconjugate(Vv51) + complexconjugate(Vv31)*complexconjugate(Vv55)) + 2*Y2n33*ZH12*complexconjugate(Vv33)*complexconjugate(Vv56) + C13*ZH13*complexconjugate(Vv34)*complexconjugate(Vv56) + C31*ZH13*complexconjugate(Vv34)*complexconjugate(Vv56) + C23*ZH13*complexconjugate(Vv35)*complexconjugate(Vv56) + C32*ZH13*complexconjugate(Vv35)*complexconjugate(Vv56)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_930 = Coupling(name = 'GC_930',
	 value = '(1./2.*complex(0,1)*(Vv36*Vv54*ZH23*complexconjugate(C13) + Vv36*Vv55*ZH23*complexconjugate(C23) + Vv36*Vv54*ZH23*complexconjugate(C31) + Vv36*Vv55*ZH23*complexconjugate(C32) + 2*Vv31*Vv54*ZH21*complexconjugate(Y1n11) + 2*Vv31*Vv55*ZH21*complexconjugate(Y1n12) + 2*Vv32*Vv54*ZH21*complexconjugate(Y1n21) + Vv34*(ZH23*(-2*Vv54*complexconjugate(BB11) + Vv55*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv56*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv51*ZH21*complexconjugate(Y1n11) + 2*Vv52*ZH21*complexconjugate(Y1n21)) + 2*Vv32*Vv55*ZH21*complexconjugate(Y1n22) + Vv35*(ZH23*(Vv54*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv55*complexconjugate(BB22) + Vv56*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv51*ZH21*complexconjugate(Y1n12) + 2*Vv52*ZH21*complexconjugate(Y1n22)) + 2*Vv36*Vv53*ZH22*complexconjugate(Y2n33) + 2*Vv33*Vv56*ZH22*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_931 = Coupling(name = 'GC_931',
	 value = '(1./2.*complex(0,1)*(2*Y1n21*ZH21*complexconjugate(Vv34)*complexconjugate(Vv52) + 2*Y1n22*ZH21*complexconjugate(Vv35)*complexconjugate(Vv52) + 2*Y2n33*ZH22*complexconjugate(Vv36)*complexconjugate(Vv53) + 2*Y1n21*ZH21*complexconjugate(Vv32)*complexconjugate(Vv54) - 2*BB11*ZH23*complexconjugate(Vv34)*complexconjugate(Vv54) + BB12*ZH23*complexconjugate(Vv35)*complexconjugate(Vv54) + BB21*ZH23*complexconjugate(Vv35)*complexconjugate(Vv54) + C13*ZH23*complexconjugate(Vv36)*complexconjugate(Vv54) + C31*ZH23*complexconjugate(Vv36)*complexconjugate(Vv54) + 2*Y1n11*ZH21*(complexconjugate(Vv34)*complexconjugate(Vv51) + complexconjugate(Vv31)*complexconjugate(Vv54)) + 2*Y1n22*ZH21*complexconjugate(Vv32)*complexconjugate(Vv55) + BB12*ZH23*complexconjugate(Vv34)*complexconjugate(Vv55) + BB21*ZH23*complexconjugate(Vv34)*complexconjugate(Vv55) + 2*BB22*ZH23*complexconjugate(Vv35)*complexconjugate(Vv55) + C23*ZH23*complexconjugate(Vv36)*complexconjugate(Vv55) + C32*ZH23*complexconjugate(Vv36)*complexconjugate(Vv55) + 2*Y1n12*ZH21*(complexconjugate(Vv35)*complexconjugate(Vv51) + complexconjugate(Vv31)*complexconjugate(Vv55)) + 2*Y2n33*ZH22*complexconjugate(Vv33)*complexconjugate(Vv56) + C13*ZH23*complexconjugate(Vv34)*complexconjugate(Vv56) + C31*ZH23*complexconjugate(Vv34)*complexconjugate(Vv56) + C23*ZH23*complexconjugate(Vv35)*complexconjugate(Vv56) + C32*ZH23*complexconjugate(Vv35)*complexconjugate(Vv56)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_932 = Coupling(name = 'GC_932',
	 value = '(1./2.*complex(0,1)*(Vv36*Vv54*ZH33*complexconjugate(C13) + Vv36*Vv55*ZH33*complexconjugate(C23) + Vv36*Vv54*ZH33*complexconjugate(C31) + Vv36*Vv55*ZH33*complexconjugate(C32) + 2*Vv31*Vv54*ZH31*complexconjugate(Y1n11) + 2*Vv31*Vv55*ZH31*complexconjugate(Y1n12) + 2*Vv32*Vv54*ZH31*complexconjugate(Y1n21) + Vv34*(ZH33*(-2*Vv54*complexconjugate(BB11) + Vv55*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv56*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv51*ZH31*complexconjugate(Y1n11) + 2*Vv52*ZH31*complexconjugate(Y1n21)) + 2*Vv32*Vv55*ZH31*complexconjugate(Y1n22) + Vv35*(ZH33*(Vv54*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv55*complexconjugate(BB22) + Vv56*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv51*ZH31*complexconjugate(Y1n12) + 2*Vv52*ZH31*complexconjugate(Y1n22)) + 2*Vv36*Vv53*ZH32*complexconjugate(Y2n33) + 2*Vv33*Vv56*ZH32*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_933 = Coupling(name = 'GC_933',
	 value = '(1./2.*complex(0,1)*(2*Y1n21*ZH31*complexconjugate(Vv34)*complexconjugate(Vv52) + 2*Y1n22*ZH31*complexconjugate(Vv35)*complexconjugate(Vv52) + 2*Y2n33*ZH32*complexconjugate(Vv36)*complexconjugate(Vv53) + 2*Y1n21*ZH31*complexconjugate(Vv32)*complexconjugate(Vv54) - 2*BB11*ZH33*complexconjugate(Vv34)*complexconjugate(Vv54) + BB12*ZH33*complexconjugate(Vv35)*complexconjugate(Vv54) + BB21*ZH33*complexconjugate(Vv35)*complexconjugate(Vv54) + C13*ZH33*complexconjugate(Vv36)*complexconjugate(Vv54) + C31*ZH33*complexconjugate(Vv36)*complexconjugate(Vv54) + 2*Y1n11*ZH31*(complexconjugate(Vv34)*complexconjugate(Vv51) + complexconjugate(Vv31)*complexconjugate(Vv54)) + 2*Y1n22*ZH31*complexconjugate(Vv32)*complexconjugate(Vv55) + BB12*ZH33*complexconjugate(Vv34)*complexconjugate(Vv55) + BB21*ZH33*complexconjugate(Vv34)*complexconjugate(Vv55) + 2*BB22*ZH33*complexconjugate(Vv35)*complexconjugate(Vv55) + C23*ZH33*complexconjugate(Vv36)*complexconjugate(Vv55) + C32*ZH33*complexconjugate(Vv36)*complexconjugate(Vv55) + 2*Y1n12*ZH31*(complexconjugate(Vv35)*complexconjugate(Vv51) + complexconjugate(Vv31)*complexconjugate(Vv55)) + 2*Y2n33*ZH32*complexconjugate(Vv33)*complexconjugate(Vv56) + C13*ZH33*complexconjugate(Vv34)*complexconjugate(Vv56) + C31*ZH33*complexconjugate(Vv34)*complexconjugate(Vv56) + C23*ZH33*complexconjugate(Vv35)*complexconjugate(Vv56) + C32*ZH33*complexconjugate(Vv35)*complexconjugate(Vv56)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_934 = Coupling(name = 'GC_934',
	 value = '(1./2.*complex(0,1)*(Vv36*Vv64*ZH13*complexconjugate(C13) + Vv36*Vv65*ZH13*complexconjugate(C23) + Vv36*Vv64*ZH13*complexconjugate(C31) + Vv36*Vv65*ZH13*complexconjugate(C32) + 2*Vv31*Vv64*ZH11*complexconjugate(Y1n11) + 2*Vv31*Vv65*ZH11*complexconjugate(Y1n12) + 2*Vv32*Vv64*ZH11*complexconjugate(Y1n21) + Vv34*(ZH13*(-2*Vv64*complexconjugate(BB11) + Vv65*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv66*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv61*ZH11*complexconjugate(Y1n11) + 2*Vv62*ZH11*complexconjugate(Y1n21)) + 2*Vv32*Vv65*ZH11*complexconjugate(Y1n22) + Vv35*(ZH13*(Vv64*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv65*complexconjugate(BB22) + Vv66*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv61*ZH11*complexconjugate(Y1n12) + 2*Vv62*ZH11*complexconjugate(Y1n22)) + 2*Vv36*Vv63*ZH12*complexconjugate(Y2n33) + 2*Vv33*Vv66*ZH12*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_935 = Coupling(name = 'GC_935',
	 value = '(1./2.*complex(0,1)*(2*Y1n21*ZH11*complexconjugate(Vv34)*complexconjugate(Vv62) + 2*Y1n22*ZH11*complexconjugate(Vv35)*complexconjugate(Vv62) + 2*Y2n33*ZH12*complexconjugate(Vv36)*complexconjugate(Vv63) + 2*Y1n21*ZH11*complexconjugate(Vv32)*complexconjugate(Vv64) - 2*BB11*ZH13*complexconjugate(Vv34)*complexconjugate(Vv64) + BB12*ZH13*complexconjugate(Vv35)*complexconjugate(Vv64) + BB21*ZH13*complexconjugate(Vv35)*complexconjugate(Vv64) + C13*ZH13*complexconjugate(Vv36)*complexconjugate(Vv64) + C31*ZH13*complexconjugate(Vv36)*complexconjugate(Vv64) + 2*Y1n11*ZH11*(complexconjugate(Vv34)*complexconjugate(Vv61) + complexconjugate(Vv31)*complexconjugate(Vv64)) + 2*Y1n22*ZH11*complexconjugate(Vv32)*complexconjugate(Vv65) + BB12*ZH13*complexconjugate(Vv34)*complexconjugate(Vv65) + BB21*ZH13*complexconjugate(Vv34)*complexconjugate(Vv65) + 2*BB22*ZH13*complexconjugate(Vv35)*complexconjugate(Vv65) + C23*ZH13*complexconjugate(Vv36)*complexconjugate(Vv65) + C32*ZH13*complexconjugate(Vv36)*complexconjugate(Vv65) + 2*Y1n12*ZH11*(complexconjugate(Vv35)*complexconjugate(Vv61) + complexconjugate(Vv31)*complexconjugate(Vv65)) + 2*Y2n33*ZH12*complexconjugate(Vv33)*complexconjugate(Vv66) + C13*ZH13*complexconjugate(Vv34)*complexconjugate(Vv66) + C31*ZH13*complexconjugate(Vv34)*complexconjugate(Vv66) + C23*ZH13*complexconjugate(Vv35)*complexconjugate(Vv66) + C32*ZH13*complexconjugate(Vv35)*complexconjugate(Vv66)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_936 = Coupling(name = 'GC_936',
	 value = '(1./2.*complex(0,1)*(Vv36*Vv64*ZH23*complexconjugate(C13) + Vv36*Vv65*ZH23*complexconjugate(C23) + Vv36*Vv64*ZH23*complexconjugate(C31) + Vv36*Vv65*ZH23*complexconjugate(C32) + 2*Vv31*Vv64*ZH21*complexconjugate(Y1n11) + 2*Vv31*Vv65*ZH21*complexconjugate(Y1n12) + 2*Vv32*Vv64*ZH21*complexconjugate(Y1n21) + Vv34*(ZH23*(-2*Vv64*complexconjugate(BB11) + Vv65*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv66*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv61*ZH21*complexconjugate(Y1n11) + 2*Vv62*ZH21*complexconjugate(Y1n21)) + 2*Vv32*Vv65*ZH21*complexconjugate(Y1n22) + Vv35*(ZH23*(Vv64*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv65*complexconjugate(BB22) + Vv66*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv61*ZH21*complexconjugate(Y1n12) + 2*Vv62*ZH21*complexconjugate(Y1n22)) + 2*Vv36*Vv63*ZH22*complexconjugate(Y2n33) + 2*Vv33*Vv66*ZH22*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_937 = Coupling(name = 'GC_937',
	 value = '(1./2.*complex(0,1)*(2*Y1n21*ZH21*complexconjugate(Vv34)*complexconjugate(Vv62) + 2*Y1n22*ZH21*complexconjugate(Vv35)*complexconjugate(Vv62) + 2*Y2n33*ZH22*complexconjugate(Vv36)*complexconjugate(Vv63) + 2*Y1n21*ZH21*complexconjugate(Vv32)*complexconjugate(Vv64) - 2*BB11*ZH23*complexconjugate(Vv34)*complexconjugate(Vv64) + BB12*ZH23*complexconjugate(Vv35)*complexconjugate(Vv64) + BB21*ZH23*complexconjugate(Vv35)*complexconjugate(Vv64) + C13*ZH23*complexconjugate(Vv36)*complexconjugate(Vv64) + C31*ZH23*complexconjugate(Vv36)*complexconjugate(Vv64) + 2*Y1n11*ZH21*(complexconjugate(Vv34)*complexconjugate(Vv61) + complexconjugate(Vv31)*complexconjugate(Vv64)) + 2*Y1n22*ZH21*complexconjugate(Vv32)*complexconjugate(Vv65) + BB12*ZH23*complexconjugate(Vv34)*complexconjugate(Vv65) + BB21*ZH23*complexconjugate(Vv34)*complexconjugate(Vv65) + 2*BB22*ZH23*complexconjugate(Vv35)*complexconjugate(Vv65) + C23*ZH23*complexconjugate(Vv36)*complexconjugate(Vv65) + C32*ZH23*complexconjugate(Vv36)*complexconjugate(Vv65) + 2*Y1n12*ZH21*(complexconjugate(Vv35)*complexconjugate(Vv61) + complexconjugate(Vv31)*complexconjugate(Vv65)) + 2*Y2n33*ZH22*complexconjugate(Vv33)*complexconjugate(Vv66) + C13*ZH23*complexconjugate(Vv34)*complexconjugate(Vv66) + C31*ZH23*complexconjugate(Vv34)*complexconjugate(Vv66) + C23*ZH23*complexconjugate(Vv35)*complexconjugate(Vv66) + C32*ZH23*complexconjugate(Vv35)*complexconjugate(Vv66)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_938 = Coupling(name = 'GC_938',
	 value = '(1./2.*complex(0,1)*(Vv36*Vv64*ZH33*complexconjugate(C13) + Vv36*Vv65*ZH33*complexconjugate(C23) + Vv36*Vv64*ZH33*complexconjugate(C31) + Vv36*Vv65*ZH33*complexconjugate(C32) + 2*Vv31*Vv64*ZH31*complexconjugate(Y1n11) + 2*Vv31*Vv65*ZH31*complexconjugate(Y1n12) + 2*Vv32*Vv64*ZH31*complexconjugate(Y1n21) + Vv34*(ZH33*(-2*Vv64*complexconjugate(BB11) + Vv65*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv66*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv61*ZH31*complexconjugate(Y1n11) + 2*Vv62*ZH31*complexconjugate(Y1n21)) + 2*Vv32*Vv65*ZH31*complexconjugate(Y1n22) + Vv35*(ZH33*(Vv64*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv65*complexconjugate(BB22) + Vv66*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv61*ZH31*complexconjugate(Y1n12) + 2*Vv62*ZH31*complexconjugate(Y1n22)) + 2*Vv36*Vv63*ZH32*complexconjugate(Y2n33) + 2*Vv33*Vv66*ZH32*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_939 = Coupling(name = 'GC_939',
	 value = '(1./2.*complex(0,1)*(2*Y1n21*ZH31*complexconjugate(Vv34)*complexconjugate(Vv62) + 2*Y1n22*ZH31*complexconjugate(Vv35)*complexconjugate(Vv62) + 2*Y2n33*ZH32*complexconjugate(Vv36)*complexconjugate(Vv63) + 2*Y1n21*ZH31*complexconjugate(Vv32)*complexconjugate(Vv64) - 2*BB11*ZH33*complexconjugate(Vv34)*complexconjugate(Vv64) + BB12*ZH33*complexconjugate(Vv35)*complexconjugate(Vv64) + BB21*ZH33*complexconjugate(Vv35)*complexconjugate(Vv64) + C13*ZH33*complexconjugate(Vv36)*complexconjugate(Vv64) + C31*ZH33*complexconjugate(Vv36)*complexconjugate(Vv64) + 2*Y1n11*ZH31*(complexconjugate(Vv34)*complexconjugate(Vv61) + complexconjugate(Vv31)*complexconjugate(Vv64)) + 2*Y1n22*ZH31*complexconjugate(Vv32)*complexconjugate(Vv65) + BB12*ZH33*complexconjugate(Vv34)*complexconjugate(Vv65) + BB21*ZH33*complexconjugate(Vv34)*complexconjugate(Vv65) + 2*BB22*ZH33*complexconjugate(Vv35)*complexconjugate(Vv65) + C23*ZH33*complexconjugate(Vv36)*complexconjugate(Vv65) + C32*ZH33*complexconjugate(Vv36)*complexconjugate(Vv65) + 2*Y1n12*ZH31*(complexconjugate(Vv35)*complexconjugate(Vv61) + complexconjugate(Vv31)*complexconjugate(Vv65)) + 2*Y2n33*ZH32*complexconjugate(Vv33)*complexconjugate(Vv66) + C13*ZH33*complexconjugate(Vv34)*complexconjugate(Vv66) + C31*ZH33*complexconjugate(Vv34)*complexconjugate(Vv66) + C23*ZH33*complexconjugate(Vv35)*complexconjugate(Vv66) + C32*ZH33*complexconjugate(Vv35)*complexconjugate(Vv66)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_940 = Coupling(name = 'GC_940',
	 value = '(1./2.*complex(0,1)*(Vv44*Vv46*ZH13*complexconjugate(C13) + Vv45*Vv46*ZH13*complexconjugate(C23) + Vv44*Vv46*ZH13*complexconjugate(C31) + Vv45*Vv46*ZH13*complexconjugate(C32) + 2*Vv41*Vv44*ZH11*complexconjugate(Y1n11) + 2*Vv41*Vv45*ZH11*complexconjugate(Y1n12) + 2*Vv42*Vv44*ZH11*complexconjugate(Y1n21) + Vv44*(ZH13*(-2*Vv44*complexconjugate(BB11) + Vv45*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv46*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv41*ZH11*complexconjugate(Y1n11) + 2*Vv42*ZH11*complexconjugate(Y1n21)) + 2*Vv42*Vv45*ZH11*complexconjugate(Y1n22) + Vv45*(ZH13*(Vv44*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv45*complexconjugate(BB22) + Vv46*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv41*ZH11*complexconjugate(Y1n12) + 2*Vv42*ZH11*complexconjugate(Y1n22)) + 4*Vv43*Vv46*ZH12*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_941 = Coupling(name = 'GC_941',
	 value = '(1./2.*complex(0,1)*(4*Y1n11*ZH11*complexconjugate(Vv41)*complexconjugate(Vv44) + 4*Y1n21*ZH11*complexconjugate(Vv42)*complexconjugate(Vv44) - 2*BB11*ZH13*complexconjugate(Vv44)**2 + 4*Y1n12*ZH11*complexconjugate(Vv41)*complexconjugate(Vv45) + 4*Y1n22*ZH11*complexconjugate(Vv42)*complexconjugate(Vv45) + 2*BB12*ZH13*complexconjugate(Vv44)*complexconjugate(Vv45) + 2*BB21*ZH13*complexconjugate(Vv44)*complexconjugate(Vv45) + 2*BB22*ZH13*complexconjugate(Vv45)**2 + 4*Y2n33*ZH12*complexconjugate(Vv43)*complexconjugate(Vv46) + 2*C13*ZH13*complexconjugate(Vv44)*complexconjugate(Vv46) + 2*C31*ZH13*complexconjugate(Vv44)*complexconjugate(Vv46) + 2*C23*ZH13*complexconjugate(Vv45)*complexconjugate(Vv46) + 2*C32*ZH13*complexconjugate(Vv45)*complexconjugate(Vv46)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_942 = Coupling(name = 'GC_942',
	 value = '(1./2.*complex(0,1)*(Vv44*Vv46*ZH23*complexconjugate(C13) + Vv45*Vv46*ZH23*complexconjugate(C23) + Vv44*Vv46*ZH23*complexconjugate(C31) + Vv45*Vv46*ZH23*complexconjugate(C32) + 2*Vv41*Vv44*ZH21*complexconjugate(Y1n11) + 2*Vv41*Vv45*ZH21*complexconjugate(Y1n12) + 2*Vv42*Vv44*ZH21*complexconjugate(Y1n21) + Vv44*(ZH23*(-2*Vv44*complexconjugate(BB11) + Vv45*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv46*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv41*ZH21*complexconjugate(Y1n11) + 2*Vv42*ZH21*complexconjugate(Y1n21)) + 2*Vv42*Vv45*ZH21*complexconjugate(Y1n22) + Vv45*(ZH23*(Vv44*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv45*complexconjugate(BB22) + Vv46*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv41*ZH21*complexconjugate(Y1n12) + 2*Vv42*ZH21*complexconjugate(Y1n22)) + 4*Vv43*Vv46*ZH22*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_943 = Coupling(name = 'GC_943',
	 value = '(1./2.*complex(0,1)*(4*Y1n11*ZH21*complexconjugate(Vv41)*complexconjugate(Vv44) + 4*Y1n21*ZH21*complexconjugate(Vv42)*complexconjugate(Vv44) - 2*BB11*ZH23*complexconjugate(Vv44)**2 + 4*Y1n12*ZH21*complexconjugate(Vv41)*complexconjugate(Vv45) + 4*Y1n22*ZH21*complexconjugate(Vv42)*complexconjugate(Vv45) + 2*BB12*ZH23*complexconjugate(Vv44)*complexconjugate(Vv45) + 2*BB21*ZH23*complexconjugate(Vv44)*complexconjugate(Vv45) + 2*BB22*ZH23*complexconjugate(Vv45)**2 + 4*Y2n33*ZH22*complexconjugate(Vv43)*complexconjugate(Vv46) + 2*C13*ZH23*complexconjugate(Vv44)*complexconjugate(Vv46) + 2*C31*ZH23*complexconjugate(Vv44)*complexconjugate(Vv46) + 2*C23*ZH23*complexconjugate(Vv45)*complexconjugate(Vv46) + 2*C32*ZH23*complexconjugate(Vv45)*complexconjugate(Vv46)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_944 = Coupling(name = 'GC_944',
	 value = '(1./2.*complex(0,1)*(Vv44*Vv46*ZH33*complexconjugate(C13) + Vv45*Vv46*ZH33*complexconjugate(C23) + Vv44*Vv46*ZH33*complexconjugate(C31) + Vv45*Vv46*ZH33*complexconjugate(C32) + 2*Vv41*Vv44*ZH31*complexconjugate(Y1n11) + 2*Vv41*Vv45*ZH31*complexconjugate(Y1n12) + 2*Vv42*Vv44*ZH31*complexconjugate(Y1n21) + Vv44*(ZH33*(-2*Vv44*complexconjugate(BB11) + Vv45*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv46*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv41*ZH31*complexconjugate(Y1n11) + 2*Vv42*ZH31*complexconjugate(Y1n21)) + 2*Vv42*Vv45*ZH31*complexconjugate(Y1n22) + Vv45*(ZH33*(Vv44*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv45*complexconjugate(BB22) + Vv46*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv41*ZH31*complexconjugate(Y1n12) + 2*Vv42*ZH31*complexconjugate(Y1n22)) + 4*Vv43*Vv46*ZH32*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_945 = Coupling(name = 'GC_945',
	 value = '(1./2.*complex(0,1)*(4*Y1n11*ZH31*complexconjugate(Vv41)*complexconjugate(Vv44) + 4*Y1n21*ZH31*complexconjugate(Vv42)*complexconjugate(Vv44) - 2*BB11*ZH33*complexconjugate(Vv44)**2 + 4*Y1n12*ZH31*complexconjugate(Vv41)*complexconjugate(Vv45) + 4*Y1n22*ZH31*complexconjugate(Vv42)*complexconjugate(Vv45) + 2*BB12*ZH33*complexconjugate(Vv44)*complexconjugate(Vv45) + 2*BB21*ZH33*complexconjugate(Vv44)*complexconjugate(Vv45) + 2*BB22*ZH33*complexconjugate(Vv45)**2 + 4*Y2n33*ZH32*complexconjugate(Vv43)*complexconjugate(Vv46) + 2*C13*ZH33*complexconjugate(Vv44)*complexconjugate(Vv46) + 2*C31*ZH33*complexconjugate(Vv44)*complexconjugate(Vv46) + 2*C23*ZH33*complexconjugate(Vv45)*complexconjugate(Vv46) + 2*C32*ZH33*complexconjugate(Vv45)*complexconjugate(Vv46)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_946 = Coupling(name = 'GC_946',
	 value = '(1./2.*complex(0,1)*(Vv46*Vv54*ZH13*complexconjugate(C13) + Vv46*Vv55*ZH13*complexconjugate(C23) + Vv46*Vv54*ZH13*complexconjugate(C31) + Vv46*Vv55*ZH13*complexconjugate(C32) + 2*Vv41*Vv54*ZH11*complexconjugate(Y1n11) + 2*Vv41*Vv55*ZH11*complexconjugate(Y1n12) + 2*Vv42*Vv54*ZH11*complexconjugate(Y1n21) + Vv44*(ZH13*(-2*Vv54*complexconjugate(BB11) + Vv55*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv56*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv51*ZH11*complexconjugate(Y1n11) + 2*Vv52*ZH11*complexconjugate(Y1n21)) + 2*Vv42*Vv55*ZH11*complexconjugate(Y1n22) + Vv45*(ZH13*(Vv54*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv55*complexconjugate(BB22) + Vv56*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv51*ZH11*complexconjugate(Y1n12) + 2*Vv52*ZH11*complexconjugate(Y1n22)) + 2*Vv46*Vv53*ZH12*complexconjugate(Y2n33) + 2*Vv43*Vv56*ZH12*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_947 = Coupling(name = 'GC_947',
	 value = '(1./2.*complex(0,1)*(2*Y1n21*ZH11*complexconjugate(Vv44)*complexconjugate(Vv52) + 2*Y1n22*ZH11*complexconjugate(Vv45)*complexconjugate(Vv52) + 2*Y2n33*ZH12*complexconjugate(Vv46)*complexconjugate(Vv53) + 2*Y1n21*ZH11*complexconjugate(Vv42)*complexconjugate(Vv54) - 2*BB11*ZH13*complexconjugate(Vv44)*complexconjugate(Vv54) + BB12*ZH13*complexconjugate(Vv45)*complexconjugate(Vv54) + BB21*ZH13*complexconjugate(Vv45)*complexconjugate(Vv54) + C13*ZH13*complexconjugate(Vv46)*complexconjugate(Vv54) + C31*ZH13*complexconjugate(Vv46)*complexconjugate(Vv54) + 2*Y1n11*ZH11*(complexconjugate(Vv44)*complexconjugate(Vv51) + complexconjugate(Vv41)*complexconjugate(Vv54)) + 2*Y1n22*ZH11*complexconjugate(Vv42)*complexconjugate(Vv55) + BB12*ZH13*complexconjugate(Vv44)*complexconjugate(Vv55) + BB21*ZH13*complexconjugate(Vv44)*complexconjugate(Vv55) + 2*BB22*ZH13*complexconjugate(Vv45)*complexconjugate(Vv55) + C23*ZH13*complexconjugate(Vv46)*complexconjugate(Vv55) + C32*ZH13*complexconjugate(Vv46)*complexconjugate(Vv55) + 2*Y1n12*ZH11*(complexconjugate(Vv45)*complexconjugate(Vv51) + complexconjugate(Vv41)*complexconjugate(Vv55)) + 2*Y2n33*ZH12*complexconjugate(Vv43)*complexconjugate(Vv56) + C13*ZH13*complexconjugate(Vv44)*complexconjugate(Vv56) + C31*ZH13*complexconjugate(Vv44)*complexconjugate(Vv56) + C23*ZH13*complexconjugate(Vv45)*complexconjugate(Vv56) + C32*ZH13*complexconjugate(Vv45)*complexconjugate(Vv56)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_948 = Coupling(name = 'GC_948',
	 value = '(1./2.*complex(0,1)*(Vv46*Vv54*ZH23*complexconjugate(C13) + Vv46*Vv55*ZH23*complexconjugate(C23) + Vv46*Vv54*ZH23*complexconjugate(C31) + Vv46*Vv55*ZH23*complexconjugate(C32) + 2*Vv41*Vv54*ZH21*complexconjugate(Y1n11) + 2*Vv41*Vv55*ZH21*complexconjugate(Y1n12) + 2*Vv42*Vv54*ZH21*complexconjugate(Y1n21) + Vv44*(ZH23*(-2*Vv54*complexconjugate(BB11) + Vv55*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv56*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv51*ZH21*complexconjugate(Y1n11) + 2*Vv52*ZH21*complexconjugate(Y1n21)) + 2*Vv42*Vv55*ZH21*complexconjugate(Y1n22) + Vv45*(ZH23*(Vv54*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv55*complexconjugate(BB22) + Vv56*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv51*ZH21*complexconjugate(Y1n12) + 2*Vv52*ZH21*complexconjugate(Y1n22)) + 2*Vv46*Vv53*ZH22*complexconjugate(Y2n33) + 2*Vv43*Vv56*ZH22*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_949 = Coupling(name = 'GC_949',
	 value = '(1./2.*complex(0,1)*(2*Y1n21*ZH21*complexconjugate(Vv44)*complexconjugate(Vv52) + 2*Y1n22*ZH21*complexconjugate(Vv45)*complexconjugate(Vv52) + 2*Y2n33*ZH22*complexconjugate(Vv46)*complexconjugate(Vv53) + 2*Y1n21*ZH21*complexconjugate(Vv42)*complexconjugate(Vv54) - 2*BB11*ZH23*complexconjugate(Vv44)*complexconjugate(Vv54) + BB12*ZH23*complexconjugate(Vv45)*complexconjugate(Vv54) + BB21*ZH23*complexconjugate(Vv45)*complexconjugate(Vv54) + C13*ZH23*complexconjugate(Vv46)*complexconjugate(Vv54) + C31*ZH23*complexconjugate(Vv46)*complexconjugate(Vv54) + 2*Y1n11*ZH21*(complexconjugate(Vv44)*complexconjugate(Vv51) + complexconjugate(Vv41)*complexconjugate(Vv54)) + 2*Y1n22*ZH21*complexconjugate(Vv42)*complexconjugate(Vv55) + BB12*ZH23*complexconjugate(Vv44)*complexconjugate(Vv55) + BB21*ZH23*complexconjugate(Vv44)*complexconjugate(Vv55) + 2*BB22*ZH23*complexconjugate(Vv45)*complexconjugate(Vv55) + C23*ZH23*complexconjugate(Vv46)*complexconjugate(Vv55) + C32*ZH23*complexconjugate(Vv46)*complexconjugate(Vv55) + 2*Y1n12*ZH21*(complexconjugate(Vv45)*complexconjugate(Vv51) + complexconjugate(Vv41)*complexconjugate(Vv55)) + 2*Y2n33*ZH22*complexconjugate(Vv43)*complexconjugate(Vv56) + C13*ZH23*complexconjugate(Vv44)*complexconjugate(Vv56) + C31*ZH23*complexconjugate(Vv44)*complexconjugate(Vv56) + C23*ZH23*complexconjugate(Vv45)*complexconjugate(Vv56) + C32*ZH23*complexconjugate(Vv45)*complexconjugate(Vv56)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_950 = Coupling(name = 'GC_950',
	 value = '(1./2.*complex(0,1)*(Vv46*Vv54*ZH33*complexconjugate(C13) + Vv46*Vv55*ZH33*complexconjugate(C23) + Vv46*Vv54*ZH33*complexconjugate(C31) + Vv46*Vv55*ZH33*complexconjugate(C32) + 2*Vv41*Vv54*ZH31*complexconjugate(Y1n11) + 2*Vv41*Vv55*ZH31*complexconjugate(Y1n12) + 2*Vv42*Vv54*ZH31*complexconjugate(Y1n21) + Vv44*(ZH33*(-2*Vv54*complexconjugate(BB11) + Vv55*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv56*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv51*ZH31*complexconjugate(Y1n11) + 2*Vv52*ZH31*complexconjugate(Y1n21)) + 2*Vv42*Vv55*ZH31*complexconjugate(Y1n22) + Vv45*(ZH33*(Vv54*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv55*complexconjugate(BB22) + Vv56*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv51*ZH31*complexconjugate(Y1n12) + 2*Vv52*ZH31*complexconjugate(Y1n22)) + 2*Vv46*Vv53*ZH32*complexconjugate(Y2n33) + 2*Vv43*Vv56*ZH32*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_951 = Coupling(name = 'GC_951',
	 value = '(1./2.*complex(0,1)*(2*Y1n21*ZH31*complexconjugate(Vv44)*complexconjugate(Vv52) + 2*Y1n22*ZH31*complexconjugate(Vv45)*complexconjugate(Vv52) + 2*Y2n33*ZH32*complexconjugate(Vv46)*complexconjugate(Vv53) + 2*Y1n21*ZH31*complexconjugate(Vv42)*complexconjugate(Vv54) - 2*BB11*ZH33*complexconjugate(Vv44)*complexconjugate(Vv54) + BB12*ZH33*complexconjugate(Vv45)*complexconjugate(Vv54) + BB21*ZH33*complexconjugate(Vv45)*complexconjugate(Vv54) + C13*ZH33*complexconjugate(Vv46)*complexconjugate(Vv54) + C31*ZH33*complexconjugate(Vv46)*complexconjugate(Vv54) + 2*Y1n11*ZH31*(complexconjugate(Vv44)*complexconjugate(Vv51) + complexconjugate(Vv41)*complexconjugate(Vv54)) + 2*Y1n22*ZH31*complexconjugate(Vv42)*complexconjugate(Vv55) + BB12*ZH33*complexconjugate(Vv44)*complexconjugate(Vv55) + BB21*ZH33*complexconjugate(Vv44)*complexconjugate(Vv55) + 2*BB22*ZH33*complexconjugate(Vv45)*complexconjugate(Vv55) + C23*ZH33*complexconjugate(Vv46)*complexconjugate(Vv55) + C32*ZH33*complexconjugate(Vv46)*complexconjugate(Vv55) + 2*Y1n12*ZH31*(complexconjugate(Vv45)*complexconjugate(Vv51) + complexconjugate(Vv41)*complexconjugate(Vv55)) + 2*Y2n33*ZH32*complexconjugate(Vv43)*complexconjugate(Vv56) + C13*ZH33*complexconjugate(Vv44)*complexconjugate(Vv56) + C31*ZH33*complexconjugate(Vv44)*complexconjugate(Vv56) + C23*ZH33*complexconjugate(Vv45)*complexconjugate(Vv56) + C32*ZH33*complexconjugate(Vv45)*complexconjugate(Vv56)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_952 = Coupling(name = 'GC_952',
	 value = '(1./2.*complex(0,1)*(Vv46*Vv64*ZH13*complexconjugate(C13) + Vv46*Vv65*ZH13*complexconjugate(C23) + Vv46*Vv64*ZH13*complexconjugate(C31) + Vv46*Vv65*ZH13*complexconjugate(C32) + 2*Vv41*Vv64*ZH11*complexconjugate(Y1n11) + 2*Vv41*Vv65*ZH11*complexconjugate(Y1n12) + 2*Vv42*Vv64*ZH11*complexconjugate(Y1n21) + Vv44*(ZH13*(-2*Vv64*complexconjugate(BB11) + Vv65*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv66*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv61*ZH11*complexconjugate(Y1n11) + 2*Vv62*ZH11*complexconjugate(Y1n21)) + 2*Vv42*Vv65*ZH11*complexconjugate(Y1n22) + Vv45*(ZH13*(Vv64*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv65*complexconjugate(BB22) + Vv66*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv61*ZH11*complexconjugate(Y1n12) + 2*Vv62*ZH11*complexconjugate(Y1n22)) + 2*Vv46*Vv63*ZH12*complexconjugate(Y2n33) + 2*Vv43*Vv66*ZH12*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_953 = Coupling(name = 'GC_953',
	 value = '(1./2.*complex(0,1)*(2*Y1n21*ZH11*complexconjugate(Vv44)*complexconjugate(Vv62) + 2*Y1n22*ZH11*complexconjugate(Vv45)*complexconjugate(Vv62) + 2*Y2n33*ZH12*complexconjugate(Vv46)*complexconjugate(Vv63) + 2*Y1n21*ZH11*complexconjugate(Vv42)*complexconjugate(Vv64) - 2*BB11*ZH13*complexconjugate(Vv44)*complexconjugate(Vv64) + BB12*ZH13*complexconjugate(Vv45)*complexconjugate(Vv64) + BB21*ZH13*complexconjugate(Vv45)*complexconjugate(Vv64) + C13*ZH13*complexconjugate(Vv46)*complexconjugate(Vv64) + C31*ZH13*complexconjugate(Vv46)*complexconjugate(Vv64) + 2*Y1n11*ZH11*(complexconjugate(Vv44)*complexconjugate(Vv61) + complexconjugate(Vv41)*complexconjugate(Vv64)) + 2*Y1n22*ZH11*complexconjugate(Vv42)*complexconjugate(Vv65) + BB12*ZH13*complexconjugate(Vv44)*complexconjugate(Vv65) + BB21*ZH13*complexconjugate(Vv44)*complexconjugate(Vv65) + 2*BB22*ZH13*complexconjugate(Vv45)*complexconjugate(Vv65) + C23*ZH13*complexconjugate(Vv46)*complexconjugate(Vv65) + C32*ZH13*complexconjugate(Vv46)*complexconjugate(Vv65) + 2*Y1n12*ZH11*(complexconjugate(Vv45)*complexconjugate(Vv61) + complexconjugate(Vv41)*complexconjugate(Vv65)) + 2*Y2n33*ZH12*complexconjugate(Vv43)*complexconjugate(Vv66) + C13*ZH13*complexconjugate(Vv44)*complexconjugate(Vv66) + C31*ZH13*complexconjugate(Vv44)*complexconjugate(Vv66) + C23*ZH13*complexconjugate(Vv45)*complexconjugate(Vv66) + C32*ZH13*complexconjugate(Vv45)*complexconjugate(Vv66)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_954 = Coupling(name = 'GC_954',
	 value = '(1./2.*complex(0,1)*(Vv46*Vv64*ZH23*complexconjugate(C13) + Vv46*Vv65*ZH23*complexconjugate(C23) + Vv46*Vv64*ZH23*complexconjugate(C31) + Vv46*Vv65*ZH23*complexconjugate(C32) + 2*Vv41*Vv64*ZH21*complexconjugate(Y1n11) + 2*Vv41*Vv65*ZH21*complexconjugate(Y1n12) + 2*Vv42*Vv64*ZH21*complexconjugate(Y1n21) + Vv44*(ZH23*(-2*Vv64*complexconjugate(BB11) + Vv65*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv66*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv61*ZH21*complexconjugate(Y1n11) + 2*Vv62*ZH21*complexconjugate(Y1n21)) + 2*Vv42*Vv65*ZH21*complexconjugate(Y1n22) + Vv45*(ZH23*(Vv64*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv65*complexconjugate(BB22) + Vv66*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv61*ZH21*complexconjugate(Y1n12) + 2*Vv62*ZH21*complexconjugate(Y1n22)) + 2*Vv46*Vv63*ZH22*complexconjugate(Y2n33) + 2*Vv43*Vv66*ZH22*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_955 = Coupling(name = 'GC_955',
	 value = '(1./2.*complex(0,1)*(2*Y1n21*ZH21*complexconjugate(Vv44)*complexconjugate(Vv62) + 2*Y1n22*ZH21*complexconjugate(Vv45)*complexconjugate(Vv62) + 2*Y2n33*ZH22*complexconjugate(Vv46)*complexconjugate(Vv63) + 2*Y1n21*ZH21*complexconjugate(Vv42)*complexconjugate(Vv64) - 2*BB11*ZH23*complexconjugate(Vv44)*complexconjugate(Vv64) + BB12*ZH23*complexconjugate(Vv45)*complexconjugate(Vv64) + BB21*ZH23*complexconjugate(Vv45)*complexconjugate(Vv64) + C13*ZH23*complexconjugate(Vv46)*complexconjugate(Vv64) + C31*ZH23*complexconjugate(Vv46)*complexconjugate(Vv64) + 2*Y1n11*ZH21*(complexconjugate(Vv44)*complexconjugate(Vv61) + complexconjugate(Vv41)*complexconjugate(Vv64)) + 2*Y1n22*ZH21*complexconjugate(Vv42)*complexconjugate(Vv65) + BB12*ZH23*complexconjugate(Vv44)*complexconjugate(Vv65) + BB21*ZH23*complexconjugate(Vv44)*complexconjugate(Vv65) + 2*BB22*ZH23*complexconjugate(Vv45)*complexconjugate(Vv65) + C23*ZH23*complexconjugate(Vv46)*complexconjugate(Vv65) + C32*ZH23*complexconjugate(Vv46)*complexconjugate(Vv65) + 2*Y1n12*ZH21*(complexconjugate(Vv45)*complexconjugate(Vv61) + complexconjugate(Vv41)*complexconjugate(Vv65)) + 2*Y2n33*ZH22*complexconjugate(Vv43)*complexconjugate(Vv66) + C13*ZH23*complexconjugate(Vv44)*complexconjugate(Vv66) + C31*ZH23*complexconjugate(Vv44)*complexconjugate(Vv66) + C23*ZH23*complexconjugate(Vv45)*complexconjugate(Vv66) + C32*ZH23*complexconjugate(Vv45)*complexconjugate(Vv66)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_956 = Coupling(name = 'GC_956',
	 value = '(1./2.*complex(0,1)*(Vv46*Vv64*ZH33*complexconjugate(C13) + Vv46*Vv65*ZH33*complexconjugate(C23) + Vv46*Vv64*ZH33*complexconjugate(C31) + Vv46*Vv65*ZH33*complexconjugate(C32) + 2*Vv41*Vv64*ZH31*complexconjugate(Y1n11) + 2*Vv41*Vv65*ZH31*complexconjugate(Y1n12) + 2*Vv42*Vv64*ZH31*complexconjugate(Y1n21) + Vv44*(ZH33*(-2*Vv64*complexconjugate(BB11) + Vv65*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv66*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv61*ZH31*complexconjugate(Y1n11) + 2*Vv62*ZH31*complexconjugate(Y1n21)) + 2*Vv42*Vv65*ZH31*complexconjugate(Y1n22) + Vv45*(ZH33*(Vv64*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv65*complexconjugate(BB22) + Vv66*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv61*ZH31*complexconjugate(Y1n12) + 2*Vv62*ZH31*complexconjugate(Y1n22)) + 2*Vv46*Vv63*ZH32*complexconjugate(Y2n33) + 2*Vv43*Vv66*ZH32*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_957 = Coupling(name = 'GC_957',
	 value = '(1./2.*complex(0,1)*(2*Y1n21*ZH31*complexconjugate(Vv44)*complexconjugate(Vv62) + 2*Y1n22*ZH31*complexconjugate(Vv45)*complexconjugate(Vv62) + 2*Y2n33*ZH32*complexconjugate(Vv46)*complexconjugate(Vv63) + 2*Y1n21*ZH31*complexconjugate(Vv42)*complexconjugate(Vv64) - 2*BB11*ZH33*complexconjugate(Vv44)*complexconjugate(Vv64) + BB12*ZH33*complexconjugate(Vv45)*complexconjugate(Vv64) + BB21*ZH33*complexconjugate(Vv45)*complexconjugate(Vv64) + C13*ZH33*complexconjugate(Vv46)*complexconjugate(Vv64) + C31*ZH33*complexconjugate(Vv46)*complexconjugate(Vv64) + 2*Y1n11*ZH31*(complexconjugate(Vv44)*complexconjugate(Vv61) + complexconjugate(Vv41)*complexconjugate(Vv64)) + 2*Y1n22*ZH31*complexconjugate(Vv42)*complexconjugate(Vv65) + BB12*ZH33*complexconjugate(Vv44)*complexconjugate(Vv65) + BB21*ZH33*complexconjugate(Vv44)*complexconjugate(Vv65) + 2*BB22*ZH33*complexconjugate(Vv45)*complexconjugate(Vv65) + C23*ZH33*complexconjugate(Vv46)*complexconjugate(Vv65) + C32*ZH33*complexconjugate(Vv46)*complexconjugate(Vv65) + 2*Y1n12*ZH31*(complexconjugate(Vv45)*complexconjugate(Vv61) + complexconjugate(Vv41)*complexconjugate(Vv65)) + 2*Y2n33*ZH32*complexconjugate(Vv43)*complexconjugate(Vv66) + C13*ZH33*complexconjugate(Vv44)*complexconjugate(Vv66) + C31*ZH33*complexconjugate(Vv44)*complexconjugate(Vv66) + C23*ZH33*complexconjugate(Vv45)*complexconjugate(Vv66) + C32*ZH33*complexconjugate(Vv45)*complexconjugate(Vv66)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_958 = Coupling(name = 'GC_958',
	 value = '(1./2.*complex(0,1)*(Vv54*Vv56*ZH13*complexconjugate(C13) + Vv55*Vv56*ZH13*complexconjugate(C23) + Vv54*Vv56*ZH13*complexconjugate(C31) + Vv55*Vv56*ZH13*complexconjugate(C32) + 2*Vv51*Vv54*ZH11*complexconjugate(Y1n11) + 2*Vv51*Vv55*ZH11*complexconjugate(Y1n12) + 2*Vv52*Vv54*ZH11*complexconjugate(Y1n21) + Vv54*(ZH13*(-2*Vv54*complexconjugate(BB11) + Vv55*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv56*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv51*ZH11*complexconjugate(Y1n11) + 2*Vv52*ZH11*complexconjugate(Y1n21)) + 2*Vv52*Vv55*ZH11*complexconjugate(Y1n22) + Vv55*(ZH13*(Vv54*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv55*complexconjugate(BB22) + Vv56*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv51*ZH11*complexconjugate(Y1n12) + 2*Vv52*ZH11*complexconjugate(Y1n22)) + 4*Vv53*Vv56*ZH12*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_959 = Coupling(name = 'GC_959',
	 value = '(1./2.*complex(0,1)*(4*Y1n11*ZH11*complexconjugate(Vv51)*complexconjugate(Vv54) + 4*Y1n21*ZH11*complexconjugate(Vv52)*complexconjugate(Vv54) - 2*BB11*ZH13*complexconjugate(Vv54)**2 + 4*Y1n12*ZH11*complexconjugate(Vv51)*complexconjugate(Vv55) + 4*Y1n22*ZH11*complexconjugate(Vv52)*complexconjugate(Vv55) + 2*BB12*ZH13*complexconjugate(Vv54)*complexconjugate(Vv55) + 2*BB21*ZH13*complexconjugate(Vv54)*complexconjugate(Vv55) + 2*BB22*ZH13*complexconjugate(Vv55)**2 + 4*Y2n33*ZH12*complexconjugate(Vv53)*complexconjugate(Vv56) + 2*C13*ZH13*complexconjugate(Vv54)*complexconjugate(Vv56) + 2*C31*ZH13*complexconjugate(Vv54)*complexconjugate(Vv56) + 2*C23*ZH13*complexconjugate(Vv55)*complexconjugate(Vv56) + 2*C32*ZH13*complexconjugate(Vv55)*complexconjugate(Vv56)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_960 = Coupling(name = 'GC_960',
	 value = '(1./2.*complex(0,1)*(Vv54*Vv56*ZH23*complexconjugate(C13) + Vv55*Vv56*ZH23*complexconjugate(C23) + Vv54*Vv56*ZH23*complexconjugate(C31) + Vv55*Vv56*ZH23*complexconjugate(C32) + 2*Vv51*Vv54*ZH21*complexconjugate(Y1n11) + 2*Vv51*Vv55*ZH21*complexconjugate(Y1n12) + 2*Vv52*Vv54*ZH21*complexconjugate(Y1n21) + Vv54*(ZH23*(-2*Vv54*complexconjugate(BB11) + Vv55*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv56*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv51*ZH21*complexconjugate(Y1n11) + 2*Vv52*ZH21*complexconjugate(Y1n21)) + 2*Vv52*Vv55*ZH21*complexconjugate(Y1n22) + Vv55*(ZH23*(Vv54*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv55*complexconjugate(BB22) + Vv56*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv51*ZH21*complexconjugate(Y1n12) + 2*Vv52*ZH21*complexconjugate(Y1n22)) + 4*Vv53*Vv56*ZH22*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_961 = Coupling(name = 'GC_961',
	 value = '(1./2.*complex(0,1)*(4*Y1n11*ZH21*complexconjugate(Vv51)*complexconjugate(Vv54) + 4*Y1n21*ZH21*complexconjugate(Vv52)*complexconjugate(Vv54) - 2*BB11*ZH23*complexconjugate(Vv54)**2 + 4*Y1n12*ZH21*complexconjugate(Vv51)*complexconjugate(Vv55) + 4*Y1n22*ZH21*complexconjugate(Vv52)*complexconjugate(Vv55) + 2*BB12*ZH23*complexconjugate(Vv54)*complexconjugate(Vv55) + 2*BB21*ZH23*complexconjugate(Vv54)*complexconjugate(Vv55) + 2*BB22*ZH23*complexconjugate(Vv55)**2 + 4*Y2n33*ZH22*complexconjugate(Vv53)*complexconjugate(Vv56) + 2*C13*ZH23*complexconjugate(Vv54)*complexconjugate(Vv56) + 2*C31*ZH23*complexconjugate(Vv54)*complexconjugate(Vv56) + 2*C23*ZH23*complexconjugate(Vv55)*complexconjugate(Vv56) + 2*C32*ZH23*complexconjugate(Vv55)*complexconjugate(Vv56)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_962 = Coupling(name = 'GC_962',
	 value = '(1./2.*complex(0,1)*(Vv54*Vv56*ZH33*complexconjugate(C13) + Vv55*Vv56*ZH33*complexconjugate(C23) + Vv54*Vv56*ZH33*complexconjugate(C31) + Vv55*Vv56*ZH33*complexconjugate(C32) + 2*Vv51*Vv54*ZH31*complexconjugate(Y1n11) + 2*Vv51*Vv55*ZH31*complexconjugate(Y1n12) + 2*Vv52*Vv54*ZH31*complexconjugate(Y1n21) + Vv54*(ZH33*(-2*Vv54*complexconjugate(BB11) + Vv55*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv56*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv51*ZH31*complexconjugate(Y1n11) + 2*Vv52*ZH31*complexconjugate(Y1n21)) + 2*Vv52*Vv55*ZH31*complexconjugate(Y1n22) + Vv55*(ZH33*(Vv54*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv55*complexconjugate(BB22) + Vv56*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv51*ZH31*complexconjugate(Y1n12) + 2*Vv52*ZH31*complexconjugate(Y1n22)) + 4*Vv53*Vv56*ZH32*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_963 = Coupling(name = 'GC_963',
	 value = '(1./2.*complex(0,1)*(4*Y1n11*ZH31*complexconjugate(Vv51)*complexconjugate(Vv54) + 4*Y1n21*ZH31*complexconjugate(Vv52)*complexconjugate(Vv54) - 2*BB11*ZH33*complexconjugate(Vv54)**2 + 4*Y1n12*ZH31*complexconjugate(Vv51)*complexconjugate(Vv55) + 4*Y1n22*ZH31*complexconjugate(Vv52)*complexconjugate(Vv55) + 2*BB12*ZH33*complexconjugate(Vv54)*complexconjugate(Vv55) + 2*BB21*ZH33*complexconjugate(Vv54)*complexconjugate(Vv55) + 2*BB22*ZH33*complexconjugate(Vv55)**2 + 4*Y2n33*ZH32*complexconjugate(Vv53)*complexconjugate(Vv56) + 2*C13*ZH33*complexconjugate(Vv54)*complexconjugate(Vv56) + 2*C31*ZH33*complexconjugate(Vv54)*complexconjugate(Vv56) + 2*C23*ZH33*complexconjugate(Vv55)*complexconjugate(Vv56) + 2*C32*ZH33*complexconjugate(Vv55)*complexconjugate(Vv56)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_964 = Coupling(name = 'GC_964',
	 value = '(1./2.*complex(0,1)*(Vv56*Vv64*ZH13*complexconjugate(C13) + Vv56*Vv65*ZH13*complexconjugate(C23) + Vv56*Vv64*ZH13*complexconjugate(C31) + Vv56*Vv65*ZH13*complexconjugate(C32) + 2*Vv51*Vv64*ZH11*complexconjugate(Y1n11) + 2*Vv51*Vv65*ZH11*complexconjugate(Y1n12) + 2*Vv52*Vv64*ZH11*complexconjugate(Y1n21) + Vv54*(ZH13*(-2*Vv64*complexconjugate(BB11) + Vv65*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv66*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv61*ZH11*complexconjugate(Y1n11) + 2*Vv62*ZH11*complexconjugate(Y1n21)) + 2*Vv52*Vv65*ZH11*complexconjugate(Y1n22) + Vv55*(ZH13*(Vv64*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv65*complexconjugate(BB22) + Vv66*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv61*ZH11*complexconjugate(Y1n12) + 2*Vv62*ZH11*complexconjugate(Y1n22)) + 2*Vv56*Vv63*ZH12*complexconjugate(Y2n33) + 2*Vv53*Vv66*ZH12*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_965 = Coupling(name = 'GC_965',
	 value = '(1./2.*complex(0,1)*(2*Y1n21*ZH11*complexconjugate(Vv54)*complexconjugate(Vv62) + 2*Y1n22*ZH11*complexconjugate(Vv55)*complexconjugate(Vv62) + 2*Y2n33*ZH12*complexconjugate(Vv56)*complexconjugate(Vv63) + 2*Y1n21*ZH11*complexconjugate(Vv52)*complexconjugate(Vv64) - 2*BB11*ZH13*complexconjugate(Vv54)*complexconjugate(Vv64) + BB12*ZH13*complexconjugate(Vv55)*complexconjugate(Vv64) + BB21*ZH13*complexconjugate(Vv55)*complexconjugate(Vv64) + C13*ZH13*complexconjugate(Vv56)*complexconjugate(Vv64) + C31*ZH13*complexconjugate(Vv56)*complexconjugate(Vv64) + 2*Y1n11*ZH11*(complexconjugate(Vv54)*complexconjugate(Vv61) + complexconjugate(Vv51)*complexconjugate(Vv64)) + 2*Y1n22*ZH11*complexconjugate(Vv52)*complexconjugate(Vv65) + BB12*ZH13*complexconjugate(Vv54)*complexconjugate(Vv65) + BB21*ZH13*complexconjugate(Vv54)*complexconjugate(Vv65) + 2*BB22*ZH13*complexconjugate(Vv55)*complexconjugate(Vv65) + C23*ZH13*complexconjugate(Vv56)*complexconjugate(Vv65) + C32*ZH13*complexconjugate(Vv56)*complexconjugate(Vv65) + 2*Y1n12*ZH11*(complexconjugate(Vv55)*complexconjugate(Vv61) + complexconjugate(Vv51)*complexconjugate(Vv65)) + 2*Y2n33*ZH12*complexconjugate(Vv53)*complexconjugate(Vv66) + C13*ZH13*complexconjugate(Vv54)*complexconjugate(Vv66) + C31*ZH13*complexconjugate(Vv54)*complexconjugate(Vv66) + C23*ZH13*complexconjugate(Vv55)*complexconjugate(Vv66) + C32*ZH13*complexconjugate(Vv55)*complexconjugate(Vv66)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_966 = Coupling(name = 'GC_966',
	 value = '(1./2.*complex(0,1)*(Vv56*Vv64*ZH23*complexconjugate(C13) + Vv56*Vv65*ZH23*complexconjugate(C23) + Vv56*Vv64*ZH23*complexconjugate(C31) + Vv56*Vv65*ZH23*complexconjugate(C32) + 2*Vv51*Vv64*ZH21*complexconjugate(Y1n11) + 2*Vv51*Vv65*ZH21*complexconjugate(Y1n12) + 2*Vv52*Vv64*ZH21*complexconjugate(Y1n21) + Vv54*(ZH23*(-2*Vv64*complexconjugate(BB11) + Vv65*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv66*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv61*ZH21*complexconjugate(Y1n11) + 2*Vv62*ZH21*complexconjugate(Y1n21)) + 2*Vv52*Vv65*ZH21*complexconjugate(Y1n22) + Vv55*(ZH23*(Vv64*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv65*complexconjugate(BB22) + Vv66*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv61*ZH21*complexconjugate(Y1n12) + 2*Vv62*ZH21*complexconjugate(Y1n22)) + 2*Vv56*Vv63*ZH22*complexconjugate(Y2n33) + 2*Vv53*Vv66*ZH22*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_967 = Coupling(name = 'GC_967',
	 value = '(1./2.*complex(0,1)*(2*Y1n21*ZH21*complexconjugate(Vv54)*complexconjugate(Vv62) + 2*Y1n22*ZH21*complexconjugate(Vv55)*complexconjugate(Vv62) + 2*Y2n33*ZH22*complexconjugate(Vv56)*complexconjugate(Vv63) + 2*Y1n21*ZH21*complexconjugate(Vv52)*complexconjugate(Vv64) - 2*BB11*ZH23*complexconjugate(Vv54)*complexconjugate(Vv64) + BB12*ZH23*complexconjugate(Vv55)*complexconjugate(Vv64) + BB21*ZH23*complexconjugate(Vv55)*complexconjugate(Vv64) + C13*ZH23*complexconjugate(Vv56)*complexconjugate(Vv64) + C31*ZH23*complexconjugate(Vv56)*complexconjugate(Vv64) + 2*Y1n11*ZH21*(complexconjugate(Vv54)*complexconjugate(Vv61) + complexconjugate(Vv51)*complexconjugate(Vv64)) + 2*Y1n22*ZH21*complexconjugate(Vv52)*complexconjugate(Vv65) + BB12*ZH23*complexconjugate(Vv54)*complexconjugate(Vv65) + BB21*ZH23*complexconjugate(Vv54)*complexconjugate(Vv65) + 2*BB22*ZH23*complexconjugate(Vv55)*complexconjugate(Vv65) + C23*ZH23*complexconjugate(Vv56)*complexconjugate(Vv65) + C32*ZH23*complexconjugate(Vv56)*complexconjugate(Vv65) + 2*Y1n12*ZH21*(complexconjugate(Vv55)*complexconjugate(Vv61) + complexconjugate(Vv51)*complexconjugate(Vv65)) + 2*Y2n33*ZH22*complexconjugate(Vv53)*complexconjugate(Vv66) + C13*ZH23*complexconjugate(Vv54)*complexconjugate(Vv66) + C31*ZH23*complexconjugate(Vv54)*complexconjugate(Vv66) + C23*ZH23*complexconjugate(Vv55)*complexconjugate(Vv66) + C32*ZH23*complexconjugate(Vv55)*complexconjugate(Vv66)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_968 = Coupling(name = 'GC_968',
	 value = '(1./2.*complex(0,1)*(Vv56*Vv64*ZH33*complexconjugate(C13) + Vv56*Vv65*ZH33*complexconjugate(C23) + Vv56*Vv64*ZH33*complexconjugate(C31) + Vv56*Vv65*ZH33*complexconjugate(C32) + 2*Vv51*Vv64*ZH31*complexconjugate(Y1n11) + 2*Vv51*Vv65*ZH31*complexconjugate(Y1n12) + 2*Vv52*Vv64*ZH31*complexconjugate(Y1n21) + Vv54*(ZH33*(-2*Vv64*complexconjugate(BB11) + Vv65*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv66*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv61*ZH31*complexconjugate(Y1n11) + 2*Vv62*ZH31*complexconjugate(Y1n21)) + 2*Vv52*Vv65*ZH31*complexconjugate(Y1n22) + Vv55*(ZH33*(Vv64*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv65*complexconjugate(BB22) + Vv66*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv61*ZH31*complexconjugate(Y1n12) + 2*Vv62*ZH31*complexconjugate(Y1n22)) + 2*Vv56*Vv63*ZH32*complexconjugate(Y2n33) + 2*Vv53*Vv66*ZH32*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_969 = Coupling(name = 'GC_969',
	 value = '(1./2.*complex(0,1)*(2*Y1n21*ZH31*complexconjugate(Vv54)*complexconjugate(Vv62) + 2*Y1n22*ZH31*complexconjugate(Vv55)*complexconjugate(Vv62) + 2*Y2n33*ZH32*complexconjugate(Vv56)*complexconjugate(Vv63) + 2*Y1n21*ZH31*complexconjugate(Vv52)*complexconjugate(Vv64) - 2*BB11*ZH33*complexconjugate(Vv54)*complexconjugate(Vv64) + BB12*ZH33*complexconjugate(Vv55)*complexconjugate(Vv64) + BB21*ZH33*complexconjugate(Vv55)*complexconjugate(Vv64) + C13*ZH33*complexconjugate(Vv56)*complexconjugate(Vv64) + C31*ZH33*complexconjugate(Vv56)*complexconjugate(Vv64) + 2*Y1n11*ZH31*(complexconjugate(Vv54)*complexconjugate(Vv61) + complexconjugate(Vv51)*complexconjugate(Vv64)) + 2*Y1n22*ZH31*complexconjugate(Vv52)*complexconjugate(Vv65) + BB12*ZH33*complexconjugate(Vv54)*complexconjugate(Vv65) + BB21*ZH33*complexconjugate(Vv54)*complexconjugate(Vv65) + 2*BB22*ZH33*complexconjugate(Vv55)*complexconjugate(Vv65) + C23*ZH33*complexconjugate(Vv56)*complexconjugate(Vv65) + C32*ZH33*complexconjugate(Vv56)*complexconjugate(Vv65) + 2*Y1n12*ZH31*(complexconjugate(Vv55)*complexconjugate(Vv61) + complexconjugate(Vv51)*complexconjugate(Vv65)) + 2*Y2n33*ZH32*complexconjugate(Vv53)*complexconjugate(Vv66) + C13*ZH33*complexconjugate(Vv54)*complexconjugate(Vv66) + C31*ZH33*complexconjugate(Vv54)*complexconjugate(Vv66) + C23*ZH33*complexconjugate(Vv55)*complexconjugate(Vv66) + C32*ZH33*complexconjugate(Vv55)*complexconjugate(Vv66)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_970 = Coupling(name = 'GC_970',
	 value = '(1./2.*complex(0,1)*(Vv64*Vv66*ZH13*complexconjugate(C13) + Vv65*Vv66*ZH13*complexconjugate(C23) + Vv64*Vv66*ZH13*complexconjugate(C31) + Vv65*Vv66*ZH13*complexconjugate(C32) + 2*Vv61*Vv64*ZH11*complexconjugate(Y1n11) + 2*Vv61*Vv65*ZH11*complexconjugate(Y1n12) + 2*Vv62*Vv64*ZH11*complexconjugate(Y1n21) + Vv64*(ZH13*(-2*Vv64*complexconjugate(BB11) + Vv65*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv66*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv61*ZH11*complexconjugate(Y1n11) + 2*Vv62*ZH11*complexconjugate(Y1n21)) + 2*Vv62*Vv65*ZH11*complexconjugate(Y1n22) + Vv65*(ZH13*(Vv64*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv65*complexconjugate(BB22) + Vv66*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv61*ZH11*complexconjugate(Y1n12) + 2*Vv62*ZH11*complexconjugate(Y1n22)) + 4*Vv63*Vv66*ZH12*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_971 = Coupling(name = 'GC_971',
	 value = '(1./2.*complex(0,1)*(4*Y1n11*ZH11*complexconjugate(Vv61)*complexconjugate(Vv64) + 4*Y1n21*ZH11*complexconjugate(Vv62)*complexconjugate(Vv64) - 2*BB11*ZH13*complexconjugate(Vv64)**2 + 4*Y1n12*ZH11*complexconjugate(Vv61)*complexconjugate(Vv65) + 4*Y1n22*ZH11*complexconjugate(Vv62)*complexconjugate(Vv65) + 2*BB12*ZH13*complexconjugate(Vv64)*complexconjugate(Vv65) + 2*BB21*ZH13*complexconjugate(Vv64)*complexconjugate(Vv65) + 2*BB22*ZH13*complexconjugate(Vv65)**2 + 4*Y2n33*ZH12*complexconjugate(Vv63)*complexconjugate(Vv66) + 2*C13*ZH13*complexconjugate(Vv64)*complexconjugate(Vv66) + 2*C31*ZH13*complexconjugate(Vv64)*complexconjugate(Vv66) + 2*C23*ZH13*complexconjugate(Vv65)*complexconjugate(Vv66) + 2*C32*ZH13*complexconjugate(Vv65)*complexconjugate(Vv66)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_972 = Coupling(name = 'GC_972',
	 value = '(1./2.*complex(0,1)*(Vv64*Vv66*ZH23*complexconjugate(C13) + Vv65*Vv66*ZH23*complexconjugate(C23) + Vv64*Vv66*ZH23*complexconjugate(C31) + Vv65*Vv66*ZH23*complexconjugate(C32) + 2*Vv61*Vv64*ZH21*complexconjugate(Y1n11) + 2*Vv61*Vv65*ZH21*complexconjugate(Y1n12) + 2*Vv62*Vv64*ZH21*complexconjugate(Y1n21) + Vv64*(ZH23*(-2*Vv64*complexconjugate(BB11) + Vv65*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv66*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv61*ZH21*complexconjugate(Y1n11) + 2*Vv62*ZH21*complexconjugate(Y1n21)) + 2*Vv62*Vv65*ZH21*complexconjugate(Y1n22) + Vv65*(ZH23*(Vv64*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv65*complexconjugate(BB22) + Vv66*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv61*ZH21*complexconjugate(Y1n12) + 2*Vv62*ZH21*complexconjugate(Y1n22)) + 4*Vv63*Vv66*ZH22*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_973 = Coupling(name = 'GC_973',
	 value = '(1./2.*complex(0,1)*(4*Y1n11*ZH21*complexconjugate(Vv61)*complexconjugate(Vv64) + 4*Y1n21*ZH21*complexconjugate(Vv62)*complexconjugate(Vv64) - 2*BB11*ZH23*complexconjugate(Vv64)**2 + 4*Y1n12*ZH21*complexconjugate(Vv61)*complexconjugate(Vv65) + 4*Y1n22*ZH21*complexconjugate(Vv62)*complexconjugate(Vv65) + 2*BB12*ZH23*complexconjugate(Vv64)*complexconjugate(Vv65) + 2*BB21*ZH23*complexconjugate(Vv64)*complexconjugate(Vv65) + 2*BB22*ZH23*complexconjugate(Vv65)**2 + 4*Y2n33*ZH22*complexconjugate(Vv63)*complexconjugate(Vv66) + 2*C13*ZH23*complexconjugate(Vv64)*complexconjugate(Vv66) + 2*C31*ZH23*complexconjugate(Vv64)*complexconjugate(Vv66) + 2*C23*ZH23*complexconjugate(Vv65)*complexconjugate(Vv66) + 2*C32*ZH23*complexconjugate(Vv65)*complexconjugate(Vv66)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_974 = Coupling(name = 'GC_974',
	 value = '(1./2.*complex(0,1)*(Vv64*Vv66*ZH33*complexconjugate(C13) + Vv65*Vv66*ZH33*complexconjugate(C23) + Vv64*Vv66*ZH33*complexconjugate(C31) + Vv65*Vv66*ZH33*complexconjugate(C32) + 2*Vv61*Vv64*ZH31*complexconjugate(Y1n11) + 2*Vv61*Vv65*ZH31*complexconjugate(Y1n12) + 2*Vv62*Vv64*ZH31*complexconjugate(Y1n21) + Vv64*(ZH33*(-2*Vv64*complexconjugate(BB11) + Vv65*(complexconjugate(BB12) + complexconjugate(BB21)) + Vv66*(complexconjugate(C13) + complexconjugate(C31))) + 2*Vv61*ZH31*complexconjugate(Y1n11) + 2*Vv62*ZH31*complexconjugate(Y1n21)) + 2*Vv62*Vv65*ZH31*complexconjugate(Y1n22) + Vv65*(ZH33*(Vv64*(complexconjugate(BB12) + complexconjugate(BB21)) + 2*Vv65*complexconjugate(BB22) + Vv66*(complexconjugate(C23) + complexconjugate(C32))) + 2*Vv61*ZH31*complexconjugate(Y1n12) + 2*Vv62*ZH31*complexconjugate(Y1n22)) + 4*Vv63*Vv66*ZH32*complexconjugate(Y2n33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_975 = Coupling(name = 'GC_975',
	 value = '(1./2.*complex(0,1)*(4*Y1n11*ZH31*complexconjugate(Vv61)*complexconjugate(Vv64) + 4*Y1n21*ZH31*complexconjugate(Vv62)*complexconjugate(Vv64) - 2*BB11*ZH33*complexconjugate(Vv64)**2 + 4*Y1n12*ZH31*complexconjugate(Vv61)*complexconjugate(Vv65) + 4*Y1n22*ZH31*complexconjugate(Vv62)*complexconjugate(Vv65) + 2*BB12*ZH33*complexconjugate(Vv64)*complexconjugate(Vv65) + 2*BB21*ZH33*complexconjugate(Vv64)*complexconjugate(Vv65) + 2*BB22*ZH33*complexconjugate(Vv65)**2 + 4*Y2n33*ZH32*complexconjugate(Vv63)*complexconjugate(Vv66) + 2*C13*ZH33*complexconjugate(Vv64)*complexconjugate(Vv66) + 2*C31*ZH33*complexconjugate(Vv64)*complexconjugate(Vv66) + 2*C23*ZH33*complexconjugate(Vv65)*complexconjugate(Vv66) + 2*C32*ZH33*complexconjugate(Vv65)*complexconjugate(Vv66)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_976 = Coupling(name = 'GC_976',
	 value = '1*complex(0,1)*(-(ZER11*ZP11*(Vv11*complexconjugate(Y1e11) + Vv12*complexconjugate(Y1e21))) - ZER12*ZP11*(Vv11*complexconjugate(Y1e12) + Vv12*complexconjugate(Y1e22)) - Vv13*ZER13*ZP12*complexconjugate(Y2e33))', 
	 order = {'QED':1} ) 
 
GC_977 = Coupling(name = 'GC_977',
	 value = '1*complex(0,1)*(-(Y1n11*ZP11*complexconjugate(Vv14)*complexconjugate(ZEL11)) - Y1n12*ZP11*complexconjugate(Vv15)*complexconjugate(ZEL11) - Y1n21*ZP11*complexconjugate(Vv14)*complexconjugate(ZEL12) - Y1n22*ZP11*complexconjugate(Vv15)*complexconjugate(ZEL12) - Y2n33*ZP12*complexconjugate(Vv16)*complexconjugate(ZEL13))', 
	 order = {'QED':1} ) 
 
GC_978 = Coupling(name = 'GC_978',
	 value = '1*complex(0,1)*(-(ZER11*ZP21*(Vv11*complexconjugate(Y1e11) + Vv12*complexconjugate(Y1e21))) - ZER12*ZP21*(Vv11*complexconjugate(Y1e12) + Vv12*complexconjugate(Y1e22)) - Vv13*ZER13*ZP22*complexconjugate(Y2e33))', 
	 order = {'QED':1} ) 
 
GC_979 = Coupling(name = 'GC_979',
	 value = '1*complex(0,1)*(-(Y1n11*ZP21*complexconjugate(Vv14)*complexconjugate(ZEL11)) - Y1n12*ZP21*complexconjugate(Vv15)*complexconjugate(ZEL11) - Y1n21*ZP21*complexconjugate(Vv14)*complexconjugate(ZEL12) - Y1n22*ZP21*complexconjugate(Vv15)*complexconjugate(ZEL12) - Y2n33*ZP22*complexconjugate(Vv16)*complexconjugate(ZEL13))', 
	 order = {'QED':1} ) 
 
GC_980 = Coupling(name = 'GC_980',
	 value = '1*complex(0,1)*(-(ZER11*ZP11*(Vv21*complexconjugate(Y1e11) + Vv22*complexconjugate(Y1e21))) - ZER12*ZP11*(Vv21*complexconjugate(Y1e12) + Vv22*complexconjugate(Y1e22)) - Vv23*ZER13*ZP12*complexconjugate(Y2e33))', 
	 order = {'QED':1} ) 
 
GC_981 = Coupling(name = 'GC_981',
	 value = '1*complex(0,1)*(-(Y1n11*ZP11*complexconjugate(Vv24)*complexconjugate(ZEL11)) - Y1n12*ZP11*complexconjugate(Vv25)*complexconjugate(ZEL11) - Y1n21*ZP11*complexconjugate(Vv24)*complexconjugate(ZEL12) - Y1n22*ZP11*complexconjugate(Vv25)*complexconjugate(ZEL12) - Y2n33*ZP12*complexconjugate(Vv26)*complexconjugate(ZEL13))', 
	 order = {'QED':1} ) 
 
GC_982 = Coupling(name = 'GC_982',
	 value = '1*complex(0,1)*(-(ZER11*ZP21*(Vv21*complexconjugate(Y1e11) + Vv22*complexconjugate(Y1e21))) - ZER12*ZP21*(Vv21*complexconjugate(Y1e12) + Vv22*complexconjugate(Y1e22)) - Vv23*ZER13*ZP22*complexconjugate(Y2e33))', 
	 order = {'QED':1} ) 
 
GC_983 = Coupling(name = 'GC_983',
	 value = '1*complex(0,1)*(-(Y1n11*ZP21*complexconjugate(Vv24)*complexconjugate(ZEL11)) - Y1n12*ZP21*complexconjugate(Vv25)*complexconjugate(ZEL11) - Y1n21*ZP21*complexconjugate(Vv24)*complexconjugate(ZEL12) - Y1n22*ZP21*complexconjugate(Vv25)*complexconjugate(ZEL12) - Y2n33*ZP22*complexconjugate(Vv26)*complexconjugate(ZEL13))', 
	 order = {'QED':1} ) 
 
GC_984 = Coupling(name = 'GC_984',
	 value = '1*complex(0,1)*(-(ZER11*ZP11*(Vv31*complexconjugate(Y1e11) + Vv32*complexconjugate(Y1e21))) - ZER12*ZP11*(Vv31*complexconjugate(Y1e12) + Vv32*complexconjugate(Y1e22)) - Vv33*ZER13*ZP12*complexconjugate(Y2e33))', 
	 order = {'QED':1} ) 
 
GC_985 = Coupling(name = 'GC_985',
	 value = '1*complex(0,1)*(-(Y1n11*ZP11*complexconjugate(Vv34)*complexconjugate(ZEL11)) - Y1n12*ZP11*complexconjugate(Vv35)*complexconjugate(ZEL11) - Y1n21*ZP11*complexconjugate(Vv34)*complexconjugate(ZEL12) - Y1n22*ZP11*complexconjugate(Vv35)*complexconjugate(ZEL12) - Y2n33*ZP12*complexconjugate(Vv36)*complexconjugate(ZEL13))', 
	 order = {'QED':1} ) 
 
GC_986 = Coupling(name = 'GC_986',
	 value = '1*complex(0,1)*(-(ZER11*ZP21*(Vv31*complexconjugate(Y1e11) + Vv32*complexconjugate(Y1e21))) - ZER12*ZP21*(Vv31*complexconjugate(Y1e12) + Vv32*complexconjugate(Y1e22)) - Vv33*ZER13*ZP22*complexconjugate(Y2e33))', 
	 order = {'QED':1} ) 
 
GC_987 = Coupling(name = 'GC_987',
	 value = '1*complex(0,1)*(-(Y1n11*ZP21*complexconjugate(Vv34)*complexconjugate(ZEL11)) - Y1n12*ZP21*complexconjugate(Vv35)*complexconjugate(ZEL11) - Y1n21*ZP21*complexconjugate(Vv34)*complexconjugate(ZEL12) - Y1n22*ZP21*complexconjugate(Vv35)*complexconjugate(ZEL12) - Y2n33*ZP22*complexconjugate(Vv36)*complexconjugate(ZEL13))', 
	 order = {'QED':1} ) 
 
GC_988 = Coupling(name = 'GC_988',
	 value = '1*complex(0,1)*(-(ZER11*ZP11*(Vv41*complexconjugate(Y1e11) + Vv42*complexconjugate(Y1e21))) - ZER12*ZP11*(Vv41*complexconjugate(Y1e12) + Vv42*complexconjugate(Y1e22)) - Vv43*ZER13*ZP12*complexconjugate(Y2e33))', 
	 order = {'QED':1} ) 
 
GC_989 = Coupling(name = 'GC_989',
	 value = '1*complex(0,1)*(-(Y1n11*ZP11*complexconjugate(Vv44)*complexconjugate(ZEL11)) - Y1n12*ZP11*complexconjugate(Vv45)*complexconjugate(ZEL11) - Y1n21*ZP11*complexconjugate(Vv44)*complexconjugate(ZEL12) - Y1n22*ZP11*complexconjugate(Vv45)*complexconjugate(ZEL12) - Y2n33*ZP12*complexconjugate(Vv46)*complexconjugate(ZEL13))', 
	 order = {'QED':1} ) 
 
GC_990 = Coupling(name = 'GC_990',
	 value = '1*complex(0,1)*(-(ZER11*ZP21*(Vv41*complexconjugate(Y1e11) + Vv42*complexconjugate(Y1e21))) - ZER12*ZP21*(Vv41*complexconjugate(Y1e12) + Vv42*complexconjugate(Y1e22)) - Vv43*ZER13*ZP22*complexconjugate(Y2e33))', 
	 order = {'QED':1} ) 
 
GC_991 = Coupling(name = 'GC_991',
	 value = '1*complex(0,1)*(-(Y1n11*ZP21*complexconjugate(Vv44)*complexconjugate(ZEL11)) - Y1n12*ZP21*complexconjugate(Vv45)*complexconjugate(ZEL11) - Y1n21*ZP21*complexconjugate(Vv44)*complexconjugate(ZEL12) - Y1n22*ZP21*complexconjugate(Vv45)*complexconjugate(ZEL12) - Y2n33*ZP22*complexconjugate(Vv46)*complexconjugate(ZEL13))', 
	 order = {'QED':1} ) 
 
GC_992 = Coupling(name = 'GC_992',
	 value = '1*complex(0,1)*(-(ZER11*ZP11*(Vv51*complexconjugate(Y1e11) + Vv52*complexconjugate(Y1e21))) - ZER12*ZP11*(Vv51*complexconjugate(Y1e12) + Vv52*complexconjugate(Y1e22)) - Vv53*ZER13*ZP12*complexconjugate(Y2e33))', 
	 order = {'QED':1} ) 
 
GC_993 = Coupling(name = 'GC_993',
	 value = '1*complex(0,1)*(-(Y1n11*ZP11*complexconjugate(Vv54)*complexconjugate(ZEL11)) - Y1n12*ZP11*complexconjugate(Vv55)*complexconjugate(ZEL11) - Y1n21*ZP11*complexconjugate(Vv54)*complexconjugate(ZEL12) - Y1n22*ZP11*complexconjugate(Vv55)*complexconjugate(ZEL12) - Y2n33*ZP12*complexconjugate(Vv56)*complexconjugate(ZEL13))', 
	 order = {'QED':1} ) 
 
GC_994 = Coupling(name = 'GC_994',
	 value = '1*complex(0,1)*(-(ZER11*ZP21*(Vv51*complexconjugate(Y1e11) + Vv52*complexconjugate(Y1e21))) - ZER12*ZP21*(Vv51*complexconjugate(Y1e12) + Vv52*complexconjugate(Y1e22)) - Vv53*ZER13*ZP22*complexconjugate(Y2e33))', 
	 order = {'QED':1} ) 
 
GC_995 = Coupling(name = 'GC_995',
	 value = '1*complex(0,1)*(-(Y1n11*ZP21*complexconjugate(Vv54)*complexconjugate(ZEL11)) - Y1n12*ZP21*complexconjugate(Vv55)*complexconjugate(ZEL11) - Y1n21*ZP21*complexconjugate(Vv54)*complexconjugate(ZEL12) - Y1n22*ZP21*complexconjugate(Vv55)*complexconjugate(ZEL12) - Y2n33*ZP22*complexconjugate(Vv56)*complexconjugate(ZEL13))', 
	 order = {'QED':1} ) 
 
GC_996 = Coupling(name = 'GC_996',
	 value = '1*complex(0,1)*(-(ZER11*ZP11*(Vv61*complexconjugate(Y1e11) + Vv62*complexconjugate(Y1e21))) - ZER12*ZP11*(Vv61*complexconjugate(Y1e12) + Vv62*complexconjugate(Y1e22)) - Vv63*ZER13*ZP12*complexconjugate(Y2e33))', 
	 order = {'QED':1} ) 
 
GC_997 = Coupling(name = 'GC_997',
	 value = '1*complex(0,1)*(-(Y1n11*ZP11*complexconjugate(Vv64)*complexconjugate(ZEL11)) - Y1n12*ZP11*complexconjugate(Vv65)*complexconjugate(ZEL11) - Y1n21*ZP11*complexconjugate(Vv64)*complexconjugate(ZEL12) - Y1n22*ZP11*complexconjugate(Vv65)*complexconjugate(ZEL12) - Y2n33*ZP12*complexconjugate(Vv66)*complexconjugate(ZEL13))', 
	 order = {'QED':1} ) 
 
GC_998 = Coupling(name = 'GC_998',
	 value = '1*complex(0,1)*(-(ZER11*ZP21*(Vv61*complexconjugate(Y1e11) + Vv62*complexconjugate(Y1e21))) - ZER12*ZP21*(Vv61*complexconjugate(Y1e12) + Vv62*complexconjugate(Y1e22)) - Vv63*ZER13*ZP22*complexconjugate(Y2e33))', 
	 order = {'QED':1} ) 
 
GC_999 = Coupling(name = 'GC_999',
	 value = '1*complex(0,1)*(-(Y1n11*ZP21*complexconjugate(Vv64)*complexconjugate(ZEL11)) - Y1n12*ZP21*complexconjugate(Vv65)*complexconjugate(ZEL11) - Y1n21*ZP21*complexconjugate(Vv64)*complexconjugate(ZEL12) - Y1n22*ZP21*complexconjugate(Vv65)*complexconjugate(ZEL12) - Y2n33*ZP22*complexconjugate(Vv66)*complexconjugate(ZEL13))', 
	 order = {'QED':1} ) 
 
GC_1000 = Coupling(name = 'GC_1000',
	 value = '1*complex(0,1)*(-(ZER21*ZP11*(Vv11*complexconjugate(Y1e11) + Vv12*complexconjugate(Y1e21))) - ZER22*ZP11*(Vv11*complexconjugate(Y1e12) + Vv12*complexconjugate(Y1e22)) - Vv13*ZER23*ZP12*complexconjugate(Y2e33))', 
	 order = {'QED':1} ) 
 
GC_1001 = Coupling(name = 'GC_1001',
	 value = '1*complex(0,1)*(-(Y1n11*ZP11*complexconjugate(Vv14)*complexconjugate(ZEL21)) - Y1n12*ZP11*complexconjugate(Vv15)*complexconjugate(ZEL21) - Y1n21*ZP11*complexconjugate(Vv14)*complexconjugate(ZEL22) - Y1n22*ZP11*complexconjugate(Vv15)*complexconjugate(ZEL22) - Y2n33*ZP12*complexconjugate(Vv16)*complexconjugate(ZEL23))', 
	 order = {'QED':1} ) 
 
GC_1002 = Coupling(name = 'GC_1002',
	 value = '1*complex(0,1)*(-(ZER21*ZP21*(Vv11*complexconjugate(Y1e11) + Vv12*complexconjugate(Y1e21))) - ZER22*ZP21*(Vv11*complexconjugate(Y1e12) + Vv12*complexconjugate(Y1e22)) - Vv13*ZER23*ZP22*complexconjugate(Y2e33))', 
	 order = {'QED':1} ) 
 
GC_1003 = Coupling(name = 'GC_1003',
	 value = '1*complex(0,1)*(-(Y1n11*ZP21*complexconjugate(Vv14)*complexconjugate(ZEL21)) - Y1n12*ZP21*complexconjugate(Vv15)*complexconjugate(ZEL21) - Y1n21*ZP21*complexconjugate(Vv14)*complexconjugate(ZEL22) - Y1n22*ZP21*complexconjugate(Vv15)*complexconjugate(ZEL22) - Y2n33*ZP22*complexconjugate(Vv16)*complexconjugate(ZEL23))', 
	 order = {'QED':1} ) 
 
GC_1004 = Coupling(name = 'GC_1004',
	 value = '1*complex(0,1)*(-(ZER21*ZP11*(Vv21*complexconjugate(Y1e11) + Vv22*complexconjugate(Y1e21))) - ZER22*ZP11*(Vv21*complexconjugate(Y1e12) + Vv22*complexconjugate(Y1e22)) - Vv23*ZER23*ZP12*complexconjugate(Y2e33))', 
	 order = {'QED':1} ) 
 
GC_1005 = Coupling(name = 'GC_1005',
	 value = '1*complex(0,1)*(-(Y1n11*ZP11*complexconjugate(Vv24)*complexconjugate(ZEL21)) - Y1n12*ZP11*complexconjugate(Vv25)*complexconjugate(ZEL21) - Y1n21*ZP11*complexconjugate(Vv24)*complexconjugate(ZEL22) - Y1n22*ZP11*complexconjugate(Vv25)*complexconjugate(ZEL22) - Y2n33*ZP12*complexconjugate(Vv26)*complexconjugate(ZEL23))', 
	 order = {'QED':1} ) 
 
GC_1006 = Coupling(name = 'GC_1006',
	 value = '1*complex(0,1)*(-(ZER21*ZP21*(Vv21*complexconjugate(Y1e11) + Vv22*complexconjugate(Y1e21))) - ZER22*ZP21*(Vv21*complexconjugate(Y1e12) + Vv22*complexconjugate(Y1e22)) - Vv23*ZER23*ZP22*complexconjugate(Y2e33))', 
	 order = {'QED':1} ) 
 
GC_1007 = Coupling(name = 'GC_1007',
	 value = '1*complex(0,1)*(-(Y1n11*ZP21*complexconjugate(Vv24)*complexconjugate(ZEL21)) - Y1n12*ZP21*complexconjugate(Vv25)*complexconjugate(ZEL21) - Y1n21*ZP21*complexconjugate(Vv24)*complexconjugate(ZEL22) - Y1n22*ZP21*complexconjugate(Vv25)*complexconjugate(ZEL22) - Y2n33*ZP22*complexconjugate(Vv26)*complexconjugate(ZEL23))', 
	 order = {'QED':1} ) 
 
GC_1008 = Coupling(name = 'GC_1008',
	 value = '1*complex(0,1)*(-(ZER21*ZP11*(Vv31*complexconjugate(Y1e11) + Vv32*complexconjugate(Y1e21))) - ZER22*ZP11*(Vv31*complexconjugate(Y1e12) + Vv32*complexconjugate(Y1e22)) - Vv33*ZER23*ZP12*complexconjugate(Y2e33))', 
	 order = {'QED':1} ) 
 
GC_1009 = Coupling(name = 'GC_1009',
	 value = '1*complex(0,1)*(-(Y1n11*ZP11*complexconjugate(Vv34)*complexconjugate(ZEL21)) - Y1n12*ZP11*complexconjugate(Vv35)*complexconjugate(ZEL21) - Y1n21*ZP11*complexconjugate(Vv34)*complexconjugate(ZEL22) - Y1n22*ZP11*complexconjugate(Vv35)*complexconjugate(ZEL22) - Y2n33*ZP12*complexconjugate(Vv36)*complexconjugate(ZEL23))', 
	 order = {'QED':1} ) 
 
GC_1010 = Coupling(name = 'GC_1010',
	 value = '1*complex(0,1)*(-(ZER21*ZP21*(Vv31*complexconjugate(Y1e11) + Vv32*complexconjugate(Y1e21))) - ZER22*ZP21*(Vv31*complexconjugate(Y1e12) + Vv32*complexconjugate(Y1e22)) - Vv33*ZER23*ZP22*complexconjugate(Y2e33))', 
	 order = {'QED':1} ) 
 
GC_1011 = Coupling(name = 'GC_1011',
	 value = '1*complex(0,1)*(-(Y1n11*ZP21*complexconjugate(Vv34)*complexconjugate(ZEL21)) - Y1n12*ZP21*complexconjugate(Vv35)*complexconjugate(ZEL21) - Y1n21*ZP21*complexconjugate(Vv34)*complexconjugate(ZEL22) - Y1n22*ZP21*complexconjugate(Vv35)*complexconjugate(ZEL22) - Y2n33*ZP22*complexconjugate(Vv36)*complexconjugate(ZEL23))', 
	 order = {'QED':1} ) 
 
GC_1012 = Coupling(name = 'GC_1012',
	 value = '1*complex(0,1)*(-(ZER21*ZP11*(Vv41*complexconjugate(Y1e11) + Vv42*complexconjugate(Y1e21))) - ZER22*ZP11*(Vv41*complexconjugate(Y1e12) + Vv42*complexconjugate(Y1e22)) - Vv43*ZER23*ZP12*complexconjugate(Y2e33))', 
	 order = {'QED':1} ) 
 
GC_1013 = Coupling(name = 'GC_1013',
	 value = '1*complex(0,1)*(-(Y1n11*ZP11*complexconjugate(Vv44)*complexconjugate(ZEL21)) - Y1n12*ZP11*complexconjugate(Vv45)*complexconjugate(ZEL21) - Y1n21*ZP11*complexconjugate(Vv44)*complexconjugate(ZEL22) - Y1n22*ZP11*complexconjugate(Vv45)*complexconjugate(ZEL22) - Y2n33*ZP12*complexconjugate(Vv46)*complexconjugate(ZEL23))', 
	 order = {'QED':1} ) 
 
GC_1014 = Coupling(name = 'GC_1014',
	 value = '1*complex(0,1)*(-(ZER21*ZP21*(Vv41*complexconjugate(Y1e11) + Vv42*complexconjugate(Y1e21))) - ZER22*ZP21*(Vv41*complexconjugate(Y1e12) + Vv42*complexconjugate(Y1e22)) - Vv43*ZER23*ZP22*complexconjugate(Y2e33))', 
	 order = {'QED':1} ) 
 
GC_1015 = Coupling(name = 'GC_1015',
	 value = '1*complex(0,1)*(-(Y1n11*ZP21*complexconjugate(Vv44)*complexconjugate(ZEL21)) - Y1n12*ZP21*complexconjugate(Vv45)*complexconjugate(ZEL21) - Y1n21*ZP21*complexconjugate(Vv44)*complexconjugate(ZEL22) - Y1n22*ZP21*complexconjugate(Vv45)*complexconjugate(ZEL22) - Y2n33*ZP22*complexconjugate(Vv46)*complexconjugate(ZEL23))', 
	 order = {'QED':1} ) 
 
GC_1016 = Coupling(name = 'GC_1016',
	 value = '1*complex(0,1)*(-(ZER21*ZP11*(Vv51*complexconjugate(Y1e11) + Vv52*complexconjugate(Y1e21))) - ZER22*ZP11*(Vv51*complexconjugate(Y1e12) + Vv52*complexconjugate(Y1e22)) - Vv53*ZER23*ZP12*complexconjugate(Y2e33))', 
	 order = {'QED':1} ) 
 
GC_1017 = Coupling(name = 'GC_1017',
	 value = '1*complex(0,1)*(-(Y1n11*ZP11*complexconjugate(Vv54)*complexconjugate(ZEL21)) - Y1n12*ZP11*complexconjugate(Vv55)*complexconjugate(ZEL21) - Y1n21*ZP11*complexconjugate(Vv54)*complexconjugate(ZEL22) - Y1n22*ZP11*complexconjugate(Vv55)*complexconjugate(ZEL22) - Y2n33*ZP12*complexconjugate(Vv56)*complexconjugate(ZEL23))', 
	 order = {'QED':1} ) 
 
GC_1018 = Coupling(name = 'GC_1018',
	 value = '1*complex(0,1)*(-(ZER21*ZP21*(Vv51*complexconjugate(Y1e11) + Vv52*complexconjugate(Y1e21))) - ZER22*ZP21*(Vv51*complexconjugate(Y1e12) + Vv52*complexconjugate(Y1e22)) - Vv53*ZER23*ZP22*complexconjugate(Y2e33))', 
	 order = {'QED':1} ) 
 
GC_1019 = Coupling(name = 'GC_1019',
	 value = '1*complex(0,1)*(-(Y1n11*ZP21*complexconjugate(Vv54)*complexconjugate(ZEL21)) - Y1n12*ZP21*complexconjugate(Vv55)*complexconjugate(ZEL21) - Y1n21*ZP21*complexconjugate(Vv54)*complexconjugate(ZEL22) - Y1n22*ZP21*complexconjugate(Vv55)*complexconjugate(ZEL22) - Y2n33*ZP22*complexconjugate(Vv56)*complexconjugate(ZEL23))', 
	 order = {'QED':1} ) 
 
GC_1020 = Coupling(name = 'GC_1020',
	 value = '1*complex(0,1)*(-(ZER21*ZP11*(Vv61*complexconjugate(Y1e11) + Vv62*complexconjugate(Y1e21))) - ZER22*ZP11*(Vv61*complexconjugate(Y1e12) + Vv62*complexconjugate(Y1e22)) - Vv63*ZER23*ZP12*complexconjugate(Y2e33))', 
	 order = {'QED':1} ) 
 
GC_1021 = Coupling(name = 'GC_1021',
	 value = '1*complex(0,1)*(-(Y1n11*ZP11*complexconjugate(Vv64)*complexconjugate(ZEL21)) - Y1n12*ZP11*complexconjugate(Vv65)*complexconjugate(ZEL21) - Y1n21*ZP11*complexconjugate(Vv64)*complexconjugate(ZEL22) - Y1n22*ZP11*complexconjugate(Vv65)*complexconjugate(ZEL22) - Y2n33*ZP12*complexconjugate(Vv66)*complexconjugate(ZEL23))', 
	 order = {'QED':1} ) 
 
GC_1022 = Coupling(name = 'GC_1022',
	 value = '1*complex(0,1)*(-(ZER21*ZP21*(Vv61*complexconjugate(Y1e11) + Vv62*complexconjugate(Y1e21))) - ZER22*ZP21*(Vv61*complexconjugate(Y1e12) + Vv62*complexconjugate(Y1e22)) - Vv63*ZER23*ZP22*complexconjugate(Y2e33))', 
	 order = {'QED':1} ) 
 
GC_1023 = Coupling(name = 'GC_1023',
	 value = '1*complex(0,1)*(-(Y1n11*ZP21*complexconjugate(Vv64)*complexconjugate(ZEL21)) - Y1n12*ZP21*complexconjugate(Vv65)*complexconjugate(ZEL21) - Y1n21*ZP21*complexconjugate(Vv64)*complexconjugate(ZEL22) - Y1n22*ZP21*complexconjugate(Vv65)*complexconjugate(ZEL22) - Y2n33*ZP22*complexconjugate(Vv66)*complexconjugate(ZEL23))', 
	 order = {'QED':1} ) 
 
GC_1024 = Coupling(name = 'GC_1024',
	 value = '1*complex(0,1)*(-(ZER31*ZP11*(Vv11*complexconjugate(Y1e11) + Vv12*complexconjugate(Y1e21))) - ZER32*ZP11*(Vv11*complexconjugate(Y1e12) + Vv12*complexconjugate(Y1e22)) - Vv13*ZER33*ZP12*complexconjugate(Y2e33))', 
	 order = {'QED':1} ) 
 
GC_1025 = Coupling(name = 'GC_1025',
	 value = '1*complex(0,1)*(-(Y1n11*ZP11*complexconjugate(Vv14)*complexconjugate(ZEL31)) - Y1n12*ZP11*complexconjugate(Vv15)*complexconjugate(ZEL31) - Y1n21*ZP11*complexconjugate(Vv14)*complexconjugate(ZEL32) - Y1n22*ZP11*complexconjugate(Vv15)*complexconjugate(ZEL32) - Y2n33*ZP12*complexconjugate(Vv16)*complexconjugate(ZEL33))', 
	 order = {'QED':1} ) 
 
GC_1026 = Coupling(name = 'GC_1026',
	 value = '1*complex(0,1)*(-(ZER31*ZP21*(Vv11*complexconjugate(Y1e11) + Vv12*complexconjugate(Y1e21))) - ZER32*ZP21*(Vv11*complexconjugate(Y1e12) + Vv12*complexconjugate(Y1e22)) - Vv13*ZER33*ZP22*complexconjugate(Y2e33))', 
	 order = {'QED':1} ) 
 
GC_1027 = Coupling(name = 'GC_1027',
	 value = '1*complex(0,1)*(-(Y1n11*ZP21*complexconjugate(Vv14)*complexconjugate(ZEL31)) - Y1n12*ZP21*complexconjugate(Vv15)*complexconjugate(ZEL31) - Y1n21*ZP21*complexconjugate(Vv14)*complexconjugate(ZEL32) - Y1n22*ZP21*complexconjugate(Vv15)*complexconjugate(ZEL32) - Y2n33*ZP22*complexconjugate(Vv16)*complexconjugate(ZEL33))', 
	 order = {'QED':1} ) 
 
GC_1028 = Coupling(name = 'GC_1028',
	 value = '1*complex(0,1)*(-(ZER31*ZP11*(Vv21*complexconjugate(Y1e11) + Vv22*complexconjugate(Y1e21))) - ZER32*ZP11*(Vv21*complexconjugate(Y1e12) + Vv22*complexconjugate(Y1e22)) - Vv23*ZER33*ZP12*complexconjugate(Y2e33))', 
	 order = {'QED':1} ) 
 
GC_1029 = Coupling(name = 'GC_1029',
	 value = '1*complex(0,1)*(-(Y1n11*ZP11*complexconjugate(Vv24)*complexconjugate(ZEL31)) - Y1n12*ZP11*complexconjugate(Vv25)*complexconjugate(ZEL31) - Y1n21*ZP11*complexconjugate(Vv24)*complexconjugate(ZEL32) - Y1n22*ZP11*complexconjugate(Vv25)*complexconjugate(ZEL32) - Y2n33*ZP12*complexconjugate(Vv26)*complexconjugate(ZEL33))', 
	 order = {'QED':1} ) 
 
GC_1030 = Coupling(name = 'GC_1030',
	 value = '1*complex(0,1)*(-(ZER31*ZP21*(Vv21*complexconjugate(Y1e11) + Vv22*complexconjugate(Y1e21))) - ZER32*ZP21*(Vv21*complexconjugate(Y1e12) + Vv22*complexconjugate(Y1e22)) - Vv23*ZER33*ZP22*complexconjugate(Y2e33))', 
	 order = {'QED':1} ) 
 
GC_1031 = Coupling(name = 'GC_1031',
	 value = '1*complex(0,1)*(-(Y1n11*ZP21*complexconjugate(Vv24)*complexconjugate(ZEL31)) - Y1n12*ZP21*complexconjugate(Vv25)*complexconjugate(ZEL31) - Y1n21*ZP21*complexconjugate(Vv24)*complexconjugate(ZEL32) - Y1n22*ZP21*complexconjugate(Vv25)*complexconjugate(ZEL32) - Y2n33*ZP22*complexconjugate(Vv26)*complexconjugate(ZEL33))', 
	 order = {'QED':1} ) 
 
GC_1032 = Coupling(name = 'GC_1032',
	 value = '1*complex(0,1)*(-(ZER31*ZP11*(Vv31*complexconjugate(Y1e11) + Vv32*complexconjugate(Y1e21))) - ZER32*ZP11*(Vv31*complexconjugate(Y1e12) + Vv32*complexconjugate(Y1e22)) - Vv33*ZER33*ZP12*complexconjugate(Y2e33))', 
	 order = {'QED':1} ) 
 
GC_1033 = Coupling(name = 'GC_1033',
	 value = '1*complex(0,1)*(-(Y1n11*ZP11*complexconjugate(Vv34)*complexconjugate(ZEL31)) - Y1n12*ZP11*complexconjugate(Vv35)*complexconjugate(ZEL31) - Y1n21*ZP11*complexconjugate(Vv34)*complexconjugate(ZEL32) - Y1n22*ZP11*complexconjugate(Vv35)*complexconjugate(ZEL32) - Y2n33*ZP12*complexconjugate(Vv36)*complexconjugate(ZEL33))', 
	 order = {'QED':1} ) 
 
GC_1034 = Coupling(name = 'GC_1034',
	 value = '1*complex(0,1)*(-(ZER31*ZP21*(Vv31*complexconjugate(Y1e11) + Vv32*complexconjugate(Y1e21))) - ZER32*ZP21*(Vv31*complexconjugate(Y1e12) + Vv32*complexconjugate(Y1e22)) - Vv33*ZER33*ZP22*complexconjugate(Y2e33))', 
	 order = {'QED':1} ) 
 
GC_1035 = Coupling(name = 'GC_1035',
	 value = '1*complex(0,1)*(-(Y1n11*ZP21*complexconjugate(Vv34)*complexconjugate(ZEL31)) - Y1n12*ZP21*complexconjugate(Vv35)*complexconjugate(ZEL31) - Y1n21*ZP21*complexconjugate(Vv34)*complexconjugate(ZEL32) - Y1n22*ZP21*complexconjugate(Vv35)*complexconjugate(ZEL32) - Y2n33*ZP22*complexconjugate(Vv36)*complexconjugate(ZEL33))', 
	 order = {'QED':1} ) 
 
GC_1036 = Coupling(name = 'GC_1036',
	 value = '1*complex(0,1)*(-(ZER31*ZP11*(Vv41*complexconjugate(Y1e11) + Vv42*complexconjugate(Y1e21))) - ZER32*ZP11*(Vv41*complexconjugate(Y1e12) + Vv42*complexconjugate(Y1e22)) - Vv43*ZER33*ZP12*complexconjugate(Y2e33))', 
	 order = {'QED':1} ) 
 
GC_1037 = Coupling(name = 'GC_1037',
	 value = '1*complex(0,1)*(-(Y1n11*ZP11*complexconjugate(Vv44)*complexconjugate(ZEL31)) - Y1n12*ZP11*complexconjugate(Vv45)*complexconjugate(ZEL31) - Y1n21*ZP11*complexconjugate(Vv44)*complexconjugate(ZEL32) - Y1n22*ZP11*complexconjugate(Vv45)*complexconjugate(ZEL32) - Y2n33*ZP12*complexconjugate(Vv46)*complexconjugate(ZEL33))', 
	 order = {'QED':1} ) 
 
GC_1038 = Coupling(name = 'GC_1038',
	 value = '1*complex(0,1)*(-(ZER31*ZP21*(Vv41*complexconjugate(Y1e11) + Vv42*complexconjugate(Y1e21))) - ZER32*ZP21*(Vv41*complexconjugate(Y1e12) + Vv42*complexconjugate(Y1e22)) - Vv43*ZER33*ZP22*complexconjugate(Y2e33))', 
	 order = {'QED':1} ) 
 
GC_1039 = Coupling(name = 'GC_1039',
	 value = '1*complex(0,1)*(-(Y1n11*ZP21*complexconjugate(Vv44)*complexconjugate(ZEL31)) - Y1n12*ZP21*complexconjugate(Vv45)*complexconjugate(ZEL31) - Y1n21*ZP21*complexconjugate(Vv44)*complexconjugate(ZEL32) - Y1n22*ZP21*complexconjugate(Vv45)*complexconjugate(ZEL32) - Y2n33*ZP22*complexconjugate(Vv46)*complexconjugate(ZEL33))', 
	 order = {'QED':1} ) 
 
GC_1040 = Coupling(name = 'GC_1040',
	 value = '1*complex(0,1)*(-(ZER31*ZP11*(Vv51*complexconjugate(Y1e11) + Vv52*complexconjugate(Y1e21))) - ZER32*ZP11*(Vv51*complexconjugate(Y1e12) + Vv52*complexconjugate(Y1e22)) - Vv53*ZER33*ZP12*complexconjugate(Y2e33))', 
	 order = {'QED':1} ) 
 
GC_1041 = Coupling(name = 'GC_1041',
	 value = '1*complex(0,1)*(-(Y1n11*ZP11*complexconjugate(Vv54)*complexconjugate(ZEL31)) - Y1n12*ZP11*complexconjugate(Vv55)*complexconjugate(ZEL31) - Y1n21*ZP11*complexconjugate(Vv54)*complexconjugate(ZEL32) - Y1n22*ZP11*complexconjugate(Vv55)*complexconjugate(ZEL32) - Y2n33*ZP12*complexconjugate(Vv56)*complexconjugate(ZEL33))', 
	 order = {'QED':1} ) 
 
GC_1042 = Coupling(name = 'GC_1042',
	 value = '1*complex(0,1)*(-(ZER31*ZP21*(Vv51*complexconjugate(Y1e11) + Vv52*complexconjugate(Y1e21))) - ZER32*ZP21*(Vv51*complexconjugate(Y1e12) + Vv52*complexconjugate(Y1e22)) - Vv53*ZER33*ZP22*complexconjugate(Y2e33))', 
	 order = {'QED':1} ) 
 
GC_1043 = Coupling(name = 'GC_1043',
	 value = '1*complex(0,1)*(-(Y1n11*ZP21*complexconjugate(Vv54)*complexconjugate(ZEL31)) - Y1n12*ZP21*complexconjugate(Vv55)*complexconjugate(ZEL31) - Y1n21*ZP21*complexconjugate(Vv54)*complexconjugate(ZEL32) - Y1n22*ZP21*complexconjugate(Vv55)*complexconjugate(ZEL32) - Y2n33*ZP22*complexconjugate(Vv56)*complexconjugate(ZEL33))', 
	 order = {'QED':1} ) 
 
GC_1044 = Coupling(name = 'GC_1044',
	 value = '1*complex(0,1)*(-(ZER31*ZP11*(Vv61*complexconjugate(Y1e11) + Vv62*complexconjugate(Y1e21))) - ZER32*ZP11*(Vv61*complexconjugate(Y1e12) + Vv62*complexconjugate(Y1e22)) - Vv63*ZER33*ZP12*complexconjugate(Y2e33))', 
	 order = {'QED':1} ) 
 
GC_1045 = Coupling(name = 'GC_1045',
	 value = '1*complex(0,1)*(-(Y1n11*ZP11*complexconjugate(Vv64)*complexconjugate(ZEL31)) - Y1n12*ZP11*complexconjugate(Vv65)*complexconjugate(ZEL31) - Y1n21*ZP11*complexconjugate(Vv64)*complexconjugate(ZEL32) - Y1n22*ZP11*complexconjugate(Vv65)*complexconjugate(ZEL32) - Y2n33*ZP12*complexconjugate(Vv66)*complexconjugate(ZEL33))', 
	 order = {'QED':1} ) 
 
GC_1046 = Coupling(name = 'GC_1046',
	 value = '1*complex(0,1)*(-(ZER31*ZP21*(Vv61*complexconjugate(Y1e11) + Vv62*complexconjugate(Y1e21))) - ZER32*ZP21*(Vv61*complexconjugate(Y1e12) + Vv62*complexconjugate(Y1e22)) - Vv63*ZER33*ZP22*complexconjugate(Y2e33))', 
	 order = {'QED':1} ) 
 
GC_1047 = Coupling(name = 'GC_1047',
	 value = '1*complex(0,1)*(-(Y1n11*ZP21*complexconjugate(Vv64)*complexconjugate(ZEL31)) - Y1n12*ZP21*complexconjugate(Vv65)*complexconjugate(ZEL31) - Y1n21*ZP21*complexconjugate(Vv64)*complexconjugate(ZEL32) - Y1n22*ZP21*complexconjugate(Vv65)*complexconjugate(ZEL32) - Y2n33*ZP22*complexconjugate(Vv66)*complexconjugate(ZEL33))', 
	 order = {'QED':1} ) 
 
GC_1048 = Coupling(name = 'GC_1048',
	 value = '1*complex(0,1)*G', 
	 order = {'QCD':1} ) 
 
GC_1049 = Coupling(name = 'GC_1049',
	 value = '1*complex(0,1)*G', 
	 order = {'QCD':1} ) 
 
GC_1050 = Coupling(name = 'GC_1050',
	 value = '1*complex(0,1)*G', 
	 order = {'QCD':1} ) 
 
GC_1051 = Coupling(name = 'GC_1051',
	 value = '1*complex(0,1)*G', 
	 order = {'QCD':1} ) 
 
GC_1052 = Coupling(name = 'GC_1052',
	 value = '1*complex(0,1)*G', 
	 order = {'QCD':1} ) 
 
GC_1053 = Coupling(name = 'GC_1053',
	 value = '1*complex(0,1)*G', 
	 order = {'QCD':1} ) 
 
GC_1054 = Coupling(name = 'GC_1054',
	 value = '1./6.*complex(0,1)*(g1*complexconjugate(ZZ11) - 3*g2*complexconjugate(ZZ21))', 
	 order = {'QED':1} ) 
 
GC_1055 = Coupling(name = 'GC_1055',
	 value = '-1./3.*complex(0,1)*g1*complexconjugate(ZZ11)', 
	 order = {'QED':1} ) 
 
GC_1056 = Coupling(name = 'GC_1056',
	 value = '1./6.*complex(0,1)*(g1*complexconjugate(ZZ11) - 3*g2*complexconjugate(ZZ21))', 
	 order = {'QED':1} ) 
 
GC_1057 = Coupling(name = 'GC_1057',
	 value = '-1./3.*complex(0,1)*g1*complexconjugate(ZZ11)', 
	 order = {'QED':1} ) 
 
GC_1058 = Coupling(name = 'GC_1058',
	 value = '1./6.*complex(0,1)*(g1*complexconjugate(ZZ11) - 3*g2*complexconjugate(ZZ21))', 
	 order = {'QED':1} ) 
 
GC_1059 = Coupling(name = 'GC_1059',
	 value = '-1./3.*complex(0,1)*g1*complexconjugate(ZZ11)', 
	 order = {'QED':1} ) 
 
GC_1060 = Coupling(name = 'GC_1060',
	 value = '1./6.*complex(0,1)*(g1*complexconjugate(ZZ12) - 3*g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_1061 = Coupling(name = 'GC_1061',
	 value = '-1./3.*complex(0,1)*g1*complexconjugate(ZZ12)', 
	 order = {'QED':1} ) 
 
GC_1062 = Coupling(name = 'GC_1062',
	 value = '1./6.*complex(0,1)*(g1*complexconjugate(ZZ12) - 3*g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_1063 = Coupling(name = 'GC_1063',
	 value = '-1./3.*complex(0,1)*g1*complexconjugate(ZZ12)', 
	 order = {'QED':1} ) 
 
GC_1064 = Coupling(name = 'GC_1064',
	 value = '1./6.*complex(0,1)*(g1*complexconjugate(ZZ12) - 3*g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_1065 = Coupling(name = 'GC_1065',
	 value = '-1./3.*complex(0,1)*g1*complexconjugate(ZZ12)', 
	 order = {'QED':1} ) 
 
GC_1066 = Coupling(name = 'GC_1066',
	 value = '(1*complex(0,1)*g2*(ZDL11*complexconjugate(ZUL11) + ZDL12*complexconjugate(ZUL12) + ZDL13*complexconjugate(ZUL13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1067 = Coupling(name = 'GC_1067',
	 value = '(1*complex(0,1)*g2*(ZDL21*complexconjugate(ZUL11) + ZDL22*complexconjugate(ZUL12) + ZDL23*complexconjugate(ZUL13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1068 = Coupling(name = 'GC_1068',
	 value = '(1*complex(0,1)*g2*(ZDL31*complexconjugate(ZUL11) + ZDL32*complexconjugate(ZUL12) + ZDL33*complexconjugate(ZUL13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1069 = Coupling(name = 'GC_1069',
	 value = '(1*complex(0,1)*g2*(ZDL11*complexconjugate(ZUL21) + ZDL12*complexconjugate(ZUL22) + ZDL13*complexconjugate(ZUL23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1070 = Coupling(name = 'GC_1070',
	 value = '(1*complex(0,1)*g2*(ZDL21*complexconjugate(ZUL21) + ZDL22*complexconjugate(ZUL22) + ZDL23*complexconjugate(ZUL23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1071 = Coupling(name = 'GC_1071',
	 value = '(1*complex(0,1)*g2*(ZDL31*complexconjugate(ZUL21) + ZDL32*complexconjugate(ZUL22) + ZDL33*complexconjugate(ZUL23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1072 = Coupling(name = 'GC_1072',
	 value = '(1*complex(0,1)*g2*(ZDL11*complexconjugate(ZUL31) + ZDL12*complexconjugate(ZUL32) + ZDL13*complexconjugate(ZUL33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1073 = Coupling(name = 'GC_1073',
	 value = '(1*complex(0,1)*g2*(ZDL21*complexconjugate(ZUL31) + ZDL22*complexconjugate(ZUL32) + ZDL23*complexconjugate(ZUL33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1074 = Coupling(name = 'GC_1074',
	 value = '(1*complex(0,1)*g2*(ZDL31*complexconjugate(ZUL31) + ZDL32*complexconjugate(ZUL32) + ZDL33*complexconjugate(ZUL33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1075 = Coupling(name = 'GC_1075',
	 value = '(1*complex(0,1)*g2*(ZEL11*complexconjugate(Vv11) + ZEL12*complexconjugate(Vv12) + ZEL13*complexconjugate(Vv13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1076 = Coupling(name = 'GC_1076',
	 value = '(1*complex(0,1)*g2*(ZEL21*complexconjugate(Vv11) + ZEL22*complexconjugate(Vv12) + ZEL23*complexconjugate(Vv13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1077 = Coupling(name = 'GC_1077',
	 value = '(1*complex(0,1)*g2*(ZEL31*complexconjugate(Vv11) + ZEL32*complexconjugate(Vv12) + ZEL33*complexconjugate(Vv13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1078 = Coupling(name = 'GC_1078',
	 value = '(1*complex(0,1)*g2*(ZEL11*complexconjugate(Vv21) + ZEL12*complexconjugate(Vv22) + ZEL13*complexconjugate(Vv23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1079 = Coupling(name = 'GC_1079',
	 value = '(1*complex(0,1)*g2*(ZEL21*complexconjugate(Vv21) + ZEL22*complexconjugate(Vv22) + ZEL23*complexconjugate(Vv23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1080 = Coupling(name = 'GC_1080',
	 value = '(1*complex(0,1)*g2*(ZEL31*complexconjugate(Vv21) + ZEL32*complexconjugate(Vv22) + ZEL33*complexconjugate(Vv23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1081 = Coupling(name = 'GC_1081',
	 value = '(1*complex(0,1)*g2*(ZEL11*complexconjugate(Vv31) + ZEL12*complexconjugate(Vv32) + ZEL13*complexconjugate(Vv33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1082 = Coupling(name = 'GC_1082',
	 value = '(1*complex(0,1)*g2*(ZEL21*complexconjugate(Vv31) + ZEL22*complexconjugate(Vv32) + ZEL23*complexconjugate(Vv33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1083 = Coupling(name = 'GC_1083',
	 value = '(1*complex(0,1)*g2*(ZEL31*complexconjugate(Vv31) + ZEL32*complexconjugate(Vv32) + ZEL33*complexconjugate(Vv33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1084 = Coupling(name = 'GC_1084',
	 value = '(1*complex(0,1)*g2*(ZEL11*complexconjugate(Vv41) + ZEL12*complexconjugate(Vv42) + ZEL13*complexconjugate(Vv43)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1085 = Coupling(name = 'GC_1085',
	 value = '(1*complex(0,1)*g2*(ZEL21*complexconjugate(Vv41) + ZEL22*complexconjugate(Vv42) + ZEL23*complexconjugate(Vv43)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1086 = Coupling(name = 'GC_1086',
	 value = '(1*complex(0,1)*g2*(ZEL31*complexconjugate(Vv41) + ZEL32*complexconjugate(Vv42) + ZEL33*complexconjugate(Vv43)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1087 = Coupling(name = 'GC_1087',
	 value = '(1*complex(0,1)*g2*(ZEL11*complexconjugate(Vv51) + ZEL12*complexconjugate(Vv52) + ZEL13*complexconjugate(Vv53)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1088 = Coupling(name = 'GC_1088',
	 value = '(1*complex(0,1)*g2*(ZEL21*complexconjugate(Vv51) + ZEL22*complexconjugate(Vv52) + ZEL23*complexconjugate(Vv53)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1089 = Coupling(name = 'GC_1089',
	 value = '(1*complex(0,1)*g2*(ZEL31*complexconjugate(Vv51) + ZEL32*complexconjugate(Vv52) + ZEL33*complexconjugate(Vv53)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1090 = Coupling(name = 'GC_1090',
	 value = '(1*complex(0,1)*g2*(ZEL11*complexconjugate(Vv61) + ZEL12*complexconjugate(Vv62) + ZEL13*complexconjugate(Vv63)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1091 = Coupling(name = 'GC_1091',
	 value = '(1*complex(0,1)*g2*(ZEL21*complexconjugate(Vv61) + ZEL22*complexconjugate(Vv62) + ZEL23*complexconjugate(Vv63)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1092 = Coupling(name = 'GC_1092',
	 value = '(1*complex(0,1)*g2*(ZEL31*complexconjugate(Vv61) + ZEL32*complexconjugate(Vv62) + ZEL33*complexconjugate(Vv63)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1093 = Coupling(name = 'GC_1093',
	 value = '-1./2.*complex(0,1)*(g1*complexconjugate(ZZ11) + g2*complexconjugate(ZZ21))', 
	 order = {'QED':1} ) 
 
GC_1094 = Coupling(name = 'GC_1094',
	 value = '-1*complex(0,1)*g1*complexconjugate(ZZ11)', 
	 order = {'QED':1} ) 
 
GC_1095 = Coupling(name = 'GC_1095',
	 value = '-1./2.*complex(0,1)*(g1*complexconjugate(ZZ11) + g2*complexconjugate(ZZ21))', 
	 order = {'QED':1} ) 
 
GC_1096 = Coupling(name = 'GC_1096',
	 value = '-1*complex(0,1)*g1*complexconjugate(ZZ11)', 
	 order = {'QED':1} ) 
 
GC_1097 = Coupling(name = 'GC_1097',
	 value = '-1./2.*complex(0,1)*(g1*complexconjugate(ZZ11) + g2*complexconjugate(ZZ21))', 
	 order = {'QED':1} ) 
 
GC_1098 = Coupling(name = 'GC_1098',
	 value = '-1*complex(0,1)*g1*complexconjugate(ZZ11)', 
	 order = {'QED':1} ) 
 
GC_1099 = Coupling(name = 'GC_1099',
	 value = '-1./2.*complex(0,1)*(g1*complexconjugate(ZZ12) + g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_1100 = Coupling(name = 'GC_1100',
	 value = '-1*complex(0,1)*g1*complexconjugate(ZZ12)', 
	 order = {'QED':1} ) 
 
GC_1101 = Coupling(name = 'GC_1101',
	 value = '-1./2.*complex(0,1)*(g1*complexconjugate(ZZ12) + g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_1102 = Coupling(name = 'GC_1102',
	 value = '-1*complex(0,1)*g1*complexconjugate(ZZ12)', 
	 order = {'QED':1} ) 
 
GC_1103 = Coupling(name = 'GC_1103',
	 value = '-1./2.*complex(0,1)*(g1*complexconjugate(ZZ12) + g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_1104 = Coupling(name = 'GC_1104',
	 value = '-1*complex(0,1)*g1*complexconjugate(ZZ12)', 
	 order = {'QED':1} ) 
 
GC_1105 = Coupling(name = 'GC_1105',
	 value = '1*complex(0,1)*G', 
	 order = {'QCD':1} ) 
 
GC_1106 = Coupling(name = 'GC_1106',
	 value = '1*complex(0,1)*G', 
	 order = {'QCD':1} ) 
 
GC_1107 = Coupling(name = 'GC_1107',
	 value = '1*complex(0,1)*G', 
	 order = {'QCD':1} ) 
 
GC_1108 = Coupling(name = 'GC_1108',
	 value = '1*complex(0,1)*G', 
	 order = {'QCD':1} ) 
 
GC_1109 = Coupling(name = 'GC_1109',
	 value = '1*complex(0,1)*G', 
	 order = {'QCD':1} ) 
 
GC_1110 = Coupling(name = 'GC_1110',
	 value = '1*complex(0,1)*G', 
	 order = {'QCD':1} ) 
 
GC_1111 = Coupling(name = 'GC_1111',
	 value = '1./6.*complex(0,1)*(g1*complexconjugate(ZZ11) + 3*g2*complexconjugate(ZZ21))', 
	 order = {'QED':1} ) 
 
GC_1112 = Coupling(name = 'GC_1112',
	 value = '2./3.*complex(0,1)*g1*complexconjugate(ZZ11)', 
	 order = {'QED':1} ) 
 
GC_1113 = Coupling(name = 'GC_1113',
	 value = '1./6.*complex(0,1)*(g1*complexconjugate(ZZ11) + 3*g2*complexconjugate(ZZ21))', 
	 order = {'QED':1} ) 
 
GC_1114 = Coupling(name = 'GC_1114',
	 value = '2./3.*complex(0,1)*g1*complexconjugate(ZZ11)', 
	 order = {'QED':1} ) 
 
GC_1115 = Coupling(name = 'GC_1115',
	 value = '1./6.*complex(0,1)*(g1*complexconjugate(ZZ11) + 3*g2*complexconjugate(ZZ21))', 
	 order = {'QED':1} ) 
 
GC_1116 = Coupling(name = 'GC_1116',
	 value = '2./3.*complex(0,1)*g1*complexconjugate(ZZ11)', 
	 order = {'QED':1} ) 
 
GC_1117 = Coupling(name = 'GC_1117',
	 value = '(1*complex(0,1)*g2*(ZUL11*complexconjugate(ZDL11) + ZUL12*complexconjugate(ZDL12) + ZUL13*complexconjugate(ZDL13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1118 = Coupling(name = 'GC_1118',
	 value = '(1*complex(0,1)*g2*(ZUL21*complexconjugate(ZDL11) + ZUL22*complexconjugate(ZDL12) + ZUL23*complexconjugate(ZDL13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1119 = Coupling(name = 'GC_1119',
	 value = '(1*complex(0,1)*g2*(ZUL31*complexconjugate(ZDL11) + ZUL32*complexconjugate(ZDL12) + ZUL33*complexconjugate(ZDL13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1120 = Coupling(name = 'GC_1120',
	 value = '(1*complex(0,1)*g2*(ZUL11*complexconjugate(ZDL21) + ZUL12*complexconjugate(ZDL22) + ZUL13*complexconjugate(ZDL23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1121 = Coupling(name = 'GC_1121',
	 value = '(1*complex(0,1)*g2*(ZUL21*complexconjugate(ZDL21) + ZUL22*complexconjugate(ZDL22) + ZUL23*complexconjugate(ZDL23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1122 = Coupling(name = 'GC_1122',
	 value = '(1*complex(0,1)*g2*(ZUL31*complexconjugate(ZDL21) + ZUL32*complexconjugate(ZDL22) + ZUL33*complexconjugate(ZDL23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1123 = Coupling(name = 'GC_1123',
	 value = '(1*complex(0,1)*g2*(ZUL11*complexconjugate(ZDL31) + ZUL12*complexconjugate(ZDL32) + ZUL13*complexconjugate(ZDL33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1124 = Coupling(name = 'GC_1124',
	 value = '(1*complex(0,1)*g2*(ZUL21*complexconjugate(ZDL31) + ZUL22*complexconjugate(ZDL32) + ZUL23*complexconjugate(ZDL33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1125 = Coupling(name = 'GC_1125',
	 value = '(1*complex(0,1)*g2*(ZUL31*complexconjugate(ZDL31) + ZUL32*complexconjugate(ZDL32) + ZUL33*complexconjugate(ZDL33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1126 = Coupling(name = 'GC_1126',
	 value = '1./6.*complex(0,1)*(g1*complexconjugate(ZZ12) + 3*g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_1127 = Coupling(name = 'GC_1127',
	 value = '2./3.*complex(0,1)*g1*complexconjugate(ZZ12)', 
	 order = {'QED':1} ) 
 
GC_1128 = Coupling(name = 'GC_1128',
	 value = '1./6.*complex(0,1)*(g1*complexconjugate(ZZ12) + 3*g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_1129 = Coupling(name = 'GC_1129',
	 value = '2./3.*complex(0,1)*g1*complexconjugate(ZZ12)', 
	 order = {'QED':1} ) 
 
GC_1130 = Coupling(name = 'GC_1130',
	 value = '1./6.*complex(0,1)*(g1*complexconjugate(ZZ12) + 3*g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_1131 = Coupling(name = 'GC_1131',
	 value = '2./3.*complex(0,1)*g1*complexconjugate(ZZ12)', 
	 order = {'QED':1} ) 
 
GC_1132 = Coupling(name = 'GC_1132',
	 value = '-1./2.*complex(0,1)*(Vv11*complexconjugate(Vv11) + Vv12*complexconjugate(Vv12) + Vv13*complexconjugate(Vv13))*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21))', 
	 order = {'QED':1} ) 
 
GC_1133 = Coupling(name = 'GC_1133',
	 value = '1./2.*complex(0,1)*(Vv11*complexconjugate(Vv11) + Vv12*complexconjugate(Vv12) + Vv13*complexconjugate(Vv13))*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21))', 
	 order = {'QED':1} ) 
 
GC_1134 = Coupling(name = 'GC_1134',
	 value = '-1./2.*complex(0,1)*(Vv21*complexconjugate(Vv11) + Vv22*complexconjugate(Vv12) + Vv23*complexconjugate(Vv13))*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21))', 
	 order = {'QED':1} ) 
 
GC_1135 = Coupling(name = 'GC_1135',
	 value = '1./2.*complex(0,1)*(Vv11*complexconjugate(Vv21) + Vv12*complexconjugate(Vv22) + Vv13*complexconjugate(Vv23))*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21))', 
	 order = {'QED':1} ) 
 
GC_1136 = Coupling(name = 'GC_1136',
	 value = '-1./2.*complex(0,1)*(Vv31*complexconjugate(Vv11) + Vv32*complexconjugate(Vv12) + Vv33*complexconjugate(Vv13))*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21))', 
	 order = {'QED':1} ) 
 
GC_1137 = Coupling(name = 'GC_1137',
	 value = '1./2.*complex(0,1)*(Vv11*complexconjugate(Vv31) + Vv12*complexconjugate(Vv32) + Vv13*complexconjugate(Vv33))*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21))', 
	 order = {'QED':1} ) 
 
GC_1138 = Coupling(name = 'GC_1138',
	 value = '-1./2.*complex(0,1)*(Vv41*complexconjugate(Vv11) + Vv42*complexconjugate(Vv12) + Vv43*complexconjugate(Vv13))*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21))', 
	 order = {'QED':1} ) 
 
GC_1139 = Coupling(name = 'GC_1139',
	 value = '1./2.*complex(0,1)*(Vv11*complexconjugate(Vv41) + Vv12*complexconjugate(Vv42) + Vv13*complexconjugate(Vv43))*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21))', 
	 order = {'QED':1} ) 
 
GC_1140 = Coupling(name = 'GC_1140',
	 value = '-1./2.*complex(0,1)*(Vv51*complexconjugate(Vv11) + Vv52*complexconjugate(Vv12) + Vv53*complexconjugate(Vv13))*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21))', 
	 order = {'QED':1} ) 
 
GC_1141 = Coupling(name = 'GC_1141',
	 value = '1./2.*complex(0,1)*(Vv11*complexconjugate(Vv51) + Vv12*complexconjugate(Vv52) + Vv13*complexconjugate(Vv53))*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21))', 
	 order = {'QED':1} ) 
 
GC_1142 = Coupling(name = 'GC_1142',
	 value = '-1./2.*complex(0,1)*(Vv61*complexconjugate(Vv11) + Vv62*complexconjugate(Vv12) + Vv63*complexconjugate(Vv13))*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21))', 
	 order = {'QED':1} ) 
 
GC_1143 = Coupling(name = 'GC_1143',
	 value = '1./2.*complex(0,1)*(Vv11*complexconjugate(Vv61) + Vv12*complexconjugate(Vv62) + Vv13*complexconjugate(Vv63))*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21))', 
	 order = {'QED':1} ) 
 
GC_1144 = Coupling(name = 'GC_1144',
	 value = '-1./2.*complex(0,1)*(Vv21*complexconjugate(Vv21) + Vv22*complexconjugate(Vv22) + Vv23*complexconjugate(Vv23))*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21))', 
	 order = {'QED':1} ) 
 
GC_1145 = Coupling(name = 'GC_1145',
	 value = '1./2.*complex(0,1)*(Vv21*complexconjugate(Vv21) + Vv22*complexconjugate(Vv22) + Vv23*complexconjugate(Vv23))*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21))', 
	 order = {'QED':1} ) 
 
GC_1146 = Coupling(name = 'GC_1146',
	 value = '-1./2.*complex(0,1)*(Vv31*complexconjugate(Vv21) + Vv32*complexconjugate(Vv22) + Vv33*complexconjugate(Vv23))*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21))', 
	 order = {'QED':1} ) 
 
GC_1147 = Coupling(name = 'GC_1147',
	 value = '1./2.*complex(0,1)*(Vv21*complexconjugate(Vv31) + Vv22*complexconjugate(Vv32) + Vv23*complexconjugate(Vv33))*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21))', 
	 order = {'QED':1} ) 
 
GC_1148 = Coupling(name = 'GC_1148',
	 value = '-1./2.*complex(0,1)*(Vv41*complexconjugate(Vv21) + Vv42*complexconjugate(Vv22) + Vv43*complexconjugate(Vv23))*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21))', 
	 order = {'QED':1} ) 
 
GC_1149 = Coupling(name = 'GC_1149',
	 value = '1./2.*complex(0,1)*(Vv21*complexconjugate(Vv41) + Vv22*complexconjugate(Vv42) + Vv23*complexconjugate(Vv43))*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21))', 
	 order = {'QED':1} ) 
 
GC_1150 = Coupling(name = 'GC_1150',
	 value = '-1./2.*complex(0,1)*(Vv51*complexconjugate(Vv21) + Vv52*complexconjugate(Vv22) + Vv53*complexconjugate(Vv23))*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21))', 
	 order = {'QED':1} ) 
 
GC_1151 = Coupling(name = 'GC_1151',
	 value = '1./2.*complex(0,1)*(Vv21*complexconjugate(Vv51) + Vv22*complexconjugate(Vv52) + Vv23*complexconjugate(Vv53))*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21))', 
	 order = {'QED':1} ) 
 
GC_1152 = Coupling(name = 'GC_1152',
	 value = '-1./2.*complex(0,1)*(Vv61*complexconjugate(Vv21) + Vv62*complexconjugate(Vv22) + Vv63*complexconjugate(Vv23))*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21))', 
	 order = {'QED':1} ) 
 
GC_1153 = Coupling(name = 'GC_1153',
	 value = '1./2.*complex(0,1)*(Vv21*complexconjugate(Vv61) + Vv22*complexconjugate(Vv62) + Vv23*complexconjugate(Vv63))*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21))', 
	 order = {'QED':1} ) 
 
GC_1154 = Coupling(name = 'GC_1154',
	 value = '-1./2.*complex(0,1)*(Vv31*complexconjugate(Vv31) + Vv32*complexconjugate(Vv32) + Vv33*complexconjugate(Vv33))*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21))', 
	 order = {'QED':1} ) 
 
GC_1155 = Coupling(name = 'GC_1155',
	 value = '1./2.*complex(0,1)*(Vv31*complexconjugate(Vv31) + Vv32*complexconjugate(Vv32) + Vv33*complexconjugate(Vv33))*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21))', 
	 order = {'QED':1} ) 
 
GC_1156 = Coupling(name = 'GC_1156',
	 value = '-1./2.*complex(0,1)*(Vv41*complexconjugate(Vv31) + Vv42*complexconjugate(Vv32) + Vv43*complexconjugate(Vv33))*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21))', 
	 order = {'QED':1} ) 
 
GC_1157 = Coupling(name = 'GC_1157',
	 value = '1./2.*complex(0,1)*(Vv31*complexconjugate(Vv41) + Vv32*complexconjugate(Vv42) + Vv33*complexconjugate(Vv43))*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21))', 
	 order = {'QED':1} ) 
 
GC_1158 = Coupling(name = 'GC_1158',
	 value = '-1./2.*complex(0,1)*(Vv51*complexconjugate(Vv31) + Vv52*complexconjugate(Vv32) + Vv53*complexconjugate(Vv33))*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21))', 
	 order = {'QED':1} ) 
 
GC_1159 = Coupling(name = 'GC_1159',
	 value = '1./2.*complex(0,1)*(Vv31*complexconjugate(Vv51) + Vv32*complexconjugate(Vv52) + Vv33*complexconjugate(Vv53))*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21))', 
	 order = {'QED':1} ) 
 
GC_1160 = Coupling(name = 'GC_1160',
	 value = '-1./2.*complex(0,1)*(Vv61*complexconjugate(Vv31) + Vv62*complexconjugate(Vv32) + Vv63*complexconjugate(Vv33))*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21))', 
	 order = {'QED':1} ) 
 
GC_1161 = Coupling(name = 'GC_1161',
	 value = '1./2.*complex(0,1)*(Vv31*complexconjugate(Vv61) + Vv32*complexconjugate(Vv62) + Vv33*complexconjugate(Vv63))*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21))', 
	 order = {'QED':1} ) 
 
GC_1162 = Coupling(name = 'GC_1162',
	 value = '-1./2.*complex(0,1)*(Vv41*complexconjugate(Vv41) + Vv42*complexconjugate(Vv42) + Vv43*complexconjugate(Vv43))*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21))', 
	 order = {'QED':1} ) 
 
GC_1163 = Coupling(name = 'GC_1163',
	 value = '1./2.*complex(0,1)*(Vv41*complexconjugate(Vv41) + Vv42*complexconjugate(Vv42) + Vv43*complexconjugate(Vv43))*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21))', 
	 order = {'QED':1} ) 
 
GC_1164 = Coupling(name = 'GC_1164',
	 value = '-1./2.*complex(0,1)*(Vv51*complexconjugate(Vv41) + Vv52*complexconjugate(Vv42) + Vv53*complexconjugate(Vv43))*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21))', 
	 order = {'QED':1} ) 
 
GC_1165 = Coupling(name = 'GC_1165',
	 value = '1./2.*complex(0,1)*(Vv41*complexconjugate(Vv51) + Vv42*complexconjugate(Vv52) + Vv43*complexconjugate(Vv53))*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21))', 
	 order = {'QED':1} ) 
 
GC_1166 = Coupling(name = 'GC_1166',
	 value = '-1./2.*complex(0,1)*(Vv61*complexconjugate(Vv41) + Vv62*complexconjugate(Vv42) + Vv63*complexconjugate(Vv43))*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21))', 
	 order = {'QED':1} ) 
 
GC_1167 = Coupling(name = 'GC_1167',
	 value = '1./2.*complex(0,1)*(Vv41*complexconjugate(Vv61) + Vv42*complexconjugate(Vv62) + Vv43*complexconjugate(Vv63))*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21))', 
	 order = {'QED':1} ) 
 
GC_1168 = Coupling(name = 'GC_1168',
	 value = '-1./2.*complex(0,1)*(Vv51*complexconjugate(Vv51) + Vv52*complexconjugate(Vv52) + Vv53*complexconjugate(Vv53))*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21))', 
	 order = {'QED':1} ) 
 
GC_1169 = Coupling(name = 'GC_1169',
	 value = '1./2.*complex(0,1)*(Vv51*complexconjugate(Vv51) + Vv52*complexconjugate(Vv52) + Vv53*complexconjugate(Vv53))*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21))', 
	 order = {'QED':1} ) 
 
GC_1170 = Coupling(name = 'GC_1170',
	 value = '-1./2.*complex(0,1)*(Vv61*complexconjugate(Vv51) + Vv62*complexconjugate(Vv52) + Vv63*complexconjugate(Vv53))*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21))', 
	 order = {'QED':1} ) 
 
GC_1171 = Coupling(name = 'GC_1171',
	 value = '1./2.*complex(0,1)*(Vv51*complexconjugate(Vv61) + Vv52*complexconjugate(Vv62) + Vv53*complexconjugate(Vv63))*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21))', 
	 order = {'QED':1} ) 
 
GC_1172 = Coupling(name = 'GC_1172',
	 value = '-1./2.*complex(0,1)*(Vv61*complexconjugate(Vv61) + Vv62*complexconjugate(Vv62) + Vv63*complexconjugate(Vv63))*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21))', 
	 order = {'QED':1} ) 
 
GC_1173 = Coupling(name = 'GC_1173',
	 value = '1./2.*complex(0,1)*(Vv61*complexconjugate(Vv61) + Vv62*complexconjugate(Vv62) + Vv63*complexconjugate(Vv63))*(g1*complexconjugate(ZZ11) - g2*complexconjugate(ZZ21))', 
	 order = {'QED':1} ) 
 
GC_1174 = Coupling(name = 'GC_1174',
	 value = '-1./2.*complex(0,1)*(Vv11*complexconjugate(Vv11) + Vv12*complexconjugate(Vv12) + Vv13*complexconjugate(Vv13))*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_1175 = Coupling(name = 'GC_1175',
	 value = '1./2.*complex(0,1)*(Vv11*complexconjugate(Vv11) + Vv12*complexconjugate(Vv12) + Vv13*complexconjugate(Vv13))*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_1176 = Coupling(name = 'GC_1176',
	 value = '-1./2.*complex(0,1)*(Vv21*complexconjugate(Vv11) + Vv22*complexconjugate(Vv12) + Vv23*complexconjugate(Vv13))*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_1177 = Coupling(name = 'GC_1177',
	 value = '1./2.*complex(0,1)*(Vv11*complexconjugate(Vv21) + Vv12*complexconjugate(Vv22) + Vv13*complexconjugate(Vv23))*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_1178 = Coupling(name = 'GC_1178',
	 value = '-1./2.*complex(0,1)*(Vv31*complexconjugate(Vv11) + Vv32*complexconjugate(Vv12) + Vv33*complexconjugate(Vv13))*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_1179 = Coupling(name = 'GC_1179',
	 value = '1./2.*complex(0,1)*(Vv11*complexconjugate(Vv31) + Vv12*complexconjugate(Vv32) + Vv13*complexconjugate(Vv33))*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_1180 = Coupling(name = 'GC_1180',
	 value = '-1./2.*complex(0,1)*(Vv41*complexconjugate(Vv11) + Vv42*complexconjugate(Vv12) + Vv43*complexconjugate(Vv13))*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_1181 = Coupling(name = 'GC_1181',
	 value = '1./2.*complex(0,1)*(Vv11*complexconjugate(Vv41) + Vv12*complexconjugate(Vv42) + Vv13*complexconjugate(Vv43))*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_1182 = Coupling(name = 'GC_1182',
	 value = '-1./2.*complex(0,1)*(Vv51*complexconjugate(Vv11) + Vv52*complexconjugate(Vv12) + Vv53*complexconjugate(Vv13))*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_1183 = Coupling(name = 'GC_1183',
	 value = '1./2.*complex(0,1)*(Vv11*complexconjugate(Vv51) + Vv12*complexconjugate(Vv52) + Vv13*complexconjugate(Vv53))*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_1184 = Coupling(name = 'GC_1184',
	 value = '-1./2.*complex(0,1)*(Vv61*complexconjugate(Vv11) + Vv62*complexconjugate(Vv12) + Vv63*complexconjugate(Vv13))*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_1185 = Coupling(name = 'GC_1185',
	 value = '1./2.*complex(0,1)*(Vv11*complexconjugate(Vv61) + Vv12*complexconjugate(Vv62) + Vv13*complexconjugate(Vv63))*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_1186 = Coupling(name = 'GC_1186',
	 value = '-1./2.*complex(0,1)*(Vv21*complexconjugate(Vv21) + Vv22*complexconjugate(Vv22) + Vv23*complexconjugate(Vv23))*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_1187 = Coupling(name = 'GC_1187',
	 value = '1./2.*complex(0,1)*(Vv21*complexconjugate(Vv21) + Vv22*complexconjugate(Vv22) + Vv23*complexconjugate(Vv23))*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_1188 = Coupling(name = 'GC_1188',
	 value = '-1./2.*complex(0,1)*(Vv31*complexconjugate(Vv21) + Vv32*complexconjugate(Vv22) + Vv33*complexconjugate(Vv23))*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_1189 = Coupling(name = 'GC_1189',
	 value = '1./2.*complex(0,1)*(Vv21*complexconjugate(Vv31) + Vv22*complexconjugate(Vv32) + Vv23*complexconjugate(Vv33))*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_1190 = Coupling(name = 'GC_1190',
	 value = '-1./2.*complex(0,1)*(Vv41*complexconjugate(Vv21) + Vv42*complexconjugate(Vv22) + Vv43*complexconjugate(Vv23))*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_1191 = Coupling(name = 'GC_1191',
	 value = '1./2.*complex(0,1)*(Vv21*complexconjugate(Vv41) + Vv22*complexconjugate(Vv42) + Vv23*complexconjugate(Vv43))*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_1192 = Coupling(name = 'GC_1192',
	 value = '-1./2.*complex(0,1)*(Vv51*complexconjugate(Vv21) + Vv52*complexconjugate(Vv22) + Vv53*complexconjugate(Vv23))*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_1193 = Coupling(name = 'GC_1193',
	 value = '1./2.*complex(0,1)*(Vv21*complexconjugate(Vv51) + Vv22*complexconjugate(Vv52) + Vv23*complexconjugate(Vv53))*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_1194 = Coupling(name = 'GC_1194',
	 value = '-1./2.*complex(0,1)*(Vv61*complexconjugate(Vv21) + Vv62*complexconjugate(Vv22) + Vv63*complexconjugate(Vv23))*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_1195 = Coupling(name = 'GC_1195',
	 value = '1./2.*complex(0,1)*(Vv21*complexconjugate(Vv61) + Vv22*complexconjugate(Vv62) + Vv23*complexconjugate(Vv63))*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_1196 = Coupling(name = 'GC_1196',
	 value = '-1./2.*complex(0,1)*(Vv31*complexconjugate(Vv31) + Vv32*complexconjugate(Vv32) + Vv33*complexconjugate(Vv33))*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_1197 = Coupling(name = 'GC_1197',
	 value = '1./2.*complex(0,1)*(Vv31*complexconjugate(Vv31) + Vv32*complexconjugate(Vv32) + Vv33*complexconjugate(Vv33))*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_1198 = Coupling(name = 'GC_1198',
	 value = '-1./2.*complex(0,1)*(Vv41*complexconjugate(Vv31) + Vv42*complexconjugate(Vv32) + Vv43*complexconjugate(Vv33))*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_1199 = Coupling(name = 'GC_1199',
	 value = '1./2.*complex(0,1)*(Vv31*complexconjugate(Vv41) + Vv32*complexconjugate(Vv42) + Vv33*complexconjugate(Vv43))*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_1200 = Coupling(name = 'GC_1200',
	 value = '-1./2.*complex(0,1)*(Vv51*complexconjugate(Vv31) + Vv52*complexconjugate(Vv32) + Vv53*complexconjugate(Vv33))*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_1201 = Coupling(name = 'GC_1201',
	 value = '1./2.*complex(0,1)*(Vv31*complexconjugate(Vv51) + Vv32*complexconjugate(Vv52) + Vv33*complexconjugate(Vv53))*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_1202 = Coupling(name = 'GC_1202',
	 value = '-1./2.*complex(0,1)*(Vv61*complexconjugate(Vv31) + Vv62*complexconjugate(Vv32) + Vv63*complexconjugate(Vv33))*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_1203 = Coupling(name = 'GC_1203',
	 value = '1./2.*complex(0,1)*(Vv31*complexconjugate(Vv61) + Vv32*complexconjugate(Vv62) + Vv33*complexconjugate(Vv63))*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_1204 = Coupling(name = 'GC_1204',
	 value = '-1./2.*complex(0,1)*(Vv41*complexconjugate(Vv41) + Vv42*complexconjugate(Vv42) + Vv43*complexconjugate(Vv43))*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_1205 = Coupling(name = 'GC_1205',
	 value = '1./2.*complex(0,1)*(Vv41*complexconjugate(Vv41) + Vv42*complexconjugate(Vv42) + Vv43*complexconjugate(Vv43))*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_1206 = Coupling(name = 'GC_1206',
	 value = '-1./2.*complex(0,1)*(Vv51*complexconjugate(Vv41) + Vv52*complexconjugate(Vv42) + Vv53*complexconjugate(Vv43))*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_1207 = Coupling(name = 'GC_1207',
	 value = '1./2.*complex(0,1)*(Vv41*complexconjugate(Vv51) + Vv42*complexconjugate(Vv52) + Vv43*complexconjugate(Vv53))*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_1208 = Coupling(name = 'GC_1208',
	 value = '-1./2.*complex(0,1)*(Vv61*complexconjugate(Vv41) + Vv62*complexconjugate(Vv42) + Vv63*complexconjugate(Vv43))*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_1209 = Coupling(name = 'GC_1209',
	 value = '1./2.*complex(0,1)*(Vv41*complexconjugate(Vv61) + Vv42*complexconjugate(Vv62) + Vv43*complexconjugate(Vv63))*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_1210 = Coupling(name = 'GC_1210',
	 value = '-1./2.*complex(0,1)*(Vv51*complexconjugate(Vv51) + Vv52*complexconjugate(Vv52) + Vv53*complexconjugate(Vv53))*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_1211 = Coupling(name = 'GC_1211',
	 value = '1./2.*complex(0,1)*(Vv51*complexconjugate(Vv51) + Vv52*complexconjugate(Vv52) + Vv53*complexconjugate(Vv53))*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_1212 = Coupling(name = 'GC_1212',
	 value = '-1./2.*complex(0,1)*(Vv61*complexconjugate(Vv51) + Vv62*complexconjugate(Vv52) + Vv63*complexconjugate(Vv53))*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_1213 = Coupling(name = 'GC_1213',
	 value = '1./2.*complex(0,1)*(Vv51*complexconjugate(Vv61) + Vv52*complexconjugate(Vv62) + Vv53*complexconjugate(Vv63))*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_1214 = Coupling(name = 'GC_1214',
	 value = '-1./2.*complex(0,1)*(Vv61*complexconjugate(Vv61) + Vv62*complexconjugate(Vv62) + Vv63*complexconjugate(Vv63))*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_1215 = Coupling(name = 'GC_1215',
	 value = '1./2.*complex(0,1)*(Vv61*complexconjugate(Vv61) + Vv62*complexconjugate(Vv62) + Vv63*complexconjugate(Vv63))*(g1*complexconjugate(ZZ12) - g2*complexconjugate(ZZ22))', 
	 order = {'QED':1} ) 
 
GC_1216 = Coupling(name = 'GC_1216',
	 value = '(1*complex(0,1)*g2*(Vv11*complexconjugate(ZEL11) + Vv12*complexconjugate(ZEL12) + Vv13*complexconjugate(ZEL13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1217 = Coupling(name = 'GC_1217',
	 value = '(1*complex(0,1)*g2*(Vv21*complexconjugate(ZEL11) + Vv22*complexconjugate(ZEL12) + Vv23*complexconjugate(ZEL13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1218 = Coupling(name = 'GC_1218',
	 value = '(1*complex(0,1)*g2*(Vv31*complexconjugate(ZEL11) + Vv32*complexconjugate(ZEL12) + Vv33*complexconjugate(ZEL13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1219 = Coupling(name = 'GC_1219',
	 value = '(1*complex(0,1)*g2*(Vv41*complexconjugate(ZEL11) + Vv42*complexconjugate(ZEL12) + Vv43*complexconjugate(ZEL13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1220 = Coupling(name = 'GC_1220',
	 value = '(1*complex(0,1)*g2*(Vv51*complexconjugate(ZEL11) + Vv52*complexconjugate(ZEL12) + Vv53*complexconjugate(ZEL13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1221 = Coupling(name = 'GC_1221',
	 value = '(1*complex(0,1)*g2*(Vv61*complexconjugate(ZEL11) + Vv62*complexconjugate(ZEL12) + Vv63*complexconjugate(ZEL13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1222 = Coupling(name = 'GC_1222',
	 value = '(1*complex(0,1)*g2*(Vv11*complexconjugate(ZEL21) + Vv12*complexconjugate(ZEL22) + Vv13*complexconjugate(ZEL23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1223 = Coupling(name = 'GC_1223',
	 value = '(1*complex(0,1)*g2*(Vv21*complexconjugate(ZEL21) + Vv22*complexconjugate(ZEL22) + Vv23*complexconjugate(ZEL23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1224 = Coupling(name = 'GC_1224',
	 value = '(1*complex(0,1)*g2*(Vv31*complexconjugate(ZEL21) + Vv32*complexconjugate(ZEL22) + Vv33*complexconjugate(ZEL23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1225 = Coupling(name = 'GC_1225',
	 value = '(1*complex(0,1)*g2*(Vv41*complexconjugate(ZEL21) + Vv42*complexconjugate(ZEL22) + Vv43*complexconjugate(ZEL23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1226 = Coupling(name = 'GC_1226',
	 value = '(1*complex(0,1)*g2*(Vv51*complexconjugate(ZEL21) + Vv52*complexconjugate(ZEL22) + Vv53*complexconjugate(ZEL23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1227 = Coupling(name = 'GC_1227',
	 value = '(1*complex(0,1)*g2*(Vv61*complexconjugate(ZEL21) + Vv62*complexconjugate(ZEL22) + Vv63*complexconjugate(ZEL23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1228 = Coupling(name = 'GC_1228',
	 value = '(1*complex(0,1)*g2*(Vv11*complexconjugate(ZEL31) + Vv12*complexconjugate(ZEL32) + Vv13*complexconjugate(ZEL33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1229 = Coupling(name = 'GC_1229',
	 value = '(1*complex(0,1)*g2*(Vv21*complexconjugate(ZEL31) + Vv22*complexconjugate(ZEL32) + Vv23*complexconjugate(ZEL33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1230 = Coupling(name = 'GC_1230',
	 value = '(1*complex(0,1)*g2*(Vv31*complexconjugate(ZEL31) + Vv32*complexconjugate(ZEL32) + Vv33*complexconjugate(ZEL33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1231 = Coupling(name = 'GC_1231',
	 value = '(1*complex(0,1)*g2*(Vv41*complexconjugate(ZEL31) + Vv42*complexconjugate(ZEL32) + Vv43*complexconjugate(ZEL33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1232 = Coupling(name = 'GC_1232',
	 value = '(1*complex(0,1)*g2*(Vv51*complexconjugate(ZEL31) + Vv52*complexconjugate(ZEL32) + Vv53*complexconjugate(ZEL33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1233 = Coupling(name = 'GC_1233',
	 value = '(1*complex(0,1)*g2*(Vv61*complexconjugate(ZEL31) + Vv62*complexconjugate(ZEL32) + Vv63*complexconjugate(ZEL33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_1234 = Coupling(name = 'GC_1234',
	 value = 'G', 
	 order = {'QCD':1} ) 
 
GC_1235 = Coupling(name = 'GC_1235',
	 value = '-1*complex(0,1)*g2*complexconjugate(ZZ21)', 
	 order = {'QED':1} ) 
 
GC_1236 = Coupling(name = 'GC_1236',
	 value = '1*complex(0,1)*g2*complexconjugate(ZZ22)', 
	 order = {'QED':1} ) 
 
GC_1237 = Coupling(name = 'GC_1237',
	 value = '-1*complex(0,1)*G**2', 
	 order = {'QCD':2} ) 
 
GC_1238 = Coupling(name = 'GC_1238',
	 value = '-1*complex(0,1)*G**2', 
	 order = {'QCD':2} ) 
 
GC_1239 = Coupling(name = 'GC_1239',
	 value = '1*complex(0,1)*G**2', 
	 order = {'QCD':2} ) 
 
GC_1240 = Coupling(name = 'GC_1240',
	 value = '-1*complex(0,1)*G**2', 
	 order = {'QCD':2} ) 
 
GC_1241 = Coupling(name = 'GC_1241',
	 value = '1*complex(0,1)*G**2', 
	 order = {'QCD':2} ) 
 
GC_1242 = Coupling(name = 'GC_1242',
	 value = '1*complex(0,1)*G**2', 
	 order = {'QCD':2} ) 
 
GC_1243 = Coupling(name = 'GC_1243',
	 value = '1*complex(0,1)*g2**2*complexconjugate(ZZ21)**2', 
	 order = {'QED':2} ) 
 
GC_1244 = Coupling(name = 'GC_1244',
	 value = '1*complex(0,1)*g2**2*complexconjugate(ZZ21)**2', 
	 order = {'QED':2} ) 
 
GC_1245 = Coupling(name = 'GC_1245',
	 value = '-2*complex(0,1)*g2**2*complexconjugate(ZZ21)**2', 
	 order = {'QED':2} ) 
 
GC_1246 = Coupling(name = 'GC_1246',
	 value = '1*complex(0,1)*g2**2*complexconjugate(ZZ21)*complexconjugate(ZZ22)', 
	 order = {'QED':2} ) 
 
GC_1247 = Coupling(name = 'GC_1247',
	 value = '-2*complex(0,1)*g2**2*complexconjugate(ZZ21)*complexconjugate(ZZ22)', 
	 order = {'QED':2} ) 
 
GC_1248 = Coupling(name = 'GC_1248',
	 value = '1*complex(0,1)*g2**2*complexconjugate(ZZ21)*complexconjugate(ZZ22)', 
	 order = {'QED':2} ) 
 
GC_1249 = Coupling(name = 'GC_1249',
	 value = '2*complex(0,1)*g2**2', 
	 order = {'QED':2} ) 
 
GC_1250 = Coupling(name = 'GC_1250',
	 value = '-1*complex(0,1)*g2**2', 
	 order = {'QED':2} ) 
 
GC_1251 = Coupling(name = 'GC_1251',
	 value = '-1*complex(0,1)*g2**2', 
	 order = {'QED':2} ) 
 
GC_1252 = Coupling(name = 'GC_1252',
	 value = '-2*complex(0,1)*g2**2*complexconjugate(ZZ22)**2', 
	 order = {'QED':2} ) 
 
GC_1253 = Coupling(name = 'GC_1253',
	 value = '1*complex(0,1)*g2**2*complexconjugate(ZZ22)**2', 
	 order = {'QED':2} ) 
 
GC_1254 = Coupling(name = 'GC_1254',
	 value = '1*complex(0,1)*g2**2*complexconjugate(ZZ22)**2', 
	 order = {'QED':2} ) 
 
GC_1255=Coupling(name='GC_1255',
	 value='-(HPP1*complex(0,1))', 
	 order={'HIW':1})

GC_1256=Coupling(name='GC_1256',
	 value='-(HGG1*complex(0,1))', 
	 order={'HIG':1})

GC_1257=Coupling(name='GC_1257',
	 value='-(HPP2*complex(0,1))', 
	 order={'HIW':1})

GC_1258=Coupling(name='GC_1258',
	 value='-(HGG2*complex(0,1))', 
	 order={'HIG':1})

GC_1259=Coupling(name='GC_1259',
	 value='-(HPP3*complex(0,1))', 
	 order={'HIW':1})

GC_1260=Coupling(name='GC_1260',
	 value='-(HGG3*complex(0,1))', 
	 order={'HIG':1})

GC_1261=Coupling(name='GC_1261',
	 value='-(APP2*complex(0,1))', 
	 order={'HIW':1})

GC_1262=Coupling(name='GC_1262',
	 value='-(AGG2*complex(0,1))', 
	 order={'HIG':1})

GC_1263=Coupling(name='GC_1263',
	 value='-(APP3*complex(0,1))', 
	 order={'HIW':1})

GC_1264=Coupling(name='GC_1264',
	 value='-(AGG3*complex(0,1))', 
	 order={'HIG':1})

