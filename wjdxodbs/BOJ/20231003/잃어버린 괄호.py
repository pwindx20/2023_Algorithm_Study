a = input()
arr = []
save = '0'
n = 0
while n < len(a):
    if a[n] == '+':
        n += 1
        save1 = ''
        while n < len(a) and a[n] not in ['+', '-']:
            save1 += a[n]
            n += 1
        else:
            save = f'{int(save)+int(save1)}'
    elif a[n] == '-':
        arr.append(int(save))
        save = '0'
        n += 1
    else:
        save += a[n]
        n += 1
else:
    arr.append(int(save))

save2 = arr[0]
for i in range(1, len(arr)):
    save2 -= arr[i]
print(save2)