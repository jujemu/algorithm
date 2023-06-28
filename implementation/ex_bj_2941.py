import sys
sys.stdin = open('./implementation/input_bj_2941.txt')
input = sys.stdin.readline

s = input().rstrip()

arr = [('c=', 2), ('c-', 2), ('dz=', 3), ('d-', 2), ('lj', 2), ('nj', 2), ('s=',2) , ('z=', 2)]
# cnt = 0
for c, l in arr:
    ol = len(s)
    s = s.replace(c, ' ')
    # cnt += (ol - len(s)) // l

print(len(s))
