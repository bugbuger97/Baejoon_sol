if __name__ == '__main__':
  result = list()
  for i in range(10):
    n = int(input())
    result.append(n%42)
  result = set(result)
  print(len(result))