if __name__ == '__main__':
  T = int(input())
  devide = [25,10,5,1]
  result = []
  for i in range(T):
    C = int(input())
    for j in devide:
      result.append(C//j)
      C%=j
    print(*result)
    result = []