import heapq
import sys
sys.stdin = open('./greedy/input_bj_1715.txt')
input = sys.stdin.readline

# input
N = int(input().rstrip())
cards = [int(input().rstrip()) for _ in range(N)]
flag = False if len(cards) == 1 else True
heapq.heapify(cards)

result = 0
while flag:
    tmp = heapq.heappop(cards) + heapq.heappop(cards)
    result += tmp
    if not cards:
        break
    heapq.heappush(cards, tmp)
print(result if flag else 0)
