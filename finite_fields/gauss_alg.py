def ord(a, n):
    i = 1
    l = [a]
    while True:
        l.append(l[i - 1] * a % n)
        i += 1
        if l[i - 1] == 1:
            return l

def Gauss(p):
    import random
    import math
    import sympy
    i = 1
    alpha = random.randint(2, p - 1)
    while True:
        t = len(ord(alpha, p))
        if t == p - 1:
            return alpha
        betta = random.randint(2, p - 1)
        while betta in ord(alpha, p):
            betta = random.randint(2, p)
        s = len(ord(betta, p))
        if s == p - 1:
            alpha = betta
        else:
            de = math.lcm(t, s)
            f = sympy.factorint(de)
            d = pow(list(f.keys())[0], list(f.values())[0])
            e = de // d 
            alpha = pow(alpha, t // d) * pow(betta, s // e) % p

def main():
    print(Gauss(47))

if __name__ == "__main__":
    main()