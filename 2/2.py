def binary_search(arr, target):
  
    left = 0  
    right = len(arr) - 1  
    count = 0
    upper_bound = None

    while left <= right:
        count +=1
        mid = (left + right) // 2  

        if arr[mid] == target:
            return count,right  
        elif arr[mid] < target:
            left = mid + 1  
        else:
            upper_bound = arr[mid]
            right = mid - 1  


    return (count, upper_bound) 


array = [2, 5, 8, 12, 16.25, 23, 38, 56, 72, 91]
target = 6
result = binary_search(array, target)

print(f"Кількість ітерацій: {result[0]}, Верхня межа: {result[1]}")