import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
tree = {}
for _ in range(N):
    parent, left, right = map(lambda x: x if x != "." else None, input().split())
    tree[parent] = [left, right]

preorder = []
def pre(cur):
    preorder.append(cur)

    for adj in tree[cur]:
        if adj:
            pre(adj)

inorder = []
def in_(cur):
    if cur:
        in_(tree[cur][0])
        inorder.append(cur)
        in_(tree[cur][1])

postorder = []
def post(cur):
    for adj in tree[cur]:
        if adj:
            post(adj)
    postorder.append(cur)

pre("A")
in_("A")
post("A")

print(*preorder, sep="")
print(*inorder, sep="")
print(*postorder, sep="")