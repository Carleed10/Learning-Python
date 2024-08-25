# has_raincoat = True
# has_umbrella = True

# if has_raincoat or has_umbrella:
#     print("The rain won't affect you")
# else:
#     print("The rain will affect you")

# mode = input("Which mode do u prefer? ").strip().lower()

# if mode == "automatic" or mode == "manual":
#     print(f"{mode} mode has been activated")
# elif mode == "off":
#     print(f"System is {mode}")
# else :
#     print("Mode not working")

# colors = input("Input first color, second color, third color: ").lower().split(",")
# color1, color2, color3 = colors
# color1, color2, color3 = color1.strip(), color2.strip(), color3.strip()
# primary_colors = ["red", "blue", "yellow"]
# # print(colors)

# if color1 in primary_colors and color2 in primary_colors and color3 in primary_colors:
#     print("All are primary colors")
# else:
#     print("Not all are primary colors")


# days = input("Input the week day: ").lower().strip()
# week_days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
# weekend = ["sunday", "saturday"]

# if days in weekend:
#     print("It's weekend")
# else:
#     print("It is a week day")


day = input("Input the week day: ").lower().strip()
week_days = ["monday", "tuesday", "wednesday", "thursday", "friday"]
weekend = ["sunday", "saturday"]

if day in weekend:
    print("It's weekend")
elif day in week_days:
    print("It is a week day")
else:
    print("Invalid day of the week")
