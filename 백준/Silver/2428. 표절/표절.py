'''
https://www.acmicpc.net/problem/2428

주제: 투 포인터
'''
import sys
input = lambda: sys.stdin.readline().rstrip()


def tp(sorted_arr):
    length = len(sorted_arr)
    if length == 1:
        return 0

    cnt = 0
    p_2 = 1
    for p_1 in range(length-1):
        if p_1 == p_2:
            if p_1 == length-1:
                break
            p_2 = p_1+1

        while p_2 < length:
            if sorted_arr[p_2] * 0.9 <= sorted_arr[p_1]:
                p_2 += 1
            else:
                break

        if p_2 != length:
            cnt += p_2 - p_1 - 1
        else:
            cnt += length - p_1 - 1

    return cnt


N = int(input())
sizes = list(map(int, input().split()))
print(tp(sorted(sizes)))
