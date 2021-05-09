
def solution(X, A):
    dist=set()
    for i in range(len(A)):
        dist.add(A[i])
        if(len(dist) == X):
            return i
        

    return -1
