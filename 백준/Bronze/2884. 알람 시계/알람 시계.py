H, M = map(int, input().split())
time = H*60 + M
result = None
time -= 45
if time < 0:
    time = 24*60 + time
print(time//60, end=" ")
print(time%60)