N = int(input())
Ps = [
    *map(int, input().split())
]

cached = [
    -1
    for _ in range(N)
]


def bf(card_sum):
    if N < card_sum:
        return None

    if N == card_sum:
        return 0

    if cached[card_sum] != -1:
        return cached[card_sum]

    mx = 0
    for i in range(N):
        result = bf(card_sum+i+1)
        if result is None:
            continue
        mx = max(Ps[i]+result, mx)
    cached[card_sum] = mx

    return cached[card_sum]


print(bf(0))
