# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    li = []

    for i, v in enumerate(A):
        li.append((i-v, -1)) #왼쪽에서 오는 원
        li.append((i+v, 1)) #오른쪽에서 오는 원

    li.sort()
    #print(li)
    answer = 0
    intervals = 0 #열린 원의 개수

    for i, v in enumerate(li):
        if v[1] == 1:
            intervals -= 1
        elif v[1] == -1:
            answer += intervals
            intervals += 1
    if answer > 10000000:
        return -1
    else:
        return answer
