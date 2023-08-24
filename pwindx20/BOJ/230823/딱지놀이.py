# #14696
# # 입력: 총라운드 수 N (1~1000)/ 라운드1 A 딱지에 나온 그림의 총 개수 a (1~100)
# #       + a개의 정수 : A가 낸 딱지 그림 1, 2,3 , 4 / b(1~100) +
# #       B 딱지에 나온 그림의 총 개수 (4, 3, 2, 1)
# # 출력: N줄 A, B, D-무승부
# # 별 4, 동그라미 3, 네모 2, 세모 1 < 우선순위 많은쪽이 이김

# N= int(input())
# for _ in range(N):
#     a_lst = list(map(int, input().split()))[1:]
#     b_lst = list(map(int, input().split()))[1:]
#     print(a_lst, b_lst)
#     if 4 in a_lst or 4 in b_lst:
#         if a_lst.count(4) != b_lst.count(4):
#             print('A') if a_lst.count(4)> b_lst.count(4) else print('B')
#             continue
#     if 3 in a_lst or 3 in b_lst:
#         if a_lst.count(3) != b_lst.count(3):
#             print('A') if a_lst.count(3)> b_lst.count(3) else print('B')
#             continue
#     if 2 in a_lst or 2 in b_lst:
#         if a_lst.count(2) != b_lst.count(2):
#             print('A') if a_lst.count(2)> b_lst.count(2) else print('B')
#             continue
#     if 1 in a_lst or 1 in b_lst:
#         if a_lst.count(1) != b_lst.count(1):
#             print('A') if a_lst.count(1)> b_lst.count(1) else print('B')
#         else:
#             print('D')

a= [1,2]
print(1 in a)