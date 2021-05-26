
def solution(A):
    s = set()
    for ele in A:
        x = abs(ele)
        s.add(x)

    return len(s)
