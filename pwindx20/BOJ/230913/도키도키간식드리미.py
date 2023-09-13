# 12789
# 입력: 서있는 학생 수 N/ 번호표가 앞에서부터 차례대로
# 출력: 'Nice' or 'Sad'

N = int(input())
ST1=list(map(int,input().split()))
ST2=[]
picked = 0

while True:
    if ST1 and ST1[0] == picked+1:    
        ST1.pop(0)
        picked += 1
    elif ST2 and ST2[-1] == picked+1:
        ST2.pop()
        picked += 1
    elif not ST1 and not ST2:
        break
    elif not ST1 and ST2[-1] != picked+1:
        break
    else:
        ST2.append(ST1.pop(0))

if ST2:
    print('Sad') # sad 라고 씀... sad...:(
else: print('Nice')