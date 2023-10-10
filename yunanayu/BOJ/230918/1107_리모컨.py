import sys
sys.stdin = open('1107.txt','r')

N = int(input())
M = int(input())
if M != 0:
    # button = list(input().split())
    button = list(map(int, input().split()))
# print(button)
elif M == 0:
    print(len(list(str(N))))

if N == 100:
    print(0)
else:
    chan = list(str(N))
    cnt = len(chan)
    L = len(chan)
    # print(chan)
    for i in range(len(chan)):
        temp = int(chan[i])
        start = 1
        a = False
        if temp in button:
            while not a:
                temp1 = temp + start
                temp2 = temp - start
                if temp1 < 10 and temp2 >= 0 and temp1 not in button or temp2 not in button:
                    cnt += 1 * 10**(L-i-1)
                    a = True
                elif temp1 < 10 and temp2 >= 0:
                    start += 1
                    cnt += 1 * 10**(L-i-1)
        # else:
        #     cnt += 1
    print(cnt)