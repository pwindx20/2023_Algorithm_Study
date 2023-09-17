T = int(input())

for test_case in range(1, T + 1):
    A, B = map(int, input().split())
    sum = A + B

    print(f'Case #{test_case}: {sum}')
