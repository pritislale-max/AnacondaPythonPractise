"""
Program to work with natural numbers from 1 to 100
"""

# Display all natural numbers from 1 to 100
print("Natural Numbers from 1 to 100:")
print("=" * 50)

for num in range(1, 101):
    print(num, end=" ")
    if num % 10 == 0:  # New line after every 10 numbers
        print()

print("\n" + "=" * 50)

# Calculate sum of natural numbers from 1 to 100
total_sum = sum(range(1, 101))
print(f"\nSum of natural numbers from 1 to 100: {total_sum}")

# Calculate average
average = total_sum / 100
print(f"Average of natural numbers from 1 to 100: {average}")

# Count even and odd numbers
even_numbers = [num for num in range(1, 101) if num % 2 == 0]
odd_numbers = [num for num in range(1, 101) if num % 2 != 0]

print(f"\nTotal even numbers: {len(even_numbers)}")
print(f"Total odd numbers: {len(odd_numbers)}")

# Sum of even and odd numbers
print(f"Sum of even numbers: {sum(even_numbers)}")
print(f"Sum of odd numbers: {sum(odd_numbers)}")

# Prime numbers between 1 and 100
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_numbers = [num for num in range(1, 101) if is_prime(num)]
print(f"\nPrime numbers from 1 to 100: {prime_numbers}")
print(f"Total prime numbers: {len(prime_numbers)}")
