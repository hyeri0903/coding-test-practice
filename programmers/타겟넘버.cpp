#include <string>
#include <vector>

using namespace std;
int answer;

void dfs(vector<int> &numbers, int target, int idx, int total){
    if(idx >= numbers.size()){
        if(target == total){
            answer++;
        }
        return;
    }
    dfs(numbers, target, idx+1, total-numbers[idx]);
    dfs(numbers, target, idx+1, total+numbers[idx]);
}

int solution(vector<int> numbers, int target) {
    answer = 0;
    int size = numbers.size();
    
    dfs(numbers, target, 0, 0);
    
    return answer;
}
