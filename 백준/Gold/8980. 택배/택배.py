from collections import defaultdict
import sys


input = lambda: sys.stdin.readline().rstrip()
N, C = map(int, input().split())
M = int(input())
tasks = [tuple(map(int, input().split())) for _ in range(M)]
tasks.sort()


def load(end, weight):
    global cur_w

    acc = 0
    if cur_w < C:
        loading_weight = min(weight, C-cur_w)
        train[end] += loading_weight
        cur_w += loading_weight
        acc += loading_weight

        if loading_weight != weight:
            acc += transfer(end, weight - loading_weight)
    else:
        acc += transfer(end, weight)
    return acc


def transfer(end, weight):
    tmp = []
    for e, w in train.items():
        if end < e:
            tmp.append((e, w))
    tmp.sort(reverse=True)

    acc = 0
    for e, w in tmp:
        w_transfer = min(weight, train[e])
        train[e] -= w_transfer
        train[end] += w_transfer
        weight -= w_transfer
        acc += w_transfer

        if weight == 0:
            break
    return acc


train = defaultdict(int)
pre_town, cur_w = 1, 0
for task in tasks:
    s, e, w = task

    if s == pre_town:
        load_w = load(e, w)
    else:
        for e_, w_ in train.items():
            if pre_town < e_ <= s:
                cur_w -= w_
        pre_town = s
        load(e, w)
        
print(sum(train.values()))
