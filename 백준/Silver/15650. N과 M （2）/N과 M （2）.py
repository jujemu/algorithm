n, m = map(int, input().split())
data = []


def combination(pre_num):
    if len(data) == m:
        print(*data)
    else:
        for i in range(1, n+1):
            if pre_num < i:
                data.append(i)
                combination(i)
                data.pop()


combination(0)