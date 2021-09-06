def solution(genres, plays):
    answer = []
    genres_cnt = {}
    
    for i in range(len(genres)):
        g = genres[i]
        if g not in genres_cnt:
            genres_cnt[g] = plays[i]
        else:
            genres_cnt[g] += plays[i]
            
    # 1.가장 많이 재생된 장르순 정렬
    genres_cnt = sorted(genres_cnt.items(), key=lambda x:x[1], reverse=True)
    for gc in genres_cnt:
        genre = gc[0]
        play_cnt = [] #idx, play_count
        for i in range(len(genres)):
            if(genres[i] == genre):
                play_cnt.append({'idx':i, 'cnt':plays[i]})

        #2. play count 높은순, 고유번호 오름차순 정렬
        play_cnt = sorted(play_cnt, key=lambda x:(-x['cnt'], x['idx']))
        if len(play_cnt)>=2: 
            answer.append(play_cnt[0]['idx'])
            answer.append(play_cnt[1]['idx'])
        else:
            answer.append(play_cnt[0]['idx'])
            
    return answer
