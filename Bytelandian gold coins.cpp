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
#include <utility>
using namespace std;

long long byte(long long n, map<long long, long long>& memo)
{
	if(n == 1 || n == 2 || n == 3 || n == 4 || n == 0) return n;
	if(memo.find(n) != memo.end()) return memo[n];
	long long tmp = max(n, (byte(n/4, memo)+byte(n/3, memo)+byte(n/2, memo)));
	memo[n] = tmp;
	return tmp;
} 

int main(void)
{
	long long n;
	map<long long,long long> memo;
	while(cin >> n)
	{
		cout << byte(n, memo) << endl;
	}
	// for(map<long long, long long> :: iterator it = memo.begin(); it != memo.end(); it++)
	// 	cout << it->first << " " << it->second << endl;
	return 0;
}