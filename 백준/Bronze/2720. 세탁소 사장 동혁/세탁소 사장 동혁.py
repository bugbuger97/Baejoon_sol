if __name__ == '__main__':
  T = int(input())
  result = []
  for i in range(T):
    C = int(input())
    result.append(C // 25)
    C%=25
    result.append(C//10)
    C%=10
    result.append(C//5)
    C%=5
    result.append(C//1)
    print(*result)
    result = []