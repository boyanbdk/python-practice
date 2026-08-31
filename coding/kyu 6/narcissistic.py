def narcissistic(value):
    value_narc = 0
    for i in range (len(str(value))):
        value_narc += pow(int(str(value)[i]), len(str(value)))
    
    return value == value_narc