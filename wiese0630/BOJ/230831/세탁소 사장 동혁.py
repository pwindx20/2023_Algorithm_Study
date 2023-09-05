T = int(input())

for test_case in range(1, T+1):
    C = int(input())

    Q = C//25
    D = (C%25) // 10
    N = ((C%25)%10) // 5
    P = (((C%25)%10)%5)

    print(Q, D, N, P)