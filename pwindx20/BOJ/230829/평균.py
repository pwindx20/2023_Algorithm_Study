# 1546
N = int(input())
score = list(map(int, input().split()))
max_score = max(score)
print(sum(score)/(N*max(score))*100)