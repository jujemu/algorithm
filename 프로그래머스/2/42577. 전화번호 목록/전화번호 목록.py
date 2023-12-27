def solution(phone_book):
    
    s = set()
    for number in sorted(phone_book, key= lambda x: -len(x)):
        if number in s:
            return False
        for idx in range(1, len(number)+1):
            n = number[:idx]
            s.add(n)
    return True