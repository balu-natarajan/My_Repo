import math

def min_sum(n):
    P = list(str(n))
    print('P: ', P)
    print('type of P', type(P))
    c = len(P)
    a = math.ceil(c / 2.0)
    p1 = P[:a]
    p2 = P[a:]
    print('p1 : ', p1)
    print('p2 : ', p2)
    p1.sort()
    print('sorted p1: ', p1)
    p2.sort()
    print('sorted p2: ', p2)
    n1 = ''.join(p1)
    print('n1: ', n1)
    N1 = int(n1)
    n2 = ''.join(p2)
    print('n2: ', n2)
    N2 = int(n2)
    min_sum = N1 + N2
    print('the minimum sum is: ', min_sum)


n = int(input('enter the n val: '))
add = min_sum(n)
