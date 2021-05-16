#2 1 1 2 3 1

def solution(A):
    dic = {}
    result = []

    for val in A:
        if val not in dic.keys():
            dic[val] = 1
        else:
            dic[val] += 1
    
    for k , v in sorted(dic.items(), key=lambda x:x[1]):
        if v == 1:
            result.append(k)
        else:
            break

    answer = len(dic.keys())
    return answer
