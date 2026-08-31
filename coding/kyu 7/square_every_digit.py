def square_digits(num):
    digits = list(str(num))
    for i in digits:
        i = int(int(i) * int(i))
    return "".join(digits)
    