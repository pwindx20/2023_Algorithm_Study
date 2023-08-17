# 2588
# 입력: 세자리수/ 세자리수
# 출력: 중간 계산값/ 최종계산값
fst = int(input())
snd = int(input())
print(fst*(snd%10))
print(fst*(snd//10%10))
print(fst*(snd//100%10))
print(fst*snd)