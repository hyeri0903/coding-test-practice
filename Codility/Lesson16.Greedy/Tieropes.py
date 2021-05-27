
def solution(K, A):
    answer = 0
    total = 0

    if len(A)==1:
        if K > A[0]:
            return 0
        else:
            return 1

    for i in range(len(A)):
        if total + A[i] < K:
            total += A[i]
        else:
            answer += 1
            total = 0

    return answer
