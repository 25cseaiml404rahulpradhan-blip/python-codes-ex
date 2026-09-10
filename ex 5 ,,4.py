def get_user_set():
    user_input = input("Enter elements for the set (separated by commas): ")
    return {element.strip() for element in user_input.split(",") if element.strip()}

def copy_set_element_by_element(source_set):
    destination_set = set()
    for element in source_set:
        destination_set.add(element)
    return destination_set

original_set = get_user_set()
copied_set = copy_set_element_by_element(original_set)

print("Original Set:", original_set)
print("Copied Set  :", copied_set)
