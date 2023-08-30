# 1157
# 입력: 알파벳 대소문자
# 출력: 가장 많이 사용된 알파벳을 대문자로 출력, 여러개일시 ? 출력
S = list(input().upper())
N = dict()
for i in range(len(S)):
    