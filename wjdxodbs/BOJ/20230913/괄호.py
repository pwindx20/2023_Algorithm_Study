from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    stack = []
    arr = input().strip()
    for i in arr:
        if not len(stack) or i == '(':
            stack.append(i)
        elif i == ')' and stack[-1] == '(':
            stack.pop()
    print('NO' if len(stack) else 'YES')