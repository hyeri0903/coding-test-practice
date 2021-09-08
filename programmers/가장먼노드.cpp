#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <queue>

using namespace std;

int solution(int n, vector<vector<int>> edge) {
    int answer = 0;
    vector<vector<int>> graph(n+1, vector<int>());
    vector<int> dist(n+1, 0);
    vector<bool> visit(n+1, false);
    queue<int> q;
    
    sort(edge.begin(), edge.end());
    // 양방향 그래프이므로 연결 정보 저장
    for(int i=0; i<edge.size(); i++){
        graph[edge[i][0]].push_back(edge[i][1]);
        graph[edge[i][1]].push_back(edge[i][0]);
    }
    
    q.push(1); //1에서부터 시작
    dist[1] = 0;
    visit[1] = true;
    while(!q.empty()){
        int cur = q.front();
        q.pop();
        
        for(int i=0; i<graph[cur].size(); i++){
            int v = graph[cur][i];
            if(!visit[v]){
                dist[v] = dist[cur]+1;
                visit[v] = true;
                q.push(v);
            }
        }

    }
    int max_val =0;
    for(int i=1; i<=n; i++){
        if(max_val < dist[i]){
            max_val = dist[i];
        }
    }
    
    for(int i=1; i<=n; i++){
        if(max_val == dist[i]){
            answer++;
        }
    }
    
    return answer;
}
