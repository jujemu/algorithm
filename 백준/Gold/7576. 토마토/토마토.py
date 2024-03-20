import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

M, N = map(int, input().split())
arr = [[-1] * (M + 2)] + [[-1] + list(map(int, input().split())) + [-1] for _ in range(N)] + [[-1] * (M + 2)]
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
q = []
ans = -1
cnt = 0

for i in range(1, N + 1):
	for j in range(1, M + 1):
		if arr[i][j] == 0:
			cnt += 1
		elif arr[i][j] == 1:
			q.append((i, j))

while q:
	new_q = []
	for i, j in q:
		for dy, dx in d:
			y, x = i + dy, j + dx
			if arr[y][x] == 0:
				cnt -= 1
				arr[y][x] = 1
				new_q.append((y, x))
	q = new_q
	ans += 1

print(ans if cnt == 0 else -1)
