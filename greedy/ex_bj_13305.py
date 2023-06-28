import sys
sys.stdin = open('./greedy/input_bj_13305.txt')
input = sys.stdin.readline

# input
N = int(input().rstrip())
roads = [int(c) for c in input().split()]
oils = [int(c) for c in input().split()]
oils.pop()

# list of available min oil price
arr = [oils.pop(0)]
for oil in oils:
    arr.append(min(arr[-1], oil))
    
result = 0
for i in range(len(arr)):
    result += arr[i] * roads[i]
print(result)
