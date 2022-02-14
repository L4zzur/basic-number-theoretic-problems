def rho(alpha, betta, n, p):
    S1, S2, S3 = [], [], []
    for i in range(1, p):
        if i % 3 == 1:
            S1.append(i)
        elif i % 3 == 0:
            S2.append(i)
        elif i % 3 == 2:
            S3.append(i)
    x = {0: 1}
    a = {0: 0}
    b = {0: 0}
    i = 0
    while True:
        if x[i] in S1:
            a[i + 1] = a[i] % n
            b[i + 1] = (b[i] + 1) % n
            x[i + 1] = (betta * x[i]) % p
        elif x[i] in S2:
            a[i + 1] = (2 * a[i]) % n
            b[i + 1] = (2 * b[i]) % n
            x[i + 1] = pow(x[i], 2, p)
        elif x[i] in S3:
            a[i + 1] = (a[i] + 1) % n
            b[i + 1] = b[i] % n
            x[i + 1] = (alpha * x[i]) % p
        if i % 2 == 0 and i != 0:
            if x[i // 2] == x[i]:
                r = (b[i // 2] - b[i]) % n
                if r == 0:
                    print('Error')
                    exit()
                else:
                    x = (pow(r, -1, n) * (a[i] - a[i // 2])) % n
                    return x
        #print(f'x[{i + 1}] = {x[i + 1]}, a[{i + 1}] = {a[i + 1]}, b[{i + 1}] = {b[i + 1]}')
        i += 1


def main():
    import sympy
    # alpha betta n p
    answer = rho(89, 799, 101, 809)
    print(answer)
    # p betta alpha
    print(sympy.discrete_log(809, 799, 89))

    answer = rho(2, 5, 28, 29)
    print(sympy.discrete_log(29, 5, 2))
    print(answer)

    answer = rho(2, 228, 191, 383)
    print(answer)
    print(sympy.discrete_log(383, 228, 2))
if __name__ ==  "__main__":
    main()