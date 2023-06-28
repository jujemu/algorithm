N = int(input())
d = [5000] * 5001

d[3] = 1
d[5] = 1
for n in range(6, N+1):
    d[n] = min(d[n-3], d[n-5]) + 1
print(d[N] if d[N] < 5000 else -1)
