a,b,c = map(int,input().split())
def solution(a,b,c):
  if b == 1:
    return a%c
  else:
    tmp = solution(a,b//2,c)
    if b%2 == 0:
      return tmp*tmp%c
    else:
      return tmp*tmp*a%c

print(solution(a,b,c))