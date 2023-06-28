N, r, c = map(int, input().split())

def z(N, r, c, n):
    thres = 2**(N-1)
    if r >= thres:
        r -= thres
        if c >= thres:
            c -= thres
            n += 3 * (2 ** (2 * N-2))
        else:
            n += 2 * (2 ** (2 * N-2))
    else:
        if c >= thres:
            c -= thres
            n += 2 ** (2 * N-2)
    
    if N == 1:
        return n
    else:
        return z(N-1, r, c, n)

print(z(N, r, c, 0))
            