n = int(input())
m = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]
dr = [1, 0, -1, 0]  # 하우상좌
dc = [0, 1, 0, - 1] # 하우상좌
num = n * n
d = r = c = 0
row = col = 0

for i in range(num, 0, -1):
    nr = r + dr[d]
    nc = c + dc[d]
    
    if ((nr >= n) | (nc >= n) | (nr < 0) | (nc < 0)) or arr[nr][nc] != 0:
        d = (d+1) % 4
        nr = r + dr[d]
        nc = c + dc[d]

    arr[r][c] = i

    if i == m:
        row = r+1
        col = c+1

    r = nr
    c = nc

for i in range(n):
    for j in range(n):
        print(arr[i][j], end =" ")
    print()    
print(row, col)