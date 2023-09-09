if __name__ == '__main__':
  star = '*'
  N = int(input())
  for i in range(N):
    print(f'{" "*(N-(i+1))}{star*(i+1)}')