import sys

move = {
    'R': (1, 0),
    'L': (-1, 0),
    'B': (0, -1),
    'T': (0, 1),
    'RT': (1, 1),
    'LT': (-1, 1),
    'RB': (1, -1),
    'LB': (-1, -1)
}


king, rock, cnt = list(sys.stdin.readline().split())
king = [ord(king[0]), int(king[1])]
rock = [ord(rock[0]), int(rock[1])]

for _ in range(int(cnt)):
    dx, dy = move[sys.stdin.readline().strip()]
    if 65 <= king[0]+dx <= 72 and 1 <= king[1]+dy <= 8:
        king = [king[0] + dx, king[1] + dy]
        if king == rock:
            if 65 <= rock[0]+dx <= 72 and 1 <= rock[1]+dy <= 8:
                rock = [rock[0]+dx, rock[1]+dy]
            else:
                king = [king[0]-dx, king[1]-dy]
            
print(chr(king[0]) + str(king[1]))
print(chr(rock[0]) + str(rock[1]))