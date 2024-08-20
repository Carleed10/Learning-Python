import string

# a = 5
# a = "5"
# a = 5.0

# ingredients = ["rice", "tomato paste", "salt", "maggi", "vegetables", "onions", "curry", "thyme", "groundnut oil"]
# print("before change", ingredients)
# ingredients[1] = "tomato"
# ingredients[1:3] = ["tomato", "paste"]
# ingredients[6:8] = ["spices"]
# print("after change", ingredients)

# print(ingredients[4])
# print(ingredients[-3:])

# print("before del", ingredients)
# del ingredients[3]
# print("after del", ingredients)


# my_name = "Winnie"
# my_name = my_name.upper()
# print(my_name)

# print("before remove", ingredients)
# ingredients.remove("maggis")
# print("after remove", ingredients)

# print("vegetables" in ingredients)

# my_list = [False, 1, 100, True, 0.9, 7]


# Assignment correction
# Create a list called fruits with items "apple", "banana", and "orange". Print the first item.
# fruits = ["apple", "banana", "orange"]
# print(fruits[0])

# Create a list called colors with items "red", "green", "blue". Print the last item using negative indexing.
# colors = ["red", "green", "blue"]
# print(colors[-1])

# Create a list called numbers with items from 1 to 10. Print items from index 3 to index 7.
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(numbers[3:8])

# Create a list called alphabets with items "a", "b", "c", ..., "z".
# Print a slice from index -3 to the end.
# alphabets = list(string.ascii_lowercase)
# print(alphabets)


# Create a list called ages with items 20, 30, 40. Change the value of the second item to 35.
# ages = [20, 30, 40]
# ages[1] = 35
# print(ages)


# Create a list called grades with items "A", "B", "C", "D". Change the values of items from index 1 to index 3 to "X".
# grades = ["A", "B", "C", "D"]
# grades[1:4] = ["X"]
# print(grades)


# Create a list called cities with items "New York", "London", "Paris". Insert "Tokyo" at the beginning of the list.
# cities = ["New York", "London", "Paris"]
# cities.insert(0, "Tokyo")
# print(cities)

# Create a list called fruits with items "apple", "banana", "cherry". Print the number of items in the list.
# fruits = ["apple", "banana", "cherry"]
# print(len(fruits))


# Create a list called prices with items 10.5, 20.0, 15.75. Print the data type of the list.
# prices = 10.5, 20.0, 15.75
# print(type(prices))

# Create a list called mixed with items 10, "apple", True. Print the list.
# mixed = [10, "apple", True]
# print(mixed)

# Create a tuple called tuple_data with items "a", "b", "c". Convert the tuple into a list.
tuple_data = ("a", "b", "c")
print(list(tuple_data))
 
# Create a list called books with items "Python", "Java". Append "JavaScript" to the end of the list.
# books = ["Python", "Java"]
# books.append("JavaScript")
# print(books)

# Create a list called names with items "Alice", "Bob", "Eve". Insert "Charlie" at index 1.
# names = ["Alice", "Bob", "Eve"]
# names.insert(1, "Charlie")

# Create two lists called list1 and list2 with items 1, 2, 3 and 4, 5, 6 respectively. Extend list1 with list2.
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list1.extend(list2)
# print(list1)

# Create a list called students with items "Alice", "Bob". Add items from 
# a tuple ("Charlie", "David") to students.
# students = ["Alice", "Bob"]
# tuple_students = ("Charlie", "David")
# students.extend(tuple_students)

# Create a list called colors with items "red", "green", "blue". Remove "green" from the list.
# colors = ["red", "green", "blue"]
# colors.remove("green")
# print(colors)

# Create a list called numbers with items 10, 20, 30, 40. Use the del keyword to remove the item at index 2.
# numbers = [10, 20, 30, 40]
# del numbers[2]
# print(numbers)

# Create a list called fruits with items "apple", "banana", "cherry". Clear the list.
# fruits = ["apple", "banana", "cherry"]
# fruits.clear()
# print(fruits)

#  19.	Create a list called names with items "Zoe", "Alice", "Bob". Sort the list alphabetically.
# names = ["Zoe", "Alice", "Bob"]
# names.sort()
# print(names)

#  20. 	Create a list called ages with items 25, 35, 20. Sort the list in descending order.
# ages = [25, 35, 20]
# ages.sort(reverse=True)
# print(ages)


#  21. 	Sorting lists is CASE-SENSITIVE by default. Create a list called words with items 
# "Apple", "banana", "Orange". Sort the list in CASE-INSENSITIVE alphabetical order.
# words = ["Apple", "banana", "Orange"]
# words.sort(key=str.lower)
# print(words)


# 22. 	Create a list called numbers with items 1, 2, 3, 4. Print the list in reverse order.
# numbers = [1, 2, 3, 4]
# # print(numbers[::-1])
# numbers.reverse()
# print(numbers)

# 23.	Create a list called letters with items "a", "b", "c", "d". Print the list in reverse order using
# slicing.
# letters = [ "a", "b", "c", "d"]
# print(letters[::-1])

#  24.	Create a list called original with items "one", "two", "three". Create a copy of the list.
# original = ["one", "two", "three"]
# copy_of_original = original.copy()
# copy_of_original.append("four")
# print(original)
# print(copy_of_original)

#  25. Create two lists called list1 with items "a", "b" and list2 with items "c", "d". Join list1 and 
#  list2 together.
list1 = ["a", "b"]
list2 = ["c", "d"]
# list1.extend(list2)
# print(list1)
print(list1 + list2)

#  26.	Access and print the second subject of the first person in the list.
# data = [
#     ["Alice", 25, ["Math", "Physics"]],
#     ["Bob", 30, ["Chemistry", "Biology"]],
#     ["Charlie", 35, ["History", "Geography"]]
# ]
# print(data[0][2][1])


#  27.	Access and print the first value in the list of numbers associated with "San Francisco".
# records = [
#     ["New York", [10, 20, 30]],
#     ["San Francisco", [40, 50, 60]],
#     ["Austin", [70, 80, 90]]
# ]

# print(records[1][1][0])


# Wedding Guest Manager
# Stage 1
confirmed_guests = ["Alice", "Charlie", "Eve", "Bob", "Frank", "Grace", "David", "Hannah", "Liam", "Mia"]
waitlist = []
print("\n\nStage 1")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)

# Stage 2
waitlist = ["Ken", "Jack", "Ivy"]
print("\n\nStage 2")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)

# Stage 3