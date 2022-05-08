def solution(survey, choices):
    result = {
        'R': 0,
        'T': 0,
        'C': 0,
        'F': 0,
        'J': 0,
        'M': 0,
        'A': 0,
        'N': 0
    }
    for i in range(len(survey)):
        result[survey[i][0]] += (4 - choices[i])

    ans = ""
    # 1번지표
    if result['R'] - result['T'] >= 0:
        ans += 'R'
    else:
        ans += 'T'

    # 2번지표
    if result['C'] - result['F'] >= 0:
        ans += 'C'
    else:
        ans += 'F'

    # 3번지표
    if result['J'] - result['M'] >= 0:
        ans += 'J'
    else:
        ans += 'M'

    # 4번지표
    if result['A'] - result['N'] >= 0:
        ans += 'A'
    else:
        ans += 'N'

    return ans