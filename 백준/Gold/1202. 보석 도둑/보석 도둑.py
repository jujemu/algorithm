'''
https://www.acmicpc.net/problem/1202

주제: 그리디, heap

구현
 - 가방에는 한 개의 보석만 넣을 수 있다.
 - 가방의 무게를 내림차순으로 정렬하고 높은 가격의 보석을 순서대로 넣으면 되지 않을까?
    - 반례 존재 -> 가격 순으로 진행하되 넣을 수 있는 최소 무게 가방을 찾자.
    - 최소 무게 가방을 찾을 때, 선형 탐색으로 진행하면 N^2 -> 시간 초과
'''
import heapq
import sys


input = lambda: sys.stdin.readline().rstrip()
N, K = map(int, input().split())
jewels = [tuple(map(int, input().split())) for _ in range(N)]
backs = sorted([int(input()) for _ in range(K)])

heapq.heapify(jewels)

result = 0
tmp = []
for back in backs:
    while jewels and back >= jewels[0][0]:
        heapq.heappush(tmp, -heapq.heappop(jewels)[1])
    if tmp:
        result -= heapq.heappop(tmp)
print(result)
