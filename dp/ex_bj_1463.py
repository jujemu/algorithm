N = int(input())
d = [0] * (int(1e6)+1)

for n in range(2, N+1):
    d[n] = d[n-1]
    if not n % 3:
        d[n] = min(d[n//3], d[n])
    if not n % 2:
        d[n] = min(d[n//2], d[n])
    d[n] += 1
print(d[N])
