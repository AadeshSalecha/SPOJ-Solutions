'''
Website   : SPOJ
Author    : Aadesh Salecha
Created   : September 2016
'''
#
# Not Optimised
#
# while(True):
# 	n = input()
# 	if n == 0:
# 		break
# 	arr = map(int, str(raw_input()).split())

# 	result = list(arr)
# 	for i in range(len(arr)):
# 		result[arr[i]-1] = i+1

# 	print 'ambiguous' if result == arr else 'not ambiguous'

while(True):
	n = input()
	if n == 0:
		break
	arr = map(int , str(raw_input()).split())

	result1 = True
	result = [0] * n
	for i in range(n):
		result[arr[i]-1] = i+1
		if result[arr[i]-1] != arr[arr[i]-1]:
		 	print 'not ambiguous'
		 	result1 = False
		 	break
 
	#print result
	if result1:
		print 'ambiguous'