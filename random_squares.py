def FactorBaseGenerator(t):
    import sympy
    factorBase = []
    amount = 0
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
        while x % p == 0:
            x //= p
    return x == 1



def main():
    import sympy
    import math
    import random

    n = int(input('Введите число n: '))
    if sympy.isprime(n):
        print(f'{n} - просто число')
        return 0
    t = int(input('Введите количество простых чисел для фактор базы: '))

    factorbase = FactorBaseGenerator(t)

    a = random.randint(1, n)
    b = random.randint(1, n)

    try_count = 0

    while True:
        try_count += 1
        print(f'########### Попытка №{try_count} ###########')

        numpairs = []
        while len(numpairs) < len(factorbase) + 1:
            if pow(a, 2, n) == b and NumberIsSmooth(b, factorbase):
                a_b = [a, b]
                numpairs.append(a_b)
                print(a_b)
            b += 1
            if b > n:
                a = random.randint(1, n)
                b = random.randint(1, n)
        print(f"Пары: {numpairs}\n", f"Количество пар: {len(numpairs)}\n")
        x = 1
        y = 1
        for numpair in numpairs:
            x *= numpair[0]
            y *= numpair[1]
        
        y = int(math.sqrt(y) % n)
        x %= n

        if pow(x, 2, n) == pow(y, 2, n) and x != y and x != (-y + n):
            result = math.gcd(abs(x - y), n)
            if 1 < result < n:
                print(
                f'Результат: {result}\nПроверка: {n} / {result} = {n / result}')
                return 0

if __name__ ==  "__main__":
    main()