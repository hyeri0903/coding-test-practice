#K개만큼 블럭이 생기는지 확인
def isValid(A, max_block_cnt, max_block_size):
    block_sum = 0
    block_cnt = 0

    for ele in A:
        #block의 최대값을 넘어가면 블록 나누기
        if block_sum + ele > max_block_size:
            block_sum  = ele
            block_cnt += 1
        #블록안의 원소 값 sum
        else:
            block_sum += ele
        if block_cnt >= max_block_cnt:
            return False
    return True


def solution(K, M, A):
    max_block_cnt = K
    lower_bound = max(A) #각 블록 sum의 최소값
    upper_bound = sum(A) #모든 블록의 sum 값

    if max_block_cnt == 1:
        return upper_bound
    if max_block_cnt>= len(A):
        return lower_bound

    while(lower_bound <= upper_bound):
        mid = (lower_bound + upper_bound) //2
        #K만큼 블록으로 나눠지면 한 블록안의 원소개수를 줄여가며 최소 최대값 찾기
        if isValid(A, max_block_cnt, mid):
            upper_bound = mid-1
        #K만큼 블록으로 안나눠지면 한 블록안의 원소개수 늘리기
        else:
            lower_bound = mid+1
    return lower_bound
