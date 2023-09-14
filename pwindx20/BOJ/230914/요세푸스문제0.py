# 11866
# 입력: N, K
# 출력: 1~N번 원 K번째 사람을 제거 한 사람이 제거 되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해나간다.
# N명의 사람이 모두 제거될 때까지 제거되는 순서를 순열이라고 한다


N, K = map(int, input().split())
lst = list(range(1, N+1))
answer = []
cnt = 1
while lst:
    v = lst.pop(0)
    if cnt ==K:
        answer.append(v)
        cnt =1
    else:
        lst.append(v)
        cnt += 1
print('<'+', '.join(map(str, answer))+'>')