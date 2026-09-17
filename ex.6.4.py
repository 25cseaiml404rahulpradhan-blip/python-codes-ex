# Method 1: Using a Lambda Function
# This lambda takes a value and a list, returning True if the value is present.
check_with_lambda = lambda val, lst: val in lst


# Method 2: Using a Standard Function (def)
def check_with_func(val, lst):
    if val in lst:
        return True
    else:
        return False


# Example Data for Testing
my_list = [10, 20, 30, 40, 50]
search_value = 30
missing_value = 99

print(f"Target List: {my_list}\n")

# --- Testing Lambda Function ---
print("--- Using Lambda Function ---")
print(f"Is {search_value} present? -> {check_with_lambda(search_value, my_list)}")
print(f"Is {missing_value} present? -> {check_with_lambda(missing_value, my_list)}\n")

# --- Testing Standard Function ---
print("--- Using Standard Function ---")
print(f"Is {search_value} present? -> {check_with_func(search_value, my_list)}")
print(f"Is {missing_value} present? -> {check_with_func(missing_value, my_list)}")
