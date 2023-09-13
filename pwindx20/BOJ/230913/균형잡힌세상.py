# 4949
# 입력: 온점으로 끝나는 문자열 소괄호, 대괄호, 알파벳, 공백
# 출력: 각줄마다 해당 문자열이 균형을 이루고 있으면 'yes' 아니면 'no'

while True:
    strings = input()
    if strings =='.': break
    ST = []
    for s in strings:
        if s in '([':
            ST.append(s)
        elif s in ')]' and ST:
            v = ST[-1]
            if s==')' and v!='(':
                print('no')
                break
            elif s==']' and v!='[':
                print('no')
                break
            else:
                ST.pop()
        elif s in ')]' and not ST:
            print('no')
            break
    else:
        if ST:
            print('no')
        else:
            print('yes')