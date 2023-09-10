if __name__ == '__main__':
  n = int(input())
  result = [i+1 for i in range(30) if i+1 != n]
  for i in range(27):
    num = int(input())
    result.remove(num)
  print(*result)