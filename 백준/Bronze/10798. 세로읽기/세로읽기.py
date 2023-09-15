if __name__ == '__main__':
  result = ''
  temp = [input() for i in range(5)]
  size = [len(temp[i]) for i in range(len(temp))]
  max_val = max(size) 
  size_adjust = [max_val - i for i in size]
  for i in range(len(size_adjust)):
    if size_adjust[i] != 0:
      temp[i] += ' ' * size_adjust[i]
  for i in range(max_val):
    for j in range(5):
      if temp[j][i] == ' ':
        continue
      else:
        result += temp[j][i]
  print(result)