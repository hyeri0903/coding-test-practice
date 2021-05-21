# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    max_sum =  -1000000
    max_part_sum = 0

    for n in A:
        max_sum = max(max_sum, max_part_sum + n)
        max_part_sum = max(0, max_part_sum + n)
    return max_sum
