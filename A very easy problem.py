'''
Website   : SPOJ
Author    : Aadesh Salecha
Created   : September 2016
'''
def two_power(n):
	if n == 0:
		return '0'
	if n == 1:
		return '1' 
	if n == 2:
		return '2'

	binary_rep = (bin(n)[2:])[::-1]
	result = []

	for i in range(len(binary_rep)):
		if binary_rep[i] == '1':
			result.append('2(' + two_power(i) + ')')

	final = ''
	for i in result[::-1]:
		if i == '2(1)':
			final += ('2' + '+')
		else:
			final += (i + '+')

	return final[:-1]

print '137=' + two_power(137)
print '1315=' + two_power(1315)
print '73=' + two_power(73)
print '136=' + two_power(136)
print '255=' + two_power(255)
print '1384=' + two_power(1384)
print '16385=' + two_power(16385)