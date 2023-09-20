# 3085
# 입력: 보드의 크기 N(3~50)/ 사탕의 색상 C: 빨강 P: 파랑 Z: 초록 Y: 노랑
# 출력: 최대 사탕 개수


#### 시간초과 바꾼 행, 열만 체크하는 함수가 필요 #####
# from sys import stdin
# input = stdin.readline

# def check(arr):
#     color = ['C', 'P', 'Z', 'Y']
#     max_cnt = [0,0,0,0]
#     for c in range(4):
#         # 행 검색    
#         j = 0
#         temp1 = 0
#         for i in range(N):
#             while j<N:
#                 if arr[i][j] == color[c]:
#                     temp1 += 1
#                 else:
#                     if max_cnt[c] <temp1:
#                         max_cnt[c] = temp1
#                     temp1 = 0
#                 j += 1
#             if max_cnt[c] <temp1:
#                 max_cnt[c] = temp1
#             j = 0    
#             temp1 = 0
        
#         # 열 검색
#         i = 0
#         temp2 = 0
#         for j in range(N):
#             while i<N:
#                 if arr[i][j] == color[c]:
#                     temp2 += 1
#                 else:
#                     if max_cnt[c] <temp2:
#                         max_cnt[c] = temp2
#                     temp2 = 0
#                 i += 1
#             if max_cnt[c] <temp2:
#                 max_cnt[c] = temp2
#             i = 0
#             temp2 = 0
            
#     # print(arr)
#     # print(max_cnt)
#     return max(max_cnt)    
        

# N = int(input())
# arr = [list(input()) for _ in range(N)]
# result= 0
# for i in range(N):
#     for j in range(N):
#         if j<=N-2 and arr[i][j] != arr[i][j+1]:
#             arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
#             temp = check(arr)
#             if temp>result:
#                 result = temp
#             arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]

#         if i<=N-2 and arr[i][j] != arr[i+1][j]:
#             arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
#             temp = check(arr)
#             if temp>result:
#                 result = temp
#             arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]

# print(result)