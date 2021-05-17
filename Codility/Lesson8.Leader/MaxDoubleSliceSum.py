# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    left_max_sum =[0] * len(A)
    right_max_sum = [0] * len(A)

    for i in range(1, len(A)-2):
        left_max_sum[i] = max(left_max_sum[i-1]+A[i], 0)
    for i in range(len(A)-2, 1, -1):
        right_max_sum[i] = max(right_max_sum[i+1]+A[i], 0)

    max_sum = left_max_sum[0] + right_max_sum[2] #(0,1,2)

    for i in range(1, len(A)-1):
        max_sum = max(max_sum, left_max_sum[i-1] + right_max_sum[i+1])
    return max_sum
