import sys
sys.stdin = open('./greedy/input_bj_1080.txt')
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
A = [[int(c) for c in input().rstrip()] for _ in range(N)]
B = [[int(c) for c in input().rstrip()] for _ in range(N)]
ones = [[1]*3 for _ in range(3)]

cnt = 0
for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]:
            for x in range(i, i+3):
                for y in range(j, j+3):
                    A[x][y] = 1 - A[x][y]
            cnt += 1

print(cnt if A == B else -1)
