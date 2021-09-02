def solution(s):
    answer = 0
    result = ''
    info = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4'
           , 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    
    tmp = ''
    for i in range(len(s)):
        if s[i].isdigit():
            result += str(s[i])
        else:
            tmp += s[i]
            if tmp in info.keys():
                result += info[tmp]
                tmp = ''
    answer = int(result)
    return answer
