'''
https://www.acmicpc.net/problem/13904

주제
'''
import heapq
import sys


input = lambda: sys.stdin.readline().rstrip()
N = int(input())
tasks = []
for _ in range(N):
    d, w = map(int, input().split())
    heapq.heappush(tasks, (-d, w))

last_day = -tasks[0][0]
answer = 0
tmp = []
for day in range(last_day, 0, -1):
    while tasks and -tasks[0][0] >= day:
        heapq.heappush(tmp, -heapq.heappop(tasks)[1])
    if tmp:
        answer -= heapq.heappop(tmp)
print(answer)
