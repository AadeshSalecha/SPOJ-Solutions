'''
Website   : SPOJ
Author    : Aadesh Salecha
Created   : September 2016
'''
while(True):
	num = input()
	if num == -1:
		break

	count = 1
	level = 1
	while (True):
		if level == num:
			print 'Y'
			break
		if level > num:
			print 'N'
			break
		level += 6 * (count)
		count += 1
