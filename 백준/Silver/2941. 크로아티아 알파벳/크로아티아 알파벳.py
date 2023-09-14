if __name__ == '__main__':
  S = input()
  character = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
  for i in character:
    S = S.replace(i,'0')
  print(len(S))