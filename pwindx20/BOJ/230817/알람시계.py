# 2884
# 입력: H, M (0~23, 0~59), 불필요한 0 사용X
# 출력: 알람을 45분 앞서는 시간으로 바꿨을 때 설정해야하는 알람 시간 입력과 같은 형태로 출력

H, M = map(int, input().split())
if M<45:
    newH = H-1 if H>0 else 23
    newM = 15+M
else:
    newH = H
    newM = M-45
print(newH, newM)