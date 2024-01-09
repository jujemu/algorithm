'''
https://www.acmicpc.net/problem/16472

주제: 투 포인터
'''
from collections import defaultdict


N = int(input())
S = input()

# init
cur_duplicate_cnt = 1
cur_alpha = defaultdict(int)
cur_alpha[S[0]] += 1

max_length = 0
p_1, p_2 = 0, 0
for _ in range(len(S)*2):
    if cur_duplicate_cnt > N:
        cur_alpha[S[p_1]] -= 1
        if not cur_alpha[S[p_1]]:
            cur_duplicate_cnt -= 1
        p_1 += 1
        continue

    max_length = max(max_length, p_2 - p_1 + 1)
    p_2 = min(p_2+1, len(S)-1)
    if not cur_alpha[S[p_2]]:
        cur_duplicate_cnt += 1
    cur_alpha[S[p_2]] += 1

print(max_length)
