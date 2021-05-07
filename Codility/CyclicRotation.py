# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    if sum(A)==0:
        return A
    
    while K>0:
        tmp = A[-1]
        cpy_A = A[:-1]
        A = [tmp] + cpy_A
        #print(A)
        K-=1

    return A
    
