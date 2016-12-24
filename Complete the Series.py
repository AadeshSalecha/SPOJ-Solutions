# 
# Website   : SPOJ
# Author    : Aadesh Salecha
# Created   : September 2016
#
for i in range(input()):
	T3, LastL3, Sn = map(float, str(raw_input()).split())
	n = int(2 * (Sn / (T3 + LastL3)))
	try:
		d = (LastL3 - T3) / (n - 5)
	except:
		d = 0

	a = T3 - (2 * d)
	
	print n
	print ' '.join([str(int(a + (i * d))) for i in range(n)])
