import sys
sys.stdin = open('./implementation/input_bj_7568.txt')
input = sys.stdin.readline

# input
N = int(input().rstrip())
wl = [tuple(map(int, input().rstrip().split())) for _ in range(N)]
result = []

for w, l in wl:
    cnt = 0
    for x, y in wl:
        cnt += 1 if x>w and y>l else 0
    result.append(cnt+1)
print(*result)
            