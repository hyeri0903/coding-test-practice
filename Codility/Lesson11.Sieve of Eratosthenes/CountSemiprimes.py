#참고 : https://killong.blogspot.com/2019/12/codility-lesson11-countsemiprimes.html
# 어렵다...ㅠ

def solution(N, P, Q):
    prime = []
    for i in range(2, N//2 + 1) :
        isprime = True
        for j in prime:
            if i%j == 0:
                isprime = False
                break
        if isprime:
            prime.append(i)

    #semi prime 이면 1, 아니면 0으로 check
    semi_prime = [0] * (N+1)
    for i in range(len(prime)):
        for j in range(i, len(prime)):
            idx = prime[i] * prime[j]
            if idx <= N:
                semi_prime[idx] = 1
            else:
                break
    
    semi_prime_cnt = [0] * (N+1) #idx번째까지 semi prime 개수
    for i in range(1, len(semi_prime)):
        if semi_prime[i] == 1:
            semi_prime_cnt[i] = semi_prime_cnt[i-1] + 1
        else:
            semi_prime_cnt[i] = semi_prime_cnt[i-1]

    result = [0] * (len(P))
    for i in range(len(result)):
        result[i] = semi_prime_cnt[Q[i]] - semi_prime_cnt[P[i]-1]

    return result
