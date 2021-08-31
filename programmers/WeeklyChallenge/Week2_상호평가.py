#자기 자신(i) 평가점수가 유일한 최고점 or 최저점인지 확인
def check(i, arr, scores):
    min_val = min(arr)
    max_val = max(arr)
    my_score = scores[i][i]
    if(arr.count(min_val)==1 and my_score == min_val):
        arr.remove(min_val)
        return arr
    if(arr.count(max_val)==1 and my_score == max_val):
        arr.remove(max_val)
        return arr
    return arr
    

def solution(scores):
    answer = ''
    
    for i in range(len(scores)):
        tmp =[]
        for j in range(len(scores)):
            tmp.append(scores[j][i])
        new_tmp = check(i, tmp, scores)
        avg = sum(new_tmp) / len(new_tmp)
        if(avg >= 90):
            answer += 'A'
        elif(avg >= 80):
            answer += 'B'
        elif(avg >= 70):
            answer += 'C'
        elif(avg >= 50):
            answer += 'D'
        elif(avg < 50):
            answer+= 'F'
        
        
    return answer
