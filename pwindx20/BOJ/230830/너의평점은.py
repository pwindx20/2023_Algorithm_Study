# 25206
gradetoscore = {'A+': 4.5, 'A0':4, 'B+':3.5, 'B0':3, 'C+': 2.5,
                'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
sum_credit = 0
sum_score = 0
for _ in range(20):
    name, credit, grade = input().split()
    if grade == 'P':
        continue
    sum_credit += float(credit)
    sum_score += float(credit) * gradetoscore[grade]
print(sum_score/sum_credit)
    