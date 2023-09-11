if __name__ == '__main__':
  result = ''
  T = int(input())
  for i in range(T):
    R,S = input().split()
    R = int(R)
    temp = [i*R for i in S]
    for j in temp:
      result += j
    temp = []
    print(result)
    result = ''