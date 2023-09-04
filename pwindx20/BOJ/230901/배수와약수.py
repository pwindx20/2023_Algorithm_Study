# 5086
# 입력: 마지막 줄에는 0이 2개, 두 수가 같은 경우는 없다.
# 출력: 첫번째 숫자가 두번째 숫자의 약수라면 factor 배수라면 multiple, 둘다 아니라면 neither출력

while True:
    A, B = map(int, input().split())
    if not B:
        break
    if A%B == 0:
        print('multiple')
    elif B%A == 0:
        print('factor')
    else:
        print('neither')
    