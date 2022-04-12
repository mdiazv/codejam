
def alternate(a, b, n):
    return (a+b)*n+a+'\n'

def render(R, C):
    s  = '..' + alternate('+', '-', C-1)
    s += '..' + alternate('|', '.', C-1)
    for k in range(R-1):
        s += alternate('+', '-', C)
        s += alternate('|', '.', C)
    s += alternate('+', '-', C)
    print (s, end ='')

T = int(input())
for x in range(1, T+1):
    R, C = map(int, input().split())
    print (f'Case #{x}:')
    render(R, C)
