# ind the maximal product of any triplet.
# 제일 큰 수 3개
# 제일 큰 수 1개, 제일 작은수 2개

def solution(A):
    A.sort()
    answer = 0

    tmp1 = A[-1] * A[-2] * A[-3]
    tmp2 = A[0] * A[1] * A[-1]
    answer = max(tmp1, tmp2)

    return answer
