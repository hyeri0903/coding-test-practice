def solution(n, k, cmd):
    answer = ''
    linked_list = {i: [i-1, i+1] for i in range(1, n+1)}
    res = ['O'] * (n) #O: 삭제안함, X: 삭제됨
    cur = k
    stack = []
    
    cur+=1
    
    for c in cmd:
        if(len(c)>1):
            tmp = c.split(' ')
            val = int(tmp[1])
            if(tmp[0] == 'D'):
                for _ in range(val):
                    cur = linked_list[cur][1]
            elif(tmp[0] =='U'):
                for _ in range(val):
                    cur = linked_list[cur][0]
        else:
            #선택한 행 삭제
            if c=='C':
                prev, nxt = linked_list[cur]
                stack.append([prev, cur, nxt])
                res[cur-1]='X'
                #마지막 행인 경우
                if nxt == n+1:
                    cur = linked_list[cur][0]
                else:
                    cur = linked_list[cur][1]
                if prev == 0:
                    linked_list[nxt][0] = prev
                elif nxt == n+1:
                    linked_list[prev][1]=nxt
                else:
                    linked_list[prev][1] = nxt
                    linked_list[nxt][0] = prev
                    
            #가장 최근에 삭제한 행 복구
            elif c=='Z':
                prev, now, nxt = stack.pop()
                res[now-1] = 'O'
                
                if prev == 0:
                    linked_list[nxt][0] = now
                elif nxt == n+1:
                    linked_list[prev][1] = now
                else:
                    linked_list[prev][1] = now
                    linked_list[nxt][0] = now
                    
                    
    for x in res:
        answer += x

    return answer
  
  
#참고: https://ckd2806.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%91%9C-%ED%8E%B8%EC%A7%91

