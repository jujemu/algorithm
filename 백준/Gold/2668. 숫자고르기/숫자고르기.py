import sys


def dfs(curr):
    global answer

    a, b = arr[curr]
    s_1.add(a)
    s_2.add(b)
    if s_1 == s_2:
        answer |= s_1

    elif len(s_1) == len(s_2):
        dfs(b)


input = lambda: sys.stdin.readline().rstrip()
N = int(input())
arr = [[i, 0] for i in range(N+1)]
for i in range(1, N+1):
    arr[i][1] = int(input())

answer = set()
for i in range(1, N+1):
    s_1, s_2 = set(), set()
    dfs(i)

print(len(answer))
print(*sorted(answer), sep="\n")
