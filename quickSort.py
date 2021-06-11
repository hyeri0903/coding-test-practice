#퀵소트
#평균시간복잡도 : nlogn
#wors case: n^2, 불균형 분할시
#pivot 기준 왼쪽은 작은값, 오른쪽은 큰값이 오도록 정렬
#pivot 기준 나누어진 두 그룹을 recursive하게 정렬함, combine 필요없음


def quick_sort(li):
    if len(li) <= 1:
        return li
    
    pivot = li[len(li) // 2]
    low , equal, high = [], [] ,[]
    for num in li:
        if num < pivot :
            low.append(num)
        elif num > pivot:
            high.append(num)
        else:
            equal.append(num)
    return quick_sort(low) +  equal + quick_sort(high)
  
  
  
if __name__ == "__main__":
    print(quick_sort([9, 3, 2, 5, 1, -1]))
