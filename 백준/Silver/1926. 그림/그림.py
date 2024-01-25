from collections import deque

n, m = map(int, input().split())
graph = []
count = 0
area = []

for _ in range(n):
    graph.append(list(map(int, input().split(" "))))

def bfs(r, c):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    queue = deque()
    queue.append((r,c))
    size = 0

    while queue:
        r, c = queue.popleft()
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < m and graph[nr][nc] == 1:
                graph[nr][nc] = 0
                queue.append((nr, nc))
                size += 1
    return size


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            area.append(bfs(i,j))
            count += 1
print(count)
if area != []:
    if max(area) == 0:
        print(1)
    else:
        print(max(area))
else:
    print(0)