def find_even_index(arr):
    cur = 0
    total_sum = sum(arr)
    for i in range(len(arr)):
        if 2 * cur == total_sum - arr[i]:
            return i
        else:
            cur += arr[i]
    
    return -1