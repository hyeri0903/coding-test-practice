#include <iostream>
#include <vector>
#include <algorithm>
#include <string.h>
#define INF 9999999
using namespace std;

int arr[16][16];
int cost[16][1 << 16] = { 0 };
int visit[16] = { 0 };
int answer = 9999999;
int n;
int visit_all_bit;


int dfs(int cur, int cur_bit) {
	if (cur_bit == visit_all_bit) {
		if (arr[cur][0] == 0) {
			return INF;
		}
		else {
			//다 방문했으면 원점으로 돌아오는 cost 반환
			return arr[cur][0];
		}
	}

	if (cost[cur][cur_bit] != -1)
		return cost[cur][cur_bit];
	cost[cur][cur_bit] = INF;

	for (int i = 0; i < n; i++) {
		//길이 없거나 방문한 도시는 pass
		if (arr[cur][i] == 0)
			continue;
		if ( (cur_bit & (1 << i)) == (1 << i))
			continue;
		//최소 비용으로 갱신
		cost[cur][cur_bit] = min(cost[cur][cur_bit], arr[cur][i] + dfs(i, cur_bit | 1 << i));
	}
	return cost[cur][cur_bit];
}

int main()
{
	freopen("input.txt", "r", stdin);
	scanf("%d", &n);
	
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			scanf("%d", &arr[i][j]);
		}
	}
	visit_all_bit = (1 << n) - 1;

	memset(cost, -1, sizeof(cost));
	cout << dfs(0, 1) << endl;

	return 0;
}
