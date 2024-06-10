import sys


input = sys.stdin.read().strip().split("\n")
for test in input:
    s, t = test.split()

    i = 0
    try:
        for c in s:
            i = t.index(c, i)+1
        print("Yes")
    except ValueError:
        print("No")