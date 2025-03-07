"""Patterns generator using nested for loops"""
for i in range(1, 6):
    # Printing spaces
    for k in range(i, 6):
        print(" ", end='')

    # Print *
    for j in range(i):
        print("* ", end='')

    print()

#2
for l in range(1, 6):
    # Print leading spaces
    for m in range(l):
        print(" ", end='')

    # Print asterisks followed by a space
    for n in range(l, 6):
        print("* ", end='')

    # Move to the next line after each row
    print()

# diamond pattern
rows = 6

# Upper half
for i in range(1, rows + 1):
    # Print spaces
    for j in range(rows - i):
        print(" ", end='')

    # Print *
    for k in range(i):
        print("* ", end='')

    print()

# Lower half
for l in range(rows - 1, 0, -1):
    # Print spaces
    for m in range(rows - l):
        print(" ", end='')

    # Print *
    for n in range(l):
        print("* ", end='')

    print()

# Double pyramid on the right side
rows = 6


for i in range(1, rows + 1):
    # Print leading spaces
    for j in range(rows - i):
        print(" ", end='')

    for k in range(i):
        print("* ", end='')

    for j in range((rows - i) * 2):
        print(" ", end='')

    for k in range(i):
        print("* ", end='')

    print()

for i in range(rows - 1, 0, -1):

    for j in range(rows - i):
        print(" ", end='')

    for k in range(i):
        print("* ", end='')

    for j in range((rows - i) * 2):
        print(" ", end='')

    for k in range(i):
        print("* ", end='')

    print()

# Pattern with slashes and exclamation marks
for i in range(1, 10):
    # print slash
    for one in range(0, i):
        print('/', end='')

    # Print !
    for j in range(10, i, -1):
        print('!.', end='')

    # print slash
    for k in range(0, i):
        print('/', end='')

    # Move to the next line after each row
    print()

# pattern
for i in range(6):
    # Print *
    for j in range(i, 6):
        print('* ', end='')


    print()

# Patterm
for i in range(6):
    # Print *
    for j in range(i + 1):
        print('* ', end='')

    print()

# Right-aligned increasing triangle pattern
for i in range(6):
    # Print leading spaces
    for k in range(i, 6):
        print(" ", end='')

    # Print asterisks
    for j in range(i + 1):
        print('*', end='')

    # Move to the next line after each row
    print()

# pattern
for i in range(6):
    # Print spaces
    for j in range(i + 1):
        print(' ', end='')

    # Print *
    for k in range(i, 6):
        print("*", end='')

    print()

# Find the second largest number in a list
l = [1, 2, 5, 56, 23, 15, -50, 23]
maxx = l[0]

# Find the maximum number in the list
for i in range(len(l)):
    if l[i] > maxx:
        maxx = l[i]

max_2 = l[0]

# Find the second maximum number in the list
for j in range(len(l)):
    if l[j] != maxx and l[j] > max_2:
        max_2 = l[j]

print(max_2)

# Function to find the second largest number in a list
def second_largest(lst):
    maxx = lst[0]
    # Find the maximum number
    for num in lst:
        if num > maxx:
            maxx = num

    max_2 = lst[0]
    # Find the second maximum number
    for num in lst:
        if num != maxx and num > max_2:
            max_2 = num

    print(f'Maximum number in the list is {maxx}')
    print(f'Second maximum number in the list is {max_2}')

    return max_2

l = [1, 2, 5, 56, 23, 15, -50, 23]
print(second_largest(l))
