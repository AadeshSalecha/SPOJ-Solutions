# 
# Website   : SPOJ
# Author    : Aadesh Salecha
# Created   : September 2016
#
for i in range(input()):
	s = str(raw_input())
	length = len(s)
	subsets = set([])

	for i in range(length):
		for j in range(i, length):
			subsets.add(s[i:j+1])

	print len(subsets)