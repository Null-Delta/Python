# variant 6

n = int(input())
m = int(input())

matrix = []

for i in range(m):
    matrix.append([0] * n)

for i in range(0,m):
    for j in range(0,n):
        matrix[i][j] = int(input())

i = int(input())
j = int(input())

for index in range(m):
    (matrix[index][i],matrix[index][j]) = (matrix[index][j],matrix[index][i])

print()

for i in range(0,m):
    result = ""
    for j in range(0,n):
        result += str(matrix[i][j]) + " "
    print(result)