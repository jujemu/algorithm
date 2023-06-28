import sys
sys.stdin = open('../input_01.txt')
n = int(input())
orders = input().split()

# orders can be
# L, R, U, D
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
order2idx = {
    'L': 0,
    'R': 1,
    'U': 2,
    'D': 3
    }

x, y = 1, 1
for idx, order in enumerate(orders):
    tmp_x = x + dx[order2idx[order]]
    tmp_y = y + dy[order2idx[order]]

    if tmp_x < 1 or tmp_x > n or tmp_y < 1 or tmp_y > n:
        continue
    x, y = tmp_x, tmp_y
    # print(idx, ': ', x, y)
print(y, x)
