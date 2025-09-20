Here are code examples in several programming languages to check if a number is even or not:

### Python
```python
def is_even(number):
    return number % 2 == 0

# Example usage
num = int(input("Enter a number: "))
if is_even(num):
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")
```

### JavaScript
```javascript
function isEven(number) {
    return number % 2 === 0;
}

// Example usage
const num = parseInt(prompt("Enter a number: "));
if (isEven(num)) {
    console.log(`${num} is even.`);
} else {
    console.log(`${num} is odd.`);
}
```

### Java
```java
import java.util.Scanner;

public class EvenOddChecker {
    public static boolean isEven(int number) {
        return number % 2 == 0;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int num = scanner.nextInt();

        if (isEven(num)) {
            System.out.println(num + " is even.");
        } else {
            System.out.println(num + " is odd.");
        }
    }
}
```

### C
```c
#include <stdio.h>

int isEven(int number) {
    return number % 2 == 0;
}

int main() {
    int num;
    printf("Enter a number: ");
    scanf("%d", &num);

    if (isEven(num)) {
        printf("%d is even.\n", num);
    } else {
        printf("%d is odd.\n", num);
    }

    return 0;
}
```

### C++
```cpp
#include <iostream>
using namespace std;

bool isEven(int number) {
    return number % 2 == 0;
}

int main() {
    int num;
    cout << "Enter a number: ";
    cin >> num;

    if (isEven(num)) {
        cout << num << " is even." << endl;
    } else {
        cout << num << " is odd." << endl;
    }

    return 0;
}
```

### C#
```csharp
using System;

class EvenOddChecker {
    static bool IsEven(int number) {
        return number % 2 == 0;
    }

    static void Main() {
        Console.Write("Enter a number: ");
        int num = int.Parse(Console.ReadLine());

        if (IsEven(num)) {
            Console.WriteLine($"{num} is even.");
        } else {
            Console.WriteLine($"{num} is odd.");
        }
    }
}
```

### Go
```go
package main

import "fmt"

func isEven(number int) bool {
    return number%2 == 0
}

func main() {
    var num int
    fmt.Print("Enter a number: ")
    fmt.Scan(&num)

    if isEven(num) {
        fmt.Printf("%d is even.\n", num)
    } else {
        fmt.Printf("%d is odd.\n", num)
    }
}
```

### Ruby
```ruby
def is_even(number)
    number % 2 == 0
end

print "Enter a number: "
num = gets.chomp.to_i

if is_even(num)
    puts "#{num} is even."
else
    puts "#{num} is odd."
end
```

### Swift
```swift
func isEven(_ number: Int) -> Bool {
    return number % 2 == 0
}

print("Enter a number: ", terminator: "")
if let num = Int(readLine() ?? "") {
    if isEven(num) {
        print("\(num) is even.")
    } else {
        print("\(num) is odd.")
    }
} else {
    print("Invalid input.")
}
```

These examples demonstrate how to check if a number is even or odd in various programming languages. The key idea is to use the modulus operator (`%`) to check the remainder when the number is divided by 2. If the remainder is 0, the number is even; otherwise, it's odd.