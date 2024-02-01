'''
https://www.acmicpc.net/problem/10799

문제 이해
 - 괄호의 시작은 반드시 "("
 - 레이저가 아닌 ")"은 쇠막대기의 끝이고 쇠막대기 끝을 만나기 전까지는 쇠막대기가 쌓여간다.
 - 즉, 쇠막대기의 누적으로 레이저마다 조각을 추가하고 쇠막대기 끝을 만나면 누적을 빼면 된다.
 - 쇠막대기 끝은 언제나 레이저 다음이다.
'''
s = input()

result = 0
stack, acc = [], 0
for c in s:
    if c == "(":
        acc += 1
    elif stack[-1] == "(":
        acc -= 1
        result += acc
    elif stack[-1] == ")":
        result += 1
        acc -= 1
    stack.append(c)

print(result)
