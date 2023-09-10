import sys
if __name__ == '__main__':
  N = int(sys.stdin.readline())  
  numbers = sys.stdin.readline()
  num = list(map(int,numbers.split()))
  print(f'{min(num)} {max(num)}')