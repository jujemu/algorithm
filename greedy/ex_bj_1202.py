import bisect
import heapq
import sys
sys.stdin = open('./greedy/input_bj_1202.txt')
input = sys.stdin.readline

# input
N, K = map(int, input().rstrip().split())
jewels = sorted([tuple(map(int, input().rstrip().split())) for _ in range(N)], key=lambda x: x[1], reverse=True)
bags = heapq.heapify([int(input().rstrip()) for _ in range(K)])

result = 0
i = 0
while bags and i < N:
    w, v = jewels[i]
    i += 1
    
    idx = bisect.bisect_right(bags, w)
    if bags[idx-1] == w:
            idx -= 1
    if idx == len(bags):
        if bags[-1] >= w:
            idx -= 1
        else:
            continue
    
    bags.pop(idx)
    result += v
print(result)
