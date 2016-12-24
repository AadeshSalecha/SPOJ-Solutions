/*
# Website   : SPOJ
# Author    : Aadesh Salecha
# Created   : September 2016
#
/*
#include <stdio.h>
int main(void)
{
	int T, n, r, u;
	scanf("%d", &T);
	while(T--)
	{
		scanf("%d", &n);
		r = 0;
		u = int(n % 2 == 0);
		for(int i = 1; i < n+1; i++)
		{
			if (i == n)
				r += n * n;
			else
			{
				r += ((i * (i+1)) / 2);
				if (n > 3 and i % 2 == 0)
				{
					r += ((u * (u+1)) / 2);
					u += 2;
				}
			}
		}
		printf("%d\n", r);
	}
}
