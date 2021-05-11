# A, C, G, T
# 1, 2, 3, 4
#해당구간의 string에서 가장 작은 충격계수 반환

def solution(S, P, Q):
    res = []
    for i in range(len(P)):
        tmpStr = S[P[i], Q[i]+1]
        if 'A' in tmpStr:
            res.append(1)
        elif 'C' in tmpStr:
            res.append(2)
        elif 'G' in tmpStr:
            res.append(3)
        else:
            res.append(4)
    return res
