# # i = 1
# # while i <= 10:
# #     print(i)
# #     i += 1


n = int(input("Enter an integer: "))

total_sum = 0
counter = 1

while counter <= n:
    total_sum += counter
    counter += 1
print(f"The sum of all natural numbers up to {n} is: {total_sum}")




# correct_password = "secret"

# while True:

#     password = input("Enter the password: ").strip()
#     if password == correct_password:
#         print("Access granted!")
#         break
#     else:
#         print("Incorrect password. Try again.")



# n = int(input("Enter a positive integer to start the countdown: "))

# while n >= 0:
#     print(n)
#     n -= 1



# n = int(input("Enter a positive integer: "))

# i = 1

# while i <= n:
#     if i % 2 == 0:
#         print(i)
#     i += 1



# base = int(input("Enter the base: "))
# exponent = int(input("Enter the exponent: "))


# result = 1
# counter = 0


# while counter < exponent:
#     result *= base
#     counter += 1

# print(f"{base} raised to the power of {exponent} is {result}")



# user_string = input("Enter a string: ").lower()
# char_count = {}
# i = 0


# while i < len(user_string):
#     char = user_string[i]
#     if char in char_count:
#         char_count[char] += 1
#     else:
#         char_count[char] = 1
#     i += 1

# print(f"The occurrences of each character are: {char_count}")





# balance = float(input("Enter your balance: "))


# while True:
#     withdrawal_amount = float(input("Enter withdrawal amount: "))
#     if withdrawal_amount > balance:
#         print("Insufficient funds. Try a smaller amount.")
#     else:
#         balance -= withdrawal_amount
#         print(f"Remaining balance: {balance}")
    
#     another_withdrawal = input("Do you want to make another withdrawal? (yes/no): ").strip().lower()
    
#     if another_withdrawal != 'yes':
#         break

# print(f"Final balance: {balance}")



# total_cost = 0.0
# while True:
#     item_price = float(input("Enter item price: "))
#     total_cost += item_price

#     another_item = input("Enter another item? (yes/no): ").strip().lower()
    
#     if another_item != 'yes':
#         break

# print(f"Total cost: {total_cost:.2f}")





# while True:
#     password = input("Enter password: ")

#     if len(password) < 8 or len(password) > 25:
#         print("Password must be at least 8 characters long and have a maximum of 25 characters.")
#     else:
#         print("Password accepted.")
#         break




# while True:

#     age = int(input("Enter your age: "))

#     if age >= 0:
#         print("Age accepted.")
#         break
#     else:
#         print("Invalid age. Please enter a valid age.")



