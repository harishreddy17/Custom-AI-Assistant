Here's a simple code snippet in Python to calculate the sum of the first 100 numbers (1 to 100):

### Python Code:
```python
# Sum of the first 100 numbers (1 to 100)
sum_of_numbers = sum(range(1, 101))
print("Sum of the first 100 numbers:", sum_of_numbers)
```

### Explanation:
1. `range(1, 101)` generates numbers from 1 to 100 (inclusive of 1, exclusive of 101).
2. `sum()` calculates the total of all numbers in the range.
3. The result is printed.

### Output:
```
Sum of the first 100 numbers: 5050
```

### Alternative (Using a Loop):
If you prefer using a loop:
```python
total = 0
for num in range(1, 101):
    total += num
print("Sum of the first 100 numbers:", total)
```

Both methods will give the same result. The first method is more concise, while the second demonstrates the underlying logic.