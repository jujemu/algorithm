'''
https://www.acmicpc.net/problem/20444

주제: 이분 탐색
시간복잡도: logN
'''
def cut_paper(n, row):
    col = n - row
    return (row+1) * (col+1)


n, k = map(int, input().split())

answer = None
s, e = 0, n//2
while s <= e:
    mid = (s+e) // 2

    paper_cnt = cut_paper(n, mid)
    if k > paper_cnt:
        s = mid+1
    elif k < paper_cnt:
        e = mid-1
    else:
        answer = mid
        break

print("YES" if answer is not None else "NO")
