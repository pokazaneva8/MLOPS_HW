import random

random_sequence = [random.randint(1, 1000) for _ in range(100)]

def generate_fibonacci_sequence(limit):
    fibonacci_numbers = [0, 1]
    while True:
        next_fib = fibonacci_numbers[-1] + fibonacci_numbers[-2]
        if next_fib > limit:
            break
        fibonacci_numbers.append(next_fib)
    return set(fibonacci_numbers)  

max_value = max(random_sequence)
fibonacci_numbers = generate_fibonacci_sequence(max_value)

fibonacci_in_sequence = [num for num in random_sequence if num in fibonacci_numbers]

print("Числа Фибоначчи в рандомной последовательности:", fibonacci_in_sequence)