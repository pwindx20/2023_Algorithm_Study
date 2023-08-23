import sys
sys.stdin = open('input2605.txt', 'r')

T = int(input())
stu = []
for i in range(1, T+1):
    stu.append(i)
# print(stu)
numbers = list(map(int, input().split()))
lst = []
p = 0
for i in range(T):
    numbers[i] = p
    lst = lst[0:p] + [i] + lst[p+1:T]
print(lst)
# 빈 리스트에서 하나씩 추가해나가야할지
# 아니면 stu 5명끼리 순서를 바꿔나가야할지 모르겠다.

