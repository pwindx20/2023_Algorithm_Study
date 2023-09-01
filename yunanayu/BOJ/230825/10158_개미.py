import sys
sys.stdin = open('input.txt','r')


TC = int(input())
for tc in range(1,TC+1):
    W, H = map(int, input().split())    # 격자 크기 가로 세로
    P, Q = map(int, input().split())    # 개미 출발 위치
    T = int(input())    # 개미가 움직일 시간

    a = (P + T) // W
    b = (Q + T) // H

    if a % 2 == 0:
        p = (P+T) % W
    else:
        p = W - (P+T) % W

    if b % 2 == 0:
        q = (Q+T) % H
    else:
        q = H - (Q+T) % H

    print(p, q)