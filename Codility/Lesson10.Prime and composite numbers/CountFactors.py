# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    if N == 1:
        return 1

    i = 1
    cnt = 0
    while i*i < N:
        if N%i == 0:
            cnt += 2
        i += 1

    if i*i == N:
        cnt += 1

    return cnt
