# 
# Website   : SPOJ
# Author    : Aadesh Salecha
# Created   : September 2016
#
for i in range(input()):
	n, k = map(int ,str(raw_input()).split())
	students = map(int, str(raw_input()).split())
	students.sort()

	min_distance = students[-1] - students[0]
	# print k/2,len(students) - k/2
	for j in range(k/2,n - (k/2 - int(k % 2 == 0))):
		upper = students[(j+k/2) - int(k % 2 == 0)]
		lower = students[j-k/2]
		min_distance = min(min_distance, upper - lower)

	print min_distance