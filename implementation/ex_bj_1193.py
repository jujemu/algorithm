X = int(input())

i = 1
while True:
    if X > i:
        X -= i
        i += 1
    else:
        X -= 1
        if i % 2:
            r, c = i, 1
            dir = -1, 1
        else:
            r, c = 1, i
            dir = 1, -1
        while X:
            r += dir[0]
            c += dir[1]
            X -= 1
        break
print(f'{r}/{c}')
