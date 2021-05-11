# 0 (east) -> 1(west)
# returns the number of pairs of passing cars.
# num of passing cars > 1000000000 -> -1 return

def solution(A):
    sum = [0]*len(A)

    for i in range(len(A)-1, -1, -1):
        if i == len(A)-1:
            sum[i] = A[i]
        else:
            sum[i] = sum[i+1]+A[i]
    
    answer = 0
    for i in range(len(A)):
        if A[i] == 0:
            answer += sum[i]
        if answer > 1000000000:
            return -1
    return answer
