N, M = map(int, input().split())
S = {input().rstrip() for _ in range(N)}

result = 0
print(sum([True for _ in range(M) if input().rstrip() in S]))