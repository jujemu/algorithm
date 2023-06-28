import sys
sys.stdin = open('./implementation/input_bj_2563.txt')
input = sys.stdin.readline

N = int(input())
blacks = [tuple(map(int, input().split())) for _ in range(N)]
white_paper = [[0] * 100 for _ in range(100)]
for x, y in blacks:
    for i in range(10):
        for j in range(10):
            white_paper[y+i][x+j] = 1

result = 0
for line in white_paper:
    result += sum(line)
print(result)
