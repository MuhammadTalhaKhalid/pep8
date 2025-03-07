lis = [3,4,5,6]
print(6 in lis)

def prime(num):
    isdiv = False
    for i in range(2, num):
        if num%i == 0:
            isdiv = True
    if isdiv == True:
        print(f'{num} is not  prime')
    else:
        print(f'{num} is a  prime number')
prime(17)

def sum_of_digits(n):
    n = abs(n)  # Ensure the number is positive
    total = 0

    while n > 0:
        total += n % 10  # Get the last digit
        n //= 10  # Remove the last digit

        return total


num = 12345
print(sum_of_digits(num))

n = abs(12345)
total = 0
num_digits = len(str(n))
for _ in range(num_digits):
    total += n % 10
    print(total)

    n //= 10
    print(n)
print(total)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a = a + b
b = a - b
a = a - b
print("After swapping: a =", a, "b =", b)

num = int(input("Enter a number: "))
rev_num = 0

while num > 0:
    rev_num = (rev_num * 10) + (num % 10)
    print(rev_num)
    num //= 10

print("Reversed number:", rev_num)

"""# Sum of Digits of a Number
👉 Write a program to find the sum of digits of a given number using only arithmetic operators.
"""

a = 205
length = len(str(a))
s = 0

for _ in range(length):
    last_digit = a % 10
    s += last_digit
    a //= 10

print(s)

num = 205
s = 0

while num > 0:
    last_digit = num % 10
    s += last_digit
    num //= 10

print(s)

"""# Count the Number of Digits in a Number
👉 Take an integer as input and count how many digits it has using arithmetic operations (//).
"""

num = 234
count = 0

while num > 0:
    num //= 10
    count += 1

print(count)

"""# reverse digit of a number"""

a = 15
length = len(str(a))
rev = ""

for _ in range(length):
    b = a % 10
    rev += str(b)
    a //= 10
print(rev)

num = int(input("Enter a number: "))
rev_num = 0

while num > 0:
    rev_num = (rev_num * 10) + (num % 10)
    num //= 10

print("Reversed number:", rev_num)

"""# Find the Power of a Number Without Using pow()
👉 Compute a^b using only multiplication and loops (no ** or pow() function).
"""

a = 10
b = 3
power = 1
for i in range(b):
    power*= a
print(power)

base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))
result = 1

for _ in range(exp):
    result*= base

print("Result:", result)

"""# You are counting items in the warehouse. There are 24 boxes, each containing 15 items. You need to determine how many items are left if 123 items are shipped out.
Question: Write a Python expression to calculate the number of items left.

"""

boxes = 24
items = 15

# Find total items by multiplying the number of boxes by items per box
total_items = boxes * items

# Shipped out items
shipped_out_items = 123

# Total items left after shipment
total_items_left = total_items - shipped_out_items

# Total boxes left after shipment
total_boxes_left = total_items_left // items

print(total_items_left)
print(total_boxes_left)

"""# Bonus Calculation (Conditions & Operators)
DataTech gives a bonus to its employees based on their performance. If an employee achieves 90% or above, they get a 10% bonus. If the performance is between 70% and 89%, they get a 5% bonus. Otherwise, no bonus is given.
Question: Write a Python program that calculates the bonus for an employee based on their performance percentage.

"""

salary = 75_000
performance = int(input("Enter performance %: "))

if performance >= 90:
    bonus = salary * 0.10
elif 70 <= performance <= 79:
    bonus = salary * 0.05
else:
    bonus = 0

total_salary = salary + bonus

if bonus > 0:
    print(f"Your bonus is {bonus} and your total salary is {total_salary}")
else:
    print(f"No bonus given. Your salary is {salary:.2f}")

"""
# Question: Write a Python program that takes a list of numbers (feedback scores) and returns the average.
"""

scores = [5, 3, 4, 2, 5]
total_feedbacks = 0
sum_scores = 0
for score in scores:
    total_feedbacks+= 1
    sum_scores+= score
average_score = sum_scores / total_feedbacks
print(f'average feedback score is {average_score}')

"""# Your manager wants to track which employees were present over the last 7 days. Each employee has a list of booleans representing their attendance for each day (e.g., attendance = [True, False, True, True, False, True, True]). The manager wants to know how many days the employee was present.
Question: Write a Python program that takes a list of booleans and returns the count of True values (the number of days the employee was present).
"""

attendence = [True, False, True, True, False, True, True]
true_count = 0
for day in attendence:
    if day == True:
        true_count+= 1
print(true_count)

"""# Error Handling in Customer Data (Lists & Conditions)
The customer data team is encountering errors because some customers have no email address or have provided an empty email.
Question: You are given a list of customer emails: emails = ["customer1@example.com", "", "customer3@example.com", None, "customer5@example.com"].
Write a Python program that removes empty or None values from the list and returns the valid emails.

"""

emails = ["customer1@example.com", "", "customer3@example.com", None, "customer5@example.com"]
updated_email = []
for email in emails:
    if email != "" and email != None:
        updated_email.append(email)

updated_email

"""# . Stock Price Analysis (Loops, Lists & Conditions)
DataTech needs to analyze stock prices. You are given a list of daily prices for a stock. You need to determine how many days the price went up from the previous day.
Question: Write a Python program that takes a list of stock prices and returns the number of days the stock price increased compared to the previous day.
Example:
prices = [100, 102, 101, 105, 107, 103]
For the list above, the program should return 3 (days 2, 4, and 5 had increases).

"""

prices = [100, 102, 101, 105, 107, 103]
increase_count = 0
for i in range(1, len(prices)):
    if prices[i] > prices[i-1]:
        increase_count+= 1
print(increase_count)

"""# Check if a Number is a Palindrome
👉 Take an integer input and check if it reads the same backward (e.g., 121 is a palindrome, but 123 is not).
"""

num=123
rev=0
while num>0:
    rev=(rev *10)+(num%10)
    num=num//10
print(rev)

numbers=[2,43,23,4,23,634]
d = {}
for index, number in enumerate(numbers):
    d[index] = number
d

sorted_dict_desc = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))

print(sorted_dict_desc)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

l = []

for i in range(4):
    transpose = []

    for j in matrix:
        transpose.append(j[i])
        l.append(transpose)
print(l)