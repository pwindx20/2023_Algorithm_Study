k = 3
m = 4
score = [1, 2, 3, 1, 2, 3, 1]

score.sort() # [1, 1, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4]
# print(score)
answer = 0
while len(score)>= m:
    lst = []
    for _ in range(m):
        s = score.pop(-1)
        lst.append(s)
    answer += m * min(lst)
print(answer)