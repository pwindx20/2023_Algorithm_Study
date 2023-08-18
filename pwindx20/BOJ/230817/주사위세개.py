# 2480
# 입력: 주사위 3개의 눈
# 출력: 같은 눈 3개: 10000+같은눈*1000원 / 같은눈 2개: 1000원+같은눈 *100/ 모두 다른눈: 가장 큰 눈 *100

my_lst = sorted(list(map(int, input().split())))
if my_lst[0]== my_lst[2]:
    print(10000+my_lst[0]*1000)
elif my_lst[0]==my_lst[1] or my_lst[1] == my_lst[2]:
    print(1000+my_lst[1]*100)
else:
    print(100*my_lst[2])