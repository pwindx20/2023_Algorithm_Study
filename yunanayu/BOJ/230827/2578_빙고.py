import sys
sys.stdin = open('input.txt','r')


def bingo():
    global ans
    global bin
    for l in lst:
        for r in range(5):
            for c in range(5):
                if arr[r][c] == l:
                    arr[r][c] = 0
                    ans += 1
                for i in range(5):
                    if arr[i] == [0,0,0,0,0]:
                        bin += 1
                # for i in range(5):
                #     cnt = 0
                #     for j in range(5):
                #         if arr[i] == 0:
                #             cnt += 1
                #     if cnt == 5:
                #         bin += 1
                        # if bin == 3:
                        #     return ans
                for n in range(5):
                    cnt2 = 0
                    for m in range(5):
                        if arr[m][n] == 0:
                            cnt2 += 1
                    if cnt2 == 5:
                        bin += 1
                        # if bin == 3:
                        #     return ans
                cnt3 = 0
                for a, b in [(0,0), (1,1), (2,2), (3,3),(4,4)]:
                    if arr[a][b] == 0:
                        cnt3 += 1
                if cnt3 == 5:
                    bin += 1
                        # if bin == 3:
                        #     return ans
                cnt4 = 0
                for c, d in [(0,4), (3,1), (2,2), (1,3),(0,4)]:
                    if arr[c][d] == 0:
                        cnt4 += 1
                if cnt4 == 5:
                    bin += 1
                        # if bin == 3:
                        #     return ans
            if bin >= 3:
                return ans

arr = [list(map(int, input().split())) for _ in range(5)]
arr2 = [list(map(int, input().split())) for _ in range(5)]
lst = []
for r in range(5):
    for c in range(5):
        lst.append(arr2[r][c])

ans = 0
bin = 0
print(bingo())
