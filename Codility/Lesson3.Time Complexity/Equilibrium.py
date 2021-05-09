def solution(A):
    answer = 99999

    if len(A)==2:
        return abs(A[0]-A[1])

    left = 0
    right = sum(A)

    for i in range(1, len(A)):
        left += A[i-1]
        right -= A[i-1]
        res = abs(left-right)

        if res < answer:
            answer = res

    return answer
