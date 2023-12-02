#Python program to implement iterative Binary search
def binary_search(arr, x):
    
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  
        if arr[mid] == x:
            return mid 
        elif arr[mid] < x:
            low = mid + 1  
        else:
            high = mid - 1  
    return -1  


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
element_to_search = 5

result = binary_search(arr, element_to_search)

if result != -1:
    print(f"Element {element_to_search} found at index {result}.")
else:
    print(f"Element {element_to_search} not found in the array.")
