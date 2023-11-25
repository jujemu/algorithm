from itertools import combinations

def solution(dice):
    answer = []

    max_value, max_index = 0, None
    n = len(dice)
    for a_dice in combinations(range(n), n//2):
        b_dice = []
        for idx in range(n):
            if idx not in a_dice:
                b_dice.append(idx)
            
        a_case, b_case = {}, {}
        play(a_dice, dice, a_case, [], 0)
        play(b_dice, dice, b_case, [], 0)
        
        win = 0
        for s_a, a in a_case.items():
            for s_b, b in b_case.items():
                if s_a > s_b:
                    win += a * b
        
        if win > max_value:
            max_value = win
            max_index = a_dice

    return list(map(lambda x: x+1, max_index))

def play(cur_dice, dice, case, cur_case, idx):
    if idx >= len(cur_dice):
        s = sum(cur_case)
        if s not in case:
            case[s] = 1
        else:
            case[s] += 1
        return

    for i in range(6):
        cur_case.append(dice[cur_dice[idx]][i])
        play(cur_dice, dice, case, cur_case, idx+1)
        cur_case.pop()