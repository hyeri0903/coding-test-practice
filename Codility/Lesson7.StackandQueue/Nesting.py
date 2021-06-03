
def solution(S):
    if len(S) == 0:
        return 1
    elif len(S) == 1:
        return 0

    st = []
    for i in S:
        if i == '(':
            st.append(i)
        else:
            if len(st) == 0:
                return 0
            else:
                if st[-1] == '(':
                    st.pop()
                else:
                    return 0

    if len(st) != 0:
        return 0
    
    return 1
    
    
