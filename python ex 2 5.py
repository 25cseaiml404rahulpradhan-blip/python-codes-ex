
data = {
    "Project_A": [1, 2, 2, 3, 3, 3],  
    "Project_B": [4, 5, 6, 7],      
    "Project_C": [9, 9, 9, 9, 9]    
}



max_unique_key = max(data, key=lambda k: len(set(data[k])))


print(f"Dictionary: {data}")
print(f"The key with the maximum unique values is: '{max_unique_key}'")
print(f"Number of unique values: {len(set(data[max_unique_key]))}")
