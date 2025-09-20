Here's a simple code snippet in Python to check if a number is even or not:

```python
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

# Example usage:
num = int(input("Enter a number: "))
if is_even(num):
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")
```

### Explanation:
1. The function `is_even` takes a number as input.
2. It checks if the number is divisible by 2 (using the modulus operator `%`).
3. If the remainder is 0, the number is even (`True`), otherwise it's odd (`False`).
4. The example usage prompts the user to enter a number and prints whether it's even or odd.

### Alternative (shorter version):
```python
number = int(input("Enter a number: "))
print(f"{number} is {'even' if number % 2 == 0 else 'odd'}.")
```

This uses a conditional expression to print the result in one line.