S = input().upper() #문자열 대문자로 받음

alpha_lst = []

for alpha in S:
    if alpha not in alpha_lst:
        alpha_lst.append(alpha)

# print(alpha_lst)

cnt_lst = [0] * len(alpha_lst)
# print(cnt_lst)

for alpha in S:
    for i in range(len(alpha_lst)):
        if alpha == alpha_lst[i]:
            cnt_lst[i] += 1

if cnt_lst.count(max(cnt_lst)) != 1:
    #최대값이 여러개면 물음표 출력
    print('?')

else:
    ansidx = cnt_lst.index(max(cnt_lst))
    print(alpha_lst[ansidx])
