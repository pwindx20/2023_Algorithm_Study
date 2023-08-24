# 13300
# 남/여/같은학년/한방에 한명만 배정도 가능
# 한 방에 배정할 수 있는 최대 인원수 K, 필요한 최소 방의 개수
# 입력: 수학여행 참가하는 학생 N(1~1000) 최대 인원수 K (~1000)/ N개 줄 성별 S(0:여학생, 1:남학생) 학년 Y(1~6) 
# 출력: 최소 방의 수

N, K = map(int, input().split())
student_data = [[0, 0] for _ in range(7)]
for _ in range(N):
    S, Y = map(int, input().split())
    student_data[Y][S] += 1

cnt = 0
for grade in student_data:
    cnt += (grade[0]+K-1)//K
    cnt += (grade[1]+K-1)//K

print(cnt)