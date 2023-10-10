N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort(reverse=True)
arr = [idx*i for idx, i in enumerate(arr, start=1)]
print(max(arr))
