def group_similar_elements(matrix):
    # Step 1: Flatten the random 2D matrix into a single 1D list
    flat_list = []
    for row in matrix:
        for item in row:
            flat_list.append(item)
            
    # Step 2: Count how many times each unique number appears
    frequencies = {}
    for item in flat_list:
        if item in frequencies:
            frequencies[item] += 1
        else:
            frequencies[item] = 1
            
    # Step 3: Create the new grouped matrix sorted by the numbers
    grouped_matrix = []
    for element in sorted(frequencies.keys()):
        count = frequencies[element]
        # Create a row where the element is repeated 'count' times
        grouped_matrix.append([element] * count)
        
    return grouped_matrix

# Setting up rows explicitly to prevent the brackets from glitching out
row1 = [4, 1, 2]
row2 = [2, 4, 1]
row3 = [1, 2, 4]

random_matrix = [row1, row2, row3]

print("Original Random Matrix:")
for row in random_matrix:
    print(row)

# Process the matrix
result_matrix = group_similar_elements(random_matrix)

print("\nMatrix with Groups of Similar Elements:")
for row in result_matrix:
    print(row)
