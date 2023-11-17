def solution(start_alp, start_cop, problems):
    INF = int(1e9)
        
    max_alp = max(problems, key=lambda x: x[0])[0]
    max_cop = max(problems, key=lambda x: x[1])[1]
    
    max_alp = max(max_alp, start_alp)
    max_cop = max(max_cop, start_cop)
    
    dp = [[INF] * (max_cop+1) for _ in range(max_alp+1)]
    for r in range(start_alp+1):
        for c in range(start_cop+1):
            dp[r][c] = 0
                                                
    for r in range(start_alp, max_alp+1):
        for c in range(start_cop, max_cop+1):
            nr, nc = min(r+1, max_alp), min(c+1, max_cop)
            dp[nr][c] = min(dp[r][c] + 1, dp[nr][c])
            dp[r][nc] = min(dp[r][c] + 1, dp[r][nc])
            
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if alp_req <= r and cop_req <= c:
                    next_alp = min(max_alp, r+alp_rwd)
                    next_cop = min(max_cop, c+cop_rwd)
                    dp[next_alp][next_cop] = min(dp[r][c] + cost, dp[next_alp][next_cop])
    
    return dp[max_alp][max_cop]