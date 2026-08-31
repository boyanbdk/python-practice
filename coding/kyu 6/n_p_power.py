def dig_pow(n, p):
    mult = 0
    for i in range(len(str(n))):
        mult += pow(int(str(n)[i]), p + i)

    return (mult / n if mult % n == 0 else -1)