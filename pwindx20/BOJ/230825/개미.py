# 10158
# 가로길이가 w 세로가 h인 2차원 격자 공간, 좌표 (p,q)에 개미 한마리
# 개미는 오른쪽 위 45도 방향으로 일정한 속력/ 한시간 후에는 (p+1, q+1)
# 경계면에 부딪치면 같은 속력으로 반사된다.
# 개미의 t시간 후 위치 계산 후 출력
# w, h(2~40,000)/ p, q / t
# t시간 후 개미 위치 좌표(x,y)

W, H = map(int, input().split())
p, q = map(int, input().split())
T = int(input())

if T%(2*W) <=W-p:
    print(p+T%(2*W), end=' ')
elif W-p< T%(2*W) <2*W-p:
    print(2*W-(T%(2*W)+p), end=' ')
else:
    print(T%(2*W)-2*W+p, end=' ')

if T%(2*H) <=H-q:
    print(q+T%(2*H))
elif H-q< T%(2*H) <2*H-q:
    print(2*H-(T%(2*H)+q))
else:
    print(T%(2*H)-2*H+q)








########### 시간초과
# t = 0
# d = [1, 1]

# while t <T:
#     np = p+d[0]
#     nq = q+d[1]
#     if not(0 <= np <= W):
#         d[0] *= -1
#         np = p+d[0]
#     if not(0 <= nq <= H):
#         d[1] *= -1
#         nq = q+d[1]
#     p = np
#     q = nq
#     t += 1
#     # print(p, q)
# print(p, q)