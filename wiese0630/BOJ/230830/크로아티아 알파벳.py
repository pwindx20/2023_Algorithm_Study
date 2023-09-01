S = input()

cnt1 = cnt2 = cnt3 = cnt4 = cnt5 = cnt6 = cnt7 = cnt8 = 0

for i in range(len(S)):
    if S[i:i+2] == 'c=':
        cnt1 += 1

for i in range(len(S)):
    if S[i:i+2] == 'c-':
        cnt2 += 1

for i in range(len(S)):
    if S[i:i+3] == 'dz=':
        cnt3 += 1

for i in range(len(S)):
    if S[i:i+2] == 'd-':
        cnt4 += 1

#lj 개수 찾기
for i in range(len(S)):
    if S[i:i+2] == 'lj':
        cnt5 += 1

for i in range(len(S)):
    if S[i:i+2] == 'nj':
        cnt6 += 1

for i in range(len(S)):
    if S[i:i+2] == 's=':
        cnt7 += 1

for i in range(len(S)):
    if S[i:i+2] == 'z=' and S[i-1] != 'd':
        cnt8 += 1

ans = len(S) - (cnt1 + cnt2 + cnt4 + cnt5 + cnt6 + cnt7 + cnt8) -2*cnt3
# print(cnt1, cnt2, cnt3, cnt4, cnt5, cnt6, cnt7, cnt8)
print(ans)

#개어거지 코드2... 답은 나오는데 너무 노가다임