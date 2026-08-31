def two_sum(numbers, target):
    for i in numbers:
        need = target - i

        if need == i:
            if numbers.count(i) > 1:
                first = numbers.index(i)
                second = numbers.index(i, first + 1)
                return (first, second)
            continue
            
        if need in numbers:
            return (numbers.index(i), numbers.index(need))