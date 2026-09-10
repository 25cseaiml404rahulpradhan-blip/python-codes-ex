def get_set_from_user(set_label):
    """Takes a comma-separated string from the user and converts it into a set."""
    user_input = input(f"Enter elements for {set_label} (separated by commas): ")
    # Split by comma, strip whitespace, and create a set
    return {element.strip() for element in user_input.split(",") if element.strip()}

def perform_set_operations(set_a, set_b):
    """Performs and prints all major set operations."""
    print("\n📊 --- SET OPERATION RESULTS ---")
    print(f"Set A: {set_a}")
    print(f"Set B: {set_b}")
    print("-" * 35)
    
    # 1. Union (Elements in either set A or set B)
    union_result = set_a | set_b  # or set_a.union(set_b)
    print(f"➡️ Union (A ∪ B)               : {union_result}")
    
    # 2. Intersection (Elements present in both A and B)
    intersection_result = set_a & set_b  # or set_a.intersection(set_b)
    print(f"➡️ Intersection (A ∩ B)        : {intersection_result}")
    
    # 3. Difference (Elements in A but not in B)
    diff_a_b = set_a - set_b  # or set_a.difference(set_b)
    print(f"➡️ Difference (A - B)          : {diff_a_b}")
    
    # 4. Difference (Elements in B but not in A)
    diff_b_a = set_b - set_a  # or set_b.difference(set_a)
    print(f"➡️ Difference (B - A)          : {diff_b_a}")
    
    # 5. Symmetric Difference (Elements in either A or B, but NOT both)
    sym_diff = set_a ^ set_b  # or set_a.symmetric_difference(set_b)
    print(f"➡️ Symmetric Difference (A Δ B): {sym_diff}")

# --- Main Program Execution ---
# 1. Get both sets from the user
set1 = get_set_from_user("Set 1")
set2 = get_set_from_user("Set 2")

# 2. Run operations if the sets aren't empty
perform_set_operations(set1, set2)
