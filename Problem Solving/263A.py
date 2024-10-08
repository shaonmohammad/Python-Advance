matrix = []
for i in range(5):
    matrix.append(list(map(int, input().split())))

for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            row_1, col_1 = i+1, j+1

center_row, center_col = 3, 3

moves = abs(row_1-center_row) + abs(col_1-center_col)
print(moves)
