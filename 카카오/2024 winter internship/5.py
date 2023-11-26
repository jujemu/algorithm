def solution(n, tops):
    dp = get_init(n, tops) + [[0, 0] for _ in range(n-2)]
    
    for idx in range(2, n):
        if idx % 1_000 == 0:
            for i in range(idx-1_000, idx-3):
                dp[i] = True

        if tops[idx]:
            for pre_dp in dp[idx-1]:
                dp[idx][0] += pre_dp*3
            rest = 0
            if tops[idx-1]:
                rest += sum(dp[idx-2]) * 2 + dp[idx-1][1]
            else:
                rest += sum(dp[idx-2]) + dp[idx-1][1]
            dp[idx][1] += rest
        
        else:
            for pre_dp in dp[idx-1]:
                dp[idx][0] += pre_dp*2
            rest = 0
            if tops[idx-1]:
                rest += sum(dp[idx-2]) * 2 + dp[idx-1][1]
            else:
                rest += sum(dp[idx-2]) + dp[idx-1][1]
            dp[idx][1] += rest

    return sum(dp[-1]) % 10007

def get_init(n, tops):
    if tops[0]:
        if n == 1:
            return [[4, 0]]

        if tops[1]:
            return [[4, 0], [12, 3]]
        return [[4, 0], [8, 3]]
    else:
        if n == 1:
            return [[3, 0]]

        if tops[1]:
            return [[3, 0], [9, 2]]
        return [[3, 0], [6, 2]]
