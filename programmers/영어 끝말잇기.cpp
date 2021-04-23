#include <string>
#include <vector>
#include <iostream>
#include <map>

using namespace std;

vector<int> solution(int n, vector<string> words) {
    vector<int> answer;
    map<int, int> people; //몇번째 사람이 몇번째 순서인지 체크
    map<string, int> word;  //말한단어 체크
    
    for(int i=0; i<n; i++)
        people[i] = 0;
    
    int num_person = 1;
    people[0] = 1;
    word[words[0]]=1;
    
    for(int i=1; i<words.size(); i++){
        string before = words[i-1];
        string cur = words[i];
        //앞 단어 마지막 문자와 다르면
        if(before[before.size()-1]!=cur[0]){
            answer.push_back(num_person+1);
            answer.push_back(people[num_person]+1);
            break;
        }//이미 나온 단어면
        else if(word[cur]>=1){
            answer.push_back(num_person+1);
            answer.push_back(people[num_person]+1);
            break;
        }//올바른 경우
        else{
            word[cur]=1; //나온단어면 1, 아니면 0
            people[num_person] += 1;
            num_person = (num_person+1)%n;
        }
    }
    //탈락자 없는 경우
    if(answer.size() <=0){
        answer.push_back(0);
        answer.push_back(0);
    }
    return answer;
}
