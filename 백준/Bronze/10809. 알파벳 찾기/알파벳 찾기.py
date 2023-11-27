S = input().rstrip()
a = ord('a')
for i in range(26):
    print(S.find(chr(a+i)) if chr(a+i) in S else -1, end=" ")