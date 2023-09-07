from sys import stdin
input = stdin.readline

result = ['Scalene', 'Isosceles', 'Equilateral']
while True:
    lst = sorted(list(map(int, input().split())))
    arr = [0] * 3
    if lst.count(0) == 3:
        break
    if lst[0] + lst[1] > lst[2]:
        for i in range(1, 3):
            if lst[i] == lst[i - 1]:
                arr[i] = arr[i - 1] + 1
        print(result[max(arr)])
    else:
        print('Invalid')
