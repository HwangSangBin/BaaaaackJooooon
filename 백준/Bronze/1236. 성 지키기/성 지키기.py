n, m = map(int, input().split())
castle_row = []
castle_col = []
count_row = 0
count_col = 0
comma = ""

for i in range(n):
    castle_row.append(input())
    if 'X' not in castle_row[i]:
        count_row += 1

for j in range(m):
    for i in range(n):
        comma += castle_row[i][j]
    castle_col.append(comma)
    comma = ""

for i in range(m):
    if 'X' not in castle_col[i]:
        count_col += 1

print(max(count_row, count_col))