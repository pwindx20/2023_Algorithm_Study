T = int(input())


for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    people = list(map(int, input().split()))
    sorted_people = sorted(people)
    # print(sorted_people)
    status = 'Possible'

    for idx in range(N):
        made_bun = (sorted_people[idx]//M)*K
        sold_bun = idx
        stock = made_bun - sold_bun
        if stock > 0:
            continue
        else:
            status = 'Impossible'
            break


    print(f'#{test_case} {status}')