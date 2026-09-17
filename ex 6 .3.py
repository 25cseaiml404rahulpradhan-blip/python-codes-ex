def matrix_with_sums():
    print("Enter the elements for a 3x3 matrix row by row:")
    matrix = []
    
    # Step 1: Take user input for 3 rows
    for i in range(3):
        while True:
            try:
                row_input = input(f"Enter 3 space-separated numbers for Row {i+1}: ")
                # Split the input string and convert each item to an integer
                row = [int(x) for x in row_input.split()]
                
                if len(row) != 3:
                    print("Error: Please enter exactly 3 numbers.")
                    continue
                    
                matrix.append(row)
                break
            except ValueError:
                print("Error: Invalid input. Please enter valid integers.")

    # Step 2: Calculate Column Sums
    col_sums = [0, 0, 0]
    for j in range(3):
        col_sums[j] = matrix[0][j] + matrix[1][j] + matrix[2][j]

    # Step 3: Print the matrix along with Row and Column sums
    print("\n--- Matrix with Row and Column Sums ---")
    
    # Print Rows and their individual sums
    for row in matrix:
        row_sum = sum(row)
        # Format print to align elements nicely
        print(f"{row[0]:<5} {row[1]:<5} {row[2]:<5} | Sum = {row_sum}")
        
    # Print a dividing line
    print("-" * 28)
    
    # Print the calculated Column sums underneath
    print(f"{col_sums[0]:<5} {col_sums[1]:<5} {col_sums[2]:<5}")

# Run the function
matrix_with_sums()
