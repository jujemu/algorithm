'''
https://www.acmicpc.net/problem/2075


'''
import heapq


N = int(input())

heap = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    for t in tmp:
        if len(heap) < N:
            heapq.heappush(heap, t)
        elif heap[0] < t:
            heapq.heappop(heap)
            heapq.heappush(heap, t)
print(heap[0])
