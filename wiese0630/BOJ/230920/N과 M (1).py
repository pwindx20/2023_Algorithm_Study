# 자연수 N과 M을 입력으로 받습니다.
N, M = map(int, input().split())

# 수열을 저장할 리스트와 사용 여부를 저장할 리스트를 초기화합니다.
sequence = [0] * M
used = [False] * (N + 1)

# 재귀 함수를 사용하여 수열을 생성합니다.
def generate_sequence(index):
    if index == M:
        # 수열을 출력합니다.
        print(" ".join(map(str, sequence)))
        return

    for i in range(1, N + 1):
        if not used[i]:
            sequence[index] = i
            used[i] = True
            generate_sequence(index + 1)
            used[i] = False

# 수열 생성 함수 호출
generate_sequence(0)