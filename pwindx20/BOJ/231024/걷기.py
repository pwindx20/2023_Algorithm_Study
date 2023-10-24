# 1459
# 입력: 집의 위치 x, y, 걸어서 한블록 가는데 걸리는 시간 W, 대각선으로 가로지르는 시간 S
# 출력: 집에 가는 최소 시간

def mintime(x, y):
    global minT
    if (x==0) or (y==0): # 이걸  if (x and not y) or (y and not x): 이렇게 쓰면 오류
        if S<W:
            if (x+y)%2 == 0:
                minT += S * max(x, y)
            else:
                minT += W + S * (max(x, y)-1)
        else:
            minT += W * max(x, y)
        return
    
    if S< 2*W :
        if x == y:
            minT += S*x
        else:
            minT += S*min(x, y)
        mintime(X-min(x, y), Y-min(x, y))
    else:
        minT += W *(x+y)
    return
    
    
X, Y, W, S = map(int,input().split())
minT = 0
mintime(X, Y)
print(minT)


# if X==Y:
#     ans = X*min(W, S)

# elif 2*W>S:
#     if (X+Y)//2 == 0 and (X+Y)*W>(X+Y-1)*S:
#         ans = S*(X+Y-1)
#     else:
#         ans = S*min(X, Y)
#         ans += W*(X+Y-2*min(X, Y))
# else:
#     ans = W*(X+Y)
# print(ans)