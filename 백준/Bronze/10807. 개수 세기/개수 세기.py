if __name__ == '__main__':
  N = int(input())
  numbers = input()
  find_num = int(input())
  numbers = list(map(int,numbers.split()))
  print(numbers.count(find_num))