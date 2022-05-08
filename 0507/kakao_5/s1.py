def check(alp, cop, p_len, problems):
    count = 0
    for problem in problems:
        if problem[0] <= alp and problem[1] <= cop:
            count += 1
    if count == p_len:
        return True
    else:
        return False


alp = 10
cop = 10
problems = [[10,15,2,1,2],[20,20,3,3,4]]
answer = 0
p_len = len(problems)

while True:
    # 모두 완료할 능력이 되면 while문 탈출
    if check(alp, cop, p_len, problems):
        break

    last_prob = max(problems, key= lambda x: x[0]+x[1]-alp-cop)
    req_alp = last_prob[0]-alp
    req_cop = last_prob[1]-cop
    best_prob = max(problems, key= lambda x: min(req_alp, x[2])+min(req_cop, x[3]))
    if min(req_alp, best_prob[2]) + min(req_cop, best_prob[3]) < best_prob[4]:
        alp += 1
        cop += 1
        answer += 2
    else:
        alp += best_prob[2]
        cop += best_prob[3]
        answer += best_prob[4]

print(answer)