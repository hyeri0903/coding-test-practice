def change_to_sec(_time):
    hh, mm, ss = _time.split(":")
    return int(hh) * 3600 + int(mm) * 60 + int(ss)

def change_to_hour(_time):
    hh = _time // 3600
    hh = '0' + str(hh) if hh<10 else str(hh)
    _time = _time % 3600
    mm = _time // 60
    mm = '0' + str(mm) if mm<10 else str(mm)
    _time = _time % 60
    ss = '0'+ str(_time) if _time<10 else str(_time)
    return hh+":"+mm+":"+ss

def solution(play_time, adv_time, logs):
    answer = ''
    play_time = change_to_sec(play_time) #초 단위로 변경
    adv_time = change_to_sec(adv_time)
    result = [0 for _ in range(play_time+1)]
    
    for l in logs:
        start, end = l.split("-")
        start = change_to_sec(start)
        end = change_to_sec(end)
        result[start] += 1
        result[end] -= 1
    #구간별 
    for i in range(1, len(result)):
        result[i] = result[i] + result[i-1]
    #모든 구간
    for i in range(1, len(result)):
        result[i] = result[i] + result[i-1]
    
    max_view = 0
    max_time = 0
    
    for i in range(adv_time-1, play_time):
        if i >= adv_time:
            if max_view< result[i] - result[i-adv_time]:
                max_view = result[i] - result[i-adv_time]
                max_time = i-adv_time+1
        else:
            if max_view < result[i]:
                max_view = result[i]
                max_time = i - adv_time + 1
    max_time = change_to_hour(max_time)
    return max_time
            
    return answer
