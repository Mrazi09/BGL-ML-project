import model THDMSBGL -modelname
define j = u1 u2 d1 d2 d1bar d2bar u1bar u2bar d3 d3bar
define p = u1 u2 d1 d2 u1bar u2bar d1bar d2bar
define l+ = e1bar e2bar
define l- = e1 e2
generate p p > h2 ah2, (ah2 > j j), (h2 > z ah2, z > l+ l-, ah2 > j j)
output 1-BGL_signal
exit



