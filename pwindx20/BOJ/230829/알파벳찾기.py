# 10809
# 입력: 단어 S 
# 출력: a, b, c, d, e,---가 처음 등장하는 위치를 공백으로 출력 없으면 -1
S = input().strip()
for i in range(97, 123):
    print(S.find(chr(i)), end = ' ')