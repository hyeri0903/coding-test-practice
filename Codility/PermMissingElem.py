# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    n = len(A)+1
    n_sum = n*(n+1)/2
    n_sum = int(n_sum)

    a_sum = 0

    for i in A:
        a_sum += i

    answer = n_sum - a_sum
    return answer


