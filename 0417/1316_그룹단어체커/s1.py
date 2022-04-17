import sys
sys.stdin = open('input.txt')

N = int(input())
answer = 0

for i in range(N):
    sentence = input()
    last_char = sentence[0]
    used_char = [sentence[0]]
    count = 1
    for i in range(1, len(sentence)):
        if sentence[i] in used_char:
            if sentence[i] == last_char:
                count += 1
            else:
                break
        else:
            count += 1
            last_char = sentence[i]
            used_char.append(sentence[i])
    if count == len(sentence):
        answer += 1
print(answer)

