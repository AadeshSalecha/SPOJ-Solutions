// # 
// # Website   : SPOJ
// # Author    : Aadesh Salecha
// # Created   : September 2016
// #
#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;

int main(void)
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	 
	while(true)
	{
		int k; cin >> k;
		if(k == 0) break;
		string a, b; cin >> a >> b ;	
		pair<int,int> grid[b.size()+1][a.size()+1];
		
		for(int i = 0; i <= a.size(); i++)
			grid[b.size()][i] = make_pair(0,0);
		for(int i = 0; i <= b.size(); i++)
			grid[i][a.size()] = make_pair(0,0);
			
		for(int i = b.size()-1; i >= 0; i--)
			for(int j = a.size()-1; j >= 0; j--)
			{
				if(b[i] == a[j])
					grid[i][j] = make_pair(1 + grid[i+1][j+1].first, grid[i+1][j+1].second+1);
				else if(i == b.size()-1 and j == a.size()-1)
					grid[i][j] = make_pair(0, 0);
				else
				{
					if(grid[i+1][j].first > grid[i][j+1].first)
					{
						if(grid[i+1][j].second < k and grid[i+1][j].second != 0)
							grid[i][j] = make_pair(0, 0);
						else
							grid[i][j] = make_pair(grid[i+1][j].first, 0);	
					}
					else
					{
						if(grid[i][j+1].second < k and grid[i][j+1].second != 0)
							grid[i][j] = make_pair(0, 0);
						else
							grid[i][j] = make_pair(grid[i][j+1].first, 0);
					}
				}
			}
		
		cout << a << endl;	
		for(int i = 0; i < b.size()+1; i++)
		{
			cout << b[i] << " ";
			for(int j = 0; j < a.size()+1; j++)
				cout << grid[i][j].first << " " << grid[i][j].second << "   ";
			cout << endl;
		}
	
		cout << grid[0][0].first << endl;
	}
}
