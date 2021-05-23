import math

def solution(A):
    n = len(A)
    cnt_li = [0] * (2*n + 1)

    for data in A:
        cnt_li[data] += 1

    answer = [0] * n
    tmp = [-1] * (2*n + 1)

    for i in range(n):
        cur = A[i]
        if tmp[cur]!=-1:
            answer[i] = tmp[cur]
        else:
            cnt = 0
            for j in range(1, int(math.sqrt(cur))+1):
                if cur%j == 0:
                    cnt += cnt_li[j]
                    if j*j != cur:
                        cnt += cnt_li[cur // j]
            answer[i] = n - cnt
            tmp[cur] = answer[i]
    return answer




    return answer
