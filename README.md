# Python Unit 1 Programs

A collection of Python practice programs and assignments covering core programming concepts from Unit 1.

---

## 📁 Project Structure

```
python/
├── main.py
└── Unit1_Programs/
    ├── P1_eval_expression.py
    ├── P2_cricket_scores.py
    ├── P3_positive_negative.py
    ├── P4_maximum_three_numbers.py
    ├── P5_sum_until_zero.py
    ├── P6_not_divisible.py
    ├── P7_armstrong_number.py
    ├── P8_perfect_number.py
    ├── P9_date_time.py
    ├── P10_add_days_to_date.py
    ├── P11_sum_of_series.py
    ├── P12_char_frequency_file.py
    ├── P13_hcf_gcd.py
    ├── P14_swap_first_last_digit.py
    ├── P15_prime_numbers_upto_n.py
    ├── P16_sum_odd_numbers.py
    ├── P17_palindrome_number.py
    ├── P18_char_frequency_string.py
    ├── P19_multiplication_table.py
    ├── P20_power_of_number.py
    ├── P21_count_digits.py
    ├── P22_sum_of_powers.py
    ├── P23_factorial_recursion.py
    ├── P24_fibonacci_series.py
    ├── P25_factors_prime_check.py
    ├── Q1_gross_salary.py
    ├── Q2_menu_area.py
    ├── Q3_employee_bonus.py
    ├── Q4_list_methods.py
    ├── Q5_tuple_methods.py
    ├── Q6_dictionary_methods.py
    ├── Q7_calculator_menu.py
    ├── Q8_percentage_grade.py
    └── sample.txt
```

---

## 🚀 Getting Started

**Requirements:** Python 3.x — no external libraries needed.

```bash
# Run any program
python Unit1_Programs/P1_eval_expression.py
```

---

## 📘 Practice Programs (P-Series)

### P1 — Evaluate Expression
**File:** `P1_eval_expression.py`  
Accepts a math expression as a string from the user and evaluates it at runtime using Python's built-in `eval()` function.

```
Input:  5 + 3 * 2
Output: Result = 11
```

---

### P2 — Cricket Scores Dictionary
**File:** `P2_cricket_scores.py`  
Builds a dictionary of player names mapped to their scores from user input, then retrieves a specific player's score by name.

```
Input:  Virat → 82, Rohit → 56, Dhoni → 44
        Search: Rohit
Output: Rohit scored 56 runs.
```

---

### P3 — Positive or Negative
**File:** `P3_positive_negative.py`  
Checks whether a given number is positive or negative using an `if-else` statement.

```
Input:  10      Output: Number is Positive
Input:  -5      Output: Number is Negative
```

---

### P4 — Maximum of Three Numbers
**File:** `P4_maximum_three_numbers.py`  
Finds the largest among three user-input integers using chained `if/elif/else` comparisons.

```
Input:  45, 78, 23
Output: Maximum number = 78
```

---

### P5 — Sum Until Zero
**File:** `P5_sum_until_zero.py`  
Continuously accepts numbers from the user in a loop and accumulates a running sum. Stops and prints the total when the user enters `0`.

```
Input:  10, 20, 30, 0
Output: Sum = 60
```

---

### P6 — Numbers Not Divisible by First 8 Primes
**File:** `P6_not_divisible.py`  
Prints all integers from 1 to 1000 that are not divisible by any of: 2, 3, 5, 7, 11, 13, 17, 19.

```
Output: 1, 23, 29, 31, 37, 41, 43, 47 ... (up to 1000)
```

---

### P7 — Armstrong Number
**File:** `P7_armstrong_number.py`  
Checks if a number is an Armstrong number — a number equal to the sum of its digits each raised to the power of the digit count.

```
Input:  153     Output: Armstrong Number       (1³ + 5³ + 3³ = 153)
Input:  100     Output: Not an Armstrong Number
```

---

### P8 — Perfect Number
**File:** `P8_perfect_number.py`  
Checks if a number is perfect — i.e., the sum of its proper divisors (excluding itself) equals the number.

```
Input:  6       Output: Perfect Number         (1 + 2 + 3 = 6)
Input:  10      Output: Not a Perfect Number
```

---

### P9 — Date and Time
**File:** `P9_date_time.py`  
Displays today's date, current time, and the combined datetime using Python's `datetime` module.

```
Output:
Today's Date: 2026-10-07
Current Time: 22:18:45.123456
Date and Time: 2026-10-07 22:18:45.123456
```

---

### P10 — Add Days to Date
**File:** `P10_add_days_to_date.py`  
Takes a number of days from the user, adds it to today's date using `timedelta`, and prints the resulting date. Handles month-end and leap year boundaries automatically.

```
Input:  10
Output: Today's date: 2026-10-07
        Date after adding days: 2026-10-17
```

---

### P11 — Sum of Series (1/2 + 1/3 + ... + 1/N)
**File:** `P11_sum_of_series.py`  
Computes the sum of the harmonic-style series: `1/2 + 1/3 + 1/4 + ... + 1/N`.

```
Input:  5
Output: Sum of series = 1.2833333333333332
```

---

### P12 — Character Frequency from File
**File:** `P12_char_frequency_file.py`  
Writes a sample string to `sample.txt`, reads it back, and counts the frequency of each character into a dictionary. Demonstrates basic file I/O.

```
Output:
H : 1   e : 1   l : 3   o : 3   (space) : 3 ...
```

---

### P13 — HCF / GCD
**File:** `P13_hcf_gcd.py`  
Finds the Highest Common Factor (GCD) of two integers using the Euclidean algorithm.

```
Input:  48, 18
Output: HCF / GCD = 6
```

---

### P14 — Swap First and Last Digit
**File:** `P14_swap_first_last_digit.py`  
Converts a number to a string and swaps its first and last characters. Handles the single-digit edge case gracefully.

```
Input:  12345
Output: Number after swapping: 52341
```

---

### P15 — Prime Numbers Up to N
**File:** `P15_prime_numbers_upto_n.py`  
Prints all prime numbers from 2 to N using nested loop trial division with an `is_prime` flag.

```
Input:  50
Output: 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
```

---

### P16 — Sum of Odd Numbers
**File:** `P16_sum_odd_numbers.py`  
Finds the sum of all odd numbers from 1 to N using `range(1, n+1, 2)`.

```
Input:  10
Output: Sum of odd numbers = 25
```

---

### P17 — Palindrome Number
**File:** `P17_palindrome_number.py`  
Checks if a number is a palindrome by reversing its digits in a `while` loop and comparing with the original.

```
Input:  121     Output: Palindrome Number
Input:  123     Output: Not a Palindrome Number
```

---

### P18 — Character Frequency from String
**File:** `P18_char_frequency_string.py`  
Counts the frequency of each character in a user-input string and stores the result in a dictionary.

```
Input:  hello
Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
```

---

### P19 — Multiplication Table
**File:** `P19_multiplication_table.py`  
Prints the multiplication table (1 to 10) for a given number.

```
Input:  5
Output: 5 x 1 = 5
        5 x 2 = 10  ...  5 x 10 = 50
```

---

### P20 — Power of a Number
**File:** `P20_power_of_number.py`  
Computes `base ** power` using Python's exponentiation operator.

```
Input:  base = 2, power = 8
Output: Result = 256
```

---

### P21 — Count Digits
**File:** `P21_count_digits.py`  
Defines a `count_digits(num)` function that counts the number of digits in an integer by repeatedly floor-dividing by 10 in a `while` loop.

```
Input:  98765
Output: Number of digits = 5
```

---

### P22 — Sum of Powers (1⁵ + 2⁵ + ... + N⁵)
**File:** `P22_sum_of_powers.py`  
Computes the sum of fifth powers: `1^5 + 2^5 + ... + N^5`.

```
Input:  3
Output: Sum of 1^5 + 2^5 + ... + 3^5 = 276
```

---

### P23 — Factorial Using Recursion
**File:** `P23_factorial_recursion.py`  
Computes the factorial of a number using a recursive function. Base case: `factorial(0) = factorial(1) = 1`.

```
Input:  5
Output: Factorial = 120
```

---

### P24 — Fibonacci Series
**File:** `P24_fibonacci_series.py`  
Prints the first N terms of the Fibonacci sequence using an iterative approach with a triple-variable swap.

```
Input:  8
Output: 0 1 1 2 3 5 8 13
```

---

### P25 — Factors and Prime Check
**File:** `P25_factors_prime_check.py`  
Defines a `factors(n)` function that returns all divisors of N, then checks primality by testing whether exactly 2 factors exist (1 and itself).

```
Input:  7       Output: Factors: [1, 7]   → Prime Number
Input:  12      Output: Factors: [1, 2, 3, 4, 6, 12]   → Not a Prime Number
```

---

## 📗 Assignment Programs (Q-Series)

### Q1 — Gross Salary Calculator
**File:** `Q1_gross_salary.py`  
Calculates gross salary based on tiered HRA and DA percentages depending on the basic salary range.

| Basic Salary | HRA  | DA  |
|-------------|------|-----|
| ≤ ₹10,000   | 20%  | 80% |
| ≤ ₹20,000   | 25%  | 90% |
| > ₹20,000   | 30%  | 95% |

```
Input:  15000
Output: HRA = 3750.0 | DA = 13500.0 | Gross Salary = 32250.0
```

---

### Q2 — Menu-Driven Area Calculator
**File:** `Q2_menu_area.py`  
A menu-driven program with 5 options: area of circle, triangle, square, rectangle, and simple interest calculation.

```
Menu:
1. Area of Circle       → π × r²
2. Area of Triangle     → ½ × base × height
3. Area of Square       → side²
4. Area of Rectangle    → length × breadth
5. Simple Interest      → (P × R × T) / 100
```

---

### Q3 — Employee Bonus Calculator
**File:** `Q3_employee_bonus.py`  
Calculates an employee's bonus based on years of service and adds it to their basic salary.

| Years of Service | Bonus |
|-----------------|-------|
| < 2 years       | 5%    |
| 2 – 5 years     | 10%   |
| 6 – 10 years    | 15%   |
| > 10 years      | 20%   |

```
Input:  Salary = 50000, Years = 7
Output: Bonus = 7500.0 | Gross Salary = 57500.0
```

---

### Q4 — List Methods Demo
**File:** `Q4_list_methods.py`  
Demonstrates common list operations on a programming languages list: `insert()`, `remove()`, `append()`, `len()`, `pop()`, and `del`.

```
Original:       ['Python', 'Java', 'C++', 'JavaScript']
After insert:   ['Python', 'C', 'Java', 'C++', 'JavaScript']
After remove:   ['Python', 'C', 'Java', 'JavaScript']
After append:   ['Python', 'C', 'Java', 'JavaScript', 'PHP']
After pop:      ['Python', 'C', 'Java', 'JavaScript']
After del:      ['Python', 'Java', 'JavaScript']
```

---

### Q5 — Tuple Methods Demo
**File:** `Q5_tuple_methods.py`  
Demonstrates tuple operations including concatenation to add items, membership check with `in`, `len()`, and index-based access.

```
languages = ('C++', 'Java', 'PHP')
After adding: ('React', 'C++', 'Java', 'PHP', 'Java')
Length: 5  |  First: React  |  Last: Java
```

---

### Q6 — Dictionary Methods Demo
**File:** `Q6_dictionary_methods.py`  
Demonstrates dictionary operations on a student record: direct key access, `get()`, value mutation, and `len()`.

```
student = {'name': 'Rahul', 'course': 'MCA', 'semester': 3, 'marks': 85}
After update: semester → 4, marks → 90
```

---

### Q7 — Menu-Driven Calculator
**File:** `Q7_calculator_menu.py`  
A menu-driven calculator with four operations defined as separate functions. Division includes a zero-division guard.

```
Menu:  1. Addition  2. Subtraction  3. Multiplication  4. Division

Input:  Choice = 1, Num1 = 15, Num2 = 10
Output: Addition = 25
```

---

### Q8 — Percentage and Grade Calculator
**File:** `Q8_percentage_grade.py`  
Accepts marks for 3 subjects, computes the average percentage, and assigns a letter grade.

| Percentage | Grade |
|-----------|-------|
| ≥ 90      | O     |
| ≥ 80      | A     |
| ≥ 70      | B     |
| ≥ 60      | C     |
| ≥ 50      | D     |
| ≥ 40      | E     |
| < 40      | F     |

```
Input:  85, 90, 78
Output: Total = 253 | Percentage = 84.33% | Grade = A
```

---

## 🧠 Concepts Covered

| Concept | Programs |
|---------|----------|
| `eval()`, expressions | P1 |
| Dictionaries | P2, P18, Q6 |
| if / elif / else | P3, P4, Q1, Q3, Q8 |
| while loops | P5, P7, P8, P13, P17, P21 |
| for loops | P6, P11, P15, P16, P19, P22, P24 |
| `datetime` module | P9, P10 |
| File I/O | P12 |
| String manipulation | P14, P18 |
| Functions | P21, P23, P25, Q7 |
| Recursion | P23 |
| Lists | Q4 |
| Tuples | Q5 |
| Menu-driven programs | Q2, Q7 |
