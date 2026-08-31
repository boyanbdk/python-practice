def is_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    else:
        return a + b + c > 2 * max(a,b,c)
