def solution(word):
    answer = 0
    cnt = 781
    ch = ['A', 'E', 'I', 'O', 'U']
    
    for i in range(len(word)):
        for j in range(len(ch)):
            if word[i] == ch[j]:
                answer += 1 + j*cnt
        cnt = (cnt-1)/5
    return answer
