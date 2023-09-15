if __name__ == '__main__':
  result = []
  max_val = 0
  for i in range(9):
    temp = list(map(int,input().split()))
    result.append(temp)
  for i in range(9):
    for j in range(9):
      if result[i][j] >= max_val:
        max_val = result[i][j]
        row = i+1
        col = j+1
  print(max_val)
  print(row,col)