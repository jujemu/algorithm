for _ in range(int(input())):
    result = [0] * 26
    s = input().split(" ")
    for word in s:
        if word == "":
            continue

        for c in word:
            idx = ord(c) - ord("a")
            result[idx] += 1
    sorted_result = sorted(result)
    if sorted_result[-1] == sorted_result[-2]:
        print("?")
    else:
        print(chr(result.index(sorted_result[-1]) + ord("a")))