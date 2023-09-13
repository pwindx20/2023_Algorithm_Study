from sys import stdin
input = stdin.readline

while True:
    S = input().rstrip()
    if S == '.':
        break
    st = []
    for i in S:
        if i in ('(', '['):
            st.append(i)
        if i in (')', ']'):
            if not len(st) or ((i == ')' and st[-1] == '[') or (i == ']' and st[-1] == '(')):
                print('no')
                break
            elif (i == ')' and st[-1] == '(') or (i == ']' and st[-1] == '['):
                st.pop()
    else:
        print('no' if len(st) else 'yes')