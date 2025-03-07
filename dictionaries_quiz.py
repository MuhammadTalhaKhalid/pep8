d = {"name": "Alice", "age": 23, "grade": "A"}
for key, value in d.items():
    print(key)
    print(value)

# Add a new key-value pair to an existing dictionary where `` is added to the dictionary from question 2.
d["Gender"] = "Male"
print(d)

# Write a program to check if a given key exists in a dictionary.
print("Gender" in d.keys())

# Remove the key `` from the dictionary in question 2 and print the modified dictionary.
d.pop("Gender")
print(d)

# Merge the following two dictionaries into a single dictionary:
dict1 = {"a": 100, "b": 200}
dict2 = {"c": 300, "d": 400}
dict3 = {}
for d in (dict1, dict2):
    dict3.update(d)
print(dict3)

# Write a Python function that returns the maximum and minimum values from a dictionary of integer values.
print(max(dict3.values()))
print(min(dict3.values()))

# Given a dictionary where keys are student names and values are lists of their marks,
# write a program to calculate the average marks for each student.
st = {"Harris": [76, 83, 59, 90], "Ahmed": [67, 76, 64, 97]}
for name, marks in st.items():
    avg = sum(marks) / len(marks)
    print(f"Average marks for {name} is {avg}")

# Write a program to count the occurrences of each character in a given string using a dictionary.
st = "Hello world"
d = {}
for i in st:
    d[i] = st.count(i)
print(d)

# Given a dictionary where keys are product names and values are prices,
# write a program to find the most expensive product.
d = {"p1": 12000, "p2": 15000, "p3": 2300, "p4": 344656}
expensive = max(d.items())
print(f"Most expensive product is {expensive[0]} and its price is {expensive[1]}")

# Create a dictionary from two lists, one containing keys and the other containing values.
fruits = ["apple", "banana", "orange", "mango", "strawberry", "grapes"]
ind = [1, 2, 3, 4, 5, 6]
d = {}
for fruit, ind in zip(fruits, ind):
    d[ind] = fruit
print(d)

# Write a function that inverts a dictionary (i.e., swap keys and values).
d2 = {}
for index, value in d.items():
    d2[value] = index
print("Original dictionary")
print(d)
print("After swapping")
print(d2)

# Implement a function that takes a dictionary and returns a new dictionary with keys transformed to uppercase.
d = {"a": 1, "b": 2, "c": 3}
d2 = {}
for key, value in d.items():
    key = key.upper()
    d2[key] = value
print(d2)

# Write a Python program that finds the key with the highest corresponding value in a dictionary of numbers.
d = {"one": 23, "twp": 345457, "three": 345}
for index, value in d.items():
    if value == max(d.values()):
        print(index)
        print(value)
