def solution(money):
    check_first_element_used = [False] * len(money)
    check_first_element_used[0] = True
    # if money[1] < money[0]:
    #     check_first_element_used[1] = True
    #     money[1] = money[0]
    
    money[1] = max(money[:2])
    for i, cur in enumerate(money[2:], start=2):
        pre_1 = money[i-1]        
        pre_2 = money[i-2]+cur
        if  pre_2 > pre_1:
            check_first_element_used[i] = check_first_element_used[i-2]
            money[i] = pre_2
        elif  pre_2 < pre_1:
            check_first_element_used[i] = check_first_element_used[i-1]
            money[i] = pre_1
        else:
            if check_first_element_used[i-1] and check_first_element_used[i-2]:
                check_first_element_used[i] = True
            money[i] = pre_1
    
    result = 0
    if check_first_element_used[-1]:
        return money[-2]
    return money[-1]