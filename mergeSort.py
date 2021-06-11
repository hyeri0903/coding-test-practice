#합병정렬
#평균시간복잡도 : nlogn

def merge(left, right):
    tmp = []
    i = j = 0
    while i<len(left) and j < len(right):
        if left[i] <= right[j]:
            tmp.append(left[i])
            i+=1
        else:
            tmp.append(right[j])
            j += 1
    if i < len(left):
        tmp += left[i:len(left)]
    if j < len(right):
        tmp += right[j:len(right)]
    return tmp
        
            
def mergeSort(li):
    if len(li) <= 1:
        return li

    mid = len(li) // 2
    left = mergeSort(li[:mid])
    right = mergeSort(li[mid:])
    return merge(left, right)


if __name__ == "__main__":
    print(mergeSort([9, 3, 2, 5, 1, -1]))
