def get_user_set(prompt):
    user_input = input(prompt)
    return {element.strip() for element in user_input.split(",") if element.strip()}

def combine_sets(set_a, set_b):
    combined = set()
    for item in set_a:
        combined.add(item)
    for item in set_b:
        combined.add(item)
    return combined

set1 = get_user_set("Enter elements for the first set (separated by commas): ")
set2 = get_user_set("Enter elements for the second set (separated by commas): ")

result_set = combine_sets(set1, set2)

print("Combined Set without duplicates:", result_set)
