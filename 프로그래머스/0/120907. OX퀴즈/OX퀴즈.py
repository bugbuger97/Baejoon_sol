def solution(quiz):
    answer = []
    for k in range(len(quiz)):
        ans = ''
        flag = False
        truth = None
        expression = ''
        temp = quiz[k].replace(" ", "")   
        for i in range(len(temp)):
            if flag:
                ans += temp[i]
            elif (not flag) and (temp[i] != "="):
                expression += temp[i]
            if temp[i] == "=":
                flag = True
        if eval(expression) == int(ans):
            answer.append("O")
        else:
            answer.append("X")
    return answer