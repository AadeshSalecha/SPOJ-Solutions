'''
Website   : SPOJ
Author    : Aadesh Salecha
Created   : September 2016
'''
for i in range(int(raw_input())):
	tmp = str(raw_input()).split()
	while (tmp == []):
		tmp = str(raw_input()).split()

	equation = tmp
	equation = [equation[0], equation[2], equation[4]]
	
	if 'machula' in equation[2].lower() :
		print equation[0],'+',equation[1],'=',int(equation[0])+int(equation[1])
	elif 'machula' in equation[1].lower():
		print equation[0],'+',int(equation[2])-int(equation[0]),'=',equation[2]
	else:
		print int(equation[2])-int(equation[1]),'+',equation[1],'=',equation[2]