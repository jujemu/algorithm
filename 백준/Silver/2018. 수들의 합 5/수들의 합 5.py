'''
https://www.acmicpc.net/problem/2018

주제: 투포인터
시간복잡도: N
'''
N = int(input())

answer = 0
p_1, p_2 = 1, 1
cur_s = 1
while p_1 <= N // 2:
    if cur_s == N:
        answer += 1

        cur_s -= p_1
        p_1 += 1
        p_2 += 1
        cur_s += p_2
        continue

    if cur_s > N:
        cur_s -= p_1
        p_1 += 1
        continue

    p_2 += 1
    cur_s += p_2
print(answer+1)
