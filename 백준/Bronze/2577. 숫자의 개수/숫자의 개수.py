if __name__ == '__main__':
  A = int(input())
  B = int(input())
  C = int(input())
  result = list(str(A*B*C))
  result = list(map(int,result))
  for i in range(10):
    print(result.count(i))