import sys

input = sys.stdin.readline

# input
n = int(input())
result = 0

# 홀수
if n % 2:
    if n >= 5:
        n -= 5
        result += 1
    else:
        result = -1
        
result += n // 10 * 2
n %= 10
result = result + n // 2 if result != -1 else result

print(result)
    