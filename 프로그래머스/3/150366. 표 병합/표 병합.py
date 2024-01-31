def solution(commands):
    global table_parent, table_value, N
    answer = []
    
    N = 50
    table_parent = [[(r, c) for c in range(N)] for r in range(N)]
    table_value = [[None]*N for _ in range(N)]
    
    for command in commands:
        cmd, *values = command.split()
        
        if cmd == "UPDATE":
            if len(values) == 3:
                r, c, value = values
                r, c = int(r)-1, int(c)-1
                update_value(r, c, value)
            else:
                v_1, v_2 = values
                update_all(v_1, v_2)
        
        elif cmd == "MERGE":
            r1, c1, r2, c2 = map(lambda x: int(x)-1, values)
            merge(r1, c1, r2, c2)
        
        elif cmd == "UNMERGE":
            r, c = map(lambda x: int(x)-1, values)
            unmerge(r, c)
        
        elif cmd == "PRINT":
            r, c = map(lambda x: int(x)-1, values)
            result = print_(r, c)
            answer.append(result if result else "EMPTY")
            
    return answer


def merge(r1, c1, r2, c2):
    global table_parent, table_value
    
    p_r1, p_c1 = find_parent(r1, c1)
    p_r2, p_c2 = find_parent(r2, c2)
    if table_value[p_r2][p_c2] and not table_value[p_r1][p_c1]:
        table_parent[p_r1][p_c1] = (p_r2, p_c2)
        return
            
    table_parent[p_r2][p_c2] = (p_r1, p_c1)

                                    
def find_parent(r, c):
    global table_parent
    
    n_r, n_c = table_parent[r][c]
    if  (n_r, n_c) != (r, c):
        table_parent[r][c] = find_parent(n_r, n_c)
    return table_parent[r][c]


def unmerge(r, c):
    global table_parent, table_value, N
    
    p_r, p_c = find_parent(r, c)
    tmp = table_value[p_r][p_c]
    table_parent_copy = [row[:] for row in table_parent]
    for i in range(N):
        for j in range(N):
            if find_parent(i, j) == (p_r, p_c):                
                table_parent_copy[i][j] = None
                table_value[i][j] = None
    table_value[r][c] = tmp
    
    for i in range(N):
        for j in range(N):
            if table_parent_copy[i][j] is None:
                table_parent[i][j] = (i, j)
    return


def update_value(r, c, value):
    global table_value
    
    p_r, p_c = find_parent(r, c)
    table_value[p_r][p_c] = value
    return


def update_all(v_1, v_2):
    global table_value, N
    
    for i in range(N):
        for j in range(N):
            if table_value[i][j] == v_1:
                table_value[i][j] = v_2
    return


def print_(r, c):
    global table_value
    
    p_r, p_c = find_parent(r, c)
    return table_value[p_r][p_c]
# 포인트
# 병합의 정보를 어떻게 저장할까
# 1. 그냥 각 셀에 다 넣어 -> 수정할 때, 어떤 셀이 병합되어 있는지 알 수 없다.
# 2. 테이블을 2개 만들고, 하나는 부모 노드(병합의 루트)를 가리키고, 하나는 리얼 값
