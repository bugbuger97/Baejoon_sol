if __name__ == '__main__':
  N = int(input())  
  numbers = input()
  num = list(map(int,numbers.split()))
  print(f'{min(num)} {max(num)}')