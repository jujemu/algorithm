"""
https://www.acmicpc.net/problem/14567
"""
from collections import deque
import sys


input = lambda: sys.stdin.readline().rstrip()
N, M = map(int, input().split())
prerequisites = [tuple(map(int, input().split())) for _ in range(M)]

# 선수과목을 저장한다.
# 매트릭스
# 행: 선수과목, 열: 과목
subjects = [[False] * (N + 1) for _ in range(N + 1)]
for A, B in prerequisites:
    subjects[A][B] = True

# 수강할 수 있는 과목들 저장 큐
q = deque()

# dp 초기화
dp = [0] * (N+1)
for idx in range(1, N+1):
    has_no_prerequisite = True
    for prerequisite in subjects:
        if prerequisite[idx]:
            has_no_prerequisite = False
            break
    
    if has_no_prerequisite:
        dp[idx] = 1
        q.append((idx, 1))

# 어떤 노드를 선택할까
# 최소? -> 힙 or 큐
# 큐로 해도 되는게, 우선순위가 앞쪽부터 보장이 된다.
while q:
    cur, cnt = q.popleft()

    if dp[cur] != cnt:
        continue

    for idx, is_pre in enumerate(subjects[cur]):
        if is_pre:
            dp[idx] = max(cnt+1, dp[idx])
            q.append((idx, cnt+1))

print(*dp[1:], sep=" ")
