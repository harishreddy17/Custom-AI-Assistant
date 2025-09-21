# Sum of 100 Numbers

Here are several ways to calculate the sum of 100 numbers in Python:

## Method 1: Using a loop
```python
numbers = range(1, 101)  # Creates numbers from 1 to 100
total = 0

for num in numbers:
    total += num

print("Sum of numbers from 1 to 100:", total)
```

## Method 2: Using the sum() function
```python
numbers = range(1, 101)
total = sum(numbers)
print("Sum of numbers from 1 to 100:", total)
```

## Method 3: Using mathematical formula (faster for large ranges)
```python
n = 100
total = n * (n + 1) // 2  # Sum of first n natural numbers
print("Sum of numbers from 1 to 100:", total)
```

## Method 4: Sum of user-input numbers
```python
numbers = []
for i in range(100):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

total = sum(numbers)
print("Sum of the 100 numbers:", total)
```

The mathematical formula method (Method 3) is the most efficient for calculating the sum of consecutive integers from 1 to n, as it computes the result in constant time O(1) rather than O(n) for the loop methods.