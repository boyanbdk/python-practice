def sort_array(arr):
    odd_arr = []
    for i in range(len(arr)):
        if arr[i] % 2:
            odd_arr.append(arr[i])
    
    odd_arr.sort()
    j = 0
    for k in range(len(arr)):
        if arr[k] % 2:
            arr[k] = odd_arr[j]
            j += 1
    return arr
