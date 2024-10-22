import sys

def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():
    """Main function to execute the prime checker."""
    if len(sys.argv) < 2:
        print("Usage: python prime.py <positive_integer>")
        return

    try:
        number = int(sys.argv[1])
        if number < 0:
            print("Please enter a positive integer.")
            return

        # Check if the number is prime
        if is_prime(number):
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is not a prime number.")

    except ValueError:
        print("Invalid input. Please provide a positive integer.")

if __name__ == "__main__":
    main()
