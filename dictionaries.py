a = ["name", "age", "city"]
b = [["Alice", 25, "New York"], ["Bob", 30, "Los Angeles"], ["Charlie", 22, "Chicago"]]

# Create a list of dictionaries by zipping keys with each sublist of values
ans = [dict(zip(a, values)) for values in b]

print(ans)

d = {15: 451, 45: 4, 3: 9, 4: 16, 5: 25}
print(d)

max(d,key=d.get)

"""# sort a dictionary by keys:"""

d = {'a': 12, 'c': 5, 'b' :18}


"""# sort dictionary by values"""

print(sorted(d.items(), key=lambda x: x[1]))

"""# sort dictionary by values in reverse order"""

d = [{'age': 10, 'name' : 'Talha'},{'age' : 15, 'name' : 'Harris'}]
print(sorted(d, key = lambda x: x['age'], reverse = True))

print(max(d, key = lambda x: x['age']))

"""# 2. Write a Python script to add a key to a dictionary.

Sample Dictionary : {0: 10, 1: 20}

Expected Result : {0: 10, 1: 20, 2: 30}
"""

s_d = {0: 10, 1: 20}
s_d[2] = 30
print(s_d)

"""# 3. Write a Python script to concatenate the following dictionaries to create a new one.

Sample Dictionary :

dic1 = {1: 10, 2: 20}

dic2 = {3: 30, 4: 40}

dic3 = {5: 50,6: 60}

"""

dic1 = {1: 10, 2: 20}

dic2 = {3: 30, 4: 40}

dic3 = {5: 50,6: 60}

dic={}
for i in (dic1, dic2, dic3):
    dic.update(i)
dic.update({7: 70})
dic[8] = 80
dic

# Write a Python program to iterate over dictionaries using for loops.
for key, value in dic.items():
    print(f"{key} = {value}")

#Write a Python program to get the maximum and minimum values of a dictionary.
print(max(dic.values()))
print(min(dic.values()))

#Write a Python program to remove duplicates from the dictionary.

student_data = {
    'id1': {
        'name': ['Sara'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
    'id2': {
        'name': ['David'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
    'id3': {
        'name': ['Sara'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
    'id4': {
        'name': ['Surya'],
        'subject_integration': ['english, math, science']
    }
}

updated_data = {}
for key, value in student_data.items():
    if value not in updated_data.values():
        updated_data[key] = value

"""Write a Python program to print all distinct values in a dictionary.
Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}"""

sample = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
final = set()
for i in sample:
    for j in i.values():
        final.add(j)
final

#merge dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3={}
for d in (dict1, dict2):
    dict3.update(d)

dict3


info = {"name": "Bob", "age": 28, "city": "Chicago"}

del info['name']


print(sorted(info.items(),key = lambda x: x[0]))

"""Count Word Frequency:
Given a list of words:

words = ["apple", "banana", "apple", "orange", "banana", "apple"]
Count how many times each word appears using a dictionary."""

words=["apple", "banana", "apple", "orange", "banana", "apple"]
d={}
for i in words:
    d[i]=words.count(i)
print(d)

"""Reverse a Dictionary:
Given:

mapping = {"a": 1, "b": 2, "c": 3}
Reverse it to {1: "a", 2: "b", 3: "c"}."""

mapping = {"a": 1, "b": 2, "c": 3}
reverse = {}

for key, value in mapping.items():
    reverse[value] = key
print(reverse)

"""Sort a Dictionary by Values:
Sort:

data = {"apple": 3, "banana": 1, "orange": 5}
in ascending order of values. """

data = {"apple": 3, "banana": 1, "orange": 5}
f_data = sorted(data.items(), key=lambda x: x[1],reverse = True)
f_data

"""Convert Two Lists into a Dictionary:

keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"] """
keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]
d = {}
for i, j in zip(keys, values):
    d[i] = j
print(d)

""" Access Nested Dictionary Values
Given the following nested dictionary:

Print the budget of the IT department.
Print the second employee in the HR department.
"""

company = {
    "department": {
        "HR": {"employees": ["Alice", "Bob"], "budget": 50000},
        "IT": {"employees": ["Charlie", "David"], "budget": 80000}
    }
}

print(f'budget of the IT department is {company['department']['IT']['budget']}')
print(f'second employee if HR department is {company['department']['HR']['employees'][1]}')


#Increase the HR department's budget by 10,000.
company['department']['HR']['budget'] = 80000
print(company)

"""3. Add a New Department
Add a new department "Finance" with the following details:
"Finance": {"employees": ["Frank"], "budget": 60000}
"""

company["department"]["Finance"]={"employees": ["Frank"], "budget": 60000}
print(company)

"""Count Total Employees Across Departments
Write a function to count the total number of employees across all departments."""
t_employees=0
for i,j in company['department'].items():
    c=len(j['employees'])
    t_employees+= c
print(f'total number of employees across all departments {t_employees}')

""" Find the Department with the Highest Budget
Determine which department has the highest budget."""

company={'department': {'HR': {'employees': ['Alice', 'Bob'], 'budget': 80000},
  'IT': {'employees': ['Charlie', 'David'], 'budget': 80000},
  'Finance': {'employees': ['Frank'], 'budget': 60000}}}

highest_budget_department = max(company['department'], key=lambda dept: company['department'][dept]['budget'])

print(highest_budget_department)

d = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30},{'name':'Talha','age':28}]
l = []

for data in d:
    print(data)

d = {'a': 10, 'b': 20, 'c': 15}
max(d.items(), key = lambda x: x[1])

d = {0: 'glean', 1: 'nealg', 2: 'car', 3: 'arc', 4 :'cat', 5: 'act', 6: 'inch', 7: 'chin', 8: '5675'}
d2 = {}
l = []
for index, value in d.items():
    l.append(value)
for i in range(len(l)):
    for j in range(i+1, len(l)):
        if len(l[i]) == len(l[j]):
            c = len(l[j])
            c2 = 0

            for k in l[i]:
                if k in l[j]:
                    c2+= 1
            if c2 == c:
                d2[l[i]] = l[j]
print(d2)

