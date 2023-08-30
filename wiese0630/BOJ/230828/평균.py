N = int(input())
s_list = list(map(int, input().split()))

M = max(s_list)

new_list = []

for score in s_list:
    new_list.append(score/M*100)


print(sum(new_list)/N)