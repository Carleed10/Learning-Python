# a = float(input("Enter the first number: "))
# b = float(input("Enter the second number: "))

# if a > 0 and b > 0 :
#     print("Both numbers are postive")
# elif a > 0 or b > 0 :
#     print("Only one is positve")  
# else:
#     print("Neither is positive")


# numbers_input = input("Enter three numbers separated by commas (e.g., 1,2,3): ")

# x, y, z = map(int, numbers_input.split(','))

# if x < y < z:
#     print("Increasing order")
# elif x > y > z:
#     print("Decreasing order")
# else:
#     print("Neither")


# palindrome = input("Enter a word to check if it's a palindrome: ").strip().lower()

# if palindrome == palindrome[::-1]:
#     print(f"{palindrome} is a palindrome")
# else:
#     print("This word is not a palindrome")    
    

x = float(input("Eneter a number x: "))
y = float(input("Eneter a number y: "))
z = float(input("Eneter a number z: "))

if (x == y and x != z) or (x == z and x != y) or (y == z and y != x):
    print("Two are equal")
elif x == y == z:
    print("All numbers are equal")    
else:
    print("Numbers are not equal")




angle1 = float(input("Enter the first angle: "))
angle2 = float(input("Enter the second angle: "))
angle3 = float(input("Enter the third angle: "))


if angle1 > 0 and angle2 > 0 and angle3 > 0 and (angle1 + angle2 + angle3 == 180):
    print("Valid triangle")
else:
    print("Invalid triangle")




alphabet = input("Enter a single alphabet character: ")
vowel = ['a', 'e', 'i', 'o', 'u']

if alphabet.lower() in vowel:
    print("Vowel")
else:
    print("Consonant")


colors = input("Input first color, second color, third color: ").lower().split(",")
color1, color2, color3 = colors
color1, color2, color3 = color1.strip(), color2.strip(), color3.strip()
primary_colors = ["red", "blue", "yellow"]


if color1 in primary_colors and color2 in primary_colors and color3 in primary_colors:
    print("All are primary colors")
else:
    print("Not all are primary colors")    


mode = input("Which mode do u prefer? ").strip().lower()

if mode == "automatic" or mode == "manual":
    print(f"{mode} mode has been activated")
elif mode == "off":
    print(f"System is {mode}")
else :
    print("Mode not working")    



message = input("Enter your message: ").lower()
priority_message = ["urgent", "important", "immediate" ]

if message in priority_message:
    print("High priority message")
else:
    print("Normal message")



status1 = input("Enter the first status (active, inactive, pending): ")
status2 = input("Enter the second status (active, inactive, pending): ")

if status1 == "active" and status2 == "active":
    print("Both active")
elif status1 == "active" or status2 == "active":
    print("One active")
else:
    print("None active")




filename = input("Enter the filename: ")


if filename.lower().endswith(('.jpg', '.png', '.gif')):
    print("Image file")
else:
    print("Not an image file")




access_level = input("Enter the access level (admin, user, guest): ")

if access_level == "admin":
    print("Full access")
elif access_level == "user":
    print("Limited access")
elif access_level == "guest":
    print("No access")
else:
    print("Invalid access level")



email = input("Input your email: ")

if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")


day = input("Input the week day: ").lower().strip()
week_days = ["monday", "tuesday", "wednesday", "thursday", "friday"]
weekend = ["sunday", "saturday"]

if day in weekend:
    print("It's weekend")
elif day in week_days:
    print("It is a week day")
else:
    print("Invalid day of the week")



input_str = input("Enter three numbers separated by commas: ")

num1, num2, num3 = map(int, input_str.split(','))

if num1 >= num2 and num1 >= num3:
    print(num1)
elif num2 >= num1 and num2 >= num3:
    print(num2)
else:
    print(num3)
d
