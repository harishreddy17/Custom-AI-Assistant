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
2. It checks if the number is divisible by 2 (i.e., `number % 2 == 0`).
3. If the remainder is 0, the number is even, and the function returns `True`. Otherwise, it returns `False`.
4. The example usage prompts the user to enter a number and then prints whether the number is even or odd.

### Alternative (using bitwise operator):
You can also use a bitwise AND operation to check if a number is even:
```python
def is_even(number):
    return (number & 1) == 0

# Example usage:
num = int(input("Enter a number: "))
if is_even(num):
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")
```

This works because the least significant bit of an even number is always 0. The bitwise AND with 1 checks this bit. If the result is 0, the number is even.