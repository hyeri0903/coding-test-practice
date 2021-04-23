#include <string>
#include <vector>
#include <algorithm>

using namespace std;
int answer=999;

int diff(string a, string b){
    int cnt = 0;
    
    for(int i=0; i<a.size(); i++){
        if(a[i] != b[i]){
            cnt++;
        }
    }
    return cnt;
}

void dfs(int cnt, int visit[51], string begin, string target, vector<string>& words){
    for(int i=0; i<words.size(); i++){
        int dist = 0;
        if(!visit[i]){
            dist=diff(begin, words[i]);
        }
        if(dist == 1){
            if(words[i] == target && answer > cnt+1)
            {
                answer = cnt + 1;
                return;
            }
            visit[i] = 1;
            dfs(cnt+1, visit, words[i], target, words);
            visit[i] = 0;
        }
    }
    
}

int solution(string begin, string target, vector<string> words) {
    bool ok = false;
    //첫문자와 target 동일하면 0 리턴
    if(begin == target)
        return 0;
    //words에 target이 존재하지않으면 0 리턴
    for(int i=0; i<words.size(); i++){
        if(words[i]==target){
            ok = true;
            break;
        }
    }
    if(!ok)
        return 0;
    
    int visit[51] = {0};
    dfs(0, visit, begin, target, words);
    
    return answer;
}
