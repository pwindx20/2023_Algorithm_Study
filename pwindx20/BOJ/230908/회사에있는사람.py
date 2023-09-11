# 7785
# 입력: 출입 기록 수 n/ 출입기록: 이름, enter or leave 
# 출력: 회사에 있는 사람의 이름을 사전순의 역순으로 한줄에 한명씩 출력

N = int(input())
company = {}
for _ in range(N):
    name, s = input().split()
    if name in company:
        if company[name] == 1:
            company[name] = 0
        else:
            company[name] = 1
    else:
        company[name] = 1
name_lst = sorted(company.keys(), reverse=True)
for name in name_lst:
    if company[name] == 1:
        print(name)
















###### 시간초과##############
# N = int(input())
# company = []
# for _ in range(N):
#     name, s = input().split()
#     if s == 'enter':
#         company.append(name)
#     else:
#         company.remove(name)
# company.sort(reverse=True)
# for i in company[0:]:
#     print(i)