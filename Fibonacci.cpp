#include <iostream>

using namespace std;

// 1.재귀함수
int fibo(int n) {
	if (n <= 1)
		return 1;

	else
		return fibo(n - 1) + fibo(n - 2);
}

// 2. 반복문
void fibo2(int n) {
	int total = 1;
	int before = 0;

	for (int i = 0; i < n; i++) {
		int tmp = total;
		total = before + total;
		before = tmp;
	}
	cout << total << endl;
}

// 3. dp(memorize)
int fibo3(int n) {
	int dp[10001] = { 0 };
	dp[0] = 1;
	dp[1] = 1;

	for (int i = 2; i <= n; i++) {
		dp[i] = dp[i - 1] + dp[i - 2];
	}
	return dp[n];
}

int main()
{
	// 1, 1, 2, 3, 5
	//cout << fibo(4) << endl;
	fibo2(4);
	//cout << fibo3(4) << endl;
		
	return 0;
}
