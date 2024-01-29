def row_col(p):
    if p <= n:
        return p-1, 0, 0
    elif p <= n+m:
        return n-1, p-n-1, 1
    elif p <= 2*n+m:
        return n-(p-(n+m)), m-1, 0
    else:
        return 0, m-(p-(2*n+m)), 1


n, m = map(int, input().split())
li = []
result = []
for _ in range(n):
    li.append(list(map(int, input().split())))

sw = True
for i in range(1, 2*(n+m)+1):
    row, col, s = row_col(i)
    if sw and i > n+m:
        sw = False
    if sw:
        d = ((0, 1), (-1, 0))
    else:
        d = ((0, -1), (1, 0))
    direction = d[s]

    while True:
        #print("i, row, col :", i, row, col)
        if li[row][col] == 0:
            row += direction[0]
            col += direction[1]
        else:
            if s == 1:
                s = 0
                direction = d[s]
            else:
                s = 1
                direction = d[s]
            row += direction[0]
            col += direction[1]

        if not(0<=row<n and 0<=col<m):
            if row == -1:
                result.append(2*(n+m)-col)
            elif row == n:
                result.append(col+n+1)
            elif col == -1:
                result.append(row+1)
            else:
                result.append(2*n+m-row)
            break
print(*result)
