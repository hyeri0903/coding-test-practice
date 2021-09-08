#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

long long solution(int n, vector<int> times) {
    long long answer = 0;
    sort(times.begin(), times.end());
    long long min = 1; //최소 시간 1분
    long long max = (long long)(times[times.size()-1]) * n;   //가장 오래걸리는 경우(최악의 시간)
    long long total;
    long long mid;
    
    while(min <= max){
        mid = (min + max) / 2;
        total = 0;    //총 심사한 인원
        // 각 심사관이 심사하는 총 인원 구하기 -> 빨리 심사하는 순으로 처리
        for(int i=0; i<times.size(); i++){
            total += mid / times[i];
        }
        //1) 총 인원이 n명보다 작으면 더 많은 시간이 필요함.
        //2) 심사한 총 인원이 n명보다 많음 -> 시간을 줄여서 최소로해야 함
        if(total < n){
            min = mid+1;
        }else{
            max = mid-1;
            answer = mid;
        }
        
    }
    
    return answer;
}
