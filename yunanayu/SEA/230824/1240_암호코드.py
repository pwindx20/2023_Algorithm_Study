import sys
sys.stdin = open('input.txt','r')


code_dct = {
            '0001101':0, 
            '0011001':1, 
            '0010011':2,
            '0111101':3,
            '0100011':4, 
            '0110001':5,
            '0101111':6,
            '0111011':7,
            '0110111':8,
            "0001011":9
            }
TC = int(input())
for tc in range(1, TC+1):
    N , M = map(int, input().split())
    arr = [input() for _ in range(N)]
    # print(arr)
    
    for i in range(N):
        if '1' in arr[i]:
            arr = arr[i:i+7]
            break          
    # print(arr)
    for i in range(M-1, -1, -1):
        if arr[0][i] == '1':
            arr = arr[0][i-55:i+1]
            break
    # print(len(arr))
    
    code_list = []
    for i in range(0,56,7):
        code = arr[i:i+7]
        code_list.append(code_dct[code])
    # print(ans)
    
    result_1 = 0
    result_2 = 0
    for c in range(len(code_list)):
        if c % 2 == 0:  # 홀수자리
            result_1 += code_list[c]
        else:   # 짝수자리
            result_2 += code_list[c]
    
    result = result_1*3 + result_2
    if result % 10 == 0:
        print(f'#{tc} {result_1 + result_2}')
    else:
        print(f'#{tc}', 0)
        
'''
#1 38 
#2 0 
#3 34
#4 28
#5 24
#6 26
#7 36
#8 30
#9 0
#10 34
'''