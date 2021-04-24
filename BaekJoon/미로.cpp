#include <iostream>
#include <vector>
#include <algorithm>
#include <string.h>
using namespace std;
/*
0: 길
1: 벽
2: 출발점
3: 돛가점
가능여부 출력- 가능 : 1, 불가능: 0
*/
int n, m;
int dir[4][2] = { {0,1}, {0,-1}, {-1,0}, {1,0} };
int arr[17][17] = { 0 };
int visit[17][17] = { 0 };
int answer = 0;

void dfs(int y, int x) {
	if (arr[y][x] == 3) {
		answer = 1;
		return;
	}
	for (int i = 0; i < 4; i++) {
		int ny = y + dir[i][0];
		int nx = x + dir[i][1];

		if (ny < 0 || ny >= n || nx < 0 || nx >= m)
			continue;
		if (arr[ny][nx] != 1 && !visit[ny][nx]) {
			visit[y][x] = 1;
			dfs(ny, nx);
			visit[y][x] = 0;
		}
	}
}

int main() {
	//freopen("input.txt", "r", stdin);

	n = 16; m = 16;
	int T = 10;
	int tc;

	while (T--)
	{
		answer = 0; int sy, sx;
		memset(arr, 0, sizeof(arr));
		scanf("%d", &tc);

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				scanf("%1d", &arr[i][j]);
				if (arr[i][j] == 2) {
					sy = i;
					sx = j;
				}
			}
		}

		dfs(sy, sx);
		
		printf("#%d %d\n", tc, answer);

	}
	
	
	return 0;
}
