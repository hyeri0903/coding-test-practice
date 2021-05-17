#include <algorithm>
#include <iostream>
#include <vector>
#include <map>

int answer = 0;

int solution(vector<int> &A) {
    int n = A.size();
    map<int, int> leader_cnt;
    int leader = 0;
    int max_val = 0;

    if(n == 0){
        return -1;
    }
    if(n==1){
        return 0;
    }

    for(int i=0; i<n; i++){
        leader_cnt[A[i]] += 1;
        if(max_val < leader_cnt[A[i]]){
            max_val = leader_cnt[A[i]];
            leader = A[i];
        }
    }
    if(max_val <= n/2){
        return 0;
    }
    int left_cnt = 0;
    int right_cnt = leader_cnt[leader];

    for(int i =0; i<n; i++){
        if(A[i] == leader){
            left_cnt++;
            right_cnt--;
        }
        //양쪽 모두 leader 일 경우
        if(right_cnt > (n-(i+1))/2 && left_cnt > (i+1)/2){
            answer++;
        }
    }

    return answer;
}


