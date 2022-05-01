import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())

words = [sys.stdin.readline().strip() for _ in range(N)]
words.sort(key=lambda x: len(x))

count = len(words)
for i in range(len(words)-1):
    for j in range(i+1, len(words)):
        if words[i] == words[j][:len(words[i])]:
            count -= 1
            break

print(count)

