import sys
sys.stdin = open('input.txt')

n, m = map(int, sys.stdin.readline().split())
pokedex = [sys.stdin.readline().strip() for _ in range(n)]


for i in range(m):
    quiz = sys.stdin.readline().strip()
    if (quiz[0] not in ['0','1','2','3','4','5','6','7','8','9']):
        print(pokedex.index(quiz)+1)
    else:
        print(pokedex[int(quiz)-1])

