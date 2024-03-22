import sys


input = lambda: sys.stdin.readline().rstrip()
N, d, k, c = map(int, input().split())
foods = [int(input()) for _ in range(N)]
window_size = len(foods)
foods += foods

unique = 0
eaten = [0] * (d+1)
for i in range(k):
    curr = foods[i]
    if not eaten[curr]:
        unique += 1
    eaten[curr] += 1
max_value = unique
if not eaten[c]:
    max_value += 1

for i in range(window_size):
    left = foods[i]
    eaten[left] -= 1
    if not eaten[left]:
        unique -= 1

    right = foods[i + k]
    if not eaten[right]:
        unique += 1
    eaten[right] += 1

    if not eaten[c]:
        max_value = max(unique+1, max_value)
    else:
        max_value = max(unique, max_value)

print(max_value)
