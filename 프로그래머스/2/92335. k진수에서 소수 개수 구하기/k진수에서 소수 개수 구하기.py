import numpy as np
import math

def solution(n, k):
    answer = 0
    
    edited_n = transfer(n, k)
    split = str(edited_n).split("0")
    print(edited_n, split)
    
    for s in split:
        if s:
            if is_prime(int(s)):
                print(s)
                answer += 1
        
    return answer

def transfer(n, k):
    result = ""
    while n > 0 :
        result += str(n%k)
        n //= k
    return result[::-1]

def is_prime(number):
    if number == 2:
        return True
    if number % 2 == 0 or number < 2:
        return False
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True