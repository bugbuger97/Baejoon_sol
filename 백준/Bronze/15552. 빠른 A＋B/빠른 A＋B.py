import sys

if __name__ == '__main__':
  T = int(sys.stdin.readline())
  for _ in range(int(T)):
    A,B = map(int, sys.stdin.readline().split()) #input
    print(A+B)