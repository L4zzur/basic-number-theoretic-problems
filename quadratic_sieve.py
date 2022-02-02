def FactorBaseGenerator(t):
    import sympy
    factorBase = [-1]
    amount = 1
    num = 2
    while True:
        if amount == t:
            break
        else:
            if sympy.isprime(num):
                factorBase.append(num)
                amount += 1
            num += 1
    return factorBase

def NumberIsSmooth(x, base):
    if x == 0:
        return False
    for p in base:
        if x < 0:
            x //= p
        elif p != -1:
            while x % p == 0:
                x //= p
    return x == 1

def SmoothSplit(x, base):
    e = []
    for p in base:
        k = 0
        if x < 0:
            x //= p
            k += 1
        elif p != -1:
            while x % p == 0:
                x //= p
                k += 1
        e.append(k)
    return e

def main():
    import math
    import random
    import time
    start = time.time()
    # n = int(input('Введите число n: '))
    n = 24961344
    #t = int(input('Введите количество простых чисел для фактор базы: '))
    m = int(math.sqrt(n))

    #factorbase = FactorBaseGenerator(t)
    factorbase = [-1, 2, 3, 5, 7, 11, 13, 17, 19, 23]
    try_count = 0
    # lsx = [12, 2522, 5794, -1, 4, 156, 102, -6, 2, 9124, 34]
    while True:
        try_count += 1
        print(f'########### Попытка №{try_count} ###########')
        e, v, numpairs = [], [], []
        while len(numpairs) < len(factorbase) + 1:
            x = random.randrange(n)
            b = pow(x + m, 2) - n
            if NumberIsSmooth(b, factorbase):
                ei = SmoothSplit(b, factorbase)
                vi = [i % 2 for i in ei]
                e.append(ei)
                v.append(vi)
                numpair = [x + m, b]
                numpairs.append(numpair)
                print('x = ', x)
            if x > 0:
                x = -x
            else:
                x = abs(x) + 1
        #print(f"Пары: {numpairs}\n", f"Количество пар: {len(numpairs)}\n")

        x = 1
        for numpair in numpairs:
            x *= numpair[0] % n

        T = []
        for i in range(len(factorbase) + 1):
            #print(v[i], sum(v[i]))
            if sum(v[i]) % 2 == 0:
                T.append(i)

        l = []
        for i in range(len(factorbase)):
            lj = 0
            if i in T:
                for j in range(len(factorbase)):
                    lj += e[i][j]
            lj //= 2
            l.append(lj)
        print(l)

        y = 1
        for j in range(len(factorbase)):
            y *= pow(factorbase[j], l[j], n) % n
        
        if ((x % n) == (y % n)) or ((x % n) == (-y % n)):
            continue
        elif math.gcd(x - y, n) != 1:
            print('делитель', math.gcd(x - y, n))
            end = time.time()
            print('выполнено за', end - start)
            return 0

if __name__ ==  "__main__":
    main()