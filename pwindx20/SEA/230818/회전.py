# 5097
# 입력: T (1~50)/ 개수 N (1000이하) 뒤로보내는 횟수 M (1000이하)/ 10억 이하 자연수 N개
# 출력: #t 가장 앞에 있는 숫자
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    print(f'#{tc} {numbers[M%N]}')
    
    # for _ in range(M):
    #     a = numbers.pop(0)
    #     numbers.append(a)
    # print(f'#{tc} {numbers.pop(0)}')