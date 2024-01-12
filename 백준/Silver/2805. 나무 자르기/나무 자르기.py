'''
https://www.acmicpc.net/problem/2805

주제: 이분탐색
시간복잡도: logN

구현
절단기의 높이를 찾기 위해 범위를 설정한다.

최적화
 - 총 길이를 구하는 과정에서 M보다 커지면 계산을 멈춘다.
 - 나무를 정렬하고 설정한 절단기보다 높은 나무들만 잘라내도록 구현한다.
 - 총합을 계산할 때 선형으로 순회하지 않도록, 설정한 높이에 따른 대상 나무의 수 변화로 높이의 합을 계산한다.
'''
# def cutting(trees, height):
#     return sum(map(lambda x: max(x-height, 0), trees))
import bisect


def cutting(height):
    result = 0
    index = index_over_height_in_trees(height)
    for tree in trees[index:]:
        result += tree - height
        if result >= M:
            return True

    return False


def index_over_height_in_trees(height):
    return bisect.bisect_left(trees, height)


N, M = map(int, input().split())
trees = sorted([*map(int, input().split())])

pre_index = None
max_height = 0
l, r = 0, max(trees)
while l <= r:
    mid = (l+r) // 2

    if cutting(mid):
        max_height = mid
        l = mid+1
    else:
        r = mid-1

print(max_height)
