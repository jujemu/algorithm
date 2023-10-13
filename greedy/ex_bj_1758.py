import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort(reverse=True)
arr = [i - idx if i-idx >0 else 0 for idx, i in enumerate(arr)]
print(sum(arr))