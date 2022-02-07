def legenre_symbol(a, p):
    ls = pow(a, (p - 1) // 2, p)
    return -1 if ls == p - 1 else ls

def algo4(a, p):
    import random
    import galois
    import sympy

    if not sympy.isprime(p):
        raise Exception(f'Введённое число {p} не является простым.')

    b = random.randint(0, p)
    while legenre_symbol((pow(b, 2, p) - 4 * a) % p, p) != -1:
        b = random.randint(0, p)
    
    GF = galois.GF(p)

    f = galois.Poly([1, -b, a], field=GF)
    print(f'{f=}')

    g = galois.Poly.Degrees([(p + 1) // 2], field=GF)
    print(f'{g=}')

    r = g % f
    print(f'{r=}')
    r = r.integer

    return r

def main():
    import time
    # INPUT
    a = int(input('Введите целое число a: '))
    p = int(input('Введите простое число p: '))
    start = time.time()
    r = algo4(a, p)
    end = time.time()
    print(end - start)
    print(f'Ответ: {r}, {-r % p}')

if __name__ ==  "__main__":
    main()