def FactorBaseGenerator(t):
    import sympy
    factorBase = []
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
    if x == 0 or x == 1:
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
def int_r(num):
    num = int(num + (0.5 if num > 0 else -0.5))
    return num

def main():
    import math
    import random
    import time
    import numpy
    from scipy.linalg import lstsq
    start = time.time()
    #g = int(input('Введите число g: '))
    #n = int(input('Введите число n: '))
    #t = int(input('Введите количество простых чисел для фактор базы: '))
    #factorbase = FactorBaseGenerator(t)

    n = 1117
    g = 2
    h = 1058
    c = 5
    factorbase = [2, 3, 5]
    t = len(factorbase)
    comparisons = {}
    #ks = [1, 13, 25]
    while True:
        i = 0
        while True:
            k = random.randint(0, n - 1)
            #print(k)
            #k = ks[i]
            #print(pow(g, k, n))
            if NumberIsSmooth(pow(g, k, n), factorbase):
                #print(SmoothSplit(pow(g, k, n), factorbase))
                comparisons[k] = SmoothSplit(pow(g, k, n), factorbase)
            
            if len(comparisons) >= t + c:
                break
            i += 1
        #print(comparisons)

        solutions = []
        a = numpy.zeros(shape=(t + c, t))
        b = numpy.zeros(shape=(t + c, 1))
        i = 0
        for key in comparisons:
            a[i] = comparisons[key]
            b[i] = key
            i += 1
        
        res = lstsq(a, b)[0]
        #print(lstsq(a, b)[0])
        for i in range(3):
            solutions.append(int_r(float(res[i])) % (n - 1))
        
        #print(solutions)
        comparisons = {}
        while True:
            k = random.randint(0, n - 1)
            if NumberIsSmooth(h * pow(g, k, n) % (n), factorbase):
                #print(h * pow(g, k, n) % (n))
                hg = SmoothSplit(h * pow(g, k, n) % (n), factorbase)
                break
        x = 0
        for i in range(len(hg)):
            x += hg[i] * solutions[i] % (n - 1)

        x = (x - k) % (n - 1)

        if pow(g, x, n) == h:
            print(x)
            end = time.time()
            print(end - start)
            return x


if __name__ ==  "__main__":
    main()