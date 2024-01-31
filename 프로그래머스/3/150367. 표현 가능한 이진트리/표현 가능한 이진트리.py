def dnc(num, left, right):
    if left == right:
        return [True, int(num[left])]

    mid = (left + right) // 2
    root = int(num[mid])

    left_subtree = dnc(num, left, mid - 1)
    right_subtree = dnc(num, mid + 1, right)

    flag = left_subtree[1] or right_subtree[1]

    if flag == 1 and root == 0:
        return [0, 0]

    return [left_subtree[0] and right_subtree[0], root]

def get_answer(num):
    tmp = ''
    while num > 0:
        tmp = tmp + str(num % 2)
        num //= 2
    size = 1
    while len(tmp) > pow(2, size) - 1:
        size += 1
    while len(tmp) < pow(2, size) - 1:
        tmp += '0'

    return int(dnc(tmp, 0, len(tmp) - 1)[0])


def solution(numbers):
    answer = [get_answer(num) for num in numbers]
    return answer