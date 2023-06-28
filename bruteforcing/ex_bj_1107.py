import sys
import time
cur = time.time()
sys.stdin = open('./bruteforcing/input_bj_1107.txt')

# input
N = int(input())
M = int(input())
ins = [str(i) for i in range(10)]
outs = input().split() if M else []
for out in outs:
    ins.remove(out)
result = [123456789] * 1000000

def surf(cha, n):
    if len(cha) >= n:
        cha = int(''.join(cha))
        result[cha] = abs(N - cha) + len(str(cha))
        return
    
    for i in ins:
        cha.append(i)
        surf(cha, n)
        cha.pop()

for n in range(1, 7):
    surf([], n)

idx, mn = 0, 123456789
for i in range(len(result)):
    if mn > result[i]:
        mn = result[i]
        idx = i
print(idx)
print(mn if (n:=abs(N-100)) > mn else n)
print(time.time() - cur)