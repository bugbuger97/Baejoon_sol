import sys
if __name__ == '__main__':
  numbers = list()
  for i in range(9):
    N = int(sys.stdin.readline())   
    numbers.append(N)
  print(max(numbers))
  print(numbers.index(max(numbers))+1)