'''
https://www.acmicpc.net/problem/12764

주제: 힙

구현
- 시작 시간과 종료 시간이 겹치는 경우는 없다.
'''
import heapq
import sys


input = lambda: sys.stdin.readline().rstrip()
N = int(input())
time_table = []
for _ in range(N):
    P, Q = map(int, input().split())
    time_table.extend([((P, 0), "start"), ((Q, P), "end")])
time_table.sort()

use_count = [0] * 100_000
computer_available = list(range(100_000))
heapq.heapify(computer_available)
uses = {}
for time, kind in time_table:
    if kind == "start":
        cur = heapq.heappop(computer_available)
        use_count[cur] += 1
        uses[time[0]] = cur
    elif kind == "end":
        end, start = time
        heapq.heappush(computer_available, uses[start])
        uses[start] = None

result = []
for cnt in use_count:
    if not cnt:
        break

    result.append(cnt)
print(len(result))
print(*result)
