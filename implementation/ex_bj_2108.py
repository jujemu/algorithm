import sys
sys.stdin = open('./implementation/input_bj_2108.txt')
input = sys.stdin.readline

# input
N = int(input().rstrip())
data = sorted([int(input().rstrip()) for _ in range(N)])
cnt_arr = [0] * 8001 

# count values
for d in data:
    cnt_arr[d+4000] += 1
    
# find most frequent value
mf = 0
for cnt in cnt_arr:
    mf = cnt if cnt > mf else mf
result = []
for idx, cnt in enumerate(cnt_arr):
    if cnt == mf:
        result.append(idx)

print(round(sum(data)/N))
print(data[N//2])
print(result[0]-4000 if len(result) == 1 else result[1]-4000)
print(data[-1] - data[0])
