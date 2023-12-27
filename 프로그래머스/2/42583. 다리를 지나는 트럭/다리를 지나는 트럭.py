from collections import deque


def solution(bridge_length, weight, truck_weights):
    idx, time = 0, 0
    q, q_t, s = deque([]), deque([]), 0

    while True:
        time += 1
        for i in range(len(q_t)):
            q_t[i] += 1

        if q_t and q_t[0] > bridge_length:
            s -= q.popleft()
            q_t.popleft()

        if len(q) <= bridge_length and idx < len(truck_weights) and s + truck_weights[idx] <= weight:
            q.append(truck_weights[idx])
            q_t.append(1)
            s += truck_weights[idx]
            idx += 1

        if not q:
            break

    return time