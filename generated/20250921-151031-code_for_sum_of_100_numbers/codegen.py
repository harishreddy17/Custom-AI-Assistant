# Code to Calculate the Sum of 100 Numbers

Here are implementations in several programming languages:

## Python
```python
# Sum of first 100 natural numbers
sum_100 = sum(range(1, 101))
print("Sum of first 100 numbers:", sum_100)

# Alternative using formula (n(n+1)/2)
n = 100
sum_100_formula = n * (n + 1) // 2
print("Sum using formula:", sum_100_formula)
```

## JavaScript
```javascript
// Sum of first 100 natural numbers
let sum = 0;
for (let i = 1; i <= 100; i++) {
    sum += i;
}
console.log("Sum of first 100 numbers:", sum);

// Using formula
const n = 100;
const sumFormula = n * (n + 1) / 2;
console.log("Sum using formula:", sumFormula);
```

## Java
```java
public class Sum100Numbers {
    public static void main(String[] args) {
        // Sum of first 100 natural numbers
        int sum = 0;
        for (int i = 1; i <= 100; i++) {
            sum += i;
        }
        System.out.println("Sum of first 100 numbers: " + sum);

        // Using formula
        int n = 100;
        int sumFormula = n * (n + 1) / 2;
        System.out.println("Sum using formula: " + sumFormula);
    }
}
```

## C++
```cpp
#include <iostream>
using namespace std;

int main() {
    // Sum of first 100 natural numbers
    int sum = 0;
    for (int i = 1; i <= 100; i++) {
        sum += i;
    }
    cout << "Sum of first 100 numbers: " << sum << endl;

    // Using formula
    int n = 100;
    int sumFormula = n * (n + 1) / 2;
    cout << "Sum using formula: " << sumFormula << endl;

    return 0;
}
```

## C
```c
#include <stdio.h>

int main() {
    // Sum of first 100 natural numbers
    int sum = 0;
    for (int i = 1; i <= 100; i++) {
        sum += i;
    }
    printf("Sum of first 100 numbers: %d\n", sum);

    // Using formula
    int n = 100;
    int sumFormula = n * (n + 1) / 2;
    printf("Sum using formula: %d\n", sumFormula);

    return 0;
}
```

All these implementations will calculate the sum of the first 100 natural numbers (1 + 2 + 3 + ... + 100). The result is 5050, which can also be calculated using the mathematical formula for the sum of the first n natural numbers: n(n+1)/2.