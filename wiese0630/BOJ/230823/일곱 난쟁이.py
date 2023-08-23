# import sys
# sys.stdin = open('input2309.txt', 'r')

dwarves = []
for _ in range(9):
    dwarves.append(int(input()))

n = len(dwarves)
for i in range(1<<n):
    sumV = 0
    cnt = 0
    real = []
    for j in range(n):
        if i &(1<<j):
            sumV += dwarves[j]
            cnt += 1
            real.append(j)

    if cnt == 7 and sumV == 100:
        break

ans = []
for elem in real:
    ans.append(dwarves[elem])
ans.sort()
for answer in ans:
    print(answer)

