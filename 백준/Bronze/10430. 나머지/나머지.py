def find_remain(A,B,C):
  print((A+B)%C)
  print(((A%C) + (B%C))%C)
  print((A*B)%C)
  print(((A%C) * (B%C))%C)

if __name__ == '__main__':
  A,B,C = input().split()
  find_remain(int(A),int(B),int(C))