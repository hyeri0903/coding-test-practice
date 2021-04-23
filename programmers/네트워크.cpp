#include <string>
#include <vector>

using namespace std;
int visit[201] = {0};

void dfs(int idx, int n, vector<vector<int>> &computers){
    visit[idx] = 1;
    
    for(int i=0; i<n; i++){
        if(!visit[i] && computers[idx][i]){
            dfs(i, n , computers);
        }
    }
}


int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
  
    for(int i=0; i<n; i++){
        if(!visit[i]){
            dfs(i, n, computers);
            answer++;
        }
    }
    
    return answer;
}
