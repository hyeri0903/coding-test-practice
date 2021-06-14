# 1. 선택정렬
#가장 작은 값의 index를 찾은(선택) 후 현재 위치와 바꿈
#평균시간복잡도 : O(n^2)

def selectionSort(li):
    for i in range(len(li)):
        minIdx = i
        for j in range(i+1, len(li)):
            if li[j] < li[minIdx]:
                minIdx = j
        #swqp(li[i], li[minIdx])
        #tmp = li[i]
        #li[i] = li[minIdx]
        #li[minIdx] = tmp
        
        li[i], li[minIdx] = li[minIdx], li[i]
        
    print(li)

    
# 2. 삽입정렬
#두번째 원소부터 시작하여 현재 위치보다 앞의 원소들과 값 비교
#현재 pivot값 보다 더 큰 수가 앞에 존재한다면 현재 위치에 (li[j+1]) 그 값(큰 값, li[j])을 넣고 계속 앞의 원소 값 탐색
#평균시간복잡도 : O(n^2)
#Best : O(N) , 이미정렬되어있는 경우

def insertionSort(li):
    for i in range(1, len(li)):
        pivot = li[i]
        j = i-1
        while j>=0 and pivot < li[j]:
            li[j+1] = li[j]
            j -= 1
        li[j+1] = pivot
    print(li)

    
# 3. 버블정렬
#2개 원소를 계속 비교해가면서 정렬
#평균시간복잡도 : O(n^2)
def bubbleSort(li):
    for i in range(len(li)-1, 0, -1):
        for j in range(0, i):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                
    print(li)
        
        
        
if __name__ == "__main__":
    li = [2, 4, 9 ,7, 1, 6, 8, 3, 5]
    selectionSort(li)
    insertionSort(li)
    bubbleSort(li)
