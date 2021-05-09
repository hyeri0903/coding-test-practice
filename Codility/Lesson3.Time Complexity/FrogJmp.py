# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    if X==Y:
        return 0
    elif X+D >= Y:
        return 1
    else:
        dist = Y-X
        if dist%D !=0:
            answer = dist//D + 1
        else:
            answer = dist//D
    
    return answer
