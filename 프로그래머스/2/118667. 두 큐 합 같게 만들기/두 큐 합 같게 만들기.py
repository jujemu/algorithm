def solution(queue1, queue2):
    length = len(queue1)
    window_length = length*2
    pointer = length-1
    s1, s2 = sum(queue1), sum(queue2)
    
    answer = 0
    q = queue1 + queue2 + queue1 + queue2
    for i in range(window_length):
        while pointer < window_length+i and s1 < s2:
            pointer += 1
            answer += 1
            
            s1 += q[i+pointer]
            s2 -= q[i+pointer]
        
        if s1 == s2:
            return answer
        
        s2 += q[i+window_length]
        s1 -= q[i]
        pointer -= 1
        answer += 1
    
    return -1
