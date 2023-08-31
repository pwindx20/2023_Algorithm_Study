TC = int(input())
for tc in range(1, TC+1):
    R, S = input().split()
    for s in S:
        print(s*int(R), end='')
    print()


