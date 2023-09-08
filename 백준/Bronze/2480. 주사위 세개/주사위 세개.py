def dice_roll(a,b,c) -> int:
  if a == b == c:
    return 10000 + a * 1000
  elif a == b or b == c or a == c:
    if a == b or b == c:
      return 1000 + b * 100
    else:
      return 1000 + a * 100
  elif a != b != c:
    comparison = [a,b,c]
    comparison = sorted(comparison,reverse=True)
    return comparison[0] * 100
  else:
    return False

if __name__ == '__main__':
  a,b,c = input().split()
  print(dice_roll(int(a),int(b),int(c)))