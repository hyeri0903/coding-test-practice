from itertools import combinations

def solution(info, query):
    answer = []
    db = {}  #key : info 경우의 수, value : [score]
    li = []
    for person in info:
        x = person.split(' ')
        score = int(x[-1])
        conditions = x[:-1]
        for n in range(5):
            combi = list(combinations(range(4), n))  #-를 넣을 index 조합
            for c in combi:
                t_c = conditions.copy()  #index에 - 삽입
                for v in c:
                    t_c[v] = '-'
                
                changed_t_c = '/'.join(t_c)
                
                if(changed_t_c in db):
                    db[changed_t_c].append(score)
                else:
                    db[changed_t_c] = [score]

    for value in db.values():
        value.sort() #dict안의 value 리스트(score)를 오름차순 정렬
    
    for q in query:
        x = [i for i in q.split() if i != 'and']
        x_score = int(x[-1])
        cmd = '/'.join(x[:-1])
        if cmd in db:
            value = db[cmd]
            #dict 내에 값(score)가 존재하면
            if len(value) > 0:
                start, end = 0, len(value)
            #lower bound로 index 찾기
            while start != end and start != len(value):
                if x_score <= value[(start+end)//2]:
                    end = (start + end)//2
                else:
                    start = (start+end)//2 + 1
            answer.append(len(value)-start)
        else:
            answer.append(0)
    
    return answer
