import heapq

def solution(alp, cop, problems):
    max_alp, max_cop = max(x[0] for x in problems), max(x[1] for x in problems)
    table = [[int(1e9) for _ in range(151)] for _ in range(151)]
    problems += [[0, 0, 1, 0, 1], [0, 0, 0, 1, 1]]

    h = [(0, alp, cop)]
    table[alp][cop] = 0
    while h:
        curr_cost, curr_alp, curr_cop = heapq.heappop(h)
        if curr_alp >= max_alp and curr_cop >= max_cop:
            return curr_cost
        if table[curr_alp][curr_cop] <= curr_cost:
            for r_alp, r_cop, a_alp, a_cop, n_cost in problems:
                n_alp, n_cop = min(150, curr_alp + a_alp), min(150, curr_cop + a_cop)
                if curr_alp >= r_alp and curr_cop >= r_cop and curr_cost + n_cost < table[n_alp][n_cop]:
                    table[n_alp][n_cop] = curr_cost + n_cost
                    heapq.heappush(h, (curr_cost + n_cost, n_alp, n_cop))