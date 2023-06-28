import sys
sys.stdin = open('./greedy/input_bj_1946.txt')
input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    # input
    N = int(input().rstrip())
    arr = [0] * N
    for _ in range(N):
        i, val = map(int, input().split())
        arr[i-1] = val
        
    result = N
    min = N+1
    for a in arr:
        if min > a:
            min = a
        else:
            result -= 1
    print(result)
    