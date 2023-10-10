N = int(input())


def check(line):
    arr = []
    for l in line:
        if l == ")":
            if arr:
                arr.pop()
            else:
                return False
        else:
            arr.append(l)
    return False if arr else True


for _ in range(N):
    line = input()
    print("YES" if check(line) else "NO")
