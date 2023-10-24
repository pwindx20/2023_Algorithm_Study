<<<<<<< HEAD
N = int(input())
perm = list(map(int, input().split()))
sorted_perm = sorted(perm)
if perm == sorted_perm:
    print(-1)
=======
# 입력 받기
N = int(input())
permutation = list(map(int, input().split()))

# 이전 순열 찾기
i = N - 2 #**여기서 왜 N-2부터 시작하는지 모르겠음
while i >= 0 and permutation[i] <= permutation[i + 1]:
    i -= 1

if i == -1:
    print(-1)  # 사전순으로 가장 처음에 오는 순열인 경우
else:
    j = N - 1
    while permutation[j] >= permutation[i]:
        j -= 1

    # i번째 숫자와 j번째 숫자를 swap
    permutation[i], permutation[j] = permutation[j], permutation[i]

    # i+1부터 마지막 숫자까지 뒤집기
    left, right = i + 1, N - 1
    while left < right:
        permutation[left], permutation[right] = permutation[right], permutation[left]
        left += 1
        right -= 1

    # 결과 출력
    print(" ".join(map(str, permutation)))
>>>>>>> eb59f5467df51664d25d347e8573b5f881cc5d25
