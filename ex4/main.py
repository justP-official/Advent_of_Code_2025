matrix = []

total = 0

indx = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)

with open("input4.txt", "r") as file:
    for row in file.readlines():
        matrix.append(list(row))

N = len(matrix)

for x in range(N):
    M = len(matrix[x])
    
    for y in range(M):
        if matrix[x][y] != "@":
            continue
        
        count = sum(
            (matrix[x + i][y + j] == "@" for i, j in indx if 0 <= x + i < N and 0 <= y + j < len(matrix[x + i]))
        )
        
        if count < 4:
            total += 1

print(total)