#언어 선호도 * 직업군 언어 점수의 총합이높은 직업군 return
#총합이 같은 직업군이 여러개일 경우 사전순으로 직업군 return

def solution(table, languages, preference):
    answer = ''
    result = []
    scores = []
    jobs = []
    
    dic = {}
    for i in range(len(languages)):
        dic[languages[i]] = preference[i]
    
    for val in table:
        job = val.split(" ")[0]
        jobs.append(job)
        arr = val.split(" ")[1:][::-1]
        score = 0
        for i in range(len(arr)):
            if arr[i] in languages:
                score += dic[arr[i]] * (i+1)
        #print(score)
        scores.append(score)
        
    max_val = max(scores)
    for i in range(len(scores)):
        if scores[i] == max_val:
            result.append(jobs[i])

    result.sort()
    answer = result[0]
    return answer
