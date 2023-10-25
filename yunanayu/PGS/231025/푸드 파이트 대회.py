food = [1, 7, 1, 2]
ans = '0'
for i in range(len(food)-1, 0, -1):
    # print(i)
    for _ in range(food[i]//2):
        ans += str(i)
        ans = str(i) + ans
print(ans)
