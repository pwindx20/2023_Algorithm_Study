import sys
sys.stdin = open('input1316.txt', 'r')

N = int(input())

cnt = N #일단 모든 단어가 그룹 단어라고 가정

for _ in range(N):
    S = input()
    for i in range(0, len(S)-1):
        if S[i] != S[i+1] and S[i] in S[i+1:]:
            cnt -= 1
            break
            # 그룹 단어가 아님이 결정되면 1 뺸다.


print(cnt)

    # lst = []
    # cnt = 1
    #
    # for i in range(len(S)):
    #     if i == len(S)-1:
    #         if [i] != [i-1]:
    #             lst.append(1)
    #         else:
    #             lst[-1] += 1
    #
    #     else:
    #         if S[i] == S[i+1]:
    #             cnt += 1
    #
    #         else:
    #             lst.append(cnt)
    #             cnt = 1
    #
    # print(lst)
    # if 1 not in lst:
    #     cnt_for_G += 1
    #
    # print(cnt_for_G)
    # 문제를 잘못읽어서 삽질하느라 한시간 버림^^