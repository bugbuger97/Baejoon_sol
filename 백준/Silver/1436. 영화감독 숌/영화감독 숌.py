N = int(input())
cnt = 0
result = 666

# 브루트 포스 알고리즘 == 완전 탐색 알고리즘
# 브루트 포스 알고리즘은 가능한 모든 수를 조합하는 방식으로 가장 원시적인 방법임.
while True:
  if '666' in str(result):
    cnt+=1
  if cnt==N:
    break
  result+=1
print(result)