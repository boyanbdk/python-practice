import math

def persistence(n):
    if(len(str(n)) == 1):
        return 0
    else:
        return 1 + persistence(math.prod(list(map(int, str(n)))))