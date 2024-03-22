import sys


def answering():
    if max_value:
        print(max_value)
        print(answer)
        return
    print("SAD")


input = lambda: sys.stdin.readline().rstrip()
N, X = map(int, input().split())
visits = list(map(int, input().split()))

answer = 1
curr_sum = sum(visits[:X])
max_value = curr_sum
for i in range(X, N):
    curr_sum += visits[i]
    curr_sum -= visits[i-X]

    if max_value < curr_sum:
        answer = 1
        max_value = curr_sum
    elif max_value == curr_sum:
        answer += 1

answering()
