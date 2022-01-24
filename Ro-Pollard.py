import math
def isNotPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return True
    return False

def pollard(x):
    a = 2
    b = 2
    while True:
        a = (pow(a, 2, x) + 1) % x
        b = (pow(b, 2, x) + 1) % x
        b = (pow(b, 2, x) + 1) % x
        d = math.gcd(a - b, x)
        if d > 1 and d < x:
            return d
        elif d == x:
            return 'f'

s = 0
f = 0
for i in range(10000, 1000000):
    if isNotPrime(i):
        if pollard(i) == 'f':
            f += 1
        else:
            s += 1

print('succsess', s, 'fails' , f)