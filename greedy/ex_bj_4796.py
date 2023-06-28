import sys
sys.stdin = open('./greedy/input_bj_4796.txt')

for idx, arr in enumerate([*open(0)][:-1], start=1):
    L, P, V = map(int, arr.rstrip().split())
    print(f'Case {idx}: {V//P * L + (n if (n := V%P) <= L else L)}')
    