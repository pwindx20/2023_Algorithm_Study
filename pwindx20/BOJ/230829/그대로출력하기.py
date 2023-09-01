# 11718
import sys
for line in sys.stdin:
    print(line.strip())
    
    
# ref) (https://developeryuseon.tistory.com/90)
#sys.stdin은 ^Z를 입력받으면 종료되며, 위 결과에서 보다시피 개행문자까지 입력되는걸 볼 수 있다.
# 따라서 strip()이나 rstrip()으로 제거해 주어야 한다.