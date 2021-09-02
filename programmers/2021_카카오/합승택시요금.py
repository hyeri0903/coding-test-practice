def floyd(n, dist):
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if(i==j or i==k or j==k):
                    continue
                if(dist[i][k] != 999999 and dist[k][j] != 999999):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist
        
def solution(n, s, a, b, fares):
    answer = 0
    arr = [[999999 for _ in range(n+1)] for _ in range(n+1)]
    
    for i in range(len(fares)):
        x = fares[i][0]
        y = fares[i][1]
        c = fares[i][2]
        
        arr[x][y] = c
        arr[y][x] = c
        
    #자기 자신 정점은 0으로 초기화
    for i in range(n+1):
        arr[i][i] = 0
        
    
    arr=floyd(n, arr)  #정점간 최소비용 구하기
    
    answer = arr[s][a] + arr[s][b]  #a, b 따로 가는 경우

    #i지점까지 동승하는 경우
    for i in range(1, n+1):
        if(arr[s][i]!=999999 and arr[i][a]!=999999 and arr[i][b]!=999999):
            answer = min(answer, arr[s][i] + arr[i][a] + arr[i][b])
    
    return answer
