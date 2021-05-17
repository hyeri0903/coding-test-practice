#include <algorithm>
#include <iostream>
#include <vector>
#include <map>

bool cmp(pair<int, int> a, pair<int, int> b){
    vector<int> answer;

    if(a.second == b.second){
        return a.first < b.first;
    }
    return a.second > b.second;
}

int solution(vector<int> &A) {
    int n = A.size();

    if(n == 0){
        return -1;
    }
    if(n==1){
        return 0;
    }

    map<int, int> m;
    for(int i=0; i<n; i++){
        m[A[i]]+=1;
    }

    vector<pair<int, int>> v(m.begin(), m.end());
    sort(v.begin(), v.end(), cmp);

    // for(int i=0; i<v.size(); i++){
    //     cout << v[i].first << " " << v[i].second << endl;
    // }
    
    if(v[0].second <= n/2)
    {
        return -1;
    }
    int dominator = v[0].first;
    for(int i=0; i<n; i++){
        if(A[i] == dominator){
            return i;
        }
    }
    return -1;
}
