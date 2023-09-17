# 10951
import sys
while True:
    try:
        a, b =map(int, input().split())
        print(a+b)
    except EOFError:
        break
    

# 다른 사람 방식
# import sys

# lines = sys.stdin.readlines()
# for line in lines:
#     A, B = map(int, line.split())
#     print(A+B)

# sys.stdin.readlines() 구문을 사용하면 파일의 끝 부분까지 한번에 가져올 수 있고,
#  가져온 내용 안에서 반복문을 사용하면 쉽게 문제를 해결할 수 있습니다.