from collections import deque


def solution(n, tops):
    dp = deque(get_init(n, tops), maxlen=3)

    index, fixed_index = 2, 2
    while index < n:
        get_dp_element(dp, index, fixed_index, tops)
        index += 1

    return sum(dp[-1]) % 10007


def get_dp_element(dp, index, fixed_index, tops):
    coefficient = 3 if tops[index] else 2
    dp.append([0, 0])

    for pre_dp in dp[fixed_index - 1]:
        dp[fixed_index][0] += pre_dp * coefficient

    if tops[index - 1]:
        rest = sum(dp[fixed_index - 2]) * 2 + dp[fixed_index - 1][1]
    else:
        rest = sum(dp[fixed_index - 2]) + dp[fixed_index - 1][1]
    dp[fixed_index][1] += rest


def get_init(n, tops):
    if tops[0]:
        if n == 1:
            return [[4, 0]]

        if tops[1]:
            return [[4, 0], [12, 3]]
        return [[4, 0], [8, 3]]
    else:
        if n == 1:
            return [[3, 0]]

        if tops[1]:
            return [[3, 0], [9, 2]]
        return [[3, 0], [6, 2]]