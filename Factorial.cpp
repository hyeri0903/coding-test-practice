#include <iostream>

using namespace std;

int dp[101] = { 0 };
 
// 1. 재귀함수 이용
int factorial(int n) {
	if (n == 1)
		return 1;
	else
		return n * factorial(n - 1);
}

// 2. 반복문 이용
void factorial2(int n) {
	int result = 1;
	for (int i = 1; i <= n; i++) {
		result = result * i;
	}
	cout << result << endl;
}

// 3. dp(memorize) 이용
int factorial3(int n) {
	if (dp[n] != 0) {
		return dp[n];
	}
	else if (n <= 1) {
		return 1;
	}
	else {
		dp[n] = n * factorial3(n - 1);
		return dp[n];
	}

	return n * factorial3(n - 1);
}

int main()
{
	//cout << factorial(5);
	//factorial2(5);
	cout << factorial3(5);
	return 0;
}
