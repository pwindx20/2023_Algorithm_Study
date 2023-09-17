def game(p1, p2):
    ans = 0
    if lst[p1] == lst[p2]:
        if p1 < p2:
            ans = p1
        else:
            ans = p2
    elif [lst[p1], lst[p2]] in [[1, 2], [2, 3], [3, 1]]:
        ans = p2
    else:
        ans = p1
    return ans

def winner(s, e):
    if s == e:
        return s
    else:
        lefwinner = winner(s, (s+e)//2)
        rigwinner = winner((s+e)//2+1, e)
        t = game(lefwinner, rigwinner)
        return t




T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    lst = [0] + list(map(int, input().split()))
    print(f'#{test_case} {winner(1, N)}')