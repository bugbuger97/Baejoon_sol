if __name__ == '__main__':
  A,B = input().split()
  A = int(A[::-1])
  B = int(B[::-1])
  print(max(A,B))