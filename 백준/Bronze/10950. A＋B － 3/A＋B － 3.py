if __name__ == '__main__':
  T = int(input())
  result = list()
  for i in range(T):
    A,B = input().split()
    result.append(int(A)+int(B))
  for i in range(len(result)):
    print(result[i])