# 
# Website   : SPOJ
# Author    : Aadesh Salecha
# Created   : September 2016
#
n = input()
arr = map(int, str(raw_input()).split())
for i in range(input()):
	a, b = map(int, str(raw_input()).split())
	print max(arr[a-1:b])