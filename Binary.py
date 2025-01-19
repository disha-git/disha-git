## Implement Binary Search for sorted array ?
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        
        elif arr[mid] > target:
            right = mid - 1
        
        else:
            left = mid + 1
    
    return -1  

sorted_array = [1, 3, 5, 7, 9, 11, 13]
target = 7
result = binary_search(sorted_array, target)
print("Index of target:", result)  


## Implement Linear Search for unsorted array?
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1  

unsorted_array = [4, 2, 9, 7, 1, 6]
target = 7
result = linear_search(unsorted_array, target)
print("Index of target:", result)  




