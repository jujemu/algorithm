'''
https://www.acmicpc.net/problem/12891

주제: sliding window
시간복잡도: N
'''
from collections import defaultdict


def check():
    global answer
    for alpha, cond in condition.items():
        if cur_alpha[alpha] < cond:
            return
    answer += 1


S_len, P_len = map(int, input().split())
S = input()
condition = {alpha: int(num) for alpha, num in zip(["A", "C", "G", "T"], input().split())}

cur_alpha = defaultdict(int)
for char in S[:P_len]:
    cur_alpha[char] += 1

p_1 = 0
answer = 0
check()
for p_2 in range(P_len, S_len):
    c_1, c_2 = S[p_1], S[p_2]
    cur_alpha[c_1] -= 1
    cur_alpha[c_2] += 1
    check()
    p_1 += 1

print(answer)
