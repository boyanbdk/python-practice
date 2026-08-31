def binary_array_to_number(arr):
    number = 0
    j = 0
    for i in arr:
        number += i * pow(2,len(arr) - j - 1)
        j+=1
    
    return number
 
print(binary_array_to_number([1,0,1,1,0]))
 # 10110 -> 16 + 4 + 2 = 22

def binary_array_to_number_oneline(arr):
    return int("".join(map(str,arr)), 2)

print(binary_array_to_number_oneline([1,0,1,1,0]))