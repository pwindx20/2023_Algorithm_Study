import sys
sys.stdin = open('input.txt', 'r')

def play():
    for i in range(4,0,-1):
        cnt_a = 0
        cnt_b = 0
        for r in A:
            if r == i:
                cnt_a += 1
        for c in B:
            if c == i:
                cnt_b += 1
        if cnt_a > cnt_b:
            return 'A'
        elif cnt_a < cnt_b:
            return 'B'
        elif cnt_a == cnt_b:
            continue
    return 'D'


def play2():
    for i in range(4,0,-1):
        if A.count(i) > B.count(i):
            return 'A'
        elif A.count(i) < B.count(i):
            return 'B'
        elif A.count(i) == B.count(i):
            continue
    return 'D'


N = int(input())
for _ in range(N):
    A = list(map(int, input().split()))
    a = A.pop(0)
    B = list(map(int, input().split()))
    b = B.pop(0)
    print(play2())