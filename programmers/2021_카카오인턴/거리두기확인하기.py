#참고: https://gingerkang.tistory.com/124
#P : 응시자 자리
#0 : 빈 테이블
#X : 파티션
# 모두 거리두기 지키면 1, 아니면 0 리턴

#상, 하, 좌, 우에 0이있고
#상, 하, 좌, 우, 대각선 8방향 중 P이 있으면 거리두기 확인
from collections import deque

dir = [[1,0],[0,1],[-1,0],[0,-1]]

def check(place, person):
    visit = [[False] * 5 for _ in range(5)]
    count = 0  #검사 횟수
    q = deque()
    q.append(person)
    
    while q:
        for _ in range(len(q)):
            y, x = q.popleft()
            visit[y][x] = True
            for i in range(4):
                ny = y + dir[i][0]
                nx = x + dir[i][1]
                if ny < 0 or nx < 0 or ny >=5 or nx >=5 or visit[ny][nx]:
                    continue
                if place[ny][nx] == 'P':   #사람이 있으면 즉시 false 반환
                    return False
                elif place[ny][nx] == 'X':  #칸막이가 있으면 pass
                    continue
                else:
                    q.append((ny ,nx))
        count+=1
        #각 위치의 검사를 2번만하면 됨
        if count==2 or not q:
            return True

            
def solution(places):
    answer = []
    for place in places:
        people = deque()
        for i in range(5):
            for j in range(5):
                if(place[i][j] == 'P'):
                    people.append((i,j))
        # 사람이 없는 경우
        if len(people)==0:
            answer.append(1)
            continue
        #queue에 P가 있는 위치를 기준으로 거리두기 검사
        flag = True
        for person in people:
            if not check(place, person):
                flag = False
                break
                
        if flag==False:
            answer.append(0)
        else:
            answer.append(1)
            
    return answer
