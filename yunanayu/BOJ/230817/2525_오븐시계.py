A, B = map(int, input().split())    # 현재 시각
C = int(input())
B = B + C
if B >= 60:
    A = A + (B // 60)
    B = B % 60
    if A >= 24:
        A -= 24
print(A , B)