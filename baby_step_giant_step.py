def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

def bsgs(g, h, n):
    import math

    m = int(math.sqrt(n)) + 1
    l = pow(g, m, n)
    table = {}
    for i in range(m):
        table[i + 1] = l
        l = (l * pow(g, m, n)) % n
    
    for j in range(m):
        k = (h * pow(g, j, n)) % n
        if k in table.values():
            return get_key(table, k) * m - j
        

def main():
    answer = bsgs(11, 586856, 2367671)
    print(answer)
    
if __name__ ==  "__main__":
    main()