if __name__ == '__main__':
  input_structure = list(map(int,input().split()))
  correct_structure = [1,1,2,2,2,8]
  result = []
  for i in range(len(correct_structure)):
    result.append(correct_structure[i] - input_structure[i])
  print(*result)