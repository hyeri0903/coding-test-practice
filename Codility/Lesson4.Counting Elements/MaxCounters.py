def solution(N, A):
    li = [0 for _ in range(N)]
    max_val = 0
    cur = 0

    for i in range(len(A)):
        if A[i] == N+1:
            max_val = cur
        else:
            if li[A[i]-1] < max_val:  #현재 값이 max보다 작으면 max값으로 조정
                li[A[i]-1] = max_val
            li[A[i]-1] += 1
            if cur < li[A[i]-1]:  #max값 갱신
                cur = li[A[i]-1]

    for i in range(N):
        if li[i] < max_val:
            li[i] = max_val

    return li
