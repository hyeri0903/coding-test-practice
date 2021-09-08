#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
/*
# 승률 높은 순
# 무거운 복서 이긴 횟수 많은 순
# 자기 몸무게가 무거운 순
# 작은 번호 순
*/
using namespace std;

typedef struct{
    float rate;  //승률
    int win_heavy_cnt; //자기보다 무거운 복서를 이긴 횟수
    int weight; //자기 몸무게가 무거운 순
    int idx; //자기 번호가 작은 순
}Info;

bool cmp(Info a, Info b){
    if(a.rate == b.rate){
         if(a.win_heavy_cnt == b.win_heavy_cnt){
             if(a.weight == b.weight){
                return a.idx < b.idx;
            }
            return a.weight > b.weight;
        }
        return a.win_heavy_cnt > b.win_heavy_cnt;
    }
   
    return a.rate > b.rate;

}

vector<int> solution(vector<int> weights, vector<string> head2head) {
    int n = weights.size();
    vector<int> answer;
    vector<Info> result;
    
    for(int i=0; i<weights.size(); i++){
        float win_cnt = 0; //이긴 횟수
        int win_heavy_cnt = 0; //무거운 복서 이긴 횟수
        int play_cnt =0; //총 경기 횟수
        string cur = head2head[i];
        for(int j=0; j<cur.size(); j++){
            if(i == j)
                continue;
            if(cur[j] =='W'){
                win_cnt++;
                if(weights[i] < weights[j]){
                    win_heavy_cnt++;
                }
            }
            if(cur[j] != 'N')
                play_cnt++;
            
        }
        float rate = 0;
        if(play_cnt !=0)
            rate = win_cnt / play_cnt * 100;
        result.push_back({rate,win_heavy_cnt, weights[i], i+1});
        
    }
    
    sort(result.begin(), result.end(), cmp);
    
    for(Info x : result){
        //cout << x.idx << " " << x.rate << " " << x.win_heavy_cnt << " " << x.weight << " "<< endl;
        answer.push_back(x.idx);
    }

    return answer;
}
