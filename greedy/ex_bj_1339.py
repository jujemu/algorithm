import sys
sys.stdin = open('./greedy/input_bj_1339.txt')
input = sys.stdin.readline

A = ord('A')
d = {chr(A + i):0 for i in range(26)}
alphas = {chr(A + i):0 for i in range(26)}
numbers = [i for i in range(10)]

# input
N = int(input().rstrip())
words = [input().rstrip() for _ in range(N)]
# print(N, words)

for word in words:
    l = len(word)
    for idx, c in enumerate(word):
        d[c] += 10 ** (l - idx - 1)
d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
for idx, key in enumerate(d):
    if idx >= 10:
        break
    alphas[key] = numbers.pop()

result = 0
for i in range(A, A+26):
    c = chr(i)
    result += d[c] * alphas[c]
print(result)
    