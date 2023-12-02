#Python program to linearly search x in arr[]. 
def linear_search(arr, x):
    
    for i in range(len(arr)):
        if arr[i] == x:
            return i  
    return -1  

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
element_to_search = 5

result = linear_search(arr, element_to_search)

if result != -1:
    print(f"Element {element_to_search} found at index {result}.")
else:
    print(f"Element {element_to_search} not found in the array.")

