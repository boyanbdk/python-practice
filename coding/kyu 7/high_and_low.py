def high_and_low(numbers):
    parts = numbers.split(" ")
    nums = list(map(int, parts))
    return (f'{max(nums)} {min(nums)}')
    

high_and_low("1 2 3")
high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4")