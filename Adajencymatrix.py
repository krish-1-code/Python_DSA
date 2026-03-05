
Edges = [(1,2),(1,3),(2,4),(3,4)]

matrix = [0]*4

for i in range(4):
    matrix[i] = [0]*4

for i,j in Edges:
    matrix[i-1][j-1] = 1
    matrix[j-1][i-1] = 1

for i in range(len(matrix)):
    print(matrix[i])