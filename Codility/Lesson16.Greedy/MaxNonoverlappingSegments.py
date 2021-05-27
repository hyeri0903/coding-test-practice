# B(end) < A(start) 인지 비교해가며 정답 갱신

def solution(A, B):
    if len(A) <  1:
        return 0

    answer = 1
    lastB = B[0]

    for i in range(1, len(A)):
        if A[i] > lastB:
            answer+=1
            lastB = B[i]

    return answer
