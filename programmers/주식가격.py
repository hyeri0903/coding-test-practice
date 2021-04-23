def solution(prices):
    answer = []

    for i in range(len(prices)):
        pivot = prices[i]
        cnt = 0
        flag = 1
        for j in range(i+1, len(prices)):
            if pivot <= prices[j]:
                cnt += 1
            else:
                cnt += 1
                answer.append(cnt)
                flag = 0
                break
        if flag != 0:
            answer.append(cnt)

    return answer
