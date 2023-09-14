if __name__ == '__main__':
  S = input().upper()
  S_list = list(set(S))
  cnt = [S.count(i) for i in S_list]
  if cnt.count(max(cnt)) > 1:
    print('?')
  else:
    print(S_list[cnt.index(max(cnt))])