answer = [None] * (15*5)
for i in range(5):
    for j, c in enumerate(input()):
        answer[i+j*5] = c
for c in answer:
    if c is not None:
        print(c, end="")