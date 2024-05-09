
# Arithmetic Operations
x = 5
y = 3

# Addition
result = x + y
print("Addition:", result)

# Subtraction
result = x - y
print("Subtraction:", result)

# Multiplication
result = x * y
print("Multiplication:", result)

# Division
result = x / y
print("Division:", result)

# String Manipulation
name = "jay"
greeting = "Hello, " + name + "!"

print(greeting)

# Conditional Statements
age = 25

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Conditional Statement with elif
score = 80

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

#list
my_list=[1,2,3,4,5]

my_list.append(8)
my_list.remove(3)
my_list[2]=15

print("updated list: ",my_list)

#dictionary
my_dict = {'name': 'jay', 'Age': 21, 'city' : 'Hyderabad'}

my_dict['gender'] = 'male'
del my_dict['city']
my_dict['age'] = 23

print("Updated dictionary: ", my_dict)

#sets
my_set={1,2,3,4,5}

my_set.add(6)
my_set.remove(3)
my_set.discard(7)

print("Updated set: ",my_set)

# Create a tuple
my_tuple = (1, 2, 3, 4, 5)
print("Original Tuple:", my_tuple)
# Indexing and Slicing
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])
print("Slice from index 1 to 3:", my_tuple[1:3])

# Tuple Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concat_tuple = tuple1 + tuple2
print("Concatenated Tuple:", concat_tuple)

# Tuple Multiplication
multiplied_tuple = my_tuple * 3
print("Multiplied Tuple:", multiplied_tuple)

# Tuple Length
print("Length of the tuple:", len(my_tuple))
