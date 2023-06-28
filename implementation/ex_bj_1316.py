import sys
sys.stdin = open('./implementation/input_bj_1316.txt')
input = sys.stdin.readline

# input
N = int(input())
arr = [input().rstrip() for _ in range(N)]

cnt = 0
for word in arr:
    s = set(word[0])
    flag = True
    for idx, c in enumerate(word[1:], start=1):
        if c == word[idx-1]:
            continue
        if c not in s:
            s.add(c)
        else:
            flag = False
            break
    if flag:
        cnt += 1
print(cnt)
