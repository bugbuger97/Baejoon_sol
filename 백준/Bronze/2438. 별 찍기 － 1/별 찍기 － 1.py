import sys
if __name__ == '__main__':
  star = '*'
  N = int(sys.stdin.readline()) # \n삭제를 안하기 때문에 input() 보다 더 빠르다
  for i in range(N):
    print(f'{star*(i+1)}')