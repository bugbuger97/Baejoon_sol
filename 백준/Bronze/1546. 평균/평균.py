if __name__ == '__main__':
  N = int(input())
  score = input()
  score = list(map(int,score.split()))
  max_score = max(score)
  for i in range(N):
    score[i] = score[i]/max_score*100
  average = sum(score) / len(score)
  print(average)