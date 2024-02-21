from collections import deque

n, m = map(int, input().split())
tomato = []
r = c = 0
cnt = 0
queue = deque([])

for i in range(m):
    tomato.append(list(map(int, input().split())))

# 시작지점
# 세로
for i in range(m):
    # 가로
    for j in range(n):
        if tomato[i][j] == 1:
            queue.append([i, j])

def bfs():
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < m and 0 <= nc < n and tomato[nr][nc] == 0:
                tomato[nr][nc] = tomato[r][c] + 1
                queue.append([nr, nc])

bfs()

for i in tomato:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    cnt = max(cnt, max(i))
print(cnt - 1)