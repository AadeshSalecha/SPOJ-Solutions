// # 
// # Website   : SPOJ
// # Author    : Aadesh Salecha
// # Created   : September 2016
// #
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main(void)
{
	int T, n, k, tmp, min_distance, upper, lower;
	cin >> T;

	while (T--)
	{
		cin >> n >> k;
		vector <int> students;
		for(int i = 0; i < n; i++)
		{
			cin >> tmp;
			students.push_back(tmp);
		}

		sort(students.begin(), students.end());
		min_distance = students[n-1] - students[0];
		for(int i = k/2; i < n - (k/2 - int(k % 2 == 0)); i++)
		{
			upper = students[i + k/2 - int(k % 2 == 0)];
			lower = students[i - k/2];
			min_distance = min(min_distance, upper - lower);
		}

		cout << min_distance << endl;
	}
	return 0;
}
