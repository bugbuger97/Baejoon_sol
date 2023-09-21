if __name__ == '__main__':
  Input_List = list(map(int,input().split(' ')))
  ascending = [1,2,3,4,5,6,7,8]
  descending = [8,7,6,5,4,3,2,1]
  if Input_List == ascending:
    print('ascending')
  elif Input_List == descending:
    print('descending')
  else:
    print('mixed') 