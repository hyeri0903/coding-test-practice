#참조 : https://smecsm.tistory.com/232
import math

def solution(A):
    peaks = [] #peaks
    for i in range(1, len(A)):
        if i == len(A)-1:
            pass
        else:
            if A[i-1] <A[i] > A[i+1]:
                peaks.append(i)

    if len(peaks) <= 2:
        return len(peaks)

    maxflag = int(math.sqrt(peaks[-1]-peaks[0])) + 1

    #find maximum number of flags on the peaks
    for k in range(maxflag, 2, -1):
        cnt = 1
        pivot = peaks[0]
        for p in peaks:
            if k <= p - pivot:
                cnt += 1
                pivot = p
        if cnt >= k:
            break
    return k

        
