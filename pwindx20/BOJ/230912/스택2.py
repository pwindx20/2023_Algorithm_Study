#28278
# 입력: N/ N줄에 명령이 하나씩
# 출력: 명령의 결과
# 1 X: 정수 X를 스택에 넣는다 / 2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1 출력/
# 3: 스택에 들어있는 정수의 개수 출력/ 4: 스택이 비어있으면 1, 아니면 0/ 5: 스택에 정수가 있다면 맨 위 정수 출력 없다면 -1
import sys
N = int(sys.stdin.readline())
ST = []
for _ in range(N):
    order = sys.stdin.readline()
    print('order, ST', order, ST)
    if order[0] =='1':
        o, num = order.split()
        ST.append(int(num))
    elif order[0] == '2':
        if not ST:
            print(-1)
        else:
            while len(ST)>1:
                print(ST.pop(0), end='')
            print()
    elif order[0] =='3':
        print(len(ST))
    elif order[0] =='4':
        if ST:
            print(0)
        else: print(1)
    else:
        if ST:
            print(ST.pop())
        else:
            print(-1)