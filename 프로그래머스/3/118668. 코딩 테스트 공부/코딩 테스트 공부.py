def solution(alp, cop, problems):
    # 목표로 하는 alp와 cop를 구한다.
    target_alp = max(max(problems, key=lambda x: x[0])[0], alp)
    target_cop = max(max(problems, key=lambda x: x[1])[1], cop)
    # dp table을 설정한다.
    # 점화식은 문제를 풀거나 공부해서 얻은 alp, cop에서 최소 시간값을 구할 수 있도록 구성한다.
    # 주의해야할 점은 문제를 풀 수 있으면 되기 때문에 목표로 하는 알고력과 코딩력을 넘어도 되게끔 해야한다.
    INF = 1000
    dp = [[INF] * (target_cop+1) for _ in range(target_alp+1)]
    dp[alp][cop] = 0
    for cur_alp in range(alp, target_alp+1):
        for cur_cop in range(cop, target_cop+1):
            cur = dp[cur_alp][cur_cop]

            # 알고력과 코딩력을 학습할 때
            if cur_cop+1 <= target_cop:
                dp[cur_alp][cur_cop+1] = min(dp[cur_alp][cur_cop+1], cur+1)
            if cur_alp+1 <= target_alp:
                dp[cur_alp+1][cur_cop] = min(dp[cur_alp+1][cur_cop], cur+1)

            # 문제를 풀 때
            for problem in problems:
                alp_req, cop_req, alp_rwd, cop_rwd, cost = problem

                if alp_req <= cur_alp and cop_req <= cur_cop:
                    n_alp, n_cop = min(target_alp, cur_alp+alp_rwd), min(target_cop, cur_cop+cop_rwd)
                    dp[n_alp][n_cop] = min(dp[n_alp][n_cop], cur+cost)
    return dp[target_alp][target_cop]