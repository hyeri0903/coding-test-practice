#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> island(101);

bool cmp(vector<int> a, vector<int> b){
    return a[2] < b[2];
}

int findParent(int idx){
    if(island[idx] == idx)
        return idx;
    return island[idx] = findParent(island[idx]);
}

int solution(int n, vector<vector<int>> costs) {
    int answer = 0;
    
    //섬 저장
    for(int i=0; i<n; i++){
        island[i] = i;
    }
    // 1. 비용이 적은순으로 정렬
    sort(costs.begin(), costs.end(), cmp);
    
    for(int i=0; i<costs.size(); i++){
        int start = findParent(costs[i][0]);
        int end = findParent(costs[i][1]);
        int cost = costs[i][2];
        
        //2. cycle이 만들어지지 않으면 다리 추가
        if(start!=end){
            answer+=cost;
            island[end] = start;
        }
        
    }
    

    return answer;
}
