import sys

if __name__ == '__main__':
  T = int(sys.stdin.readline())
  for i in range(int(T)):
    A,B = map(int, sys.stdin.readline().split()) #input
    print(f'Case #{i+1}: {A+B}')