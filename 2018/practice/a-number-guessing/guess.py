import sys

T = int(input())
for x in range(1, T+1):
    A, B = map(int, input().split(' '))
    N = int(input())
    while N > 0:
        print('Solving for ({}, {}] in {} attempts'.format(A, B, N), file=sys.stderr)
        g = ((A+B) // 2) + 1
        print('Guess: {}'.format(g), file=sys.stderr)
        print(g)
        feedback = input()
        if feedback == 'CORRECT':
            print('Success', file=sys.stderr)
            break
        elif feedback == 'TOO_SMALL':
            A = g
        elif feedback == 'TOO_BIG':
            B = g-1
        elif feedback == 'WRONG_ANSWER':
            print('Got WA', file=sys.stderr)
            sys.exit(0)
        N -= 1

