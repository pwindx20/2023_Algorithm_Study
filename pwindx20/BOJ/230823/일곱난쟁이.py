# 2309
# 입력: 아홉 개의 키
# 출력: 진짜 난쟁이 7명 (키 합이 100)

height = [int(input()) for _ in range(9)]

for i in range(1<<9):
    cnt = 0
    part = []
    for j in range(9):
        if i & 1<<j:
            cnt += 1
            part.append(height[j])
    # print(part)
    if cnt == 7 and sum(part)==100:
        for x in sorted(part):
           print(x)
        break # break 를 안해서 정답이 여러개이면 여러개 출력됨