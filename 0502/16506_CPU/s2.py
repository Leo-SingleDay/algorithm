import sys
sys.stdin = open('input.txt')

to_assembly = {
    'ADD': '0000',
    'SUB': '0001',
    'MOV': '0010',
    'AND': '0011',
    'OR': '0100',
    'NOT': '0101',
    'MULT': '0110',
    'LSFTL': '0111',
    'LSFTR': '1000',
    'ASFTR': '1001',
    'RL': '1010',
    'RR': '1011'
}

N = int(sys.stdin.readline())

for _ in range(N):
    result = ''
    opcode, rD, rA, rB = sys.stdin.readline().strip().split()
    rD, rA = map(lambda x: x[2:].zfill(3), map(bin, map(int, (rD, rA))))
    result += (rD+rA)

    if opcode[-1] == 'C':
        result += bin(int(rB))[2:].zfill(4)
        result = to_assembly[opcode[:len(opcode)-1]] + '10' + result
    else:
        result += bin(int(rB))[2:].zfill(3)
        result = to_assembly[opcode]+'00' + result + '0'
    print(result)
