/*# 
# Website   : SPOJ
# Author    : Aadesh Salecha
# Created   : September 2016
#
*/
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <cstdio>
#include <numeric>
using namespace std;

const long long int MOD = 1000007;
int main(void)
{
	long long T, n, s; cin >> T;
	while(T--)
	{
		s = 0;
		cin >> n;
		cout << ((n*(n+1)) + ((n * (n-1))/2)) % MOD << endl;
	}
	return 0;
}