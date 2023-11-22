def solution(alp, cop, problems):
    max_alp = max(max(problems, key=lambda x: x[0])[0], alp)
    max_cop = max(max(problems, key=lambda x: x[1])[1], cop)
    
    INF = int(1e9)
    dp = [[INF] * (max_cop+1) for _ in range(max_alp+1)]
    for r in range(alp+1):
        for c in range(cop+1):
            dp[r][c] = 0
    
    for r in range(alp, max_alp+1):
        for c in range(cop, max_cop+1):
            nr, nc = min(r+1, max_alp), min(c+1, max_cop)
            dp[nr][c] = min(dp[nr][c], dp[r][c]+1)
            dp[r][nc] = min(dp[r][nc], dp[r][c]+1)
            
            for problem in problems:
                alp_req, cop_req, alp_rwd, cop_rwd, cost = problem
                if alp_req <= r and cop_req <= c:
                    n_alp, n_cop = min(r+alp_rwd, max_alp), min(c+cop_rwd, max_cop)
                    dp[n_alp][n_cop] = min(dp[n_alp][n_cop], dp[r][c] + cost)
    return dp[max_alp][max_cop]