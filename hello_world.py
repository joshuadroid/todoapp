# %%
# write 4 expressions with different arithmetic operators that equal 100.
# Challenge, see if you can use all of the operators in one expression: +, -, *, /, %, **
print(99 + 1 - 1 * 1 / 1 % 1**1)

# %%
## write a string index that returns the letter "r" from "Hello World"
x = "Hello World"
print(x.find("r"))
print(x[8])

# %%
# Use string slicing to grab the word 'ink'  from inside 'tinker'
x = "tinker"
x[1:4]

# %%
# Create a list that contains at least one string, one integer and one float.
myList = ["mustaaaaaaard", 3, 1.00]
print(type(myList[0]))
print(type(myList[1]))
print(type(myList[2]))

# %%
# Write an expression that would turn the string 'Mississippi' into a set of unique letters.

# Declaring Variables
x = "Mississippi"
y = []
print(y)

# For Loop to add each index into a list
for z in range(len(x)):
    y.append(x[z])
print(y)

# Turn list into a set
a = set(y)
print(a)

# %%
x = set("Mississippi")
print(x)

# %%
# Create a list of students with properties for their first name, last name, and age (use a dictionary).
# Change the age of the 2nd student in the list. Print the name of the 3rd student in the list

students = [
    {"fname": "Josh", "lname": "Bozo", "age": 69},
    {"fname": "Dak", "lname": "Disabled", "age": 40},
    {"fname": "Kendrick", "lname": "Lamar", "age": "Mustard"},
]
print(students[1]["age"])
students[1]["age"] = 4
print(students[1]["age"])
print(students[2]["fname"] + " " + students[2]["lname"])
