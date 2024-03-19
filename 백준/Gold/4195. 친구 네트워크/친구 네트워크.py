import sys
sys.setrecursionlimit(100_000)


def add_people(x):
    global index

    if x not in people:
        people[x] = index
        index += 1


def find_parent(x):
    if parents[x] != x:
        parents[x] = find_parent(parents[x])
    return parents[x]


def union(x, y):
    x = people[x]
    y = people[y]

    x = find_parent(x)
    y = find_parent(y)

    parents[x] = y
    if x != y:
        number_of_set[y] += number_of_set[x]


input = lambda: sys.stdin.readline().rstrip()
for _ in range(int(input())):
    F = int(input())

    index = 0
    people = {}
    parents = [i for i in range(2*F+1)]
    number_of_set = [1 for i in range(2*F+1)]
    for _ in range(F):
        a, b = input().split()

        add_people(a)
        add_people(b)

        union(a, b)
        a, b = find_parent(people[a]), find_parent(people[b])
        print(max(number_of_set[a], number_of_set[b]))
