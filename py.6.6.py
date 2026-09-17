def find_intersection(arr1, arr2):
    # Use filter and lambda inside the function to find common elements
    return list(filter(lambda x: x in arr2, arr1))

# Example usage:
array1 = [1, 2, 3, 4, 5]
array2 = [3, 4, 5, 6, 7]

result = find_intersection(array1, array2)

print("Array 1:", array1)
print("Array 2:", array2)
print("Intersection:", result)
