'''
https://www.acmicpc.net/problem/1068


'''
N = int(input())
tree_parent = list(map(int, input().split()))
target = int(input())

root = None
tree = [[] for _ in range(N)]
for node, parent in enumerate(tree_parent):
    if parent == -1:
        root = node
        continue

    tree[parent].append(node)

leaf = []
stack = [(root, None)]
while stack:
    cur, parent = stack.pop()
    if cur == target:
        if parent is not None and len(tree[parent]) == 1:
            leaf.append(parent)
        continue

    if not tree[cur]:
        leaf.append(cur)

    for child in tree[cur]:
        stack.append((child, cur))
print(len(leaf))
