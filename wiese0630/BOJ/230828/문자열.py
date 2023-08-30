T = int(input())

for test_case in range(1, T+1):
    str = input()
    fst = str[0]
    lst = str[len(str)-1]

    print(fst+lst)