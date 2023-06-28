# pibonachi
def pibo(n):
    d = {
        1: 1,
        2: 1
    }
    
    for i in range(3, n+1):
        if i not in d:
            d[i] = d[i-1] + d[i-2]
    return d

num = int(input())
print(pibo(num)[num])
