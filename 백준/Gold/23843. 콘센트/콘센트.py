import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort(reverse=True)
totalTime = [0] * M # totalTime[i]는 i번째 콘센트로 충전하는 전자기기 들의 시간 총합

idx = 0 # 현재 몇 번째 콘센트를 가리키는지
for i in range(len(arr)):
    if idx == 0: # 첫 번째 콘센트에 남은 것중 가장 충전 시간이 긴 것을 넣는다.
        totalTime[idx] += arr[i]
        idx = (idx + 1) % M
        continue
    
    # 나머지 콘센트에는 이전 콘센트의 시간 총합을 넘지 않도록 최대한 넣는다.
    totalTime[idx] += arr[i]
    if totalTime[idx] == totalTime[idx - 1]:
        idx = (idx + 1) % M
    
print(totalTime[0]) # 첫 번째 콘센트가 가장 충전이 오래 걸리고 이 시간이 곧 총 충전 시간이다.