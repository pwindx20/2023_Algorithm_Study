def solution(s):
    st = []
    for i in s:
        if st:
            if st[-1] == i:
                st.pop()
            else:
                st.append(i)
        else:
            st.append(i)


    return 0 if st else 1