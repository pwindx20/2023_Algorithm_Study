# 11724
# 입력: 정점의 개수N, 간선의개수M/ M개의 줄에 간선 양 끝점 u, v 한번만
# 출력: 연결요소의 개수
import sys

def find_set(x):
    if lst[x] == x:
        return x
    else:
        return find_set(lst[x])
    
def union_set(x, y):
    x=find_set(x)
    y=find_set(y)
    if x==y:
        return
    elif x>y:
        lst[x] = y
        return
    else:
        lst[y] = x
        return

N, M = map(int,sys.stdin.readline().split())
lst = [i for i in range(N+1)]
for _ in range(M):
    u, v = map(int,sys.stdin.readline().split())
    union_set(u, v)
st = set()
for i in lst:
    st.add(find_set(i))
print(len(st)-1)