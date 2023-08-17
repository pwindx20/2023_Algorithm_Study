# 9498
# 입력: 시험점수
# 출력: 시험성적 90~100:A 80~89:B 70~79:C 60~69:D 나머지 F

grade = int(input())
if 90<=grade<=100:
    print('A')
elif 80<=grade<90:
    print('B')
elif 70<=grade<80:
    print('C')
elif 60<=grade<70:
    print('D')
else:
    print('F')