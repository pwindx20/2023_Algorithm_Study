G = {'A+': 4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5,
     'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0, 'P':0.0}

N = 20
lst_s = []
lst_n = []

for i in range(20):
    lst = list(input().split())
    if lst[2] == 'P':
        N -= 1
    else:
        lst_s.append(float(lst[1]) * G[lst[2]])
        lst_n.append(float(lst[1]))
print(sum(lst_s)/sum(lst_n))