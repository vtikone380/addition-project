# addition.py

def add_two_numbers(a, b):
    return a + b

def add_three_numbers(a, b, c):
    return a + b + c

if __name__ == "__main__":
    result_two = add_two_numbers(5, 3)
    print(f"Sum of 5 and 3 is {result_two}")

    result_three = add_three_numbers(5, 3, 2)
    print(f"Sum of 5, 3, and 2 is {result_three}")
