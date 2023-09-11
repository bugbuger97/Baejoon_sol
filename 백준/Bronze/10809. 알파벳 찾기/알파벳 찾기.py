if __name__ == '__main__':
  S = input()
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  for i in alphabet:
    print(S.find(i), end = ' ') # string.find(finding str, start Index, end Index)
    # 찾는 문자가 존재한다면 해당 위치의 index를 반환
    # 찾는 문자가 존재하지 않는다면 -1을 반환