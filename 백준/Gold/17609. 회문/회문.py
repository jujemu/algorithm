def sandwich(s):
    # print(s)
    if s == s[:: -1]:
        return 0
        
    chance, chance_2nd = True, True
    diff_cnt, diff_index = None, None
    p1, p2 = 0, len(s)-1
    cnt = 0
    while cnt < len(s) // 2:
        if s[p1] != s[p2]:
            if chance:
                chance = False
                if s[p1+1] == s[p2]:
                    diff_cnt = cnt
                    diff_index = p1, p2
                    p1 += 1
                elif s[p1] == s[p2-1]:
                    p2 -= 1
                else:
                    return 2
            else:
                if chance_2nd and diff_index:
                    chance_2nd = False
                    p1, p2 = diff_index
                    if s[p1] == s[p2 - 1]:
                        p2 -= 1
                        cnt = diff_cnt
                    else:
                        return 2
                else:
                    return 2

        p1 += 1
        p2 -= 1
        cnt += 1

    return 0 if chance else 1


for _ in range(int(input())):
    print(sandwich(input()))