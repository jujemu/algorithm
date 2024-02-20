def solution(money):
    dp_1 = money[:-1]
    result_1 = dp(dp_1)
    
    dp_2 = money[1:]
    result_2 = dp(dp_2)
    
    return max(result_1, result_2)

    
def dp(arr):
    n = len(arr)
    if n == 0:
        return 0
    
    if n == 1:
        return arr[0]
    
    arr[1] = max(arr[:2])
    for i in range(2, n):
        arr[i] = max(arr[i-2]+arr[i], arr[i-1])
    return arr[-1]
