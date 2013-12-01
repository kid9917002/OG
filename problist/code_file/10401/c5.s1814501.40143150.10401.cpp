#include <iostream>
using namespace std;

inline void fib(int *list, int n) {
	list[0] = 1;
	list[1] = 2;
	for(int i = 2; i < n; i++) list[i] = list[i - 1] + list[i - 2];
}

int main() {
	char str[39];
	int i, j, k, n, sum, value, temp, list[38];
	fib(list, 38);
	cin >> n;
	for(i = 0; i < n; i++) {
		cin >> value;
		temp = value;
		sum = 0;
		for(j = 37; list[j] > value; j--);
		for(k = 0; j >= 0; j--)
			if(temp >= list[j]) {
				str[k++] = '1';
				sum += list[j];
				temp -= list[j];
			}
			else str[k++] = '0';
		str[k] = '\0';
		cout << value << " = " << str << " (fib)" << endl;
	}
}
