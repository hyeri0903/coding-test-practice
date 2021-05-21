# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    answer = 0
    
    if len(A)<=1:
        return 0

    min_val = A[0]
    for i in range(1,len(A)):
        val = A[i] - min_val
        if val <= 0:
            min_val = A[i]
        else:
            if answer < val:
                answer = val
        
    
    return answer
