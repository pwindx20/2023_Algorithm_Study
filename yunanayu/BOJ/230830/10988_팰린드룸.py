def room(item):
    if item == item[::-1]:
        return 1
    else:
        return 0


S = input()
print(room(S))