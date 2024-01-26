'''
https://www.acmicpc.net/problem/13975

주제
'''
import heapq
import sys

input = lambda: sys.stdin.readline().rstrip()
answer = []
T = int(input())
for _ in range(T):
    _ = int(input())
    chapters = list(map(int, input().split()))

    heapq.heapify(chapters)

    result = 0
    while True:
        min_chapter = heapq.heappop(chapters)
        second_min_chapter = heapq.heappop(chapters)

        cur_sum = min_chapter + second_min_chapter
        result += cur_sum

        if not chapters:
            break
        heapq.heappush(chapters, cur_sum)
    answer.append(result)
print(*answer, sep="\n")
