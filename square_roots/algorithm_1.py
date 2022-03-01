def legenre_symbol(a, p):
    ls = pow(a, (p - 1) // 2, p)
    return -1 if ls == p - 1 else ls

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Обратного по модулю не существует.')
    else:
        return x % m

def algo1(a, p):
    import sympy
    import random
    if not sympy.isprime(p):
        raise Exception(f'Введённое число {p} не является простым.')
    if a > p - 1:
        print(f'Число a = {a} не может быть больше p - 1 = {p - 1}')
        return 0
    # STEP 1
    if legenre_symbol(a, p) == -1:
        print(f'a = {a} не имеет квадратного корня по модулю p = {p}')
        return 0
    # STEP 2
    b = random.randint(1, p - 1)
    while legenre_symbol(b ,p) != -1:
        b = random.randint(1, p - 1)
    # STEP 3
    s = 0
    t = p - 1
    while t % 2 == 0 and t != 1:
        s += 1
        t = t // 2
    # STEP 4
    a1 = modinv(a, p)
    # STEP 5
    c = pow(b, t, p)
    r = pow(a, ((t + 1) // 2), p)
    # STEP 6
    for i in range(1, s):
        d = pow(pow(r, 2) * a1, pow(2, s - i - 1), p) # 6.1
        if d % p == p - 1:
            r = (r * c) % p # 6.2
        c = pow(c, 2, p)
    
    return r

def main():
    # INPUT
    #a = int(input('Введите целое число a: '))
    #p = int(input('Введите простое число p: '))
    a = 245649
    p = 156808513
    r = algo1(a, p)
    print(f'Ответ: {r}, {-r % p}')
    
if __name__ ==  "__main__":
    main()