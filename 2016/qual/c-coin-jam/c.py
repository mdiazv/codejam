
sieve_until = 10000000
primes = set()
first_div = {}
sprimes = []

def sieve(K):
    P = set(range(2, K+1))
    for p in xrange(2, K+1):
        if p in first_div:
            continue
        primes.add(p)
        sprimes.append(p)
        for x in xrange(p, K+1, p):
            first_div[x] = p

def onediv(k):
    if k in primes:
        return 1
    if k in first_div:
        return first_div[k]
    top = int(k ** 0.5)+1
    for i in sprimes:
        if i > top:
            break
        if k % i == 0:
            first_div[k] = i
            return i
    return 1

def inbase(k, b, N):
    m = 1
    r = 0
    for i in xrange(N):
        if k & (m << i):
            r += b ** i
    return r;

def main():
    T = int(raw_input())
    for x in xrange(1, T+1):
        N, J = map(int, raw_input().split())
        print "Case #{}:".format(x)
        start = (1 << (N-1)) + 1
        end = (1 << N) - 1
        for k in xrange(start, end+1, 2):
            D = {}
            prime = False
            for b in xrange(2, 11):
                K = inbase(k, b, N)
                D[b] = onediv(K)
                prime = D[b] == 1
                if prime:
                    break

            if not prime:
                print "{:b}".format(k),
                for b in xrange(2, 11):
                    print " {}".format(D[b]),
                print ""
                J -= 1

            if J == 0:
                break

sieve(sieve_until)
main()
