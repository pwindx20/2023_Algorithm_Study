# 1223 [S/W 문제해결 기본] 6일차 - 계산기2
# 입력: 길이/ 계산식 연산자: +, * , 피연산자: 0 ~ 9
# 출력: #t 계산값 후위표기식>변환식 계산 

for tc in range(1):
    N = int(input())
    ST = []
    icp = {'+':1, '*':2}
    result = ''

    # step1 후위표기식으로 변환
    for c in input():
        if c.isdigit():
            result = result + c
        else:
            if not ST:
                ST.append(c)
            else:
                bc = ST.pop()
                if icp[bc] >= icp[c]:
                    while ST:
                        result = result + bc
                        bc = ST.pop()
                else:
                    ST.append(bc)
                ST.append(c)
          
    while ST:
        result = result +ST.pop()
    print(result)