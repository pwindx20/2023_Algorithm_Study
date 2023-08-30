S = input().upper()
set_s = list(set(S))
cnt_list= []
for key in set_s:
    cnt_list.append(S.count(key))
maxV = max(cnt_list)
idx = cnt_list.index(maxV)
if cnt_list.count(maxV) > 1:
    print('?')
else:
    print(set_s[idx])