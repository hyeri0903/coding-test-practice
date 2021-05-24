# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    A = [1] + A + [1]
    n = len(A)
    f = [1, 1]
    while f[-1] + f[-2] < n:
        f.append(f[-1]+f[-2])

    dist = [-1] * n
    dist[0] = 0

    for cur in range(n):
        if dist[cur] != -1:
            for i in range(len(f)):
                target = f[i] + cur
                if target >= n:
                    break
                if A[target] == 1:
                    if dist[target] == -1:
                        dist[target] = dist[cur] + 1
                    elif dist[target] > dist[cur]+1:
                        dist[target] = dist[cur]+1
    return dist[-1]



