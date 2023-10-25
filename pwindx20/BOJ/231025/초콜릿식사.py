# 2885
# 입력: 정사각형의 개수 K
# 출력: 상근이가 구매해야하는 가장 작은 초콜릿의 크기와 최소 몇번 쪼개야하는지
# 초콜릿은 정사각형 N개로 이루어져있다. 초콜릿의 크기는 항상 2^N 형태
# 적어도 K개 정사각형이 되도록 초콜릿을 쪼갠다.
# 정사각형이 D개 있는 막대는 D/2 막대 두조각으로 쪼개진다
# 여러개 합쳤을 때 K개
K = int(input())
binary = bin(K)[2:]
N = len(binary)
divide = 0
if int(binary[1:]) == 0:
    print(2**(N-1), 0)
else:
    for i, v in enumerate(binary, start=1):
        if v == '1':
          divide = i  
    print(2**N,divide)
