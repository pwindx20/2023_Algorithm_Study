import sys
sys.stdin = open('input1316.txt', 'r')

N = int(input())

cnt_for_G = 0 #그룹 단어의 개수

for _ in range(N):
    S = input()

    lst = []
    cnt = 1

    for i in range(len(S)):
        if i == len(S)-1:
            if [i] != [i-1]:
                lst.append(1)
            else:
                lst[-1] += 1

        else:
            if S[i] == S[i+1]:
                cnt += 1

            else:
                lst.append(cnt)
                cnt = 1

    print(lst)
    if 1 not in lst:
        cnt_for_G += 1

    print(cnt_for_G)
