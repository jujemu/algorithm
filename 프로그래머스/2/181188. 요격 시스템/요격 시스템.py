def solution(targets):
    targets.sort(key=lambda x: (x[1], x[0]))
    cur_target = 0
    
    answer = 0
    for s, e in targets:
        if s >= cur_target:
            cur_target = e
            answer += 1
        
    return answer 