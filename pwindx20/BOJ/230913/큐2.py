# 18258
# 입력: 명령수 N/ 명령 하나씩
# 출력: 명령 하나당 한줄에 하나씩 출력
import sys
from collections import deque

N = int(sys.stdin.readline())
Q = deque()
for _ in range(N):
    order = sys.stdin.readline()[:-1]
    if 'push' in order:
        push, num = order.split()
        Q.append(int(num))
    elif order == 'pop':
        print(Q.popleft()) if Q else print(-1)
    elif order == 'size':
        print(len(Q))
    elif order == 'empty':
        print(0) if Q else print(1)
    elif order == 'front':
        print(Q[0]) if Q else print(-1)
    elif order == 'back':
        print(Q[-1]) if Q else print(-1)