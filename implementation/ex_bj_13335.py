from collections import deque
import sys
sys.stdin = open('./implementation/input_bj_13335.txt')
input = sys.stdin.readline

# input
n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))

# go cross the bridge
cnt = 1
bridge = deque([trucks.pop(0)])
for truck in trucks:    
    while True:
        cnt += 1
        if len(bridge) >= w:
            bridge.popleft()
        
        if sum(bridge) + truck <= L:
            bridge.append(truck)
            break
        bridge.append(0)
print(cnt + w)
