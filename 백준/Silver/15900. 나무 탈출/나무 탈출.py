'''
https://www.acmicpc.net/problem/15900

주제

구현
임의로 루트 노드를 1로 정하고
부모-자식 관계를 풀어낸다.
각 리프 노드의 레벨을 구해서 더하고 홀수면 이길 수 있다.
'''
import sys
sys.setrecursionlimit(500_001)
input = lambda: sys.stdin.readline().rstrip()


N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

leaf = {}
stack = [(1, 0)]
while stack:
    cur, level = stack.pop()

    if not tree[cur]:
        leaf[cur] = level

    for child in tree[cur]:
        tree[child].remove(cur)
        stack.append((child, level+1))
print("Yes" if sum(leaf.values()) % 2 else "No")
