# 11005
# 입력 N, B
# 출력 10진법수를 B진법으로 표시
N, B = map(int, input().split())
answer = ''
while N:
    temp = N%B
    if temp>9:
        answer= chr(temp+55)+answer
    else:
        answer = str(temp)+answer
    N//=B
print(answer)