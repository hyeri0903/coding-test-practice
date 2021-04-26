#include <algorithm>
#include <iostream>
#include <vector>
#include <string>

int solution(int N) {
    string str = "";
    int answer = -1;

    while(N>0){
        if(N%2 == 1){
            str += '1';
        }
        else{
            str += '0';
        }
        N = N/2;
    }
    reverse(str.begin(), str.end());

    bool ok = false;
    int cnt = 0;
    int idx = 1;
    int size = str.size();
    while(idx < size){
        if(str[idx] == '0' && str[idx-1] == '1'){
            while(str[idx] == '0'){
                cnt++;
                idx++;
            }
            if(str[idx]=='1')
            {
                ok = true;
                answer = max(cnt,  answer);
            }
            cnt = 0;
            ok = false;
        }
        idx++;
    }
    if(answer == -1)
        answer = 0;
    return answer;
}
