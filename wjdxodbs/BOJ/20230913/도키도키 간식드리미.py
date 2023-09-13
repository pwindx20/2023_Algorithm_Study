from sys import stdin
input = stdin.readline

N = int(input())
arr = list(map(int, input().split()))
min_n = min(arr)
st = [0]
result = min_n-1
for i in arr:
    if result + 1 == i:
        result = i
    elif result + 1 == st[-1]:
        while result + 1 == st[-1]:
            result = st.pop()
        st.append(i)
    else:
        st.append(i)
for i in range(len(st)-1, 0, -1):
    if result + 1 == st[i]:
        result = st[i]
    else:
        print('Sad')
        break
else:
    print('Nice')