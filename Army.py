'''
Website   : SPOJ
Author    : Aadesh Salecha
Created   : September 2016
'''
for i in range(input()):
	blank = str(raw_input())
	ng, nm = map(int, str(raw_input()).split())

	godzilla = sorted(map(int, str(raw_input()).split()))
	mecha = sorted(map(int, str(raw_input()).split()))

	weak_g = 0
	weak_m = 0

	while not(ng == 0 or nm == 0):
		if godzilla[weak_g] < mecha[weak_m]:
			ng -= 1
			weak_g += 1
		else:
			nm -= 1
			weak_m += 1
		#print godzilla[weak_g:], mecha[weak_m:], ng, nm

	print 'MechaGodzilla' if ng == 0 else 'Godzilla'
