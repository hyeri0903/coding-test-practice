from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    menu = {}
    
    #단품메뉴 조합 개수 구하기
    for i in course:
        tmp = []
        for order in orders:
            li = sorted(list(order))
            combi = list(map(''.join, combinations(li, i)))
            tmp += combi
        #{문자열 조합 : 개수}
        counter = Counter(tmp)
        #print(counter)
        
        #2인 이상 주문된 음식만 취급, 1개만 주문된 음식은 제거           
        #2인 이상 주문했으면서 가장 많이 주문된 메뉴 구성만 출력
        if len(counter)>0 and max(counter.values())>1:
            print(max(counter.values()))
            answer += [''.join(key) for key in counter if counter[key] == max(counter.values())]

    answer.sort()
    return answer
