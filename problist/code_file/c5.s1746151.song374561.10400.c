#include <stdio.h>

long long int countlen(long long int k);

main()
{
	int m,n;
	int i;
	int max;
	int temp;
	while(scanf("%d %d",&m,&n)!=EOF){
		if (m > n){
			max = countlen(n);
			for (i = n+1; i <= m ; i++){
				temp = countlen(i);
				if (max < temp)
					max = temp;
			}
		}
		else{
			max = countlen(m);
			for (i = m+1 ; i <= n; i++){
				temp = countlen(i);
				if (max < temp)
					max = temp;
			}
		}
		printf("%d %d %d\n",m,n,max);
	}
	return 0;
}

long long int countlen(long long int k)
{
	long long int count=0;
	while(k != 1){
		if (k % 2 == 0){
			k /= 2;
		}
		else{
			k = 3*k+1;
		}
		count++;
	}
	return count+1;
}