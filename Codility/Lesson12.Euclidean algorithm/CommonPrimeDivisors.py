def gcd(a, b):
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)

def check(a, b):
    gcd_ab = gcd(a, b)
    gcd_a = 0
    gcd_b = 0

    while(gcd_a != 1):
        gcd_a = gcd(a, gcd_ab)
        a = a/gcd_a

    while(gcd_b != 1):
        gcd_b = gcd(b, gcd_ab)
        b = b/gcd_b

    if a==1 and b==1:
        return True
    else:
        return False


def solution(A, B):
    answer = 0

    for i in range(len(A)):
        if check(A[i], B[i]):
            answer += 1

    return answer
