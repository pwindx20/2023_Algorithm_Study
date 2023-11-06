N, M = map(int, input().split())

pm_lst = []
ans_lst = []

for _ in range(N):
    pm_lst.append(input())

for _ in range(M):
    ans_lst.append(input())

pm_tpl = tuple(pm_lst)
ans_tpl = tuple(ans_lst)

for elem in ans_tpl:
    if elem.isdecimal():
        print(pm_tpl[int(elem)-1])
    else:
        idx = pm_tpl.index(elem)
        print(idx+1)

#리스트로는 시간초과
#set으로 바꿨는데 생각해보니 set에는 index 개념이 없음
#근데 tuple은 요소 추가가 안되는데?
#list를 tuple로 바꾸는 것도 생각해봤는데 망...
#