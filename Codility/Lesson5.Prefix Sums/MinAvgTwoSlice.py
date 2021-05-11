# return the smallest starting position of such a slice.
# average = sum[P:Q]/(Q-P+1)

def solution(A):
    minavg = (A[0] + A[1])/2
    answer = 0

    for i in range(2, len(A)):
        avg = (A[i]+A[i-1]+A[i-2])/3
        if minavg > avg:
            minavg = avg
            answer = i-2

        avg = (A[i]+A[i-1])/2
        if minavg > avg:
            minavg = avg
            answer = i-1
            
    return answer
