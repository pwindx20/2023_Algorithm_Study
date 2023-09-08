# 1764
# 입력: N, M/ N줄에 걸쳐 사람이름, M줄에 걸쳐 보도 못한 사람이름/
#      중복되는 이름은 없다
# 출력: 듣보잡의 수, 명단을 사전순으로 출력
import sys
N, M = map(int,sys.stdin.readline().split())
Nset = set(sys.stdin.readline()[:-1] for _ in range(N))
Mset = set(sys.stdin.readline()[:-1] for _ in range(M))
name_lst = list(Nset & Mset)
print(len(name_lst))
for i in  sorted(name_lst):
    print(i)