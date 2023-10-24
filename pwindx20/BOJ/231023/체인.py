# 2785

# 입력: 체인의 개수 N (2~500000)/ 체인의 길이를 나타내는 N개의 양의정수 Li (1~1000000)
# 출력: 연결에 필요한 최소 고리 개수

N = int(input())
chain_lst = sorted(list(map(int, input().split())))
remain = N-1
answer = 0
while chain_lst:
    # print(remain, answer)
    # print(chain_lst)
    chain = chain_lst.pop(0)
    if chain >= remain-1:
        answer += remain-1
        break
    else:
        answer += chain
        remain -= chain
if not answer:
    answer = 1
print(answer)
        