# A~B사이 정수 중에 K로 나누어질 수 있는 수의 개수

def solution(A, B, K):
    answer = 0
    if A == B:
        if A%K == 0:
            return 1
        else:
            return 0

    start = 0
    for i in range(A, B+1):
        if i%K == 0:
            start = i
            break
    
    answer = int(B/K - start/K + 1)

    return answer
    
