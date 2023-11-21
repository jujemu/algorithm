N = int(input())
d = {
    1: 1,
    2: 0,
    3: 1
}

# top-down
def solve(n):
    if n not in d:
        d[n] = 0 if solve(n-1) and solve(n-3) else 1
    return d[n]

# bottom-up
def solve(N):
    if N in d:
        return d[N]
    
    for n in range(4, N+1):
        d[n] = 0 if d[n-1] and d[n-3] else 1
    return d[N]

print('SK' if solve(N) else 'CY') # if N is 5, 'SK'

