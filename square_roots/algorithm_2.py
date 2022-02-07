def algo2(a, p):
    import sympy
    if not sympy.isprime(p):
        raise Exception(f'Введённое число {p} не является простым.')
    
    if p % 4 != 3:
        print(f'Условие {p} ≡ 3 (mod 4) не выполняется.')
        return 0
    
    r = pow(a, (p + 1) // 4, p)

    return r

def main():
    # INPUT
    a = int(input('Введите целое число a: '))
    p = int(input('Введите простое число p: '))

    if algo2(a, p) != 0:
        r = algo2(a, p)
        print(f'Ответ: {r}, {-r % p}')

if __name__ ==  "__main__":
    main()