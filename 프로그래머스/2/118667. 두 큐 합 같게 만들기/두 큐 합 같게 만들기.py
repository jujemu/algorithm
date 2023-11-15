from collections import deque

def solution(queue1, queue2):
    sum_q = sum(queue1) + sum(queue2)
    if sum_q % 2 != 0:
        return -1
    
    cur_q1, sum_cur_q1 = deque(queue1), sum(queue1)
    cur_q2, sum_cur_q2 = deque(queue2), sum(queue2)
    cnt, ref, num_of_last = 0, sum_q // 2, len(queue1) * 3
    while True:
        if sum_cur_q1 == ref:
            break
            
        if cnt == num_of_last:
            cnt = -1
            break
            
        if sum_cur_q1 > ref:
            cur = cur_q1.popleft()
            cur_q2.append(cur)
            sum_cur_q2 += cur
            sum_cur_q1 -= cur
        else:
            cur = cur_q2.popleft()
            cur_q1.append(cur)
            sum_cur_q1 += cur
            sum_cur_q2 -= cur
        cnt += 1
    return cnt