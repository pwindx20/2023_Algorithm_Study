# 2875
# 입력: 여학생 N, 남학생 M, 인턴쉽에 참여해야하는 인원 K 여2남1
# 출력: 만들 수 있는 팀의 최대 개수

N, M, K = map(int,input().split())

team = 0
if N>2*M+K:
    team = M
else:
    for i in range(K+1):
        if N-i > 2*(M-(K-i)):
            temp = (M-(K-i))
        else:
            temp = (N-i)//2
        if team<temp:
            team = temp

print(team)