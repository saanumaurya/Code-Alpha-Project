def fibonacci_generator(n):
    fib_sequence = [0, 1]  # Initialize with the first two Fibonacci numbers
    
    # Generate Fibonacci sequence up to the nth term
    while len(fib_sequence) < n:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    
    return fib_sequence

# Example usage:
n_terms = 10  # Change this to generate the sequence up to a different number of terms
fib_sequence = fibonacci_generator(n_terms)
print("Fibonacci sequence up to {} terms:".format(n_terms))
print(fib_sequence)

     