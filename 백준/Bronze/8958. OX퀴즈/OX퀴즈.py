def Return_OX(ox) -> int:
  flag = []
  score = 0
  result = 0
  for j in ox:
    if len(flag) >= 1:
      if flag[0] == 'O' and j == 'O':
        score += 1
        result += score
        flag.append(j)
    elif j == 'O':
      score = 1
      result += score
      flag.append(j)
    if j == 'X':
      score = 0
      flag = []
  return result

if __name__ == '__main__':
  n = int(input())
  for i in range(n):
    ox = input()
    print(Return_OX(ox))