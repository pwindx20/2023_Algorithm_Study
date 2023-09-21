#input
N = int(input())
nPr = list(map(int, input().split()))

def next_permutation(arr):
    # 1. 오른쪽에서 왼쪽으로 이동하며 첫 번째로 꺾이는 위치(i-1) 찾기
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    
    # 이미 사전순으로 가장 큰 순열인 경우 종료
    if i == 0:
        return False
    
    # 2. 꺾인 위치(i-1)의 값보다 크면서 가장 가까운 값(j) 찾기
    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1
    
    # 3. 교환
    arr[i - 1], arr[j] = arr[j], arr[i - 1]
    
    # 4. 꺾인 위치(i-1) 이후의 순열을 뒤집어서 사전순으로 최소로 만들기
    arr[i:] = reversed(arr[i:])
    
    return True

def generate_lexicographic_permutations(arr):
    arr.sort()  # 초기 순열은 오름차순으로 정렬
    while True:
        ans_list.append(arr)
        if not next_permutation(arr):
            break

numbers = list(range(1, N + 1))
generate_lexicographic_permutations(numbers)
ans_list = []

for i in range(N):
    if ans_list[i] == nPr:
        print(i)
        break
    print(-1)