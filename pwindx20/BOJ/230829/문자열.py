# 9086
# 입력: T/ 문자열
# 출력: 첫글자와 마지막글자를 연속으로 출력
T = int(input())
for _ in range(T):
    s = input()
    print(f'{s[0]}{s[-1]}')