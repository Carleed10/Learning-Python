# def raise_to_power(base, exponent):
#     return base **exponent

# print(raise_to_power(2, 2))


# def all_caps(word="text"):
#     return word.upper()

# print(all_caps())

# def is_even(n):
#     return n % 2 == 0

# print(is_even(9))


# def lesser_of_two_evens(a, b):
#     if(a % 2 == 0 and b % 2 == 0):    
#         return min(a, b)
#     return max(a, b)

# print(lesser_of_two_evens(89, 4))


# def old_macdonald(word="text"):
#     return word.capitalize()

# print(old_macdonald("macdonald"))

# def upper_lower(word="text"):
#     return len(word.isupper()), len(word.islower())

# print(upper_lower("MACdonald"))


# def product(*numbers):
#     product_of_numbers = 1
#     for mul in numbers:
#         product_of_numbers *= mul

#     return product_of_numbers

# print(product(2, 5, 7, 9, 9,  3))



# def power(base, exponent):
#     result = 1

#     while exponent > 0:
#         result *= base
#         exponent -= 1

#     return result

# print(power(2, 2000))



# def is_multiple_of_three(number):
#     """
#     This function checks if the number is a multiple of 3.
#     It expects an integer and returs a boolean (either true or false)
    
#     """

#     return number % 3 == 0

# print(is_multiple_of_three(18))

















# assinment


# def add_two_numbers(a, b):
#     return a + b

# print(add_two_numbers(12, 20))


# def is_even(n):
#     return n % 2 == 0

# print(is_even(9))

# def lesser_of_two_evens(a, b):
#     if (a % 2 == 0 and b % 2 == 0):
#         return min(a, b)
#     return max(a, b)

# print(lesser_of_two_evens(11, 8))

# Write a function is_alliteration(two_word_string) that takes a two-word string  and returns True if both words begin with the same letter.
# is_alliteration(‘Levelheaded llama’) —> True
# is_alliteration(‘Crazy Kangaroo’) –> False

# def is_alliteration(word=""):
#     words = word.split(" ")

#     if len(words) == 2 and words[0][0].lower() == words[1][0].lower():
#         return True
    
#     return False

# print(is_alliteration('Levelheaded llama'))  
# print(is_alliteration('Crazy Kangaroo'))  

  
  


# def old_macdonald(name):
#     return name[:3].capitalize() + name[3:].capitalize()


# def old_macdonald(name):
#     return name[0].upper() + name[1:3] + name[3].upper() + name[4:]

# print(old_macdonald("maccarthy"))









# Write a function spy_game(list_of_ints) that takes in a list of integers and returns True if it contains 007 in order.
# spy_game([1, 2, 4, 0, 0, 7, 5]) —> True
# spy_game([1, 0, 2, 4, 0, 5, 7]) —> True
# spy_game([1, 7, 2, 0, 4, 5, 0]) —> False

# def spy_game(lists_of_int):
#     number = int(["0", "0", "7"])

#     for number in lists_of_int:
#         return True
#     return False

# print(spy_game([1, 2, 3, 4, 0, 0, 7]))




# Write a function vol(radius) that computes the volume of a sphere given its radius.
# Write a function range_check(num, low, high) that checks whether a number is in a given range (inclusive of high and low).
# Write a function upper_lower(text) that accepts a string and calculates the number of uppercase letters and lowercase letters.
# Write a function unique_list(list_items) that takes in a list and returns a new list with unique elements of the first list. Do not use the set() constructor.

