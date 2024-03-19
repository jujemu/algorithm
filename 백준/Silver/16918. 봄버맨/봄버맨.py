R, C, N = map(int, input().split())
g = []
flag = 1
for _ in range(R):
    line = []
    for c in input():
        line.append(flag if c == "O" else 0)
    g.append(line)

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

N -= 1
for t in range(N):
    # 폭탄 설치하는 시기
    if t % 2 == 0:
        flag *= -1
        for i in range(R):
            for j in range(C):
                if not g[i][j]:
                    g[i][j] = flag

    # 폭탄이 터지는 시기
    else:
        for i in range(R):
            for j in range(C):
                # 바로 직전에 설치한 폭탄이 아닐 때
                if g[i][j] == flag * -1:
                    g[i][j] = "boom"

        for i in range(R):
            for j in range(C):
                if g[i][j] == "boom":
                    for d in range(4):
                        ni, nj = i + di[d], j + dj[d]
                        if 0 <= ni < R and 0 <= nj < C and g[ni][nj] != "boom":
                            g[ni][nj] = 0
        for i in range(R):
            for j in range(C):
                if g[i][j] == "boom":
                    g[i][j] = 0

for i in range(R):
    for j in range(C):
        print("O" if g[i][j] else ".", end="")
    print()
