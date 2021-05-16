# 가장 인접한 3변의 길이 비교 (가까운 변일수록 삼각형 될 확률 높음)
# p+q > r 조건을 만족하면 나머지 2개 조건 자동으로 만족


def solution(A):
    A.sort()
    
    for i in range(len(A)-2):
        p = A[i]
        q = A[i+1]
        r = A[i+2]
        if p+q > r:
            return 1

    return 0
