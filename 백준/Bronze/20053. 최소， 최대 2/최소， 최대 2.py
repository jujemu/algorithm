T = int(input())
for _ in range(T):
    _ = input()
    arr = list(map(int, input().split()))
    print("{} {}".format(min(arr), max(arr)))