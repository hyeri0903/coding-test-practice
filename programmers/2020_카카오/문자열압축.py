def solution(s):
    answer = 9999
    n = len(s)
    
    for size in range(1, n+1):
        result = ''
        pivot = s[:size]
        cnt = 1
        start = size
        while(1):
            tmp = s[start:start+size]
            if(tmp == pivot):
                cnt += 1
            else:
                if(cnt == 1):
                    result += pivot
                else:
                    result += str(cnt) + pivot
                pivot = tmp
                cnt = 1
            start += size
            if(start >= len(s)):
                if(cnt==1):
                    result += pivot
                else:
                    result += str(cnt) + pivot
                break
        if(len(result) < answer):
            answer = len(result)
    
    return answer
