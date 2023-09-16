# 24511
# 입력: 0: 큐, 1: 스택, 자료구조 개수 N/ 수열 A/ 수열 B 자료규조에 있던 원소/ 삽입할 수열 M/ 삽입할 원소 수열 C
# 출력: 리턴값 공백으로 구분하여 출력
import sys
from collections import deque
N = sys.stdin.readline()
A = sys.stdin.readline().split()
B = sys.stdin.readline().split()
M = sys.stdin.readline()
C = deque(sys.stdin.readline().split())

for i in range(int(N)):
    if A[i] =='0':
        C.appendleft(B[i])
for j in range(int(M)):
    print(C.popleft(), end=' ')