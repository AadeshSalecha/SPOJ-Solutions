'''
Website   : SPOJ
Author    : Aadesh Salecha
Created   : September 2016
'''
def evaluate(equation):
	if equation[1] == '+':
		return int(equation[0]) + int(equation[2])
	elif equation[1] == '-':
		return int(equation[0]) - int(equation[2])
	elif equation[1] == '*':
		return int(equation[0]) * int(equation[2])
	elif equation[1] == '/':
		return int(equation[0]) / int(equation[2])
	return None		

for i in range(input()):
	str(raw_input());equation = str(raw_input()).split()[:-1]

	result = evaluate([equation[0], equation[1], equation[2]])
	for i in range(3, len(equation), 2):
		result = evaluate([result, equation[i], equation[i+1]])

	print result

