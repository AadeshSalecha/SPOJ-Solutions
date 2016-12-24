# 
# Website   : SPOJ
# Author    : Aadesh Salecha
# Created   : September 2016
#
for i in range(input()):
	num_stalls ,num_cows = map(int, str(raw_input()).split())
	stalls = sorted(map(int, str(raw_input()).split())) #sorted([input() for i in range(num_stalls)])

	num = (max(stalls) + min(stalls)) / float(num_cows)
	for i in range(int(num_cows)):
		print i * num