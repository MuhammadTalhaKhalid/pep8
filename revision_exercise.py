
#group anagrams
words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
d={}

for word in words:
    word2="".join(sorted(word))
    if word2 not in d:
        d[word2]=[word]
    else:
        d[word2].append(word)
print(d)

def validate_sudoku(board):
    l=[]
    nums=[1,2,3,4,5,6,7,8,9]
    iscorrect=True
    for i in range(0,9):
        l2=[]

        for j in range(0,9):
            l2.append(board[j][i])
        l.append(l2)

        for k in nums:
            if k  not in board[i]:
                print(f'incorrect matrix {k} not present in row {i+1}')
                iscorrect=False



        for m in nums:
            if m  not in l[i]:
                print(f'incorrect matrix {m} not present in column {i+1}')
                iscorrect=False
    return iscorrect

print(validate_sudoku([
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]
))

print(validate_sudoku([
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 5, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 2, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]))

"""Write a function first_non_repeating_char that takes a string and returns
   the first non-repeating character. If all characters repeat, return None."""
s='hello'
def first_non_repeating_char(word):
    d={}

    for i in word:
        d[i] = word.count(i)
        if d[i] == 1:
            print(i,d[i])
            break

first_non_repeating_char('hellho')

words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
d={}

for word in words:
    word2="".join(sorted(word))
    if word2 not in d:
        d[word2]=[word]
    else:
        d[word2].append(word)
print(d)

""" Reverse a List Without Using Built-in Functions
Write a function to reverse a list without using the built-in .reverse() or slicing."""

def rev(lis):
    lis2 = []
    for i in range(len(lis)-1, -1, -1):
        lis2.append(lis[i])
    return lis2

print(rev([1,2,3,4,5,7,8,9,10]))

"""Find the Second Largest Number in a List
Write a function to find the second largest number in a given list."""

def second_largest(lis):
    maxx1 = float('-inf')
    maxx2 = float('-inf')

    for i in range(len(lis)):
        if lis[i] > maxx1:
            maxx1 = lis[i]
    for j in range(len(lis)):
        if lis[j] > maxx2 and lis[j] != maxx1:
            maxx2 = lis[j]
    return maxx1,maxx2

print(second_largest([1,2,3,4,5,23,45,56,-34,-323,45]))

"""Count Unique Elements in a List
Given a list of numbers, return the count of unique elements."""

def count_unique(lis):
    unique_count = 0

    for i in lis:
        if lis.count(i) == 1:
            unique_count +=1
    return unique_count

print(count_unique([1,1,2,3,5,4,8,5,5,2]))

"""Find the Intersection of Two Lists
Write a function that returns the common elements between two lists without duplicates."""

def common(lis1,lis2):
    comm = set()
    for i in lis1:
        if i in lis2:
            comm.add(i)
    return comm
print(common([2,4,5],[2,3,1,5]))

"""Find the Greatest Common Divisor (GCD)
Write a function to find the GCD of two numbers using Euclidean Algorithm."""

def GCD(num1, num2):
    if num1 > num2:
        smaller = num2
    else:
        smaller = num2

    for i in range(smaller, 0, -1):
        if num1 % i == 0 and num2 % i ==0:
            gcd = i
            break
    return gcd
print(GCD(18,30))

