
def solution(A):
    A.sort()
    pivot = 1
    for i in range(len(A)):
        if A[i] < 0:
            continue
        if A[i] == pivot:
            pivot+=1

    return pivot
