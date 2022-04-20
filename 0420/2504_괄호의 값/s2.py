import sys
sys.stdin = open('input.txt')

brackets = list(input())

stack = []
temp = 1
answer = 0
for i in range(0, len(brackets)):
    if brackets[i] == '(':
        stack.append('(')
        temp *= 2
    elif brackets[i] == '[':
        stack.append('[')
        temp *= 3
    elif brackets[i] == ')':
        if not stack or stack[-1] != '(':
            answer = 0
            break
        if brackets[i-1] == '(':
            answer += temp
        stack.pop()
        temp //= 2
    elif brackets[i] == ']':
        if not stack or stack[-1] != '[':
            answer = 0
            break
        if brackets[i - 1] == '[':
            answer += temp
        stack.pop()
        temp //= 3
    else:
        answer = 0
        break

if stack:
    answer = 0
print(answer)
