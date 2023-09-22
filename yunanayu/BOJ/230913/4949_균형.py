while True:
    text = input()
    if text == '.':
        break
    ST = []
    for t in text:
        if t in ['(', '[']:
            ST.append(t)
        else:
            if t == ')':
                if ST and ST[-1] == '(':
                    ST.pop()
                else:
                    ST.append(t)
                    break
            elif t == ']':
                if ST and ST[-1] == '[':
                    ST.pop()
                else:
                    ST.append(t)
                    break
                # else:
                #     ST.append(t)
    if ST:
        print('no')
    else:
        print('yes')
