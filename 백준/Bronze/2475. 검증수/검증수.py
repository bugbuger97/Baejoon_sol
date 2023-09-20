if __name__ == '__main__':
  num = list(map(int,input().split(' ')))
  result = sum([i**2 for i in num])
  print(result%10)