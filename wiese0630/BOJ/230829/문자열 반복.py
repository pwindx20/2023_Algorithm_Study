T = int(input())

for test_case in range(1, T+1):
    R, S = input().split()
    # print(R, S)

    ans = []
    for elem in S:
        ans. append(elem*int(R))
    # print(ans)

    rst = ''.join(ans)
    print(rst)