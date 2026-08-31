def is_square(n):
    if n < 0:
        return False
    x = n ** 0.5
    return int(x) == x


print(is_square(5)) 
print(is_square(4)) 
print(is_square(1))
print(is_square(0))
print(is_square(25))
print(is_square(27))
