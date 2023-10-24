def generate_permutations(arr, n, i):
    if i == n:
        print(" ".join(map(str, arr)))
    for j in range(i, n):
        # Swap the current element with itself and all the following elements
        arr[i], arr[j] = arr[j], arr[i]
        generate_permutations(arr, n, i + 1)
        # Undo the previous swap to backtrack
        arr[i], arr[j] = arr[j], arr[i]

# N을 입력으로 받습니다.
N = int(input())

# 1부터 N까지의 숫자 리스트를 생성합니다.
numbers = list(range(1, N + 1))

# 순열을 생성하고 출력합니다.
generate_permutations(numbers, N, 0)

#테케는 다 맞는데 틀렸다고 뜬다...
#뭐가 문젠지 모르겠음