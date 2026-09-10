
def remove_duplicate_values(input_dict):
    """
    Removes duplicate values from a dictionary, 
    keeping only the first occurrence of each value.
    """
    seen_values = set()
    cleaned_dict = {}
    
    for key, value in input_dict.items():
        if value not in seen_values:
            cleaned_dict[key] = value
            seen_values.add(value)
            
    return cleaned_dict



inventory = {
    "Laptop": 1200,
    "Phone": 800,
    "Monitor": 300,
    "Tablet": 800,   
    "Keyboard": 100,
    "TV": 1200
}

result = remove_duplicate_values(inventory)


print("Original:", inventory)
print("Cleaned :", result)
