import getpass
import string

name = input("What is your name? ")
print(f"Hello {name}")

age = input("What year were you born? ")
print(f"You are {2024 - int(age)} years old")

favourite_color = input("What is your favourite color?")
print(f"Your favorite color is {favourite_color}.")

palindrome = input("Please enter a word: ")
normalized_palindrome = palindrome.replace(" ", "").strip().lower()
is_palindrome = normalized_palindrome == normalized_palindrome[::-1]
print(f"It is {is_palindrome} that '{palindrome}' is a palindrome.")



password = getpass.getpass("Please enter your password: ")
is_valid = 8 <= len(password) <= 30
print(f"It is {is_valid} that the password fulfils the criteria.")



weight = input("Please enter your weight in kilograms: ")
height = input("Please enter your height in meters: ")
bmi = float(weight) / float(height) ** 2
bmi = round(bmi, 2)
print(f"Your BMI is {bmi}")

# LIST ASSIGNMENT
fruits = ["apple", "banana", "orange"]
print(fruits[0])

colors = ["red", "green", "blue"]
print(colors[-1])

numbers = list(range(1, 11))
print(numbers[3:8])

# alphabets = [chr(i) for i in range(ord('a'), ord('z') + 1)]
# print(alphabets[-3:])

alphabets = list(string.ascii_lowercase)
print(alphabets[-3:])

ages = [20, 30, 40]
ages[1] = 35
print(ages)

grades = ["A", "B", "C", "D"]
grades[1:4] = ["X", "X", "X"]
print(grades)


cities = ["New York", "London", "Paris"]
cities.insert(0, "Tokyo")
print(cities)

fruits = ["apple", "banana", "cherry"]
print(len(fruits))


prices = [10.5, 20.0, 15.75]
print(type(prices))


mixed = [10, "apple", True]
print(mixed)


tuple_data = ("a", "b", "c")
list_data = list(tuple_data)
print(list_data)


books = ["Python", "Java"]
books.append("JavaScript")
print(books)


names = ["Alice", "Bob", "Eve"]
names.insert(1, "Charlie")
print(names)


list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)


students = ["Alice", "Bob"]
students.extend(("Charlie", "David"))
print(students)


colors = ["red", "green", "blue"]
colors.remove("green")
print(colors)


numbers = [10, 20, 30, 40]
del numbers[2]
print(numbers)

