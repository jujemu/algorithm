N, M = map(int, input().split())
nums = [
    *map(int, input().split())
]
nums.sort()


def NM6(s):
    if len(s) == M:
        print(*s)
        return

    smallest = s[-1] if s else 0
    for n in nums:
        if smallest < n:
            s.append(n)
            NM6(s)
            s.pop()


NM6([])
