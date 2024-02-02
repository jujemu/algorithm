import sys

def max_sum(n, m, arr):
    dp = [[None] * (m+1) for _ in range(n)]

    def solve(i, j):
        if j == 0:
            return 0
        if i < 0:
            return -sys.maxsize

        if dp[i][j] is not None:
            return dp[i][j]

        # Case 1: Do not include arr[i]
        res = solve(i-1, j)

        # Case 2: Include arr[i]
        curr_sum = 0
        max_sum = -sys.maxsize
        for k in range(i, -1, -1):
            curr_sum += arr[k]
            max_sum = max(max_sum, curr_sum + solve(k-2, j-1))

        res = max(res, max_sum)

        dp[i][j] = res
        return res

    return solve(n-1, m)

def main():
    n, m = map(int, input().split())
    arr = [int(input()) for _ in range(n)]

    print(max_sum(n, m, arr))

if __name__ == "__main__":
    main()
