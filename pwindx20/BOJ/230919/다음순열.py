# 10972
# 입력: N/ 순열
# 출력: 다음 순열...

N = int(input())
arr = list(map(int,input().split()))
if arr == list(range(N, 0, -1)):
    print(-1)
else:
    idx = arr.index(N)
    isF = False
    for i in range(N-1, idx-1):
        for j in range(i, idx-1):
            if arr[i]>arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                print(*arr)
                isF = True
                break
        if isF:
            break
    else:
        print()  
        # 흠.. 모르겠다.       
        



# 재귀깊이 때문에 런타임에러인듯
# def per(k, target):
#     global temp
#     if target == [-1]+list(range(N,0,-1)):
#         print(-1)
#         return 
    
#     if k==N+1:
#         # print('temp:', temp)
#         if temp == target:
#             print(*result[1:])
#             return 1
#         temp = result[:]
#         return 0
    
#     for i in range(1,N+1):
#         if not used[i]:
#             result[k] = i
#             used[i] = True
#             a = per(k+1, target)
#             if a:
#                 break
#             used[i] = False

# N = int(input())
# arr = [-1] +list(map(int,input().split()))
# result = [-1]*(N+1)
# temp = []
# used = [False]*(N+1)
# per(1, arr)
# # print(arr)