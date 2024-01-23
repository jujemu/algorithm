'''
https://www.acmicpc.net/problem/15681


'''
import sys
sys.setrecursionlimit(100_001)
input = lambda: sys.stdin.readline().rstrip()


def find_tree(parent, cur):
    for child in adj[cur]:
        if child == parent:
            continue
        find_tree(cur, child)
        tree[cur].append(child)


def calculate_sub_total_cnt(cur):
    if cur in node_to_total_sub_cnt:
        return node_to_total_sub_cnt[cur]

    if not tree[cur]:
        node_to_total_sub_cnt[cur] = 1
        return 1

    total = 1
    for child in tree[cur]:
        total += calculate_sub_total_cnt(child)
    node_to_total_sub_cnt[cur] = total
    return total


N, R, Q = map(int, input().split())

adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    U, V = map(int, input().split())
    adj[U].append(V)
    adj[V].append(U)

tree = [[] for _ in range(N+1)]
find_tree(None, R)

node_to_total_sub_cnt = {}
calculate_sub_total_cnt(R)

result = []
for _ in range(Q):
    result.append(calculate_sub_total_cnt(int(input())))
print(*result, sep="\n")
