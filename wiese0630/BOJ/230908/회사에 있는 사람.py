ans_set = set()

N = int(input())

for _ in range(N):
    name, action = input().split()
    if action == 'enter':
        ans_set.add(name)
    else:
        ans_set.remove(name)

new_set = sorted(ans_set, reverse=True)

for elem in new_set:
    print(elem)

#당연히 리스트로 문제풀었는데 시간초과가 여러번 나서 당황했다
#시간초과가 나면 set이나 dict로 풀자
#why 리스트 / set, dict 연산에 시간 차이가 나는가?

