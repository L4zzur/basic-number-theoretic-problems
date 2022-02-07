def algo3(a, p):
    import sympy
    if not sympy.isprime(p):
        raise Exception(f'Введённое число {p} не является простым.')
    r = 0
    if p % 8 != 5:
        print(f'Условие {p} ≡ 5 (mod 8) не выполняется.')
        return 0
    # STEP 1
    d = pow(a, (p - 1) // 4, p)
    # STEP 2
    if d == 1:
        r = pow(a, (p + 3) // 8, p)
        return r
    # STEP 3
    elif d == p - 1:
        r = (2 * a * pow(4 * a, (p - 5) // 8, p)) % p
        return r
    
    return r

def main():
    # INPUT
    a = int(input('Введите целое число a: '))
    p = int(input('Введите простое число p: '))
    
    if algo3(a, p) != 0:
        r = algo3(a, p)
        # STEP 4
        print(f'Ответ: {r}, {-r % p}')

if __name__ ==  "__main__":
    main()