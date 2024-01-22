dic = defaultdict(int)
skip = 1
for x in range(len(matrix)):
   if skip:
       skip = 0
       continue
   for y in range(len(matrix)):
       if (x == y and y+1 <= len(matrix) - 1):
           matrix[x][y] = min(matrix[x][y],matrix[x][y+1])
       elif ((y == (len(matrix) - 1)) and (y-1 > 0)):
           matrix[x][y] = min(matrix[x][y],matrix[x][y-1])
       elif ((y-1 >= 0) and (y+1 <= len(matrix) - 1)):
           matrix[x][y] = min(matrix[x][y-1],matrix[x][y],matrix[x][y+1])
print(matrix)