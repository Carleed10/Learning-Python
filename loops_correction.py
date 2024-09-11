# 1
# Write a program that takes an integer input from the user and uses a loop to calculate 
# the sum of its digits. Print the sum. Example:
# Input: 1234
# Output: 10 (1+2+3+4)


# number = input("Enter a number: ")
# sum_of_digits = 0
# for num in number:
#     sum_of_digits += int(num)

# print(sum_of_digits)

# 2
# Collect a string from the user and use loops to count the number of vowels and consonants in the string. Print the counts. Example:
# Input: "hello world"
# Output: Vowels: 3, Consonants: 7

# import string

# lowercase_letters = string.ascii_lowercase
# vowels = "aeiou"

# consonants = [letter for letter in lowercase_letters if letter not in vowels]

# text = input("Enter some text: ").lower()
# no_of_vowels = 0
# no_of_consonants = 0
# for char in text:
#     if char in vowels:
#         no_of_vowels += 1
#     elif char in consonants:
#         no_of_consonants += 1

# print(f"Vowels: {no_of_vowels}, COnsonants: {no_of_consonants}")

# 3
# Write a program that takes an integer input from the user and prints the 
# multiplication table for that number up to 12. Example:
# Input: 5
# Output:
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# ...
# 5 x 12 = 60

# multiplication_table = int(input("Enter the multiplication table number: "))
# for i in range(1, 13):
#     print(f"{multiplication_table} X {i} = {multiplication_table * i}")


# 6
# Write a program that takes an integer input n from the user and prints the first 
# n numbers in the Fibonacci sequence. Example:
# Input: 10
# Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

# n = int(input("Enter n where n is the first n numbers in the fibonacci sequence: "))
# fibonacci_nums = [0, 1]

# for i in range(1, n-1):
#     second_to_last_num = fibonacci_nums[i-1]
#     last_num = fibonacci_nums[i]
#     fibonacci_nums.append(second_to_last_num + last_num)

# print(fibonacci_nums)

# 7
# Collect a list of numbers from the user (entered as comma-separated values) and use a 
# loop to find and print the largest number in the list. Don’t use the built-in max 
# function or anything similar.
# Input: "10, 20, 5, 15"
# Output: 20

# list_of_numbers = input("Enter a list of numbers seperated by comma :").split(",")
# greatest_num = int(list_of_numbers[0])

# for number in list_of_numbers:
#     num = int(number)
#     if num >= greatest_num:
#         greatest_num = num
# print(greatest_num)

# list_of_numbers = input("Enter a list of numbers seperated by comma :").split(",")
# int_list_of_numbers = [int(num) for num in list_of_numbers]
# print(max(int_list_of_numbers))

# 9
# Collect a string from the user and use a loop to count the frequency of each character 
# in the string. Print each character along with its frequency. Example:
# Input: "hello"
# Output:
# h: 1
# e: 1
# l: 2
# o: 1

# text = input("Enter some text: ").lower().strip()
# char_frequency = {}
# for char in text:
#     if char in char_frequency:
#         char_frequency[char] += 1
#     else:
#         char_frequency[char] = 1

# print(char_frequency)

# 10
# Write a program that takes an integer n from the user and calculates the sum of 
# squares of all numbers from 1 to n. Print the sum. Example:
# Input: 3
# Output: 14 (1^2 + 2^2 + 3^2)

# 1^2 + 2^2 + 3^2 = 14

# n = int(input("Enter an integer: "))
# sum_of_squares = 0
# output = ""
# for num in range(1, n+1):
#     output += f"{num}^2"
#     if num != n:
#         output += " + "
#     sum_of_squares += num ** 2

# print(f"{output} = {sum_of_squares}")

# 11
# Collect a phrase from the user and use a loop to generate an acronym by taking the first
# letter of each word. Print the acronym. Example:
# Input: "Portable Network Graphics"
# Output: "PNG"

# phrase = input("Enter a phrase: ")
# words = phrase.split(" ")
# acronym = ""
# for word in words:
#     acronym += word[0]

# print(acronym)

# 12
# Collect a string from the user and use a loop to count the number of words in the string. 
# Print the count. Example:
# Input: "Hello world from Python"
# Output: 4

# phrase = input("Enter a phrase: ")
# words = phrase.split(" ")
# word_count = 0
# for word in words:
#     word_count += 1

# print(word_count)


# 13
# Collect a string from the user and only print out the words that start with the letter 
# ‘S’. Example:
# Input: “Print only the words that start with s in this sentence”
# Output: 
# start
# s
# Sentence

# text = input("Enter some text: ").strip()
# words = text.split(" ")

# for word in words:
#     if word.startswith(("s", "S")):
#         print(word)


# 14
# Print all the even numbers from 1 to 20 using the range function and a loop.
# for num in range(0, 21, 2):
#     print(num)


# 15
# Use a list comprehension to create a list of numbers between 1 and 50 that are divisible
# by 3.

# divisible_by_3 = []
# for num in range(1, 51):
#     if num % 3 == 0:
#         divisible_by_3.append(num)

# print(divisible_by_3)

# divisible_by_3 = [num for num in range(1, 51) if num % 3 == 0]
# print(divisible_by_3)

# 16
# Go through the string below and if the length of a word is even, print that word.
# st = ‘Print every word in this sentence that has an even number of letters’
# Output: 
# word
# in
# this
# sentence
# that
# an
# even
# number
# of

# st = "Print every word in this sentence that has an even number of letters"
# words = st.split(" ")
# for word in words:
#     if len(word) % 2 == 0:
#         print(word)


# 17
# Write a program that prints the integers from 1 to 100. But for multiples of three, print 
# “Fizz” instead of the number, and for multiples of five, print “Buzz”. For numbers which 
# are multiples of both three and five, print “FizzBuzz”.

# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz

# for num in range(1, 101):
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)


# Pig Latin Translator
# young => oungyay 
# text = "programming"

# vowels = "aeiouy"
# pig_latin = ""

# for i, char in enumerate(text):
#     if char in vowels:
#         if i == 0:
#             if char == "y":
#                 continue
#             pig_latin = text + "way"
#             break
#         pig_latin = text[i:] + text[:i] + "ay"
#         break    

# if not pig_latin:
#     pig_latin = text + "ay"

# print(pig_latin)  


# Password Validator
# password = "Passw0rd"
# # Is at least 8 characters long.
# has_at_least_8_chars = len(password) >= 8

# # Contains both uppercase and lowercase characters.
# uppercase = any(char.isupper() for char in password)
# lowercase = any(char.islower() for char in password)
# both_upper_and_lower = uppercase and lowercase

# # Contains at least one digit.
# at_least_1_digit = any(char.isdigit() for char in password)

# # Contains at least one special character (e.g., !@#$%^&*()).
# special_chars = "!@#$%^&*()"
# has_at_least_1_special_char = any(char in special_chars for char in password)

# is_strong_password = has_at_least_8_chars and both_upper_and_lower and at_least_1_digit and has_at_least_1_special_char
# print(is_strong_password)


def addition(num1, num2):
    return f"{num1} + {num2} = {num1 + num2}"

def subtraction(num1, num2):
    return f"{num1} - {num2} = {num1 - num2}"

menu = """
Select operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
"""

print("Welcome to the Simple Calculator")
while True:
    print(menu)
    choice = int(input("Choose an option from the menu: "))
    if choice == 5:
        print("Goodbye!")
        break

    if choice not in [1, 2, 3, 4]:
        print("Enter a valid choice from the menu")
        continue

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == 1:
        print(addition(num1, num2))
    elif choice == 2:
        print(subtraction(num1, num2))
