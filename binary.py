def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        mid_element = arr[mid]
        
        if mid_element == target:
            return mid  
        elif mid_element < target:
            low = mid + 1  
        else:
            high = mid - 1  
    
    return -1  

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 3
result = binary_search(array, target)

if result != -1:
    print(f"Элемент {target} найден в массиве на позиции {result}.")
else:
    print(f"Элемент {target} не найден в массиве.")
