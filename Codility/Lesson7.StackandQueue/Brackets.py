# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    st = []
    for x in S:
        if x == '{' or x == '[' or x == '(':
            st.append(x)
        else:
            if len(st) == 0:
                return 0
            if x == '}':
                if st[-1] == '{':
                    st.pop()
                else:
                    return 0
            elif x == ']':
                if st[-1] == '[':
                    st.pop()
                else:
                    return 0
            elif x == ')':
                if st[-1] == '(':
                    st.pop()
                else:
                    return 0
    if len(st) >= 1:
        return 0
    return 1

