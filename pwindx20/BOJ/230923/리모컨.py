# 1107
# 입력: N/ 고장난버튼의 개수 M(0~10)/ 고장난 버튼
# 출력: N으로 이동하기 위해 최소 몇번 눌러야하는지
# 현재 100번
def solve(k, num):
    global minv, button

    if k == len(N)-1 and not k==0:
        temp = abs(numN - int(num))
        if temp <= minv:
            minv = temp
            if temp +len(str(int(num))) <button:
                button = temp +len(str(int(num)))
        
    
    if k == len(N):
        temp = abs(numN - int(num))
        if temp <= minv:
            minv = temp
            if temp +len(str(int(num))) <button:
                button = temp +len(str(int(num)))
        
    
    if k == len(N)+1:
        temp = abs(numN - int(num))
        if temp <= minv:
            minv = temp
            if temp +len(str(int(num))) <button:
                button = temp +len(str(int(num)))
        return
    

    for i in arr:
        # if k == 0 and i==0:
        #     continue
        solve(k+1, num+str(i))
        

N = input()
numN = int(N)
M = int(input())
arr = [i for i in range(10)]
if M:
    for i in map(int,input().split()):
        arr.remove(i)
minv = abs(numN-100)+1
button = minv
if N == '100':
    print(0)
elif N == '99' or N == '101':
    print(1)
elif N == '102':
    print(2)
else:
    solve(0, '0')
    if button>abs(100-numN):
        button = abs(100-numN)
    print(button)    


