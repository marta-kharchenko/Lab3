# Part_1: If the number is even or odd
Num = int(input("Please enter the integer value: "))
if Num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
print(" ")

# Part_2: The test score
Score = float(input("Please enter the exam score: "))
if Score > 100 or Score < 0:
    print("Error")
elif Score >= 90:
    print("Your mark: A")
elif Score >= 80:
    print("Your mark: B")
elif Score >= 70:
    print("Your mark: C")
elif Score >= 60:
    print("Your mark: D")
elif Score >= 0:
    print("Your mark: F")
print(" ")

# Part_3: The Fibonacci number
Value = int(input("Please enter the number of Fibonacci element: "))


def Fibonacci(a):
    if a < 0:
        return "Error"
    elif a <= 1:
        return a
    else:
        return Fibonacci(a - 1) + Fibonacci(a - 2)


print("The", Value, "-th of Fibonacci element is:", Fibonacci(Value))
print(" ")

# Part_4: The factorial
N = int(input("Please enter the number: "))


def Factorial(b):
    if b <= 1:
        return 1
    else:
        return b * Factorial(b - 1)


print("The factorial of the number is:", Factorial(N))
print(" ")

# Part_5: The diamond shape
Row = int(input("Please enter the odd number of rows: "))

if Row % 2 == 0:
    Row += 1
    print("One extra row was added to the number of rows, you have written.")
for j in range(0, Row // 2 + 1):
    print(" " * (Row // 2 - j), "*" * (1 + 2 * j))
for j in range(Row // 2, 0, -1):
    print(" " * (Row // 2 + 1 - j), "*" * (2*j - 1))
