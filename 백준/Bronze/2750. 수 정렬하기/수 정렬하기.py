if __name__ == "__main__":
  number = []
  N = int(input())
  for i in range(N):
    number.append(int(input()))
  number = sorted(number)
  for i in number:
    print(i)