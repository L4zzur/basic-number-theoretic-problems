from algorithm_1 import algo1
from algorithm_2 import algo2
from algorithm_3 import algo3
from algorithm_4 import algo4

def legenre_symbol(a, p):
    ls = pow(a, (p - 1) // 2, p)
    return -1 if ls == p - 1 else ls

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def algo5(n, p, q, a):
    r, s = 0, 0

    if p % 2 == 0 or legenre_symbol(a, p) == -1 or q % 2 == 0 or legenre_symbol(a, q) == -1:
        return False

    print('------ Поиск r ------')
    if algo2(a, p) != 0:
        print('- 2 алгоритм -')
        r = algo2(a, p)
    elif algo3(a, p) != 0:
        print('- 3 алгоритм -')
        r = algo3(a, p)
    elif algo4(a, p) != 0:
        print('- 4 алгоритм -')
        r = algo4(a, p)
    print('------ Поиск s ------')
    if algo2(a, q) != 0:
        print('- 2 алгоритм -')
        s = algo2(a, q)
    elif algo3(a, q) != 0:
        print('- 3 алгоритм -')
        s = algo3(a, q)
    elif algo4(a, q) != 0:
        print('- 4 алгоритм -')
        s = algo4(a, q)

    z, c, d = egcd(p ,q)
    
    x = (r * d * q + s * c * p) % n
    y = (r * d * q - s * c * p) % n
    
    return x, y

def main():
    # INPUT
    #n = int(input('Введите число n: '))
    #p = int(input('Введите простое число p: '))
    #q = int(input('Введите простое число q: '))
    #a = int(input('Введите число a: '))
    n = 2929
    p = 29
    q = 101
    a = 4

    res = algo5(n, p, q, a)
    if not res:
        print('Error')
    else:
        print(f'Ответ: {res[0]}, {-res[0] % n}, {res[1]}, {-res[1] % n}')

if __name__ ==  "__main__":
    main()
