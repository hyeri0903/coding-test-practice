def solution(N, M):
    a, b = N, M

    while(b):
        a, b = b, a % b
    gcd = a #최대공약수
    answer = N // gcd
    
    return answer
