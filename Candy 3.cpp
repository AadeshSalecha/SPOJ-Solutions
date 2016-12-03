// # 
// # Website   : SPOJ
// # Author    : Aadesh Salecha
// # Created   : September 2016
// #
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <cstdio>
#include <numeric>
using namespace std;

int main(void)
{
	unsigned long long T,n,s, tmp; cin >> T;
	while(T--)
	{
		cin >> n;
		s = 0;
		for(int i = 0; i < n; i++)
		{
			cin >> tmp; s = (s + tmp) % n;
		}
		if(s % n == 0)
			cout << "YES\n";
		else
			cout << "NO\n";	
	}
	return 0;
}