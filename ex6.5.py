def fibonacci_func(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    # Initialize the series with the first two terms
    series = [0, 1]
    
    # Loop to calculate the rest of the terms
    for i in range(2, n):
        next_term = series[-1] + series[-2]
        series.append(next_term)
        
    return series

# Example Usage
terms = 10
print(f"Fibonacci series up to {terms} terms (using standard function):")
print(fibonacci_func(terms))
