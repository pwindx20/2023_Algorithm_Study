import sys
sys.stdin = open('input.txt', 'r')


H = []
for _ in range(9):
    H.append(int(input()))
sumH = sum(H)

found = False

for i in range(8):
    for j in range(i+1,9):
        if sumH - H[i] - H[j] == 100:
            H.pop(j)
            H.pop(i)
            found = True            
            break
        else:
            continue
    if found:
        break
for i in sorted(H):
    print(i)

#-----------------------------------------아래가 제출한 정답
def seven():
    for i in range(8):
        for j in range(i+1,9):
            if sumH - H[i] - H[j] == 100:
                H.pop(j)
                H.pop(i)
                return H
            else:
                continue



H = []
for _ in range(9):
    H.append(int(input()))

sumH = sum(H)

lst = seven()
for i in sorted(lst):
    print(i)
