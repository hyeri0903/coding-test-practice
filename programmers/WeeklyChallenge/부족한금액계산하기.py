def solution(price, money, count):
    answer = -1
    total = 0
    for i in range(1, count+1):
        p = price * i
        total += p
        
    if(money > total):
        answer = 0
    else:
        answer = total - money
    return answer
