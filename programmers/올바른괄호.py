def solution(s):
    answer = True
    st = []
    if s[0] == ')':
        return False
    
    for i in range(len(s)):
        if s[i] == '(':
            st.append(s[i])
        else:
            if len(st)<=0:
                return False
            if st[-1] == '(':
                st.pop()
            else:
                return False
    if len(st) >=1:
        return False
    return True
