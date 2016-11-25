/*
Website   : SPOJ
Author    : Aadesh Salecha
Created   : September 2016
*/
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <cstdio>
#include <numeric>
using namespace std;

int main(void)
{
	int n;cin >> n;
	if(n % 10 == 0)
		cout << 2 << endl;
	else
		cout << 1 << endl << n % 10 << endl;
	return 0;
}