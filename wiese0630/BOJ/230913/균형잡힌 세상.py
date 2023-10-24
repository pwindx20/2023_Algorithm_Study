while True :    #while true 사용
    s = input()    
    result = 'yes'
    ST = [] #빈 스택 먼저 만들기
    if s == '.': #.만 들어오면 종료시킴
        break
    else:
        for c in s: # 인풋에서 원소 하나씩 뜯어감
            if c in ['(', '[']: #왼쪽 괄호면 집어넣음
                ST.append(c)
            elif c in [')', ']']: #오른쪽 괄호면
                if ST: #빈스택이 아니면
                    checkC = ST.pop() #가장 나중에 넣은 원소 가져옴
                    if c == ')' and checkC == '[':
                        result = 'no'
                        break
                    elif c == ']' and checkC == '(':
                        result = 'no'
                        break 
                else: #빈스택이면
                    result = 'no'        
                    break
  
    
    if ST:
        result = 'no'

    print(result)

    