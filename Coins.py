# 
# Website   : SPOJ
# Author    : Aadesh Salecha
# Created   : September 2016
#
def maximise(coin, memo):
	if coin in memo:
		return memo[coin]
	else:
		half = coin / 2		
		third = coin / 3
		quater = coin / 4

		if half + third + quater > coin:
			memo[coin] = maximise(half, memo) + maximise(third, memo) + maximise(quater, memo)
			return memo[coin]
		else:
			memo[coin] = coin
			return memo[coin]			


memo = {}
while(True):
	try:
		coin = int(raw_input())
	except:
		break
	print maximise(coin, memo)	