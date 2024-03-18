from itertools import combinations


cost = {
    "dia": {"diamond": 1, "iron": 1, "stone": 1},
    "iron": {"diamond": 5, "iron": 1, "stone": 1},
    "stone": {"diamond": 25, "iron": 5, "stone": 1}
}

cost_by_index = {
    "dia": [0] * 15,
    "iron": [0] * 15,
    "stone": [0] * 15
}

def solution(picks, minerals):
    dia, iron, stone = picks
    sum_picks = sum(picks)
    picks = ["dia", "iron", "stone"]
    
    # brute force 풀이
    # 곡괭이의 순서를 무작위로 선택함
    # 곡괭이 순서가 결정되면 그 순서에서 나오는 피로도 결정되기 때문에
    # 곡괭이와 인덱스로 피로를 구할 수 있는 cost_by_index 정의한다.
    for pick in picks:
        for idx_pick in range(sum_picks):
            s = idx_pick*5
            e = s+5
            e = e if len(minerals) >= e else len(minerals)
            for idx_m in range(s, e):
                cur_minerals = minerals[idx_m]
                cost_by_index[pick][idx_pick] += cost[pick][cur_minerals]
    
    min_value = 10_000
    for dia_idxes in combinations(range(sum_picks), dia):
        cur_value = 0
        for idx in dia_idxes:
            cur_value += cost_by_index["dia"][idx]
        
        rest_idxes = [i for i in range(sum_picks) if i not in dia_idxes]
        for iron_idxes in combinations(rest_idxes, iron):
            stone_idxes = [i for i in range(sum_picks) if i not in dia_idxes+iron_idxes]
            
            tmp = cur_value
            for idx in iron_idxes:
                cur_value += cost_by_index["iron"][idx]
            
            for idx in stone_idxes:
                cur_value += cost_by_index["stone"][idx]
                
            min_value = min(min_value, cur_value)
            cur_value = tmp

    return min_value if min_value != 10_000 else 0
            
            