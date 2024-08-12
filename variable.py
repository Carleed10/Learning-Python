# name = "My name is Khalid"
# print(name)

# greetings = 'Good morning'
# print(greetings)

# long_string = "This is very long string.\nThis is on the next line"
# print(long_string)

# multi_line_string = """Good morning
# Good afternoon
# Good evening
# Good night """

# print(multi_line_string)

# my_name = "Khalid"
# print(my_name[1 : 5])

my_string = "Python is amazing!"
print(my_string[3:9])
# print(my_string[0:10:3])
# print(my_name[len(my_name) - 1])
# print(my_name [-1])

# positve_name = len(my_name)
# print(my_name[positve_name - 1])



# String interpolation and concatenation
 
name = 'Alice'
age =  12
height = 5.6
is_student = True

introduction  = 'My name is ' + name + ". I am " + str(age) + " years old. I am " + str(height) + " ft tall and it is " + str(is_student) + " that i am a student"
print(introduction)

introduction = f"My name is {name}. I am {age} years old. I am {height} ft tall and it is {is_student} that i am a student" 
print(introduction)

introduction = "My name is {}. I am {} years old. I am {} ft tall and it is {} that i am a student".format(name, age, height, is_student)
print(introduction)



# Scenario: You need to format a given string to make sure it starts with a capital letter and ends with a period.

# Task: Write a program in a file `text_formatter.py` that takes a string called `text` and ensures it starts with a capital letter and ends with a period. It should also trim any whitespace at the beginning and the end if any. 

# Assume that the string will never be an empty string before or after it is trimmed. 
# Also assume it does not already have a period at the end.

# This tests your knowledge of string manipulation


word = " lorem ipsum dolor sit amet "

introduction = "{}.".format(word.strip().capitalize())
print(introduction)


number_of_cars = 22
weight = 66.5
print(type(number_of_cars))
print(type(weight))

a = 6e-6
b = 5
print(a / b)


a = 25
b = 5

print(int(a + b))


is_young =  True
print(type(is_young))

print(10 >= 10)

is_true =  True
is_false = False

print(is_true and is_false)


color_1, color_2, color_3 = "red", "green", "blue"
print("Color 1 is :", color_1)
print("Color 2 is :", color_2)
print("Color 3 is :", color_3)

