import random
import math

def isPrime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def pollard_p_1(x):
    B = 20
    a = random.randint(2, x - 1)
    d = math.gcd(a, x)

    if d >= 2:
        return d
    
    for q in range(B + 1):
        if isPrime(q):
            l = int(math.log(x) // math.log(q))
            a = pow(a, pow(q, l), x)
    
    d = math.gcd(a - 1, x)
    if d == 1 or d == x:
        return 'f'
    else:
        return d

s = 0
f = 0
for i in range(10000, 1000000):
    if pollard_p_1(i) == 'f':
        f += 1
    else:
        s += 1

print('success', s, 'fails' , f)