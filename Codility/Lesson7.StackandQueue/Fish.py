# p < q
# 0: upstream, 1:downstream
# the same direction never meet. 
# The goal is to calculate the number of fish that will stay alive.

def solution(A, B):
    total = len(A)
    alive = 0
    #아무도 안잡아 먹히는 경우
    if sum(B) == total or sum(B) == 0:
        return total

    st = []
    for i in range(total):
        if B[i] == 1:
            st.append(A[i])
        else:
            if len(st) == 0:
                alive += 1
            else:
                while(len(st)> 0):
                    if A[i] > st[-1]:
                        st.pop()
                        if(len(st) == 0):
                            alive+=1
                    else:
                        break

    return alive + len(st)
                







