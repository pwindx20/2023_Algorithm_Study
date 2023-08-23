T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    cheese = [0] + list(map(int, input().split()))
    pans = [0] * N

    newPizza = 1
    while pans:
        # 1번 화덕에서 빼서
        pizzaNo = pans.pop(0)
        #치즈량 감소
        cheese[pizzaNo] //= 2
        # if 치즈량이 0이면:
        if cheese[pizzaNo] == 0:
            # 화덕에 넣을 피자가 있으면 새피자를 화덕에
            if newPizza <= M:
                pans.append(newPizza)
                newPizza += 1
        else:
            pans.append(pizzaNo)


    print(f'#{test_case} {pizzaNo}')
