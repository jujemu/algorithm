import time
import sys
# sys.stdin = open('../input.txt')

# 86400
# print(60 * 60 * 24)
n = int(input())


def check_three(s):
    s = str(s)
    if '3' in s:
        return 1
    return 0


current = time.time()
cnt = 0
for hour in range(n+1):
    if check_three(hour):
        cnt += 60 * 60
        continue
    for min in range(60):
        if check_three(min):
            cnt += 60
            continue
        for sec in range(60):
            if check_three(sec):
                cnt += 1
print(time.time() - current)
print(cnt)
