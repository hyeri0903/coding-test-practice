
def solution(A):
    dic = {}
    answer = 0

    for val in A:
        if val not in dic:
            dic[val] = 1
        else:
            if dic[val] == 2:
                dic[val] = 1
            else:
                dic[val] += 1

    for i in range(len(A)):
        val = A[i]
        if dic[val] == 1:
            answer = val
            break

    return answer
