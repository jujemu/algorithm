import sys
sys.stdin = open('./data_structure/input_bj_10828.txt')
input = sys.stdin.readline

def com(s, c):
    if c == 'pop':
        return s.pop() if s else -1
    elif c == 'size':
        return len(s)
    elif c == 'empty':
        return 0 if s else 1
    return s[-1] if s else -1

stack = []
for _ in range(int(input())):
    c = input().split()
    if c[0] == 'push':
        stack.append(int(c[1]))
        continue
    print(com(stack, c[0]))
    