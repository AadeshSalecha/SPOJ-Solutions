'''
Website   : SPOJ
Author    : Aadesh Salecha
Created   : September 2016
'''

while(True):
	try:
		n = input()
	except:
		break

	if n == 0 or n == 1:
		print n
	else:
		print n + (n - 2)