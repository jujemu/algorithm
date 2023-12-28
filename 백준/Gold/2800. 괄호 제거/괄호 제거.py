'''
https://acmicpc.net/problem/2800
괄호 제거

주제: 스택
시간복잡도: N
'''
def find_couple(exp):
    s, couple = [], []
    for idx, ele in enumerate(exp):
        if ele == "(":
            s.append(idx)
        elif ele == ")":
            couple.append((s.pop(), idx))
    return couple


def bf(arr, target, index, target_length, s):
    if len(arr) >= target_length:
        print_exp(arr, s)
        return

    for next in [target[index], None]:
        arr.append(next)
        bf(arr, target, index+1, target_length, s)
        arr.pop()


def print_exp(arr, s: str):
    indexes = []
    for a in arr:
        if a:
            indexes.extend(a)
    indexes.sort()

    s = [string for string in s]
    for i, index in enumerate(indexes):
        s.pop(index-i)
    result.append("".join(s))


result = []
expression = input()
couple = find_couple(expression)
bf([], couple, 0, len(couple), expression)
print(*sorted(list(set(result[:-1]))), sep="\n")
