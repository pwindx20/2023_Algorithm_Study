# 10798
s_lst = [input()+' '*15 for _ in range(5)]

for i in range(15):
    for j in range(5):
        if s_lst[j][i] == ' ':
            continue
        print(s_lst[j][i], end='')