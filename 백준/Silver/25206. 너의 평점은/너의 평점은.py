# 그룹 단어 확인 횟수 만들기
if __name__ == '__main__':
  judge = {'A+':4.5,'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0.0}
  result = 0
  credit_total_sum = 0
  for i in range(20):
    subject,credit,score = input().split()
    if score == 'P':
      pass
    else:
      credit = float(credit)
      score = judge[score]
      credit_total_sum += credit
      result += credit*score
  print(result/credit_total_sum)