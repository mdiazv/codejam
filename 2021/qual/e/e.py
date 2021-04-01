from collections import Counter
from operator import itemgetter
import random

def cheater(Rs):
    QD = [0] * 10000 # Question Difficulty
    PS = [0] * 100   # Player Score
    for i, R in enumerate(Rs):
        for j, r in enumerate(R):
            QD[j] += r == '0' # Most mistakes ==> harder question
            PS[i] += r == '1' # Correct answer

    # Permutations
    PP = sorted(enumerate(PS), key=itemgetter(1))
    QP = sorted(enumerate(QD), key=itemgetter(1))

    M = []  # Sorted matrix
    TD = [] # Tail delta
    for p, _ in PP:
        M.append(''.join(Rs[p][q] for q, _ in QP[-500:]))
        C = Counter(M[-1])
        TD.append(C['1'] - C['0'])

    # Compare average of similarly ranked players on the hardest questions
    sus = []
    BLOCK = 5
    THRESHOLD = 100
    while not sus:
        for k in range(101-BLOCK):
            avg = sum(TD[k+i] for i in range(BLOCK)) / BLOCK
            sus += [PP[k+i][0] for i in range(BLOCK) if TD[k+i]-avg > THRESHOLD]

        THRESHOLD -= 5

    return random.choice(sus)+1

T = int(input())
P = int(input())
for x in range(1, T+1):
    Rs = [input() for _ in range(100)]
    print(f"Case #{x}: {cheater(Rs)}")
