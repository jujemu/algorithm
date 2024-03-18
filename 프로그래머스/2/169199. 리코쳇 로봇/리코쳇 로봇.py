from collections import deque


dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def solution(board):
    
    # 시작 지점
    s_r, s_c = None, None
    R, C = len(board), len(board[0])
    for i in range(R):
        for j in range(C):
            if board[i][j] == "R":
                s_r, s_c = i, j
    
    answer = int(1e9)
    q = deque([(s_r, s_c, 0)])
    visited = [[False]*C for _ in range(R)]
    while q:
        r, c, cnt = q.popleft()
        if visited[r][c] or cnt >= answer:
            continue
            
        visited[r][c] = True
        for d in range(4):
            nr, nc = r, c
            while True:
                nr, nc = nr+dr[d], nc+dc[d]
                if 0 <= nr < R and 0 <= nc < C and board[nr][nc] != "D":
                    continue
                break
            
            nr, nc = nr-dr[d], nc-dc[d]
            if board[nr][nc] == "G":
                answer = cnt+1
            
            if not visited[nr][nc]:
                q.append([nr, nc, cnt+1])
    
    return answer if answer != int(1e9) else -1