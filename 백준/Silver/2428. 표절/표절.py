'''
https://www.acmicpc.net/problem/2428

주제: 투 포인터
시간복잡도: N

구현
오름차순 정렬 후에 작은 원소부터 초점을 맞추고
검사하지 않아도 되는 다른 원소 짝을 찾는다.
짝을 찾으면 두 원소 사이의 값과 작은 원소는 쌍을 이룰 수 있으므로 count
만약, 검사하지 않아도 되는 다른 원소 짝을 찾을 수 없을 때는
다른 원소에 대해서 모두 쌍을 이룰 수 있음을 의미
'''
import sys
input = lambda: sys.stdin.readline().rstrip()


def tp(sorted_arr):
    length = len(sorted_arr)
    if length == 1:
        return 0

    cnt, p_2 = 0, 1
    for p_1 in range(length-1):
        if p_1 == p_2:
            p_2 = p_1+1

        while p_2 < length and sorted_arr[p_2] * 0.9 <= sorted_arr[p_1]:
            p_2 += 1

        if p_2 != length:
            cnt += p_2 - p_1 - 1
        else:
            cnt += (length-1) - p_1

    return cnt


N = int(input())
sizes = list(map(int, input().split()))
print(tp(sorted(sizes)))
