# 1269
# 입력: A의 원소, B의 원소/ 집합A의 원소/ 집합B의 원소
# 출력: 대창 차집합의 원소의 개수를 출력
import sys
N, M = map(int,sys.stdin.readline().split())
Aset = set(sys.stdin.readline().split())
Bset = set(sys.stdin.readline().split())
print(len(Aset.difference(Bset).union(Bset.difference(Aset))))