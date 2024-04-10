def solution(queue1, queue2):
    length = len(queue1)
    total_length = length * 2
    s1, s2 = sum(queue1), sum(queue2)

    answer = 0
    q = queue1 + queue2
    p1 = 0
    for p2 in range(length, total_length):
        while s1 > s2:
            s1 -= q[p1]
            s2 += q[p1]
            p1 += 1
            answer += 1

        if s1 == s2:
            return answer

        s1 += q[p2]
        s2 -= q[p2]
        answer += 1

    return answer if answer >= total_length else -1
