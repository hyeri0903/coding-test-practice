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
    
def insertionSort(li):
    for i in range(len(li)):
        pivot = li[i]
        j = i-1
        while j>=0 and pivot < li[j]:
            li[j+1] = li[j]
            j -= 1
        li[j+1] = pivot
    print(li)
    
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
