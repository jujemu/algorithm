record = input()

d = {
    key: i for i, key in enumerate("quack")
}
arr = [0] * 4


def solve():
    result = 0
    for c in record:
        index = d[c]
        if index == 0:
            arr[0] += 1
            result = max(result, sum(arr))
        else:
            if arr[index-1] > 0:
                arr[index-1] -= 1
                if index != 4:
                    arr[index] += 1
            else:
                return -1
    return result


answer = solve()
print(answer if sum(arr) == 0 else -1)
