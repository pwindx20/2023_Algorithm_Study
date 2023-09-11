# 10816
# 입력: 숫자카드 개수 N/ 숫자카드에 적혀있는 정수/ M 
#       / 상근이가 몇개 가지고 있는 숫자카드인지 구해야할 M개의 정수
# 출력: M개의 수에 대해 각 수가 적힌 숫자카드를 상근이가 몇개 가지고 있는지 공백으로 구분 출력
import sys
N = int(sys.stdin.readline())
card_dict = {}
for i in sys.stdin.readline()[:-1].split():
    if i in card_dict:
        card_dict[i] = card_dict[i]+ 1
    else:
        card_dict[i] = 1
M = int(sys.stdin.readline())
for i in list(sys.stdin.readline()[:-1].split()):
    if i in card_dict:
        print(card_dict[i], end=' ')
    else:
        print(0, end=' ')