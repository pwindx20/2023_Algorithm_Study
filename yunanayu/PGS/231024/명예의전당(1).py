k = 4
score =[0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]
lst = []
answer = []
for i in range(k):
    lst.append(score[i])
    answer.append(min(lst))

for i in range(k, len(score)):
    if score[i] > min(lst):
        lst.remove(min(lst))
        lst.append(score[i])
    answer.append(min(lst))

print(answer)