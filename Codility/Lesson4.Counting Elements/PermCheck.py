def solution(A):
    A.sort()
    pivot = 1
    answer = 1

    for i in A:
        if i == pivot:
            pivot +=1
        else:
            answer = 0
            break

    return answer
