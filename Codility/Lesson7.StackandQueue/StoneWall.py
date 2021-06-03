
def solution(H):
    cnt = 1
    st = [H[0]]

    for i in range(1, len(H)):
        while len(st) > 0 and st[-1] > H[i]:
            st.pop()

        if len(st) == 0 or st[-1] < H[i]:
            st.append(H[i])
            cnt += 1

    return cnt
