from algorithm_2 import algo2
from algorithm_3 import algo3
from algorithm_4 import algo4

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def algo5(n, p, q, a):
    r, s = 0, 0

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
    n = int(input('Введите число n: '))
    p = int(input('Введите простое число p: '))
    q = int(input('Введите простое число q: '))
    a = int(input('Введите число a: '))

    x, y = algo5(n, p, q, a)

    print(f'Ответ: {x}, {-x % n}, {y}, {-y % n}')

if __name__ ==  "__main__":
    main()
