# 28279
from collections import deque
import sys
N = int(sys.stdin.readline())
my_deque = deque()

for _ in range(N):
    order = sys.stdin.readline()[:-1]
    
    if '1 'in order:
        order, num = map(int, order.split())
        my_deque.appendleft(num)
    elif '2 ' in order:
        order, num = map(int, order.split())
        my_deque.append(num)
    elif order =='3':
        if my_deque:
            print(my_deque.popleft())
        else: print(-1)
    elif order =='4':
        if my_deque:
            print(my_deque.pop())
        else: print(-1)
    elif order =='5':
        print(len(my_deque))
    elif order =='6':
        print(0) if my_deque else print(1)
    elif order == '7':
        if my_deque:
            print(my_deque[0])
        else:
            print(-1)
    else:
        if my_deque:
            print(my_deque[-1])
        else:
            print(-1)
    # print(my_deque)