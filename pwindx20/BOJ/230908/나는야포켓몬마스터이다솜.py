# 1620
# 입력: 도감에 등록되어있는 포켓몬 개수 N, 맞춰야하는 문제 M/
#       1번인 포켓몬부터 하나씩 이름/ M줄에 맞춰야하는 문제 : 알파벳>번호 번호>포켓몬 번호
# 출력: M개의 줄에 정답

########### 아오 input도 못쓰게 하네#################

import sys

N, M = map(int,sys.stdin.readline()[:-1].split())
po_lst = [0] + [sys.stdin.readline()[:-1] for _ in range(N)]
po_dict = {}
j = 0
for i in po_lst:
    po_dict[i]= j
    j+= 1
# print(po_dict)
# print(po_lst)
for i in range(M):
    q = sys.stdin.readline()[:-1]
    if q.isdigit():
        print(po_lst[int(q)])
    else:
        print(po_dict[q])
        # print(po_lst.index(q))


############ 출력 초과 ################
############딕셔너리 주석처리 안함############
##########하지만 시간초과##################
# N, M = map(int, input().split())
# num_to_name = {}
# name_to_num = {}
# for i in range(1, N+1):
#     name = input().strip()
#     num_to_name[i] = name
#     name_to_num[name] = i
# print(num_to_name, name_to_num)

# for _ in range(M):
#     q = input()
#     if q.isdigit():
#         print(num_to_name[int(q)])
#     else:
#         print(name_to_num[q])