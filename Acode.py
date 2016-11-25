'''
Website   : SPOJ
Author    : Aadesh Salecha
Created   : September 2016
'''
while(True):
	s = str(raw_input())
	if (s == '0'):
		break
	else:
		count = 0
		for i in range(len(s)-1):
			if int(s[i:i+2]) < 26:
				count += 1
		print count				